# Oumomo Skills

[English](README.md) | [简体中文](README.zh-CN.md)

在 AI Agent 里，从商品品类、商品链接或 TikTok 参考视频直接开始创作带货视频。Oumomo Skill 负责引导创作流程，轻量的 `oumomo-agent` CLI 负责登录、上传商品图片和调用 Oumomo 视频接口；用户不需要配置 OpenAI API Key 或 MCP Key。

## 安装

```bash
npm install -g oumomo-agent
oumomo-agent setup
npx skills add Oumomo-Video/oumomo-skill --skill oumomo-video-replica --agent '*' -g -y
```

安装后请重启 Agent。使用 `oumomo-agent --version` 检查 CLI，使用 `npx skills ls -g` 检查 Skill。

## 可以做什么

- 按商品和目标市场推荐真实、可访问的爆款参考视频。
- 收到 TikTok 视频链接时直接将其作为复刻参考，不会误走爆款搜索。
- 读取支持的 TikTok Shop 或 FastMoss 商品链接，并推荐适合该商品的参考方向。
- 上传一张或多张商品图，整理复刻 Prompt 和生成参数，只有在用户明确确认后才提交生成。

## 把这段话发给你的 Agent

```text
请安装并使用 Oumomo CLI，帮我完成爆款视频复刻和商品链接生成视频。

1. 安装 CLI：运行 `npm install -g oumomo-agent`。
2. 登录 Oumomo：运行 `oumomo-agent setup`，并让我在打开的浏览器中完成登录。
3. ��装配套 Skill：运行 `npx skills add Oumomo-Video/oumomo-skill --skill oumomo-video-replica --agent '*' -g -y`。

完成后重启 Agent，并告诉我是否已经准备好。之后严格按照 Skill 调用 oumomo-agent：根据我的商品链接、品类或参考视频推荐真实可访问的爆款视频；确认参考方向和商品素材后，整理复刻 Prompt 与生成参数供我确认；只有在我明确确认后才提交视频生成。不要调用远程 Agent 或 Chat 接口。
```
