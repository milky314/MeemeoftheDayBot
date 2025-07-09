# MeemeoftheDayBot

This bot auto-posts the most viral meme of the day to your X (Twitter) account.

## 🔧 Setup Instructions

1. Go to your repo's Settings → Secrets → Actions
2. Add these 4 secrets:
   - `API_KEY`
   - `API_SECRET`
   - `ACCESS_TOKEN`
   - `ACCESS_TOKEN_SECRET`

3. Push this repo.
4. GitHub Actions will run once daily and post your meme.

To test it manually, go to **Actions** tab and trigger the workflow via `workflow_dispatch`.
