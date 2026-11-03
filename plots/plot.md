# Plot Validity & Empirical Provenance Documentation

Every figure generated in `/plots/` corresponds strictly to audited datasets in `/datasets/` and primary source literature in `/literature/`.

## Master Figure Inventory

| Output File | Panel | Core Theme | Methodological Category |
| :--- | :---: | :--- | :--- |
| `panel_a_global_mine_production_by_country.png` | Panel A | Global natural graphite mine production by country (2024e) | `Deskriptive_Vollerhebung` |
| `panel_b_70yr_production_trajectory.png` | Panel B | 74-Year mine production trajectory vs. synthetic anode emergence | `Parametrische_Wachstumsmodellierung` |
| `panel_c_supply_chain_chokepoints.png` | Panel C | Upstream mine vs. midstream processing concentration | `Wertschoepfungs_Konzentrationsanalyse` |
| `panel_d_process_electricity_intensity.png` | Panel D | Specific electricity intensity across 4 processing pathways | `Industrielle_LCA_Inventaranalyse` |
| `panel_e_grade_price_spectrum.png` | Panel E | Price spectrum across carbon purity and morphological grades | `Markterhebung_Querschnitt` |
| `panel_f_2d_carbon_response_surface.png` | Panel F | 2D GHG response surface (process power x grid emission factor) | `Bivariate_Reaktionsflaeche_Marginalerhaltend` |
| `panel_g_70yr_real_price_history.png` | Panel G | 74-Year nominal vs. real deflated price series (1950–2024) | `Oekonometrische_Trendanalyse` |
| `panel_h_econometric_price_purity_regression.png` | Panel H | Log-log price escalation vs. carbon purity defect index | `OLS_Regressionsmodellierung` |
| `panel_i_shapley_waterfall_decomposition.png` | Panel I | Sequential cost escalation (Shapley K! permutations) & TOST | `Kausale_Shapley_Dekomposition` |
| `graphite_synoptic_3x3_en.png` | All A–I | Publication-ready 9-panel synoptic analysis matrix (English) | `Synoptische_Synthese_Matrix` |
| `graphite_synoptic_3x3_de.png` | All A–I | Publication-ready 9-panel synoptic analysis matrix (German) | `Synoptische_Synthese_Matrix` |

---

## Detailed Methodological Specifications

### Panel A: Global Natural Graphite Mine Production by Country of Origin (2024e)
- **Primary Sources**: USGS Mineral Commodity Summaries 2025 (`literature/USGS_MCS_2025_Graphite.pdf`, Table 'World Mine Production and Reserves', p. 85).
- **Mathematical Formula**: Bar lengths represent reported 2024e national mine extraction P_i in thousand metric tonnes (P_tot = 1,600 kt).
- **Findings**: China accounts for 1,270 kt of 1,600 kt world mine production (79.38%), followed by Madagascar (89 kt, 5.56%), Mozambique (75 kt, 4.69%), and Brazil (68 kt, 4.25%).

### Panel B: 74-Year Historical Mine vs. Synthetic Battery Anode Trajectory (1950–2024)
- **Primary Sources**: USGS Data Series 140 (`rawdata/ds140-graphite-2022.xlsx`), USGS MCS 2025, and IEA Critical Minerals Outlook 2024.
- **Findings**: Global mine output expanded from 159 kt in 1950 to 1,600 kt in 2024. Finished synthetic battery anode active material (AAM) surged to 2,700 kt in 2024.

### Panel C: Supply Chain Chokepoints: Upstream Mining vs. Downstream Refining Control
- **Primary Sources**: USGS MCS 2025 and IEA Global Critical Minerals Outlook 2024 (p. 173).
- **Findings**: China extracts 79.4% of mined flake, but controls 99% of commercial spherical graphite (uSPG) and 97% of synthetic graphitization, confirming Hypothesis 1.

### Panel D: Process Electricity Intensity by Route (kWh/kg Anode)
- **Primary Sources**: Argonne National Laboratory GREET Model (Report ANL-22/74 Table 3, p. 18), Engels et al. (2022), and Surovtseva et al. (2022).
- **Findings**: Chemically purified natural CSPG consumes 6.77 kWh/kg intermediate (7.91 kWh/kg finished cSPG). Synthetic Acheson consumes 13.79 kWh/kg (2.04x natural), while modern LWG consumes 8.69 kWh/kg (1.28x natural).

### Panel E: Value Escalation Across the Purity and Morphology Spectrum (USD/t)
- **Primary Sources**: USGS Minerals Yearbook 2022 Table 4 (p. 32.13) for primary grades and trade benchmarks.
- **Findings**: Prices step from amorphous powder ($468/t) to fine flake ($793/t), medium flake ($1,100/t), large flake ($1,300/t), uSPG ($2,900/t), US SPG import ($4,480/t), and synthetic anode material ($5,130/t).

### Panel F: 2D Response Surface: Process Energy vs. Grid Carbon Footprint
- **Mathematical Formula**: E_GHG = 2.5 + (e * g) / 1000 (kg CO2e/kg).
- **Exact Marginal Conservation**: Analytically verified across 100 x 100 mesh (drift < 1e-10).

### Panel G: 74-Year Real Price History (1950–2024)
- **Primary Sources**: USGS DS140 and FRED Monthly CPIAUCSL.
- **Findings**: Empirical long-run real price mean is $914.90/t (2023 USD). The OLS secular drift slope is +$13.91/yr (p = 1.86e-15), decisively **falsifying Hypothesis 2** of non-trending mean-reversion.

### Panel H: Econometric Price vs. Purity Log Regression
- **Mathematical Model**: ln(Price) = 5.858 + 0.730 * [-log10(1 - Purity)]
  - Slope beta_1 = 0.730 +/- 0.102 (R2 = 0.911, p = 0.0008, n = 7).

### Panel I: Shapley Value Decomposition (K! Permutations) & Hypothesis 4 Inferential Tests
- **Shapley Value Formulation**: Evaluated across all 5! = 120 permutations (k=5). Total cost delta = $6,200/t.
- **Hypothesis 4 Test Outcomes**:
  - Superiority Test: difference = -4.72 kg CO2e/kg, z = -6.64, p < 0.001 -> **CONFIRMED** (renewable synthetic is cleaner than coal-grid natural).
  - TOST Equivalence: margin +/- 3.0 kg, p_TOST = 1.000 -> **REJECTED** (carbon disparity exceeds equivalence corridor).
