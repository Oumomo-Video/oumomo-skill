---
name: oumomo-video-replica
description: 通过 Oumomo CLI 从商品链接、品类或参考视频中推荐真实可访问的爆款视频；选定参考后收集商品图片、多角度白底图、复刻提示词和修改要求，确认生成参数并生成视频。
---

# Oumomo Viral Remake

## Trigger

Use for viral ecommerce references, TikTok/FastMoss reference URLs,
TikTok Shop/FastMoss product-detail URLs, `viral_video` selections, Link to
Video requests, and remake requests. Do not use for standalone scripts,
image-only generation, deduplication, or publishing.

## CLI

Run declared adapters with `oumomo-agent tool <name> --args '<JSON>'`.
Use `oumomo-agent image upload --file <path>` for one local image, or repeat
`--file` to upload several images in one command. Do not call a remote agent
or chat endpoint.

Before the first CLI call, run `command -v oumomo-agent` and
`oumomo-agent auth status`. If the CLI is missing or the session is not
authenticated, read [setup.md](references/setup.md) and complete setup before
continuing.

## Tools

- `url_to_video_fetch_product` (only for product-detail URLs)
- `tiktok_resolve_reference`
- `video_replica_search`
- `video_replica_generate_video`
- `replica_progress`
- `replica_project_result`

## Workflow

1. Classify a supplied URL before calling a tool:
   - For a TikTok reference-video URL, including `https://vt.tiktok.com/...`,
     call `tiktok_resolve_reference` first, read [tiktok-reference-url.md](references/tiktok-reference-url.md), and treat the returned canonical URL as the selected reference. Do not call `video_replica_search`.
   - For a TikTok Shop/FastMoss product-detail URL, call
   `url_to_video_fetch_product` first and use its product/category context for
   `video_replica_search`.
2. For category requests or product-link requests without a selected reference,
   translate a non-English category into a concise English ecommerce search
   term. Call `video_replica_search` with that term in `words` and the target
   market in `region`. For example, use exactly
   `oumomo-agent tool video_replica_search --args '{"region":"US","words":"electric mosquito swatter"}'`
   for a US electric-mosquito-swatter request. Do not invent category IDs or
   claim that free-text search requires a numeric category. Check the returned
   business `code`; `code: 0` is a successful search even when unrelated items
   also appear in the result. Select only items whose description or hashtags
   match the requested product. If the first term has no relevant results, retry
   with one concise English synonym such as `electric fly swatter` or
   `bug zapper racket`. Every displayed
   recommendation must include its real `videoUrl`, `embedUrl`, or `url` as a
   clickable/copyable link. Describe recommendations briefly using the returned
   metadata and the user's actual product context.
   If no usable link exists, ask for a reference URL.
3. Reuse product images already available in the current conversation. If no
   product image is available, ask for one. A clean multi-angle white-background
   image set is preferred but optional. Ask whether the user wants to provide a
   remake Prompt or any changes; both are optional.

   Upload all supplied local product images together with one command, repeating
   `--file` for each path. Preserve every returned `fileNo`; use the clearest
   primary product image as `productImageFileNo` for the current video submit.

   Chinese collection copy when product images already exist: `已收到商品图。你也可以补充多角度白底图、复刻 Prompt 或想调整的地方；这些都可以不填，我会根据参考视频和现有商品素材整理生成方案，再给你确认。`
4. If the user provides a remake Prompt, preserve it and apply their requested
   changes. Otherwise, create the Prompt from the selected reference analysis
   and available product materials. Use an empty `userRequirements` value when
   the user has no additional changes.
5. Before generation, collect and present a structured generation review. The
   following values require an explicit user choice or approval: target
   country/market, language, duration, ratio, quality, and generation mode.
   Target country/market is the creative-market context; use it when preparing
   the final Prompt and ensure the chosen language is appropriate for it.
   Also include the selected reference URL, primary product image, Prompt,
   optional changes, and a brief video description.

   - Ask for every missing required generation value. You may recommend a value
     based on the product and selected reference, but do not silently apply a
     default. The final review must contain every value explicitly; never
     replace it with a vague question such as "Should I start?".
   - Use user-facing names in the review, not API codes. For example, show
     `English (United States)` rather than `EN_US`; convert the confirmed name
     to the CLI language code only when constructing the tool arguments.
   - Use only supported duration values: 10, 15, or 30 seconds. Use only
     supported quality values: 480p or 720p.
   - Keep Prompt and requested changes optional; state the proposed values even
     when they are empty.
   - Do not call `video_replica_generate_video`, prepare a `--confirm` command,
     or imply that generation has started until the user explicitly approves
     this complete review. A generic earlier request such as "make this video"
     is not approval of the final parameters.

   Chinese review format:

   ```text
   生成参数确认
   - 参考视频：<resolved TikTok URL>
   - 商品主图：<fileNo 或图片说明>
   - 目标国家/市场：<country/market>
   - 视频语言：<language>
   - 时长：<10/15/30 秒>
   - 比例：<9:16 或 16:9>
   - 清晰度：<480p 或 720p>
   - 生成模式：<mode/version>
   - 复刻 Prompt：<text 或未提供>
   - 修改要求：<text 或无>
   - 视频说明：<text>
   ```

6. Only after explicit approval, call `video_replica_generate_video` once,
   passing the numeric `videoId` when known; otherwise pass the TikTok URL as
   `videoUrl`. Pass the approved Prompt as `replicaPrompt` and requested
   changes as `userRequirements`, then poll with `replica_progress` and
   `replica_project_result`.
