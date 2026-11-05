# Research Goals: Empirical Analysis of Critical Energy Materials & Carbon Management

This repository hosts empirical investigations under the **Responsible Empirical Research Protocol**, currently encompassing two parallel, mutually reinforcing industrial tracks:
1. **Track 1: Global Graphite Economy**: Anode material value chain, pricing regimes, process energy intensity, and carbon coupling.
2. **Track 2: Global Carbon Capture, Utilization, and Storage (CCUS) & Direct Air Capture (DAC)**: Thermodynamic minimum work of separation, point-source capture vs. atmospheric removal, process energy duties, infrastructure chokepoints, and permanent mineralization.

---

## Part I. Global Graphite Value Chain

### 1. Context and Problem Statement
Graphite is a critical mineral essential to modern industry and the global energy transition. It serves as the primary active anode material in lithium-ion batteries for electric vehicles (EVs) and energy storage systems (ESS), as well as a foundational refractory, metallurgical, and nuclear material.

Despite its ubiquity, public and scientific discourse frequently conflates:
1. **Raw Natural Mine Production vs. Processed Battery Anode Output**: Natural flake graphite extraction is geographically diversified across multiple continents (China, Mozambique, Madagascar, Brazil, India, Canada, Norway), whereas downstream spherical shaping, chemical/thermal purification, pitch coating, and synthetic graphitization remain overwhelmingly concentrated in China (>90% processing share).
2. **Bulk Commodity Pricing vs. Value-Chain Grade Differentials**: Real historical unit values for natural graphite concentrate have fluctuated within a long-run mean-reverting band, whereas battery-grade coated spherical purified graphite (cSPG) and high-purity synthetic graphite command substantial processing premia reflecting high capital and energy inputs.
3. **Natural Flake vs. Synthetic Processing Energy Pathways**: Synthetic graphite requires extreme thermal energy inputs (2,800–3,000 °C) in Acheson or Longitudinal Graphitization (LWG) furnaces, while natural graphite requires significant mechanical grinding energy and suffers an intensive 30–50% mass yield loss during mechanical spheronization, followed by acid leaching (hydrofluoric HF) or ultra-high-temperature thermal purification.
4. **Process Energy vs. Regional Power Grid Carbon Intensity**: The cradle-to-gate environmental footprint of graphite is governed by a bivariate interaction between specific electrical intensity ($\text{kWh/kg}$) and the carbon intensity of the local electrical grid ($\text{g CO}_2\text{/kWh}$), meaning synthetic graphite produced on a hydro-dominated grid can exhibit a lower carbon intensity than natural graphite purified on a coal-dominated grid.

### 2. Research Scope & Accounting Boundaries (Graphite)
- **Time Horizon**: 1950–2024 for long-term historical mine production and real/nominal commodity prices; 2015–2024 for modern battery-grade anode supply and synthetic graphitization expansion.
- **Physical Commodities Analyzed**:
  - Natural Flake Graphite (Amorphous, Fine `-100 mesh`, Medium `+80 mesh`, Large `+50 mesh`, Jumbo `+32 mesh`)
  - Uncoated Spherical Purified Graphite (uSPG, 99.95% C)
  - Coated Spherical Purified Graphite (cSPG, battery-grade)
  - Synthetic Graphite Anode Material (Needle coke precursor, baked carbon, graphitized anode)
- **Accounting Boundaries**:
  - *Natural Route*: Cradle-to-gate from mine extraction, froth flotation beneficiation, micronization & spheronization, chemical leaching vs. thermal purification, and pitch coating.
  - *Synthetic Route*: Cradle-to-gate from petroleum needle coke / coal tar pitch calcination, milling, binder pitch mixing, baking (800–1,000 °C), and high-temperature graphitization (2,800–3,000 °C Acheson vs. LWG).

---

## Part II. Global Carbon Capture (CCUS & DAC)

### 1. Context and Problem Statement
Carbon Capture, Utilization, and Storage (CCUS) and Direct Air Capture (DAC) constitute foundational components of global net-zero emission trajectories. While point-source capture targets high-concentration industrial exhausts ($3.5\%\text{ to }99\%\text{ CO}_2$), atmospheric carbon dioxide removal (CDR) via Direct Air Capture extracts ultra-dilute ambient $\text{CO}_2$ ($\sim 420\text{ ppm}$ or $0.042\%\text{ CO}_2$).

Crucial empirical disparities governing the carbon capture landscape include:
1. **Low-Cost Associated Separation vs. Industrial Flue Gas Capture**: Currently operational CCUS capacity ($\sim 51\text{ Mt/yr}$) is overwhelmingly dominated by natural gas processing/sweetening ($65\%$) and enhanced oil recovery (EOR, $75\text{–}80\%$), while hard-to-abate industrial sectors (cement, steel) and DAC remain in early demonstration phases ($<5\%$ combined).
2. **Sherwood Dilution Scaling & Thermodynamic Work**: The theoretical minimum work of separation ($W_{\min} = \Delta G_{\text{mix}}$) scales logarithmically with dilution ($20.0\text{ kJ/mol}$ for air vs. $6.8\text{ kJ/mol}$ for coal flue gas), but practical equipment footprint, sorbent volumes, and air handling duties scale inversely ($\propto 1/y_0$), driving DAC capital costs to $\sim \$350\text{–}\$700\text{/t CO}_2$ compared to $\$15\text{–}\$35\text{/t}$ for pure ethanol/ammonia streams.
3. **Thermal Regeneration Dominance**: Regeneration of chemical sorbents (reboiler steam in amine scrubbing at $120^\circ\text{C}$ or oxy-calciner heat in liquid DAC at $900^\circ\text{C}$) consumes $>70\%$ of primary energy inputs across capture routes.
4. **Power Grid Carbon Coupling & Net Removal Efficiency**: Operating DAC or electric capture systems on a fossil-heavy power grid ($>400\text{ g CO}_2\text{/kWh}$) induces parasitic indirect emissions that collapse net carbon removal efficiency below $50\%$ or turn installations into net-positive greenhouse gas emitters. High net efficiency ($\ge 85\text{–}93\%$) strictly requires dedicated low-carbon thermal and electrical energy sources (geothermal, waste heat, hydropower).

### 2. Research Scope & Accounting Boundaries (CCUS & DAC)
- **Time Horizon**: 1972–2024 for commercial operational capture projects and historical deployment trajectories; 2011–2024 for modern DAC development and commercial scaling.
- **Capture Routes Analyzed**:
  - *Point-Source Post-Combustion Amine Scrubbing*: 30 wt% MEA, advanced piperazine (PZ), and Shell CANSOLV systems applied to pulverized coal power ($12.5\%\text{ CO}_2$), natural gas combined cycle NGCC ($4.1\%\text{ CO}_2$), cement kilns ($20\%\text{ CO}_2$), and SMR syngas ($45\%\text{ CO}_2$).
  - *Oxy-Fuel Combustion*: Cryogenic air separation (ASU) oxy-combustion yielding $70\text{–}85\%\text{ CO}_2$ dry flue gas.
  - *Liquid Direct Air Capture (L-DAC)*: Aqueous $\text{KOH}$ air contactor coupled to fluidized-bed causticization pellet reactor, $900^\circ\text{C}$ oxy-fired circulating fluidized-bed calciner, and steam slaker.
  - *Solid Sorbent Direct Air Capture (S-DAC)*: Modular temperature-vacuum swing adsorption (TVSA) using amine-functionalized cellulose/silica or metal-organic framework (CALF-20) sorbents regenerated at $80\text{–}110^\circ\text{C}$.
- **Transport & Storage Boundaries**:
  - *Conditioning & Transport*: Multi-stage centrifugal compression to supercritical dense phase ($11\text{–}15\text{ MPa}$, $\rho \approx 600\text{–}900\text{ kg/m}^3$), triethylene glycol (TEG) dehydration to $<50\text{ ppmv H}_2\text{O}$, and onshore/offshore pipeline transport.
  - *Permanent Storage*: Class VI deep saline aquifer injection ($>800\text{ m}$ depth) with impermeable caprock containment vs. Carbfix in-situ volcanic basalt mineralization ($>95\%$ solid calcite conversion within 2 years).
