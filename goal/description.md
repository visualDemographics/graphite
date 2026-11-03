# Research Goal: Empirical Analysis of Global Graphite Production, Prices, and Process Energy Intensity

## 1. Context and Problem Statement
Graphite is a critical mineral essential to modern industry and the global energy transition. It serves as the primary active anode material in lithium-ion batteries for electric vehicles (EVs) and energy storage systems (ESS), as well as a foundational refractory, metallurgical, and nuclear material.

Despite its ubiquity, public and scientific discourse frequently conflates:
1. **Raw Natural Mine Production vs. Processed Battery Anode Output**: Natural flake graphite extraction is geographically diversified across multiple continents (China, Mozambique, Madagascar, Brazil, India, Canada, Norway), whereas downstream spherical shaping, chemical/thermal purification, pitch coating, and synthetic graphitization remain overwhelmingly concentrated in China (>90% processing share).
2. **Bulk Commodity Pricing vs. Value-Chain Grade Differentials**: Real historical unit values for natural graphite concentrate have fluctuated within a long-run mean-reverting band, whereas battery-grade coated spherical purified graphite (cSPG) and high-purity synthetic graphite command substantial processing premia reflecting high capital and energy inputs.
3. **Natural Flake vs. Synthetic Processing Energy Pathways**: Synthetic graphite requires extreme thermal energy inputs (2,800–3,000 °C) in Acheson or Longitudinal Graphitization (LWG) furnaces, while natural graphite requires significant mechanical grinding energy and suffers an intensive 30–50% mass yield loss during mechanical spheronization, followed by acid leaching (hydrofluoric HF) or ultra-high-temperature thermal purification.
4. **Process Energy vs. Regional Power Grid Carbon Intensity**: The cradle-to-gate environmental footprint of graphite is governed by a bivariate interaction between specific electrical intensity ($\text{kWh/kg}$) and the carbon intensity of the local electrical grid ($\text{g CO}_2\text{/kWh}$), meaning synthetic graphite produced on a hydro-dominated grid can exhibit a lower carbon intensity than natural graphite purified on a coal-dominated grid.

## 2. Research Scope & Accounting Boundaries
- **Time Horizon**: 1950–2024 for long-term historical mine production and real/nominal commodity prices; 2015–2024 for modern battery-grade anode supply and synthetic graphitization expansion.
- **Physical Commodities Analyzed**:
  - Natural Flake Graphite (Amorphous, Fine `-100 mesh`, Medium `+80 mesh`, Large `+50 mesh`, Jumbo `+32 mesh`)
  - Uncoated Spherical Purified Graphite (uSPG, 99.95% C)
  - Coated Spherical Purified Graphite (cSPG, battery-grade)
  - Synthetic Graphite Anode Material (Needle coke precursor, baked carbon, graphitized anode)
- **Accounting Boundaries**:
  - *Natural Route*: Cradle-to-gate from mine extraction, froth flotation beneficiation, micronization & spheronization (accounting for the 1.8–2.2× raw flake input mass penalty per unit of SPG), chemical leaching vs. thermal purification, and pitch coating.
  - *Synthetic Route*: Cradle-to-gate from petroleum needle coke / coal tar pitch calcination, milling, binder pitch mixing, baking (800–1,000 °C), and high-temperature graphitization (2,800–3,000 °C Acheson vs. LWG).
  - *Financial & Price Accounting*: Nominal USD per metric tonne ($\text{USD/t}$) converted to constant real 2023 USD ($\text{USD}_{2023}\text{/t}$) using the U.S. Consumer Price Index (CPI) deflator.
  - *Energy & Carbon Accounting*: Cumulative Process Electricity ($\text{kWh/kg}$), Process Thermal Energy ($\text{MJ/kg}$), and Cradle-to-Gate Greenhouse Gas Emissions ($\text{kg CO}_2\text{e/kg}$).

## 3. Methodological Deliverable: Synoptic 9-Panel ($3 \times 3$) Matrix
A unified, publication-grade $3 \times 3$ synoptic visualization (`plots/graphite_synoptic_3x3_en.png` and `plots/graphite_synoptic_3x3_de.png`) synthesizing the three-row analytical progression:
- **Row 1 (Panels A–C)**: Global Mine Production by Country of Origin, 70-Year Historical Trajectory & Supply Regimes, and Supply-Chain Midstream Bottleneck Concentration.
- **Row 2 (Panels D–F)**: Stage-by-Stage Process Energy Intensity (Natural vs. Synthetic), Flake & Anode Grade Price Spectrum with 95% CIs, and 2D Marginal-Conserving Carbon Footprint Response Surface ($E_{\text{GHG}} = f(\text{Electricity}, \text{Grid})$).
- **Row 3 (Panels G–I)**: 70-Year Nominal vs. Real Price Trajectory with Structural Break Fit, Econometric Gradient of Value-Chain Price/Cost vs. Specific Energy & Purity, and Path-Independent Shapley Waterfall Decomposition ($\phi_j$) of Value-Chain Escalation with TOST Equivalence Testing.

