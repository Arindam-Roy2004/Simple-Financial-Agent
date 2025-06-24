# 💼 Simple Financial Agent

**Simple Financial Agent** is a multi-agent Streamlit-based AI assistant that combines finance and web search capabilities using the [`agno`](https://pypi.org/project/agno/) framework and OpenAI's GPT-4o model.

It allows users to:
- 📈 Get real-time stock prices
- 🌐 Search the web for the latest news or information
- 🧠 Combine finance and general queries in one interface


## 🧩 Features

- 🌍 **Web Agent**: Searches the internet using DuckDuckGo.
- 📊 **Finance Agent**: Fetches stock price data using YFinance.
- 🧠 **Powered by GPT-4o**: High performance with reliable reasoning.
- 🧰 **Tool-based Agent Architecture** via `agno`
- ⚡️ Fast, responsive UI via Streamlit

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Arindam-Roy2004/Simple-Financial-Agent.git
cd Simple-Financial-Agent
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Add `.env` File

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=your_openai_key
PHIDATA_API_KEY=your_phidata_key  # optional
GEMINI_API_KEY=your_gemini_key    # optional
```

---

## ▶️ Running the App

```bash
streamlit run app.py
```

Then visit [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🛠️ Tech Stack

- [Streamlit](https://streamlit.io/)
- [agno](https://pypi.org/project/agno/)
- [OpenAI GPT-4o](https://platform.openai.com/)
- [DuckDuckGo Search API](https://pypi.org/project/duckduckgo-search/)
- [Yahoo Finance (yfinance)](https://pypi.org/project/yfinance/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 📄 Example Queries

- "What is the current stock price of AAPL?"
- "Latest news about artificial intelligence chips"
- "How did the S&P 500 perform today?"

---

## 🙌 Acknowledgements

- Built using [agno](https://pypi.org/project/agno/) agent framework
- Inspired by LangChain & Agentic design patterns
- Created by [Arindam Roy](https://github.com/Arindam-Roy2004)

---

## 🪪 License

This project is licensed under the [MIT License](LICENSE).
