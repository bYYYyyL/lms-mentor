# LMS Mentor

LMS Mentor 是一个面向 CS LMS 作业的 Agent Skill。它帮助用户定位并检查选定的作业、提交答案，并结合题目讲解 AP Computer Science A（AP CSA）知识点和难题陷阱。

> **提交说明：**确认要处理哪些作业，即表示授权 agent 完成并直接提交这些作业。使用前请了解课程和作业的相关要求。

## 安装

向支持联网和安装技能的 agent 发送：

> 帮我从 https://github.com/bYYYyyL/lms-mentor 安装 lms-mentor。

也可以在安装了 Node.js 的环境中，使用 [skills CLI](https://github.com/vercel-labs/skills)：

```sh
npx skills add bYYYyyL/lms-mentor --skill lms-mentor
```

对于 Codex，也可以要求它使用技能安装器，指定仓库 `bYYYyyL/lms-mentor` 和路径 `skills/lms-mentor`。手动安装时，将 `skills/lms-mentor` 文件夹复制到所用 agent 的技能目录，并按该 agent 的要求重新加载。

不同 agent 的安装方式和搜索范围不同。只提供名称不一定能找到本项目；提供仓库地址可以明确安装来源。

## 使用方法

1. 在 agent 能够操作的浏览器或应用中打开并登录 CS LMS；必要时提供课程页面或 LMS 地址。
2. 按所用 agent 的要求启用浏览器或设备操作工具，并授予必要权限。
3. 发送：“使用 LMS Mentor，列出当前课程的待提交作业。”
4. 确认需要完成并提交的作业，之后查看提交状态和知识点讲解。

技能会按知识点解释规则和题目推理，说明难题的潜在陷阱，并列出较难题目的题号。

## 使用前了解

- **浏览器和设备：**技能优先使用用户指定或已登录的可操作会话。优先使用 agent 已有的控制工具；在支持本地 Python 和图形界面的桌面环境，也可按技能内的浏览器连接指南配置 Playwright 辅助程序，在独立浏览器窗口中手动登录。设备、浏览器和应用的支持情况仍取决于运行环境及权限。
- **登录：**遇到登录、验证码或会话过期时，请在浏览器或应用中自行处理，不要在聊天中发送密码。
- **连接失败：**agent 会提醒用户，不自动等待或重试；处理问题后，明确要求它继续。
- **验证范围：**仓库中的技能已通过格式校验，并测试过从 GitHub 安装；尚未验证所有 agent、设备和 LMS 环境。

## 项目结构

```text
lms-mentor/
├── README.md
└── skills/
    └── lms-mentor/
        ├── SKILL.md
        ├── references/browser-setup.md
        └── scripts/browser_session.py
```

`SKILL.md` 包含技能的触发描述和执行规则；本页面说明如何安装和使用。
