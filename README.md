# 🚀 Binance Futures Testnet Trading Bot

This is a simplified Python-based trading bot for the **Binance Futures Testnet**.  
It supports placing:

- ✅ Market Orders  
- ✅ Limit Orders  
- ✅ Stop-Limit Orders  
- ✅ BUY and SELL sides  
- ✅ Command-line interaction  
- ✅ Logging of all API requests and responses

This project was built as part of a hiring challenge for the **Junior Python Developer – Crypto Trading Bot** role.

---

## 📂 Project Structure

```
Trading_bot/
├── bot.py              # Core bot logic (API interaction, order placement)
├── cli.py              # Command-line interface for user input
├── .env                # Stores API_KEY and API_SECRET (not pushed to GitHub)
├── trading_bot.log     # Log file for order results and errors
├── .gitignore          # Ensures sensitive files aren't tracked
└── README.md           # Project overview and setup instructions
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Maheshagathamudi/Trading_bot.git
cd Trading_bot
```

### 2. Install Dependencies
```bash
pip install python-binance python-dotenv
```

### 3. Create `.env` File

Create a file named `.env` in the root directory and add your Binance **Futures Testnet** credentials:

```env
API_KEY=your_testnet_api_key_here
API_SECRET=your_testnet_api_secret_here
```

> ⚠️ Do **NOT** share or upload this file publicly.

---

## ▶️ How to Run

```bash
python cli.py
```

You'll be prompted to enter:

- **Symbol** (e.g., BTCUSDT)
- **Side** (BUY / SELL)
- **Order Type** (MARKET, LIMIT, STOP-LIMIT)
- **Quantity**
- **Price / Stop Price** (depending on order type)

---

## 🧾 Logs

All order responses, requests, and errors are logged in:

```
trading_bot.log
```

This file is auto-generated and useful for debugging and submission.

---

## 👨‍💻 Author

**Mahesh Agathamudi**  
B.Tech CSE | Python Developer | Data & Web Enthusiast  
[GitHub Profile](https://github.com/Maheshagathamudi)

---

## 📝 License

This project is for educational and testing purposes only.  
Binance Testnet is a safe environment for simulation — **no real funds involved**.
