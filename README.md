# Oumomo Skills

[English](README.md) | [简体中文](README.zh-CN.md)

Turn a product category, product link, or TikTok reference into a ready-to-generate ecommerce video from your AI agent. The Oumomo Skill guides the conversation; the lightweight `oumomo-agent` CLI signs in, uploads product images, and calls Oumomo's video APIs. No OpenAI API key or MCP key is required.

## Install

```bash
npm install -g oumomo-agent
oumomo-agent setup
npx skills add Oumomo-Video/oumomo-skill --skill oumomo-video-replica --agent '*' -g -y
```

Restart your agent after installation. Verify the CLI with `oumomo-agent --version` and verify the Skill with `npx skills ls -g`.

## What it does

- Finds real, accessible viral reference videos for a product and target market.
- Treats a TikTok video link as the chosen reference instead of replacing it with search results.
- Reads supported TikTok Shop and FastMoss product links and recommends suitable creative references.
- Uploads one or several product images, prepares the remake Prompt and generation settings, and submits only after explicit confirmation.

## Give this to your agent

```text
Set up Oumomo CLI so you can help me remake viral ecommerce videos and turn product links into videos.

1. Install the CLI: run `npm install -g oumomo-agent`.
2. Authenticate: run `oumomo-agent setup` and let me complete sign-in in the browser it opens.
3. Install the companion Skill: run `npx skills add Oumomo-Video/oumomo-skill --skill oumomo-video-replica --agent '*' -g -y`.

Once that is done, restart the agent and let me know when it is ready.
```
