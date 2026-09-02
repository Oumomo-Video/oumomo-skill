# Oumomo Skills

[English](README.md) | [简体中文](README.zh-CN.md)

<p align="center">
  <img src="docs/oumomo-logo.jpg" width="110" alt="Oumomo logo" />
</p>

<p align="center">
  <a href="https://github.com/Oumomo-Video/oumomo-cli"><img src="https://img.shields.io/badge/CLI-oumomo--cli-24292f?logo=github" alt="oumomo-cli" /></a>
  <a href="https://www.npmjs.com/package/oumomo-agent"><img src="https://img.shields.io/npm/v/oumomo-agent" alt="npm version" /></a>
  <a href="https://github.com/Oumomo-Video/oumomo-skill/stargazers"><img src="https://img.shields.io/github/stars/Oumomo-Video/oumomo-skill?style=social" alt="Stars" /></a>
</p>

**在 AI Agent 里，把已经验证能出单的爆款带货视频，换成你自己的商品重新生成。**

Oumomo Skills 是给跨境电商卖家（TikTok Shop / 独立站）准备的 Agent 工作流。不用从零开始想创意——直接从一条已经被市场验证过的爆款视频出发，Oumomo 把它的转化结构复刻到**你的**商品、**你的**素材、**你的**卖点上。

## 核心思路：爆款复刻（Viral Remake）

一条爆款带货视频背后不是运气，而是一套被验证过的创意结构：前 3 秒的钩子、节奏、镜头脚本、CTA。**爆款复刻**要做的，就是保留这套「能转化的结构」，把商品换成你的。

在 Agent 里，Oumomo 把难做的部分都接管了：

1. **找到被验证过的结构** — 你自己发一条信任的 TikTok 链接；或者让 Oumomo 按你的商品和目标市场（美国、欧洲、东南亚……）推荐真实可访问的爆款参考。
2. **喂进你的商品** — 商品图、可选的多角度白底图、复刻 Prompt 和修改要求。
3. **确认后再生成** — 时长、语言、画幅、质量、最终 Prompt 全部摆在你面前。你不说确认，一分钱都不会扣。

## 装进 Agent 之后能做什么

- **只推荐真实存在的参考** — 推荐的爆款视频全部真实可访问，不编造链接。
- **链接直达** — 你发一条 TikTok 视频链接，它就是选定的参考，不会被搜索结果顶掉。
- **读得懂商品链接** — 发一条 TikTok Shop 或 FastMoss 商品详情页链接，Oumomo 会基于这个商品推荐合适的创意方向。
- **零 Key 配置** — 不需要 OpenAI API Key，也不需要 MCP Key。轻量的 `oumomo-agent` CLI 负责浏览器登录，模型和视频生成都在 Oumomo 后端完成。
- **确认后才付费** — 生成参数完整呈现，`y/N` 确认之后才提交，没有隐性扣费。

## 快速开始

把下面这段话直接丢给你的 Agent——装 CLI、浏览器登录、装 Skill，它全包了：

```text
请安装并使用 Oumomo CLI，帮我完成爆款视频复刻和商品链接生成视频。

1. 安装 CLI：运行 `npm install -g oumomo-agent`。
2. 登录 Oumomo：运行 `oumomo-agent setup`，并让我在打开的浏览器中完成登录。
3. 安装配套 Skill：运行 `npx skills add Oumomo-Video/oumomo-skill`。

完成后重启 Agent，并告诉我是否已经准备好。
```

装好之后，直接说人话：

```text
帮我找几条美国市场高赞的牙齿美白 TikTok 参考视频，选一条给我的商品复刻。
```

**想手动安装？**

```bash
npm install -g oumomo-agent
oumomo-agent setup
npx skills add Oumomo-Video/oumomo-skill
```

安装后重启 Agent。用 `oumomo-agent --version` 检查 CLI，用 `npx skills ls -g` 检查 Skill。

## 仓库中的 Skill

- [`skills/oumomo-video-replica`](skills/oumomo-video-replica/SKILL.md) — 爆款复刻与商品链接转视频两条工作流，随 `npx skills add Oumomo-Video/oumomo-skill` 一并安装。

## 为什么拆成 Skill + CLI？

Skill 文件（SKILL.md）公开并在这个仓库里版本化，教你的 Agent 掌握工作流；CLI 是一个只做登录、传图、调用授权工具的瘦客户端——Prompt、适配器和业务执行都留在 Oumomo 服务端，任何敏感的东西都不会下发到终端。设计细节见 CLI 仓库的 [docs/distribution.md](https://github.com/Oumomo-Video/oumomo-cli/blob/main/docs/distribution.md)。

## 相关链接

- CLI 仓库：[Oumomo-Video/oumomo-cli](https://github.com/Oumomo-Video/oumomo-cli)
- npm 包：[oumomo-agent](https://www.npmjs.com/package/oumomo-agent)
- 官网：[oumomo.ai](https://www.oumomo.ai)

## 开源协议

[MIT](LICENSE)
