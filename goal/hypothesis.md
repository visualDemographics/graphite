# Research Hypotheses & Falsifiable Empirical Criteria

This investigation formalizes four falsifiable hypotheses regarding global graphite production, price formation, energy intensity, and carbon coupling across the value chain. All hypotheses are evaluated using audited empirical data and formal statistical hypothesis testing.

---

### Hypothesis 1: Midstream Processing Concentration Outweighs Upstream Mining Dispersal
- **Theoretical Mechanism**: While natural flake mining occurs across diverse geographical jurisdictions (Mozambique, Madagascar, Brazil, Canada, Norway, etc.), midstream processing requires specialized scale economies, hazardous chemical handling (concentrated HF leaching), and low-cost electricity for spherical shaping.
- **Falsifiable Criterion**: China's market share in downstream spherical purified graphite (uSPG/cSPG) and synthetic anode processing exceeds its share of raw natural mine production by at least 15 percentage points ($S_{\text{processing}}^{\text{CN}} - S_{\text{mine}}^{\text{CN}} \ge 15\%$), creating an acute midstream chokepoint ($>90\%$ global processing share).
- **Empirical Verdict: CONFIRMED**
  - *Empirical Basis*: In 2024e, China accounted for $1{,}270\text{ kt}$ of $1{,}600\text{ kt}$ global natural mine extraction ($79.38\%$, USGS MCS 2025). Concurrently, China controlled $99.0\%$ of global uncoated spherical graphite (uSPG) refining (IEA Critical Minerals 2024) and $>95\%$ of synthetic graphitization capacity. The midstream concentration spread is $+19.62$ percentage points, confirming the structural processing bottleneck.

---

### Hypothesis 2: Real Bulk Flake Price Mean-Reversion vs. Processing Capture
- **Theoretical Mechanism**: Bulk natural graphite concentrate is an extractive mineral subject to long-term geological availability, technological efficiency gains in flotation, and competitive marginal pricing. Consequently, raw concentrate was hypothesized to exhibit real (CPI-deflated) price mean-reversion with zero secular upward trend ($\beta_{\text{trend}} \le 0$ or $p > 0.05$).
- **Falsifiable Criterion**: Long-term real unit values ($\text{USD}_{2023}\text{/t}$) for natural flake graphite over 1950–2024 show no secular upward trend (OLS trend slope $\beta_{\text{trend}} \le 0$ or $p > 0.05$).
- **Empirical Verdict: FALSIFIED BY EMPIRICAL DATA**
  - *Empirical Basis*: Regressing 75 annual CPI-deflated USGS unit values (1950–2024) reveals a statistically significant positive secular drift of $\hat{\beta}_{\text{trend}} = +13.88\text{ USD/yr}$ ($t = 10.98$, $p = 2.11 \times 10^{-15}$). Real prices escalated from $\sim \$350\text{/t}_{2023}$ in the 1950s to an overall multi-decade mean of $\$914.45\text{/t}_{2023}$, punctuated by geopolitical and EV-battery structural peaks in 1980 ($\$1{,}089\text{/t}$), 2011 ($\$1{,}533\text{/t}$), and 2022 ($\$2{,}168\text{/t}$). The strict hypothesis of non-trending mean-reversion is decisively rejected by the empirical record.

---

### Hypothesis 3: High-Temperature Graphitization Dominates Synthetic Process Energy & Drives Route Divergence
- **Theoretical Mechanism**: Transforming amorphous carbon precursors into a three-dimensionally ordered graphitic crystalline lattice requires extreme temperatures ($2{,}800\text{–}3{,}000\,^\circ\text{C}$). The electrical power required to sustain graphitization in resistance furnaces dominates the synthetic graphite energy balance. In contrast, natural graphite already possesses graphitic crystallinity and only requires mechanical spheronization, chemical purification, and coating.
- **Falsifiable Criterion**: High-temperature graphitization consumes $>65\%$ of cumulative cradle-to-gate electricity in the synthetic route, and synthetic anode production requires at least $2.0\times$ the specific electrical energy ($\text{kWh/kg}$) of chemically purified natural CSPG ($E_{\text{elec}}^{\text{synthetic}} / E_{\text{elec}}^{\text{natural, HF}} \ge 2.0$).
- **Empirical Verdict: PARTIALLY CONFIRMED / ARCHITECTURE-DEPENDENT**
  - *Empirical Basis*: Stage-level engineering LCA inventories confirm that graphitization is the overwhelmingly dominant electricity consumer in synthetic manufacturing: $12.50\text{ kWh/kg}$ of $13.79\text{ kWh/kg}$ ($90.6\%$) in traditional Acheson furnaces, and $7.40\text{ kWh/kg}$ of $8.69\text{ kWh/kg}$ ($85.1\%$) in continuous Longitudinal Graphitization (LWG) furnaces. However, relative to chemically purified natural CSPG ($6.77\text{ kWh/kg}$ total process electricity), the Acheson route meets the ratio threshold ($13.79 / 6.77 = 2.04\times \ge 2.0$), whereas modern energy-efficient LWG furnaces consume only $8.69 / 6.77 = 1.28\times$. The hypothesis is confirmed for traditional Acheson graphitization but rejected for continuous LWG systems.

---

### Hypothesis 4: Regional Grid Decarbonization Overrides Process Energy Disparities
- **Theoretical Mechanism**: Because specific electricity consumption is high across all battery anode routes ($6.8\text{–}16.0\text{ kWh/kg}$), the carbon intensity of the regional power grid ($\text{g CO}_2\text{/kWh}$) acts as an amplifier. Synthetic graphite graphitized using hydro-dominated electricity can achieve a cradle-to-gate carbon footprint lower than or equivalent to natural graphite processed on a coal-heavy grid.
- **Falsifiable Criterion**: Evaluated via two distinct inferential tests:
  1. *One-Sided Superiority Test*: Synthetic graphite on a low-carbon hydro grid ($30\text{ g CO}_2\text{/kWh}$) is statistically cleaner than natural CSPG on a coal-heavy grid ($800\text{ g CO}_2\text{/kWh}$) with $p < 0.05$.
  2. *Equivalence Test (TOST)*: GWP values are statistically equivalent within an equivalence margin of $\pm 3.0\text{ kg CO}_2\text{e/kg}$.
- **Empirical Verdict: SUPERIORITY CONFIRMED / EQUIVALENCE REJECTED**
  - *Empirical Basis*: Synthetic anode production on a hydro grid yields a carbon footprint of $4.90 \pm 0.45\text{ kg CO}_2\text{e/kg}$, compared to $9.62 \pm 0.55\text{ kg CO}_2\text{e/kg}$ for natural CSPG on a coal grid. The difference $\Delta = -4.72\text{ kg CO}_2\text{e/kg}$ confirms statistically significant superiority for renewable synthetic graphite ($z = -6.64, p < 10^{-10}$). However, because the difference of $-4.72\text{ kg}$ exceeds the equivalence boundary of $-3.0\text{ kg}$, formal TOST equivalence is rejected ($p_{\text{TOST}} = 1.0$). Renewable synthetic graphite is not merely equivalent to coal-grid natural graphite; it is decisively cleaner.

