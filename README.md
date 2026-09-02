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

**Remake proven viral ads around your own product — from inside your AI agent.**

Oumomo Skills are agent workflows for cross-border e-commerce sellers on TikTok Shop. Instead of starting from a blank canvas, you start from a viral video that has already proven it sells, and Oumomo rebuilds it around *your* product, *your* images, and *your* offer.

## The idea: viral remake

A viral product video is not luck — it is a proven creative format: the hook, the pacing, the shot structure, the CTA. A **viral remake** keeps the part that converts and swaps in your product.

Oumomo handles the hard parts inside your agent:

1. **Find a proven format** — send a TikTok link you already trust, or ask Oumomo to surface real, accessible viral references for your product and target market (US, EU, SEA…).
2. **Feed in your product** — product images, optional multi-angle white-background shots, a remake prompt, and any changes you want.
3. **Confirm, then generate** — review duration, language, aspect ratio, quality, and the final prompt. Nothing is charged until you explicitly confirm.

## What the skill does inside your agent

- **Real references only** — recommends viral TikToks that actually exist and are accessible. No hallucinated links.
- **Link-aware** — send a TikTok video link and it is treated as *the chosen reference*, not overwritten by search results.
- **Reads product links** — paste a TikTok Shop or FastMoss product-detail URL and Oumomo suggests reference directions suited to that product.
- **Zero key juggling** — no OpenAI API key, no MCP key. The lightweight `oumomo-agent` CLI signs you in via browser and talks to Oumomo's backend, which manages the model and video generation.
- **Paid only after confirmation** — generation parameters are presented for review, and the video is submitted only after your explicit `y/N`.

## Install

```bash
npm install -g oumomo-agent
oumomo-agent setup
npx skills add Oumomo-Video/oumomo-skill
```

Restart your agent after installation. Verify with `oumomo-agent --version` and `npx skills ls -g`.

## Skills in this repository

- [`skills/oumomo-video-replica`](skills/oumomo-video-replica/SKILL.md) — the viral remake and product-link-to-video workflows, installed together with `npx skills add Oumomo-Video/oumomo-skill`.

## Give this to your agent

```text
Set up Oumomo CLI so you can help me remake viral ecommerce videos and turn product links into videos.

1. Install the CLI: run `npm install -g oumomo-agent`.
2. Authenticate: run `oumomo-agent setup` and let me complete sign-in in the browser it opens.
3. Install the companion Skill: run `npx skills add Oumomo-Video/oumomo-skill`.

Once that is done, restart the agent and let me know when it is ready.
```

## Why a skill + CLI split?

The skill file (SKILL.md) is public and versioned here; it teaches your agent the workflow. The CLI is a thin client: prompts, adapters, and business execution stay on Oumomo servers, so nothing sensitive ships to the terminal. See [docs/distribution.md](https://github.com/Oumomo-Video/oumomo-cli/blob/main/docs/distribution.md) in the CLI repo for the design.

## Related

- CLI repo: [Oumomo-Video/oumomo-cli](https://github.com/Oumomo-Video/oumomo-cli)
- npm package: [oumomo-agent](https://www.npmjs.com/package/oumomo-agent)
- Website: [oumomo.ai](https://www.oumomo.ai)

## License

[MIT](LICENSE)
