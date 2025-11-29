import os
import requests
import base64

# --- CONFIGURATION & ASSETS ---
# Modern "DeFi" Color Palette
COLORS = {
    "bg_gradient_start": "#0f172a", # Deep Blue/Black
    "bg_gradient_end": "#1e293b",   # Lighter Slate
    "accent_primary": "#33E6C8",    # Your Teal
    "accent_secondary": "#8b5cf6",  # Violet
    "glass_bg": "rgba(255, 255, 255, 0.05)",
    "glass_border": "rgba(255, 255, 255, 0.1)",
    "text_main": "#f1f5f9",
    "text_dim": "#94a3b8"
}

# --- 1. FETCH LIVE DATA ---
def get_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,polkadot&vs_currencies=usd&include_24hr_change=true"
        data = requests.get(url, timeout=10).json()
        return data
    except:
        return None

data = get_prices()

# Fallback data if API fails
btc = data['bitcoin']['usd'] if data else 0
eth = data['ethereum']['usd'] if data else 0
sol = data['solana']['usd'] if data else 0
dot = data['polkadot']['usd'] if data else 0

# --- 2. GENERATE SVG ---
# We use raw SVG string construction for maximum control over CSS animations
svg = f"""
<svg width="800" height="400" viewBox="0 0 800 400" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:{COLORS['bg_gradient_start']};stop-opacity:1" />
      <stop offset="100%" style="stop-color:{COLORS['bg_gradient_end']};stop-opacity:1" />
    </linearGradient>
    
    <linearGradient id="glassGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:white;stop-opacity:0.1" />
      <stop offset="100%" style="stop-color:white;stop-opacity:0.0" />
    </linearGradient>

    <style>
      .float {{ animation: float 6s ease-in-out infinite; }}
      .float-delayed {{ animation: float 6s ease-in-out infinite; animation-delay: 3s; }}
      .pulse {{ animation: pulse 3s infinite; }}
      .spin {{ animation: spin 20s linear infinite; transform-origin: 400px 200px; }}
      .dash {{ stroke-dasharray: 10; animation: dash 1s linear infinite; }}
      
      @keyframes float {{ 0% {{ transform: translateY(0px); }} 50% {{ transform: translateY(-10px); }} 100% {{ transform: translateY(0px); }} }}
      @keyframes pulse {{ 0% {{ opacity: 0.5; }} 50% {{ opacity: 1; }} 100% {{ opacity: 0.5; }} }}
      @keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}
      @keyframes dash {{ to {{ stroke-dashoffset: -20; }} }}
      
      .text-price {{ font-family: 'Segoe UI', sans-serif; font-weight: bold; font-size: 14px; fill: {COLORS['text_main']}; }}
      .text-label {{ font-family: 'Segoe UI', sans-serif; font-size: 10px; fill: {COLORS['text_dim']}; }}
      .card {{ fill: {COLORS['glass_bg']}; stroke: {COLORS['glass_border']}; stroke-width: 1; }}
    </style>
  </defs>

  <rect width="800" height="400" rx="20" fill="url(#bgGrad)" />
  
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(255,255,255,0.03)" stroke-width="1"/>
  </pattern>
  <rect width="800" height="400" fill="url(#grid)" />

  <g transform="translate(400, 200)">
    <circle r="60" fill="none" stroke="{COLORS['accent_primary']}" stroke-width="1" stroke-opacity="0.3" class="spin" stroke-dasharray="20 10" />
    <circle r="50" fill="{COLORS['glass_bg']}" stroke="{COLORS['accent_primary']}" stroke-width="2" />
    <text x="0" y="5" text-anchor="middle" font-family="monospace" font-weight="bold" fill="white" font-size="14">DANIAL.NET</text>
  </g>

  <line x1="400" y1="200" x2="200" y2="100" stroke="{COLORS['accent_primary']}" stroke-width="1" stroke-opacity="0.5" class="dash" />
  <line x1="400" y1="200" x2="600" y2="100" stroke="{COLORS['accent_secondary']}" stroke-width="1" stroke-opacity="0.5" class="dash" />
  <line x1="400" y1="200" x2="200" y2="300" stroke="{COLORS['accent_primary']}" stroke-width="1" stroke-opacity="0.5" class="dash" />
  <line x1="400" y1="200" x2="600" y2="300" stroke="{COLORS['accent_secondary']}" stroke-width="1" stroke-opacity="0.5" class="dash" />

  <g transform="translate(140, 70)" class="float">
    <rect width="120" height="60" rx="10" class="card" />
    <circle cx="20" cy="30" r="4" fill="#F7931A" />
    <text x="35" y="25" class="text-label">BITCOIN</text>
    <text x="35" y="45" class="text-price">${btc:,}</text>
  </g>

  <g transform="translate(540, 70)" class="float-delayed">
    <rect width="120" height="60" rx="10" class="card" />
    <circle cx="20" cy="30" r="4" fill="#627EEA" />
    <text x="35" y="25" class="text-label">ETHEREUM</text>
    <text x="35" y="45" class="text-price">${eth:,}</text>
  </g>

  <g transform="translate(140, 270)" class="float-delayed">
    <rect width="120" height="60" rx="10" class="card" />
    <circle cx="20" cy="30" r="4" fill="#14F195" />
    <text x="35" y="25" class="text-label">SOLANA</text>
    <text x="35" y="45" class="text-price">${sol:,}</text>
  </g>

  <g transform="translate(540, 270)" class="float">
    <rect width="120" height="60" rx="10" class="card" />
    <circle cx="20" cy="30" r="4" fill="#512BD4" />
    <text x="35" y="25" class="text-label">DOT NET 8</text>
    <text x="35" y="45" class="text-price">SYSTEM ONLINE</text>
  </g>

</svg>
"""

# --- 3. SAVE ---
os.makedirs("dist", exist_ok=True)
with open("dist/defi_reactor.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Reactor Online. SVG Generated.")
