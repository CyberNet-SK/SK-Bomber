# SK-Bomber
This too create for entertainment and fun do not use any illegal work stay alert stay safe thanks
# SK-Bomber

**SK-Bomber** is a lightweight, Termux-optimized SMS/OTP bomber tool written in Python.  
It supports 30+ Bangladeshi APIs (BTCL, GP, healthcare, e-commerce, entertainment, gaming, etc.) with controlled sending rates to avoid quick blocks.

> ⚠️ **Important Legal Notice**  
> This tool is created **only for educational purposes and fun/pranks among friends**.  
> **Do NOT** use it for harassment, spam, revenge, or any illegal/harmful activity.  
> Misuse can lead to legal consequences — stay safe, stay alert, stay legal.

## Features
- 30+ real Bangladeshi APIs (BTCL MyBTCL, PhoneBill, Bioscope, GP services, Arogga, ePharma, Bikroy, etc.)
- **Slow & Controlled** mode (ideal for Termux – low ban risk)
- **Fast** mode (high concurrency – use with caution)
- Automatic phone number formatting (+88, 880, 0, etc.)
- Beautiful animated banner & loading animation
- Pause (CTRL+Z) / Resume & Stop (CTRL+C)
- Real-time success/failure counter
- No root required – runs perfectly on Termux

## Requirements
- Termux app (from F-Droid or official GitHub)
- Python 3
- Internet connection (mobile data/Wi-Fi)

## Installation (Termux)

### Quick One-Liner

```bash
pkg update -y && pkg upgrade -y && \
pkg install python git -y && \
git clone https://github.com/CyberNet-SK/SK-Bomber.git && \
cd SK-Bomber && \
python3 bom.py
