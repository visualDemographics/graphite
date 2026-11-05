# Plot Validity & Empirical Provenance Documentation

Every figure generated in `/plots/` corresponds strictly to audited datasets in `/datasets/` and primary source literature in `/literature/`.

## Master Figure Inventory

| Output File | Panel | Core Theme | Methodological Category |
| :--- | :---: | :--- | :--- |
| `panel_a_global_mine_production_by_country.png` | Panel A | Global natural graphite mine production by country (2024e) | `Deskriptive_Vollerhebung` |
| `panel_b_synthetic_throughput_by_country.png` | Panel B | Global synthetic graphite battery anode throughput by country (2024e) | `Deskriptive_Vollerhebung` |
| `panel_c_70yr_production_trajectory.png` | Panel C | 74-Year mine production trajectory vs. synthetic anode emergence | `Parametrische_Wachstumsmodellierung` |
| `panel_d_supply_chain_chokepoints.png` | Panel D | Upstream mine vs. midstream processing concentration | `Wertschoepfungs_Konzentrationsanalyse` |
| `panel_e_process_electricity_intensity.png` | Panel E | Specific electricity intensity across 4 processing pathways | `Industrielle_LCA_Inventaranalyse` |
| `panel_f_grade_price_spectrum.png` | Panel F | Price spectrum across carbon purity and morphological grades | `Markterhebung_Querschnitt` |
| `panel_g_2d_carbon_response_surface.png` | Panel G | 2D GHG response surface (process power x grid emission factor) | `Bivariate_Reaktionsflaeche_Marginalerhaltend` |
| `panel_h_70yr_real_price_history.png` | Panel H | 74-Year nominal vs. real deflated price series (1950–2024) | `Oekonometrische_Trendanalyse` |
| `panel_i_econometric_price_purity_regression.png` | Panel I | Log-log price escalation vs. carbon purity defect index | `OLS_Regressionsmodellierung` |
| `graphite_synoptic_3x3_en.png` | All A–I | Publication-ready 9-panel synoptic analysis matrix (English) | `Synoptische_Synthese_Matrix` |
| `graphite_synoptic_3x3_de.png` | All A–I | Publication-ready 9-panel synoptic analysis matrix (German) | `Synoptische_Synthese_Matrix` |

---

## Detailed Methodological Specifications

### Panel A: Global Natural Graphite Mine Production by Country of Origin (2024e)
- **Primary Sources**: USGS Mineral Commodity Summaries 2025 (`literature/USGS_MCS_2025_Graphite.pdf`, Table 'World Mine Production and Reserves', p. 85).
- **Mathematical Formula**: Bar lengths represent reported 2024e national mine extraction P_i in thousand metric tonnes (P_tot = 1,600 kt).
- **Findings**: China accounts for 1,270 kt of 1,600 kt world mine production (79.38%), followed by Madagascar (89 kt, 5.56%), Mozambique (75 kt, 4.69%), and Brazil (68 kt, 4.25%).

### Panel B: Global Synthetic Graphite Battery Anode Throughput by Country of Origin (2024e)
- **Primary Sources**: IEA Global Critical Minerals Outlook 2024 (`literature/IEA_Critical_Minerals_Outlook_2024.pdf`), Benchmark Mineral Intelligence 2024, USGS Minerals Yearbook 2022.
- **Mathematical Formula**: Bar lengths represent national synthetic battery anode active material (AAM) throughput T_i in thousand metric tonnes (T_tot = 2,660 kt).
- **Findings**: China accounts for 2,550 kt of 2,660 kt world synthetic anode throughput (95.86%), followed by Japan (45 kt, 1.69%), South Korea (22 kt, 0.83%), Rest of World (15 kt, 0.56%), United States (14 kt, 0.53%), India (8 kt, 0.30%), and Europe (6 kt, 0.23%).

### Panel C: 74-Year Historical Mine vs. Synthetic Battery Anode Trajectory (1950–2024)
- **Primary Sources**: USGS Data Series 140 (`rawdata/ds140-graphite-2022.xlsx`), USGS MCS 2025, and IEA Critical Minerals Outlook 2024.
- **Findings**: Global mine output expanded from 159 kt in 1950 to 1,600 kt in 2024. Finished synthetic battery anode active material (AAM) surged to 2,660 kt in 2024.

### Panel D: Supply Chain Chokepoints: Upstream Mining vs. Downstream Refining Control
- **Primary Sources**: USGS MCS 2025 and IEA Global Critical Minerals Outlook 2024 (p. 173).
- **Findings**: China extracts 79.4% of mined flake, but controls 99% of commercial spherical graphite (uSPG) and 97% of synthetic graphitization, confirming Hypothesis 1.

### Panel E: Process Electricity Intensity by Route (kWh/kg Anode)
- **Primary Sources**: Argonne National Laboratory GREET Model (Report ANL-22/74 Table 3, p. 18), Engels et al. (2022), and Surovtseva et al. (2022).
- **Findings**: Chemically purified natural CSPG consumes 6.77 kWh/kg intermediate (7.91 kWh/kg finished cSPG). Synthetic Acheson consumes 13.79 kWh/kg (2.04x natural), while modern LWG consumes 8.69 kWh/kg (1.28x natural).

### Panel F: Value Escalation Across the Purity and Morphology Spectrum (USD/t)
- **Primary Sources**: USGS Minerals Yearbook 2022 Table 4 (p. 32.13) for primary grades and trade benchmarks.
- **Findings**: Prices step from amorphous powder ($468/t) to fine flake ($793/t), medium flake ($1,100/t), large flake ($1,300/t), uSPG ($2,900/t), US SPG import ($4,480/t), and synthetic anode material ($5,130/t).

### Panel G: 2D Response Surface: Process Energy vs. Grid Carbon Footprint
- **Mathematical Formula**: E_GHG = 2.5 + (e * g) / 1000 (kg CO2e/kg).
- **Exact Marginal Conservation**: Analytically verified across 100 x 100 mesh (drift < 1e-10).

### Panel H: 74-Year Real Price History (1950–2024)
- **Primary Sources**: USGS DS140 and FRED Monthly CPIAUCSL.
- **Findings**: Empirical long-run real price mean is $914.90/t (2023 USD). The OLS secular drift slope is +$13.91/yr (p = 1.86e-15), decisively **falsifying Hypothesis 2** of non-trending mean-reversion.

### Panel I: Econometric Price vs. Purity Log Regression
- **Mathematical Model**: ln(Price) = 5.858 + 0.730 * [-log10(1 - Purity)]
  - Slope beta_1 = 0.730 +/- 0.102 (R2 = 0.911, p = 0.0008, n = 7).

---

# Part II. Carbon Capture (CCUS & DAC) Synoptic Visualization Inventory

| Output File | Panel | Core Theme | Methodological Category |
| :--- | :---: | :--- | :--- |
| `ccus_panel_a_global_capacity_by_country.png` | Panel A | Operational commercial CCUS capacity by country (2024e, Mt/yr) | `Deskriptive_Vollerhebung` |
| `ccus_panel_b_capacity_by_sector_and_fate.png` | Panel B | Operational capacity by source sector and storage fate (EOR vs. Dedicated) | `Deskriptive_Vollerhebung` |
| `ccus_panel_c_50yr_deployment_trajectory.png` | Panel C | 52-Year historical deployment trajectory (1972–2024) | `Parametrische_Wachstumsmodellierung` |
| `ccus_panel_d_value_chain_fate_chokepoints.png` | Panel D | Value-chain fate shift: EOR (75%) vs. dedicated saline storage hub pipeline | `Wertschoepfungs_Konzentrationsanalyse` |
| `ccus_panel_e_process_energy_intensity.png` | Panel E | Specific process energy: Electrical auxiliaries vs. thermal regeneration heat | `Ingenieurtechnische_LCA_Bilanz` |
| `ccus_panel_f_dilution_cost_spectrum.png` | Panel F | Levelized cost of capture (LCOC) across industrial and atmospheric streams | `Oekonometrische_Kostenspektroskopie` |
| `ccus_panel_g_2d_net_removal_response_surface.png` | Panel G | 2D Bivariate response surface: Net carbon removal efficiency vs. grid emissions | `Bivariate_Response_Flaeche` |
| `ccus_panel_h_shapley_cost_waterfall.png` | Panel H | Path-independent Shapley value decomposition ($K!=120$) from compression to DAC | `Shapley_Wert_Dekomposition` |
| `ccus_panel_i_sherwood_dilution_scaling_regression.png` | Panel I | Sherwood dilution scaling: $\ln(	ext{LCOC})$ vs. $-\log_{10}(y_0)$ across 5 orders of magnitude | `Oekonometrische_Regressionsmodellierung` |
| `ccus_synoptic_3x3_en.png` | Matrix | Composite 9-panel synoptic research matrix (English publication grade) | `Synoptische_Gesamtsynthese` |
| `ccus_synoptic_3x3_de.png` | Matrix | Composite 9-panel synoptic research matrix (German publication grade) | `Synoptische_Gesamtsynthese` |

### Detailed CCUS Panel Methodological Descriptions

#### Panel A: Operational Commercial CCUS Capacity by Country (2024e)
- **Data Provenance**: Global CCS Institute (2024), *Global Status of CCS 2024*, and IEA CCUS Projects Database.
- **Mathematical Formulation**:
  $$S_i = rac{C_i}{\sum_{j} C_j} 	imes 100\%$$
- **Findings**: The United States accounts for $22.0	ext{ Mt/yr}$ ($42.3\%$), followed by Brazil ($12.0	ext{ Mt/yr}$, $23.1\%$), Canada ($4.8	ext{ Mt/yr}$, $9.2\%$), and China ($4.5	ext{ Mt/yr}$, $8.7\%$). Total global commercial capacity stands at $51.0	ext{–}52.0	ext{ Mt/yr}$.

#### Panel B: Operational Capacity by Sector & Storage Fate (2024e)
- **Data Provenance**: IEA CCUS Projects Database (2024).
- **Mathematical Formulation**:
  $$C_{	ext{sector}} = C_{	ext{EOR}} + C_{	ext{Dedicated}}$$
- **Findings**: Natural gas processing represents $63.9\%$ of capacity ($33.2	ext{ Mt/yr}$), while hydrogen/ammonia accounts for $11.7\%$ ($6.1	ext{ Mt/yr}$). Hard-to-abate sectors (cement $<0.5\%$, steel $1.5\%$) and DAC ($0.08\%$) represent only $2.0\%$ combined.

#### Panel C: 52-Year Historical Deployment Trajectory (1972–2024)
- **Data Provenance**: Global CCS Institute, IEA, and project registries.
- **Mathematical Formulation**: Parametric growth fit:
  $$C(t) = C_0 \cdot \exp(k \cdot (t - t_0))$$
- **Findings**: Commercial CCUS originated in 1972 at the Terrell/Val Verde gas processing facilities for EOR in the Permian Basin ($1.3	ext{ Mt/yr}$). Offshore dedicated saline storage commenced in 1996 with Sleipner ($1.0	ext{ Mt/yr}$).

#### Panel D: Value-Chain Fate Shift: EOR (75%) vs. Dedicated Storage
- **Data Provenance**: Global CCS Institute (2024).
- **Findings**: $75\%$ of active operational capacity serves EOR, whereas $>70\%$ of the $416	ext{ Mt/yr}$ pipeline is targeted for dedicated permanent geological storage in deep saline formations.

#### Panel E: Specific Process Energy: Electric Auxiliaries vs. Thermal Duty
- **Data Provenance**: NETL Baseline Rev 4a (2022), Keith et al. (2018), Deutz & Bardow (2021).
- **Findings**: Advanced CANSOLV on coal requires $2.45	ext{ GJ}_{	ext{th}}/	ext{t}$ reboiler heat $+ 111	ext{ kWh}_{	ext{e}}/	ext{t}$ electricity; Liquid DAC requires $5.25	ext{–}8.81	ext{ GJ}_{	ext{th}}/	ext{t}$ calcination heat $+ 366	ext{ kWh}_{	ext{e}}/	ext{t}$; Solid TVSA DAC requires $6.8	ext{ GJ}_{	ext{th}}/	ext{t}$ low-temperature heat $+ 640	ext{ kWh}_{	ext{e}}/	ext{t}$ electricity.

#### Panel F: Levelized Cost of Capture (LCOC) Across Streams
- **Data Provenance**: NETL Baseline Rev 4a, House et al. (2011), IEA (2024).
- **Findings**: Near-pure streams (ethanol/ammonia) cost $\$15	ext{–}\$38	ext{/t}$; Coal flue gas costs $\$48	ext{–}\$78	ext{/t}$ ($\$63	ext{/t}$ avoided); NGCC costs $\$68	ext{–}\$110	ext{/t}$; Direct air capture costs $\$350	ext{–}\$650	ext{/t}$ ($\$500	ext{/t}$ midpoint).

#### Panel G: 2D Net Carbon Removal Surface: Power vs. Grid Emissions
- **Mathematical Formulation**:
  $$	ext{Emissions}_{	ext{indirect}} = rac{E_{	ext{elec}} \cdot g_{	ext{grid}}}{1000} \quad (	ext{kg CO}_2	ext{e/t})$$
  $$	ext{Net Removal Efficiency (\%)} = 100\% - rac{	ext{Emissions}_{	ext{indirect}}}{10.0}$$
  Runtime marginal conservation assertion verified ($< 10^{-10}$ drift).

#### Panel H: Path-Independent Shapley Cost Decomposition ($K!=120$)
- **Mathematical Formulation**: Evaluated across all $5! = 120$ permutations:
  $$\phi_i = \sum_{S \subseteq N \setminus \{i\}} rac{|S|!(|N| - |S| - 1)!}{|N|!} (v(S \cup \{i\}) - v(S))$$
- **Findings**: Base compression accounts for $\$25	ext{/t}$; Air contactor fans contribute $\$120	ext{/t}$; Sorbent replacement contributes $\$85	ext{/t}$; Thermal desorption contributes $\$115	ext{/t}$; Vacuum pumping contributes $\$65	ext{/t}$; Class VI storage/MMV contributes $\$90	ext{/t}$; Total: $\$500	ext{/t CO}_2$.

#### Panel I: Sherwood Dilution Scaling Regression
- **Data Provenance**: House et al. (2011 PNAS).
- **Mathematical Formulation**:
  $$\ln(	ext{LCOC}) = lpha + eta \cdot [-\log_{10}(y_0)]$$
- **Findings**: Slope $eta = 0.96 \pm 0.10$ ($p < 0.001$, $R^2 = 0.941$), confirming that levelized capture cost scales inversely with inlet concentration across 5 orders of magnitude.

