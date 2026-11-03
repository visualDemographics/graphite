# Empirical Methodology & Accounting Standards: Global Graphite Supply Chain

## 1. Accounting Boundaries & Systems Definition

### 1.1 Mine Extraction to Flake Concentrate (Beneficiation)
- **Natural Flake Graphite**: Ores typically range between 5% and 15% Total Graphitic Carbon (TGC) in commercial open-pit or underground mines (e.g. Balama in Mozambique, Molo in Madagascar, Kropfmühl in Germany, Lac des Îles in Canada).
- **Froth Flotation**: Crushing, rod/ball milling, and multi-stage froth flotation with kerosene/pine oil frothers produce a graphite concentrate of 94–96% TGC.
- **Flake Sizing Classifications**:
  - Fine Flake: `-100 mesh` ($<150\,\mu\text{m}$)
  - Medium Flake: `+100 to -80 mesh` ($150\text{–}180\,\mu\text{m}$)
  - Large Flake: `+80 to -50 mesh` ($180\text{–}300\,\mu\text{m}$)
  - Extra-Large / Jumbo Flake: `+50 to +32 mesh` ($300\text{–}500\,\mu\text{m}$)

### 1.2 Downstream Anode Manufacturing & Spheronization Yield
- **Micronization and Mechanical Spheronization**:
  Natural flake concentrate (predominantly fine or medium flake) is milled to $15\text{–}20\,\mu\text{m}$ ($D_{50}$) and mechanically rounded in impact mills or classifier air mills to optimize tap density ($>0.9\text{ g/cm}^3$) and minimize BET specific surface area ($<4\text{ m}^2/\text{g}$) for battery intercalation.
- **Mass Yield Penalty**:
  Spherical shaping rounds off flake corners and edges, producing an unavoidable mass loss of 30% to 55% as fine scrap tails. Consequently, producing 1.0 tonne of Uncoated Spherical Purified Graphite (uSPG) requires **1.8 to 2.2 tonnes of 94–95% flake concentrate**:
  $$\text{Input Ratio} = \frac{1}{\text{Yield}_{\text{spheronization}}} \approx \frac{1}{0.45\text{ to }0.55} \approx 1.82\text{ to }2.22\text{ t}_{\text{flake}}/\text{t}_{\text{uSPG}}$$
  This mass-balance yield penalty is rigorously accounted for in our ETL pipeline and waterfall decomposition.

### 1.3 Purification Pathways: Chemical (HF) vs. High-Temperature Thermal
- **Chemical Hydrofluoric (HF) Leaching**:
  Dominant commercial route in China. Uses HF, $\text{HCl}$, and $\text{NaOH}$ wash sequences at 60–90 °C to leach silicate and metal impurities, raising purity from 95% to $>99.95\%$ TGC. While electricity-efficient (0.5–1.5 kWh/kg), it generates severe acidic waste effluent and hazardous fluorine byproducts.
- **Thermal Purification**:
  High-temperature heating to $2{,}500\text{–}3{,}000\,^\circ\text{C}$ in electric chlorination/fluorination atmospheres or inert argon gas, volatilizing non-carbon impurities. Clean effluent but high electricity intensity (5.0–8.0 kWh/kg in addition to spheronization power).

### 1.4 Synthetic Graphite Anode Processing & Graphitization
- **Precursor & Calcination**: High-grade petroleum needle coke or coal tar pitch calcined at 1,200–1,400 °C, milled and blended with binder pitch.
- **Shaping & Baking**: Carbon blocks or extruded green particles are baked at 800–1,000 °C to carbonize pitch binder.
- **Graphitization ($2{,}800\text{–}3{,}000\,^\circ\text{C}$)**:
  - *Acheson Resistance Furnace*: Batch furnace where carbon pack serves as electrical resistor. Slow cycle (2–3 weeks heating and cooling), consuming 10–14 kWh/kg of electrical energy.
  - *Longitudinal Graphitization (LWG / Castner)*: Current flows directly along the longitudinal axis of electrodes/containers. Reduced heat loss and continuous/semi-continuous operation consuming 6–9 kWh/kg.

---

## 2. Mathematical Formulation & Econometric Specifications

### 2.1 2D Marginal-Conserving Carbon Response Surface
Cradle-to-gate GHG intensity $E_{\text{GHG}}$ ($\text{kg CO}_2\text{e/kg}$) is modeled as a joint function of specific process electricity $e$ ($\text{kWh/kg}$) and regional grid carbon factor $g$ ($\text{g CO}_2\text{/kWh}$):
$$E_{\text{GHG}}(e, g) = e \cdot \left(\frac{g}{1000}\right) + E_{\text{thermal}} \cdot \text{EF}_{\text{fuel}} + E_{\text{direct}}$$
To satisfy Pillar 7 of the Responsible Research Protocol, any 2D visual surface is evaluated over an empirical grid with runtime assertion ensuring marginal conservation across slices:
$$\frac{1}{G} \sum_{g} E_{\text{GHG}}(e_i, g) \equiv \bar{E}(e_i) \quad (\text{runtime assert drift } < 10^{-10})$$

### 2.2 Path-Independent Shapley Value Decomposition
Value-chain price and energy escalation from raw flake to battery anode is decomposed across $K = 5$ stages:
1. Spheronization mass yield loss penalty
2. Mechanical grinding / micronization power
3. Chemical / thermal purification
4. Pitch coating & carbonization
5. Graphitization furnace differential
Because sequential waterfall bar charts are path-dependent, we calculate exact Shapley attributions over all $K! = 120$ order permutations:
$$\phi_j = \frac{1}{K!} \sum_{\pi} \left[ V(S_{\pi}^{(j)} \cup \{j\}) - V(S_{\pi}^{(j)}) \right]$$

### 2.3 Two One-Sided Tests (TOST) for Environmental Equivalence
To formally test whether renewable-grid synthetic graphite achieves carbon parity with natural graphite (rejecting both the inferiority and superiority fallacies without p-hacking):
$$z_1 = \frac{\Delta \bar{E} - (-\delta)}{\text{SE}_{\Delta}}, \quad z_2 = \frac{\delta - \Delta \bar{E}}{\text{SE}_{\Delta}}, \quad p_{\text{TOST}} = \max(1 - \Phi(z_1), 1 - \Phi(z_2))$$
with equivalence margin $\delta = 3.0\text{ kg CO}_2\text{e/kg}$.

