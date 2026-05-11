# 🪙 Bitcoin Price Speaker

A small Python script that fetches the **real-time Bitcoin price** using the [CoinDesk API](https://api.coindesk.com/v1/bpi/currentprice.json) and reads it aloud using the `pyttsx3` text-to-speech library.

---

## 🔧 Features
- Fetches live BTC to USD price from CoinDesk.
- Converts the price into a readable number.
- Speaks the value using your system voice.
- Automatically updates every 24 hours.

---

## 📦 Requirements

Install the required Python packages:
```bash
pip install requests pyttsx3
