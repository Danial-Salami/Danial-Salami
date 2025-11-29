import os
import requests

# 1. Fetch Data (CoinGecko API - Free)
try:
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
    data = requests.get(url).json()
    btc = data['bitcoin']['usd']
    eth = data['ethereum']['usd']
    sol = data['solana']['usd']
    btc_chg = data['bitcoin']['usd_24h_change']
except:
    btc, eth, sol, btc_chg = (0, 0, 0, 0) # Fallback

# 2. Define colors (Financial Dark Mode)
COLOR_BG = "#0D1117"
COLOR_TEXT = "#C9D1D9"
COLOR_GREEN = "#33E6C8" # Your brand teal
COLOR_RED = "#FF6B6B"
trend_color = COLOR_GREEN if btc_chg >= 0 else COLOR_RED
arrow = "▲" if btc_chg >= 0 else "▼"

# 3. Create SVG Content
svg_content = f"""
<svg width="400" height="120" viewBox="0 0 400 120" xmlns="http://www.w3.org/2000/svg">
  <style>
    .bg {{ fill: {COLOR_BG}; }}
    .text {{ font-family: 'Courier New', monospace; fill: {COLOR_TEXT}; font-size: 14px; }}
    .green {{ fill: {COLOR_GREEN}; font-weight: bold; }}
    .title {{ font-size: 16px; font-weight: bold; fill: #8B949E; }}
    .blink {{ animation: blinker 1s linear infinite; }}
    @keyframes blinker {{ 50% {{ opacity: 0; }} }}
  </style>

  <rect width="400" height="120" rx="10" class="bg" stroke="{COLOR_GREEN}" stroke-width="2"/>

  <text x="20" y="30" class="title">/// NETWORK_STATUS_ACTIVE</text>
  <circle cx="370" cy="25" r="5" fill="{COLOR_GREEN}" class="blink"/>

  <text x="20" y="60" class="text">BTC_CORE:  ${btc:,} <tspan fill="{trend_color}">({arrow} {btc_chg:.2f}%)</tspan></text>
  <text x="20" y="80" class="text">ETH_MAIN:  ${eth:,} <tspan class="green">GAS: LOW</tspan></text>
  <text x="20" y="100" class="text">SOL_NET:   ${sol:,} <tspan fill="#8B949E">TPS: 2400</tspan></text>
</svg>
"""

# 4. Save to file
os.makedirs("dist", exist_ok=True)
with open("dist/crypto_status.svg", "w") as f:
    f.write(svg_content)
