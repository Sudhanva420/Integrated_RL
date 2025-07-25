# 📈 Reinforcement Learning for Stock Price Prediction and Portfolio Optimization

A cutting-edge system that integrates sentiment analysis from financial news and reports with reinforcement learning to predict stock movements and optimize portfolio value through intelligent buy/sell/hold strategies.

## 🧠 Key Features
- **Sentiment-Aware Trading**: Combines sentiment from news articles and company reports using FinBERT.
- **Custom Daily Sentiment Score**: Aggregates sentiment from multiple sources to represent market perception.
- **Multi-Modal Feature Set**: Integrates numerical indicators (e.g., revenue, EPS) with sentiment signals.
- **RL-Based Strategy**: Employs a Deep Q-Network (DQN) or PPO agent to learn optimal actions in a dynamic market.
- **Backtesting Module**: Evaluates performance on historical data with custom reward functions.
- **Buy/Sell/Hold Decision System**: Action space designed for practical portfolio management.

---

## 🏗️ Architecture
```
+---------------------+       +----------------------+        +----------------+
|  Financial News     |       |  Earnings Reports     |        |  Stock Prices   |
|  (Web + API Feeds)  |       |  (PDFs)               |        |  (Yahoo Finance)|
+---------------------+       +----------------------+        +----------------+
         |                              |                              |
         v                              v                              v
+---------------------+     +--------------------------+      +-------------------+
|  FinBERT Sentiment  |     | FinBERT PDF Sentiment    |      |  Technical/Numerical|
|  Analysis (Articles)|     | Analysis (Reports)       |      |  Feature Extraction |
+---------------------+     +--------------------------+      +-------------------+
         \__________________________|_________________________/
                                      |
                                      v
                       +-------------------------------+
                       |     Daily Feature Vector       |
                       +-------------------------------+
                                      |
                                      v
                       +-------------------------------+
                       |   Reinforcement Learning Agent |
                       |      (DQN / PPO / A2C)         |
                       +-------------------------------+
                                      |
                                      v
                         +--------------------------+
                         |   Buy / Sell / Hold      |
                         +--------------------------+
```

---

## 🧾 Data Sources
- 📊 **Stock Prices**: Yahoo Finance (via yfinance)
- 📰 **Financial News**: News APIs (e.g., NewsAPI, Alpha Vantage)
- 📄 **Earnings Reports**: Company filings (PDFs from EDGAR / investor sites)

---

## 🛠️ Tech Stack
- **FinBERT** (HuggingFace Transformers)
- **OpenAI Gym / Stable Baselines3**
- **yfinance**, **Pandas**, **NumPy**, **Matplotlib**
- **scikit-learn**, **PyMuPDF (fitz)** for PDF parsing


