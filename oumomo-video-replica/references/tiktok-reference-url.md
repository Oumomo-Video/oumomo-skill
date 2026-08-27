# TikTok Reference URLs

Treat a user-supplied TikTok video URL as the selected reference video. Do not
replace it with recommendations and do not call `video_replica_search`.

## Short links

For `https://vt.tiktok.com/...` links, resolve the reference with the Oumomo
read-only tool before showing the confirmation:

```bash
oumomo-agent tool tiktok_resolve_reference \
  --args '{"url":"https://vt.tiktok.com/SHORT_CODE/"}'
```

Use the returned numeric `videoId` for generation and show the returned
canonical TikTok URL as the selected reference. Never resolve the link with
`curl`, scrape TikTok, or send the short link to `video_replica_search`.
