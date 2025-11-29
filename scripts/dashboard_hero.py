import os

# CONFIG: The "Stripe-like" Fintech Palette
COLORS = {
    "bg": "#0B1120",        # Midnight Blue
    "surface": "#1E293B",   # Slate 800
    "border": "#334155",    # Slate 700
    "accent": "#2DD4BF",    # Teal 400
    "text_main": "#F8FAFC", # Slate 50
    "text_dim": "#94A3B8",  # Slate 400
    "success": "#34D399",   # Emerald
    "chart": "rgba(45, 212, 191, 0.2)"
}

# SVG GENERATOR
svg = f"""
<svg width="100%" height="320" viewBox="0 0 1000 320" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="glow" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="{COLORS['accent']}" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="{COLORS['bg']}" stop-opacity="0"/>
    </linearGradient>
    <filter id="shadow">
      <feDropShadow dx="0" dy="4" stdDeviation="10" flood-color="#000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <rect width="1000" height="320" fill="{COLORS['bg']}" />
  
  <pattern id="grid" width="50" height="50" patternUnits="userSpaceOnUse">
    <path d="M 50 0 L 0 0 0 50" fill="none" stroke="{COLORS['border']}" stroke-width="0.5" stroke-opacity="0.3"/>
  </pattern>
  <rect width="1000" height="320" fill="url(#grid)" />

  <g transform="translate(60, 80)">
    <text x="0" y="0" font-family="'Segoe UI', sans-serif" font-weight="800" font-size="42" fill="{COLORS['text_main']}" letter-spacing="-1">
      DANIAL SALAMI
    </text>
    <text x="0" y="40" font-family="'Segoe UI', sans-serif" font-weight="400" font-size="18" fill="{COLORS['accent']}" letter-spacing="2">
      /// BLOCKCHAIN ARCHITECT
    </text>
    <text x="0" y="80" font-family="'Segoe UI', sans-serif" font-weight="300" font-size="16" fill="{COLORS['text_dim']}" width="400">
      Building institutional-grade financial infrastructure
    </text>
    <text x="0" y="105" font-family="'Segoe UI', sans-serif" font-weight="300" font-size="16" fill="{COLORS['text_dim']}">
      on .NET 8 and Ethereum.
    </text>
    
    <g transform="translate(0, 140)">
      <rect width="140" height="32" rx="16" fill="{COLORS['surface']}" stroke="{COLORS['success']}" stroke-width="1" />
      <circle cx="20" cy="16" r="4" fill="{COLORS['success']}">
        <animate attributeName="opacity" values="1;0.5;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="35" y="21" font-family="monospace" font-size="12" fill="{COLORS['success']}">SYSTEM ONLINE</text>
    </g>
  </g>

  <g transform="translate(500, 40)" filter="url(#shadow)">
    <rect width="440" height="240" rx="8" fill="{COLORS['surface']}" stroke="{COLORS['border']}" stroke-width="1" />
    
    <circle cx="20" cy="20" r="4" fill="#EF4444" />
    <circle cx="36" cy="20" r="4" fill="#F59E0B" />
    <circle cx="52" cy="20" r="4" fill="#10B981" />
    
    <rect x="0" y="40" width="440" height="1" fill="{COLORS['border']}" />
    <text x="420" y="25" text-anchor="end" font-family="monospace" font-size="10" fill="{COLORS['text_dim']}">ETH_MAINNET_L2</text>
    
    <g transform="translate(20, 60)">
      <text x="0" y="20" font-family="sans-serif" font-weight="bold" font-size="24" fill="{COLORS['text_main']}">$3,420.50</text>
      <text x="130" y="20" font-family="sans-serif" font-size="14" fill="{COLORS['success']}">+4.2%</text>
      
      <path d="M0,100 Q40,90 80,110 T160,80 T240,60 T320,90 T400,40" 
            fill="none" stroke="{COLORS['accent']}" stroke-width="2" />
      <path d="M0,100 Q40,90 80,110 T160,80 T240,60 T320,90 T400,40 V150 H0 Z" 
            fill="url(#glow)" stroke="none" />
            
      <circle cx="400" cy="40" r="4" fill="{COLORS['accent']}" />
      <rect x="340" y="10" width="60" height="20" rx="4" fill="{COLORS['accent']}" />
      <text x="370" y="24" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#000" font-weight="bold">LATEST</text>
    </g>
  </g>
</svg>
"""

os.makedirs("dist", exist_ok=True)
with open("dist/hero_dashboard.svg", "w", encoding="utf-8") as f:
    f.write(svg)
