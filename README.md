# 🎬 MovieSeeker

An intelligent movie & theatre assistant powered by an AI agent. Find the cheapest, nearest, and best-rated theatres for any movie near you — just by chatting naturally.

---

## ✨ Features

- 🤖 Conversational AI agent — talk to it like ChatGPT
- 🎬 Find theatres showing any movie in your city
- 📍 Auto-detects your location for accurate distances
- 💰 Ranks theatres by price, distance & rating
- 🎟️ Direct booking link to TicketNew
- 🌐 Clean web UI with a beautiful chat interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI Agent | LangChain + Groq (openai/gpt-oss-120b) |
| Backend | FastAPI + Uvicorn |
| Frontend | Vanilla HTML/CSS/JS |
| Scraping | BeautifulSoup + Requests |
| Distance | GeoPy |
| Hosting | Render.com |

---


## 📁 Project Structure
Movie_seeker/
├── app.py                   # Agent setup & prompt
├── api.py                   # FastAPI backend
├── tools.py                 # Agent tools (scraping + theatre logic)
├── utils/
│   ├── data_with_coords.py  # Theatre dataset with coordinates
│   └── utils.py             # Helper utilities
├── static/
│   └── index.html           # Chat UI frontend
├── requirements.txt
├── render.yaml              # Render deployment config
└── .env                     # API keys (never commit this!)


---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/movieseeker.git
cd movieseeker
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
GROQ_API_KEY=your_groq_api_key_here
Get your free API key at [console.groq.com](https://console.groq.com)

### 5. Run the server
```bash
python -m uvicorn api:app --reload
```

### 6. Open in browser
http://localhost:8000

---

## 💬 How to Use

Just chat naturally! Examples:

- `"Find theatres for Biker in Bengaluru"`
- `"Top 10 theatres in Bangalore"`
- `"Where can I watch Pushpa 2 in Chennai?"`
- `"What movies are playing near me?"`
- `"Cheapest theatre for Kannappa in Hyderabad"`

The agent understands natural language — no strict format required.

---

## 🌐 Deployment

This project is deployed on **Render.com**.

### Steps:
1. Push code to GitHub (make sure `.env` is in `.gitignore`)
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Add environment variable: `GROQ_API_KEY`
5. Deploy!

Start command:
```bash
python -m uvicorn api:app --host 0.0.0.0 --port 10000
```

---

## ⚠️ Important

- Never commit your `.env` file or API keys to GitHub
- Regenerate your Groq API key if it gets exposed
- Geolocation works on HTTPS — Render provides this automatically

---

## 📄 License

MIT License — feel free to use and modify.

---

Made with ❤️ by Manas Khatri
---
