# LMS Mentor

An Agent Skill for selected CS LMS assignments: inspect and check the work, submit the assignments selected by the user, then explain AP Computer Science A concepts and difficult points. The skill's instructions and explanations are primarily in Chinese.

> Selecting an assignment authorizes the agent to complete and submit it. Check the assignment and course rules before use. The skill requires a compatible agent with access to the user's LMS session and suitable browser or device controls; it does not provide those tools.

## Install

Ask a capable agent:

> Install `lms-mentor` from https://github.com/bYYYyyL/lms-mentor

Or, where Node.js and the [skills CLI](https://github.com/vercel-labs/skills) are available:

```sh
npx skills add bYYYyyL/lms-mentor --skill lms-mentor
```

For Codex, ask it to use its skill installer with repository `bYYYyyL/lms-mentor` and path `skills/lms-mentor`. To install manually, copy `skills/lms-mentor` into the skills directory used by your agent and reload the agent if necessary.

Different agents use different discovery, permissions, and installation mechanisms. A name-only request may not find this repository; providing the URL makes the source unambiguous. Not every device or agent supports access to an existing browser session.

## Use

1. Open and sign in to CS LMS in an agent-accessible browser or app. Provide the course page or LMS address when needed.
2. Enable the browser or device control tools and permissions required by your agent.
3. Ask: “Use LMS Mentor to list my pending CS LMS assignments.” Confirm which assignments to complete and submit.
4. Review the submission status and the explanation of concepts and difficult questions.

If login or verification is required, complete it yourself; do not send passwords in chat. If connection fails, the skill reports the problem and waits for you to request another attempt. No LMS or browser integration has yet been tested for every environment.

## 中文说明

这是一个面向 CS LMS 作业的 Agent Skill。使用前请登录 LMS，并确保 agent 能操作目标浏览器或设备会话。技能会列出待提交作业，等待用户确认；确认所选作业即授权 agent 完成并提交，随后总结 AP CSA 知识点和难题陷阱。

可以直接告诉支持安装技能的 agent：“从 https://github.com/bYYYyyL/lms-mentor 安装 lms-mentor”。不同 agent 的安装方式、联网能力和设备权限不同，单凭技能名称不一定能搜索到仓库。

## Structure

```text
skills/lms-mentor/SKILL.md
```
