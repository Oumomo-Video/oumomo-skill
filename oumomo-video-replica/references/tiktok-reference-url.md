# TikTok Reference URLs

Treat a user-supplied TikTok video URL as the selected reference video. Do not
replace it with recommendations and do not call `video_replica_search`.

## Short links

For `https://vt.tiktok.com/...` links, resolve redirects locally before showing
the confirmation:

```bash
curl -LsS -o /dev/null \
  --connect-timeout 10 --max-time 30 --max-redirs 10 \
  -w '%{url_effective}\n' \
  'https://vt.tiktok.com/SHORT_CODE/'
```

Accept the result only when it uses HTTPS, belongs to `tiktok.com` or one of
its subdomains, and contains `/video/<numeric-id>`. Extract that numeric ID and
use it as `videoId`. Show the resolved long URL as the selected reference.

If local redirect resolution fails, preserve the original short URL and pass it
as `videoUrl` to `video_replica_generate_video`. The CLI calls Oumomo's TikTok
resolver before submitting and returns the resolved numeric `videoId`. Present
the canonical reference as `https://www.tiktok.com/video/<videoId>` after that
resolution. Never send the short link to `video_replica_search`.
