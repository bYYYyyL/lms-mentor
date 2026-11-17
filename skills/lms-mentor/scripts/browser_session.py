"""Visible, isolated Playwright session controlled by newline-delimited JSON on stdin."""
import argparse
import json
import sys
from pathlib import Path


def emit(data):
    print(json.dumps(data, ensure_ascii=False), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--profile', required=True, help='Dedicated browser profile directory')
    parser.add_argument('--url', default='about:blank')
    parser.add_argument('--channel', choices=['chromium', 'chrome', 'msedge'], default='chromium')
    parser.add_argument('--headless', action='store_true', help='For local tests only; user login requires a visible browser')
    args = parser.parse_args()
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        emit({'ok': False, 'error': 'Playwright is not installed. Install the Python playwright package in an isolated environment.'})
        return 1
    with sync_playwright() as p:
        options = {'headless': args.headless}
        if args.channel != 'chromium':
            options['channel'] = args.channel
        context = p.chromium.launch_persistent_context(str(Path(args.profile).resolve()), **options)
        try:
            page = context.pages[0] if context.pages else context.new_page()
            page.goto(args.url, wait_until='domcontentloaded')
            emit({'ok': True, 'event': 'ready', 'url': page.url, 'message': 'Log in manually in the visible browser if needed.'})
            for line in sys.stdin:
                try:
                    cmd = json.loads(line)
                    op = cmd['op']
                    if op == 'close':
                        emit({'ok': True}); break
                    if op == 'status':
                        result = {'url': page.url, 'title': page.title()}
                    elif op == 'text':
                        result = {'url': page.url, 'title': page.title(), 'text': page.locator('body').inner_text(timeout=10000)[:30000]}
                    elif op == 'elements':
                        selector = 'button, input, textarea, select, a, [role=button]'
                        elements = page.locator(selector)
                        items = []
                        for i in range(min(elements.count(), 150)):
                            item = elements.nth(i)
                            if item.is_visible():
                                items.append({'selector': selector + ' >> nth=' + str(i), 'tag': item.evaluate('(e) => e.tagName.toLowerCase()'), 'type': item.get_attribute('type'), 'name': item.get_attribute('name'), 'label': item.get_attribute('aria-label'), 'placeholder': item.get_attribute('placeholder'), 'text': item.inner_text(timeout=1000)[:200]})
                        result = {'url': page.url, 'elements': items}
                    elif op == 'goto':
                        page.goto(cmd['url'], wait_until='domcontentloaded'); result = {'url': page.url}
                    elif op == 'click':
                        page.locator(cmd['selector']).click(timeout=10000); result = {'url': page.url}
                    elif op == 'fill':
                        page.locator(cmd['selector']).fill(cmd['value'], timeout=10000); result = {'url': page.url}
                    elif op == 'screenshot':
                        path = str(Path(cmd['path']).resolve()); page.screenshot(path=path, full_page=True); result = {'path': path}
                    else:
                        raise ValueError('Unknown operation: ' + str(op))
                    emit({'ok': True, **result})
                except Exception as exc:
                    emit({'ok': False, 'error': str(exc)})
        finally:
            context.close()
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        emit({'ok': False, 'error': str(exc)})
        raise SystemExit(1)
