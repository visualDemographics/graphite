# Empirical Datasets & Data Dictionary

All active empirical datasets in `datasets/` are derived deterministically by `src/data_preparation.py` and `src/ccus_data_preparation.py` from raw files in `rawdata/` and primary source PDFs in `literature/`.

---

# Part I. Global Graphite Value Chain Datasets

## 1. `graphite_world_production_by_country.csv`
- **Source**: U.S. Geological Survey (USGS), Mineral Commodity Summaries 2025: Graphite (Natural), Table 'World Mine Production and Reserves', p. 85.
- **Fields**:
  - `country` (string): Standardized sovereign jurisdiction name.
  - `production_2023_tonnes` (float): Reported natural mine output in metric tonnes for 2023.
  - `production_2024e_tonnes` (float): Official USGS estimated mine output in metric tonnes for 2024.
  - `reserves_tonnes` (float): Economically extractable reserves in metric tonnes (-1.0 if withheld or unmeasured).
  - `is_major_producer` (integer): Indicator (1 = major producer >=10 kt or reserves >=5 Mt; 0 = other).

## 2. `graphite_synthetic_production_by_country.csv`
- **Source**: International Energy Agency (IEA), Global Critical Minerals Outlook 2024 (pp. 173–176), USGS Minerals Yearbook 2022 (p. 32.5), and Benchmark Mineral Intelligence (2024).
- **Fields**:
  - `country` (string): Manufacturing country or region.
  - `throughput_2024e_kt` (float): Estimated annual synthetic battery anode throughput/production in thousand metric tonnes (kt).
  - `share_pct` (float): Percentage share of global synthetic battery anode output.
  - `primary_producers` (string): Leading operational corporate manufacturers.
  - `data_source` (string): Primary institutional literature citation.

## 3. `graphite_historical_production_and_prices.csv`
- **Source**: USGS Data Series 140 (`rawdata/ds140-graphite-2022.xlsx`), supplemented with USGS MCS 2025 and Federal Reserve Economic Data (FRED) monthly CPI-U (`rawdata/fred_cpi_monthly.csv`).
- **Fields**:
  - `year` (integer): Observation year (1950 to 2024).
  - `nominal_usd_per_tonne` (float): Average annual USGS unit value in nominal USD per metric ton.
  - `constant_1998_usd_per_tonne` (float): Deflated real unit value in constant 1998 USD per metric ton.
  - `constant_2023_usd_per_tonne` (float): Deflated real unit value in constant 2023 USD per metric ton.
  - `world_mine_production_tonnes` (float): Global natural graphite mine production in metric tonnes.
  - `synthetic_aam_production_tonnes` (float): Estimated global synthetic graphite active anode material (AAM) production in metric tonnes (IEA Critical Minerals Outlook 2024).

## 4. `graphite_grade_price_spectrum.csv`
- **Source**: USGS Minerals Yearbook 2022, Table 4 ('Representative Yearend Graphite Prices') and industry benchmarks.
- **Fields**:
  - `grade_id` (string): Unique identifier (`AMORPHOUS`, `FINE_FLAKE`, `MEDIUM_FLAKE`, `LARGE_FLAKE`, `UNCOATED_SPG`, `US_IMPORT_SPG`, `SYNTHETIC_ANODE_IMPORT`, `COATED_CSPG_ESTIMATE`).
  - `carbon_purity_mid` (float): Midpoint fixed carbon fraction (0.0 to 1.0).
  - `price_mid_usd_t` (float): Midpoint market transaction price in USD per metric ton.
  - `is_primary_source` (integer): Flag (1 = official USGS Minerals Yearbook statistical table; 0 = secondary trade-press estimate).

## 5. `graphite_process_energy_lca.csv`
- **Source**: Argonne National Laboratory GREET Model (Report ANL-22/74 Tables 2 & 3), Engels et al. (2022), and Surovtseva et al. (2022).
- **Fields**:
  - `route` (string): Processing pathway (`Natural_Chemical_HF`, `Natural_Thermal`, `Synthetic_Acheson`, `Synthetic_LWG_Castner`).
  - `stage` (string): Distinct value chain transformation step.
  - `electricity_intermediate_kwh` (float): Specific electricity consumption per kg of intermediate stage output.
  - `electricity_cumulative_kwh` (float): Cumulative electricity consumption required per kg of finished coated battery anode material.
  - `thermal_energy_mj_per_kg` (float): Direct thermal fuel consumption in MJ per kg.
  - `mass_yield_stage_pct` (float): Percentage mass yield of primary product through the stage.
  - `cumulative_mass_factor` (float): Kilograms of starting raw material required per kilogram of stage output.

## 6. `graphite_supply_chain_flows.csv`
- **Source**: Physical mass-balance accounting across 4 functional supply tiers.
- **Fields**:
  - `tier` (string): Functional supply tier (`Ore_Extraction_Partition`, `Spheronization_Mass_Partition`, `Synthetic_Precursor_Partition`, `Global_AAM_Market_Allocation`).
  - `source` (string): Precursor material or sector node.
  - `target` (string): Output stream or allocation partition.
  - `value` (float): Mass in kg (per 1,000 kg input) or market share in percent.
  - `unit` (string): Measurement unit (`kg` or `pct`).

---

# Part II. Global Carbon Capture (CCUS & DAC) Datasets

## 7. `ccus_global_capacity_by_country.csv`
- **Source**: Global CCS Institute (2024), *Global Status of CCS 2024*, and International Energy Agency (IEA), *CCUS Projects Database 2024*.
- **Fields**:
  - `country` (string): Country name.
  - `operational_capacity_mtpa` (float): Commercial operational capture capacity in million metric tonnes per annum ($\text{Mt/yr}$).
  - `share_pct` (float): Percentage share of global operational capture capacity.
  - `pipeline_projects` (integer): Total number of commercial projects in operation and active development pipeline.
  - `key_facilities` (string): Primary operating facilities and regional hubs.

## 8. `ccus_capacity_by_sector_and_fate.csv`
- **Source**: Global CCS Institute (2024), IEA (2024).
- **Fields**:
  - `sector` (string): Industrial source category (`Natural_Gas_Processing`, `Hydrogen_Ammonia_Syngas`, `Chemicals_and_Refining`, `Bioethanol_Biofuels`, `Power_Generation`, `Iron_and_Steel`, `Cement_and_Lime`, `Direct_Air_Capture`).
  - `operational_mtpa` (float): Operational capture capacity in $\text{Mt/yr}$.
  - `eor_utilization_mtpa` (float): Volume routed to Enhanced Oil Recovery ($\text{Mt/yr}$).
  - `dedicated_storage_mtpa` (float): Volume routed to dedicated geological storage formations ($\text{Mt/yr}$).
  - `sector_share_pct` (float): Percentage of global operational capacity.
  - `purity_co2_pct` (float): Typical raw stream $\text{CO}_2$ concentration.

## 9. `ccus_historical_deployment_and_costs.csv`
- **Source**: Historical CCUS project commissioning records (1972–2024) combined with FRED monthly CPI-U inflation deflators.
- **Fields**:
  - `year` (integer): Observation year (1972 to 2024).
  - `capacity_mtpa` (float): Global cumulative operational capacity in $\text{Mt/yr}$.
  - `eor_share_pct` (float): Percentage of operational capacity utilized for EOR.
  - `dedicated_storage_share_pct` (float): Percentage routed to dedicated geological storage.
  - `nominal_cost_usd_t` (float): Average benchmark capture cost in nominal $\text{USD/t}$.
  - `constant_2023_usd_t` (float): Inflation-deflated real capture cost in constant $2023\text{ USD/t}$.
  - `milestone` (string): Key commercial or technological deployment milestone.

## 10. `ccus_dilution_price_and_work_spectrum.csv`
- **Source**: House et al. (2011 PNAS), NETL Cost and Performance Baseline Rev 4a, Wilcox (2012).
- **Fields**:
  - `stream_id` (string): Unique identifier.
  - `stream_name` (string): Detailed industrial or atmospheric source stream description.
  - `co2_concentration_pct` (float): $\text{CO}_2$ concentration in volume percent.
  - `co2_mole_fraction_y0` (float): Inlet mole fraction ($y_0$).
  - `dilution_index_log10` (float): Thermodynamic dilution index $-\log_{10}(y_0)$.
  - `w_min_kj_per_mol` (float): Gibbs free energy minimum separation work in $\text{kJ/mol CO}_2$.
  - `w_min_kwh_per_tonne` (float): Minimum thermodynamic work in $\text{kWh/t CO}_2$.
  - `actual_exergy_kwh_per_tonne` (float): Real-world specific exergy consumption in $\text{kWh/t CO}_2$.
  - `second_law_efficiency_pct` (float): Second-law thermodynamic efficiency ($\eta_{\text{II}} = W_{\min}/W_{\text{actual}}$).
  - `lcoc_min_usd_t` (float): Lower bound levelized cost of capture in $\text{USD/t}$.
  - `lcoc_max_usd_t` (float): Upper bound levelized cost of capture in $\text{USD/t}$.
  - `lcoc_mid_usd_t` (float): Midpoint levelized cost of capture in $\text{USD/t}$.
  - `capture_technology` (string): Prevailing separation technology.
  - `is_point_source` (integer): Flag (1 = industrial point source; 0 = direct air capture).

## 11. `ccus_process_energy_lca.csv`
- **Source**: NETL Baseline Rev 4a (2022), Keith et al. (2018 Joule), Deutz & Bardow (2021 Nature Energy).
- **Fields**:
  - `route` (string): Capture route identifier (`PostCombustion_Amine_MEA`, `PostCombustion_CANSOLV_Coal`, `PostCombustion_CANSOLV_NGCC`, `OxyFuel_Combustion`, `DAC_Liquid_KOH_Loop`, `DAC_Solid_Amine_TVSA`).
  - `stage` (string): Specific process transformation unit.
  - `electricity_kwh` (float): Electrical auxiliary requirement in $\text{kWh/t CO}_2$ captured.
  - `thermal_energy_gj` (float): Thermal regeneration heat duty in $\text{GJ/t CO}_2$ captured.
  - `solvent_makeup_kg` (float): Solvent or sorbent chemical makeup in $\text{kg/t CO}_2$.
  - `stage_description` (string): Technical process description.

## 12. `ccus_mass_balance_flows.csv`
- **Source**: Engineering mass-balance inventories across 4 functional CCUS value chain tiers.
- **Fields**:
  - `tier` (string): Functional tier (`Flue_Gas_Amine_Scrubbing_Partition`, `Liquid_DAC_Calcination_Loop_Partition`, `Supercritical_Compression_Dehydration_Partition`, `Subsurface_Mineralization_Trapping_Allocation`).
  - `source` (string): Inlet stream node.
  - `target` (string): Partition stream or buffer node.
  - `value` (float): Mass value in kg per 1,000 kg basis.
  - `unit` (string): Measurement unit (`kg`).

## 13. `literature_empirical_benchmarks.csv`
- **Source**: Cryptographically audited primary source citations, exact table coordinates, and verbatim quotes in `literature/`.
