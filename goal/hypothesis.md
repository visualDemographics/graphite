# Research Hypotheses & Falsifiable Empirical Criteria

This document formalizes the falsifiable hypotheses, theoretical mechanisms, empirical criteria, and verified statistical verdicts across both research tracks under the Responsible Empirical Research Protocol.

---

# Part I. Global Graphite Economy Hypotheses

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

---

# Part II. Global Carbon Capture (CCUS & DAC) Hypotheses

### Hypothesis CCUS-1: Upstream Low-Cost Gas Processing Dominates Current Deployment over Hard-to-Abate Sectors
- **Theoretical Mechanism**: Early commercial CCUS projects concentrated in natural gas sweetening and fertilizer production because acid gas removal is an intrinsic operational requirement yielding concentrated $\text{CO}_2$ ($>40\text{–}98\%$), resulting in minimal capture costs ($\$15\text{–}\$35\text{/t}$) that were monetized via Enhanced Oil Recovery (EOR). In contrast, capturing dilute point sources ($3.5\text{–}20\%\text{ CO}_2$) in power, cement, and steel requires extensive thermal solvent regeneration and capital equipment without offsetting hydrocarbon revenues.
- **Falsifiable Criterion**: Natural gas processing and chemical fertilizer production represent $>65\%$ of global operational commercial capture capacity in 2024, whereas hard-to-abate industrial point sources (cement, iron/steel) and direct air capture represent $<5\%$ of operational tonnage.
- **Empirical Verdict on CCUS Hypothesis 1: CONFIRMED**
  - *Empirical Basis*: Operational capacity tracked by the Global CCS Institute (2024) and IEA projects database confirms that natural gas processing accounts for $65.0\%$ ($33.2\text{ Mt/yr}$) and fertilizer/hydrogen accounts for $12.0\%$ ($6.1\text{ Mt/yr}$) of the $51.0\text{ Mt/yr}$ global commercial total. Cement ($<0.5\%$, $\sim 0.1\text{ Mt/yr}$), iron/steel ($1.5\%$, $0.8\text{ Mt/yr}$), and DAC ($0.03\%$, $0.015\text{ Mt/yr}$) collectively represent only $2.03\% < 5\%$ of operational deployment, confirming severe application concentration.

---

### Hypothesis CCUS-2: Empirical Capture Cost Follows Sherwood Dilution Scaling Across Five Orders of Magnitude
- **Theoretical Mechanism**: Following the classic Sherwood separation principle (House et al. 2011; Gruber 2008), the economic cost of gas separation is governed not merely by logarithmic thermodynamic minimum work ($\Delta G_{\text{mix}} \propto \ln(1/y_0)$), but by the physical volume of carrier gas processed ($V_{\text{gas}} \propto 1/y_0$), requiring larger contactor footprints, higher solvent circulation, and greater parasitic fan duties.
- **Falsifiable Criterion**: Levelized cost of capture ($\text{LCOC}$, $\text{USD/t CO}_2$) across industrial and atmospheric streams demonstrates a statistically significant positive log-log linear scaling against the dilution defect index $-\log_{10}(y_{\text{CO}_2})$ with $R^2 \ge 0.85$ and slope coefficient $b \ge 0.50$ ($p < 0.001$).
- **Empirical Verdict on CCUS Hypothesis 2: CONFIRMED**
  - *Empirical Basis*: Regressing empirical LCOC midpoints across 8 distinct streams (ranging from $99\%$ fermentation off-gas at $\$20\text{/t}$ through $12.5\%$ coal flue gas at $\$65\text{/t}$ to $420\text{ ppm}$ ambient air at $\$450\text{/t}$) against $-\log_{10}(y_{\text{CO}_2})$ yields $\ln(\text{LCOC}) = 2.85 + 0.96 \times [-\log_{10}(y_{\text{CO}_2})]$ with $R^2 = 0.941$ and $p = 4.8 \times 10^{-5}$. The empirical slope $b = 0.96 \approx 1.0$ matches the classical Sherwood inverse concentration scaling exponent.

---

### Hypothesis CCUS-3: Thermal Regeneration Accounts for Over 70% of Capture Primary Energy Input
- **Theoretical Mechanism**: Chemical absorption systems (amine carbamate formation) and thermochemical sorption cycles (calcium looping) involve strongly exothermic forward capture reactions ($\Delta H_{\text{abs}} = -50\text{ to }-180\text{ kJ/mol}$). Consequently, the reverse stripping reaction consumes massive quantities of latent and sensible heat to regenerate the lean sorbent, far exceeding the mechanical pumping and compression auxiliary power duties.
- **Falsifiable Criterion**: Thermal regeneration duty accounts for $>70\%$ of the primary energy equivalent across post-combustion amine capture ($2.4\text{–}3.5\text{ GJ}_{\text{th}}\text{/t}$) and liquid DAC ($5.25\text{–}8.81\text{ GJ}_{\text{th}}\text{/t}$).
- **Empirical Verdict on CCUS Hypothesis 3: CONFIRMED**
  - *Empirical Basis*: In NETL Baseline Rev 4a (Case B12B.90), low-pressure steam extraction for the CANSOLV reboiler consumes $2.40\text{–}2.50\text{ GJ}_{\text{th}}/\text{t CO}_2$ ($\sim 694\text{ kWh}_{\text{th}}/\text{t}$), compared to $111.0\text{ kWh}_{\text{e}}/\text{t}$ total capture and compression electricity. On an equivalent thermal basis ($\eta_{\text{th}} = 38\%$), thermal heat accounts for $70.4\%$ of capture primary energy. In Keith et al. (2018) liquid DAC, natural gas calcination requires $5.25\text{–}8.81\text{ GJ}_{\text{th}}/\text{t CO}_2$ compared to $366\text{ kWh}_{\text{e}}/\text{t}$ ($1.32\text{ GJ}_{\text{e}}/\text{t}$), representing $79.9\%\text{ to }87.0\%$ of total energy input.

---

### Hypothesis CCUS-4: Grid Carbon Intensity Determines Direct Air Capture Net Removal Feasibility
- **Theoretical Mechanism**: Direct Air Capture processes $1.5\text{–}2.5\text{ million m}^3$ of air per tonne of $\text{CO}_2$ captured, consuming $450\text{–}750\text{ kWh}_{\text{e}}/\text{t}$ in electricity plus $1.5\text{–}2.5\text{ MWh}_{\text{th}}/\text{t}$ in thermal energy. If supplied by electricity with carbon intensity $g > 400\text{ g CO}_2\text{/kWh}$, upstream indirect emissions negate a large portion of the gross captured carbon.
- **Falsifiable Criterion**:
  1. *Superiority Test*: DAC powered by low-carbon geothermal/hydro energy achieves statistically superior net removal efficiency ($>85\%$) compared to fossil-grid configurations ($<50\%$) with $p < 0.001$.
  2. *Equivalence Test (TOST)*: Net carbon removal efficiency on a coal grid ($800\text{ g/kWh}$) is statistically non-equivalent to clean-grid operation within an equivalence margin of $\pm 20\%$.
- **Empirical Verdict on CCUS Hypothesis 4: SUPERIORITY CONFIRMED / EQUIVALENCE REJECTED**
  - *Empirical Basis*: Operational LCA inventories from Deutz & Bardow (2021) demonstrate net removal efficiencies of $93.1\%$ at Hellisheiði (geothermal) and $85.4\%$ at Hinwil (waste heat). Under a standard grid carbon intensity of $500\text{ g CO}_2\text{/kWh}$, net removal falls to $38.2\%$ (an emissions penalty of $618\text{ kg CO}_2\text{e/t}$ captured), and exceeds $100\%$ (net positive emitter) on a coal-heavy grid ($800\text{ g/kWh}$). The difference $\Delta = -54.9\text{ percentage points}$ confirms superiority for low-carbon energy ($z = 18.2, p < 10^{-15}$), while TOST equivalence is rejected ($p_{\text{TOST}} = 1.0$).
