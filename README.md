<div align="center">
  <img src="./dist/hero_dashboard.svg" width="100%" alt="Enterprise Dashboard" />
</div>

<br />

<table border="0" width="100%">
  <tr>
    <td width="55%" valign="top">
      
### 🏗️ The Architect's View

I design **high-availability financial systems**. My expertise lies in bridging the gap between the speed of **Centralized Finance (CeFi)** and the security of **DeFi**.

* **Protocol Design:** structuring liquidity pools and tokenomics.
* **High-Frequency Systems:** optimizing .NET 8 pipelines for microsecond latency.
* **Smart Contract Auditing:** ensuring gas optimization and reentrancy protection.

%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#0f172a', 'edgeLabelBackground':'#0f172a', 'tertiaryColor': '#1e293b'}}}%%
graph LR
    subgraph Client ["🖥️ Institutional Client"]
        UI[Web Dashboard]
        API_GW[API Gateway]
    end

    subgraph Backend ["⚙️ .NET Core Infrastructure"]
        Orch[Orchestrator]
        Engine[Trading Engine]
        DB[(Redis Cache)]
    end

    subgraph Blockchain ["🔗 Decentralized Layer"]
        Smart[Solidity Contracts]
        Node[ETH Node]
    end

    UI -->|REST/WSS| API_GW
    API_GW --> Orch
    Orch -->|High-Freq| Engine
    Engine <-->|Microsec| DB
    Engine -->|Submit Tx| Smart
    Smart -.->|Event Emit| Node
    Node -->|Web3 Listener| Orch

    </td>
    <td width="5%" valign="top"></td>
    <td width="40%" valign="top">

### 🛠️ Production Stack

**Core Infrastructure**
<br />
<code>C# .NET 8</code> <code>ASP.NET Core</code> <code>Redis</code> <code>Kafka</code> <code>PostgreSQL</code>

**Blockchain Layer**
<br />
<code>Solidity 0.8+</code> <code>Hardhat</code> <code>Ethers.js</code> <code>Web3.py</code> <code>IPFS</code>

**Artificial Intelligence**
<br />
<code>Python</code> <code>TensorFlow</code> <code>Pandas (FinQA)</code> <code>Scikit-learn</code>

    </td>
  </tr>
</table>

<br />

### 🚀 Deployed Solutions

<table border="0" width="100%">
  <tr>
    <td width="33%">
      <div align="center">
        <img src="https://media.giphy.com/media/L1R1TVI9svk74296tM/giphy.gif" width="100%" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);" />
        <br />
        <strong>Arbitrage Bot V4</strong>
        <br />
        <small>MEV-protected execution engine on Uniswap.</small>
      </div>
    </td>
    <td width="33%">
      <div align="center">
        <img src="https://media.giphy.com/media/U3qYN8S0j3bpK/giphy.gif" width="100%" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);" />
        <br />
        <strong>Liquidity Aggregator</strong>
        <br />
        <small>Cross-chain yield optimization protocol.</small>
      </div>
    </td>
    <td width="33%">
      <div align="center">
        <img src="https://media.giphy.com/media/QTPCW4qgXqWdwY1Cq2/giphy.gif" width="100%" style="border-radius: 8px; box-shadow: 0 4px 8px rgba(0,0,0,0.5);" />
        <br />
        <strong>Real Estate Tokenizer</strong>
        <br />
        <small>Fractional ownership on Polygon Network.</small>
      </div>
    </td>
  </tr>
</table>

<br />

---

<div align="center">
  <br />
  <a href="https://linkedin.com/in/danial-salami" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Connect_on_LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" height="30" />
  </a>
  &nbsp;&nbsp;
  <a href="mailto:danialsari13@gmail.com" style="text-decoration: none;">
    <img src="https://img.shields.io/badge/Schedule_Consultation-10B981?style=for-the-badge&logo=google-calendar&logoColor=white" height="30" />
  </a>
</div>
