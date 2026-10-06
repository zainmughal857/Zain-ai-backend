# ZAIN AI Media Manager — Backend

Mobile-first FastAPI backend for the ZAIN AI Media Manager frontend.

## What works now
- Health endpoint: `/health`
- AI chat: `POST /api/ai/chat`
- AI content generation: `POST /api/ai/content`
- CORS configured for the current GitHub Pages site
- OpenAI API key stays on the server

## Deploy on Render
1. Create a GitHub repository and upload these files.
2. In Render, create **New → Web Service** and connect that repository.
3. Runtime: Python 3
4. Build command:
   `pip install -r requirements.txt`
5. Start command:
   `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables in Render:
   - `OPENAI_API_KEY` = your OpenAI API key
   - `OPENAI_MODEL` = a model available to your API account
   - `ALLOWED_ORIGINS` = `https://zainmughal857.github.io`
7. Deploy and open:
   `https://YOUR-SERVICE.onrender.com/health`

## Security
Never put the OpenAI API key in `index.html`, `app.js`, GitHub Pages, or chat messages.
Keep it only in the backend host's environment variables.

## Next phase
After this backend is online, connect the existing frontend to these endpoints.
Then add OAuth/API integrations one platform at a time (Meta, YouTube, TikTok), with user authorization and platform-required app review where applicable.
