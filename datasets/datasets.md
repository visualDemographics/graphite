# Empirical Datasets & Data Dictionary

All active empirical datasets in `datasets/` are derived deterministically by `src/data_preparation.py` from raw files in `rawdata/` and primary source PDFs in `literature/`.

## 1. `graphite_world_production_by_country.csv`
- **Source**: U.S. Geological Survey (USGS), Mineral Commodity Summaries 2025: Graphite (Natural), Table 'World Mine Production and Reserves', p. 85.
- **Fields**:
  - `country` (string): Standardized sovereign jurisdiction name.
  - `production_2023_tonnes` (float): Reported natural mine output in metric tonnes for 2023.
  - `production_2024e_tonnes` (float): Official USGS estimated mine output in metric tonnes for 2024.
  - `reserves_tonnes` (float): Economically extractable reserves in metric tonnes (-1.0 if withheld or unmeasured).
  - `is_major_producer` (integer): Indicator (1 = major producer >=10 kt or reserves >=5 Mt; 0 = other).

## 2. `graphite_historical_production_and_prices.csv`
- **Source**: USGS Data Series 140 (`rawdata/ds140-graphite-2022.xlsx`), supplemented with USGS MCS 2025 and Federal Reserve Economic Data (FRED) monthly CPI-U (`rawdata/fred_cpi_monthly.csv`).
- **Fields**:
  - `year` (integer): Observation year (1950 to 2024).
  - `nominal_usd_per_tonne` (float): Average annual USGS unit value in nominal USD per metric ton.
  - `constant_1998_usd_per_tonne` (float): Deflated real unit value in constant 1998 USD per metric ton.
  - `constant_2023_usd_per_tonne` (float): Deflated real unit value in constant 2023 USD per metric ton.
  - `world_mine_production_tonnes` (float): Global natural graphite mine production in metric tonnes.
  - `synthetic_aam_production_tonnes` (float): Estimated global synthetic graphite active anode material (AAM) production in metric tonnes (IEA Critical Minerals Outlook 2024). Note: active anode material reflects downstream finished battery product, whereas mine production reflects upstream concentrate.

## 3. `graphite_grade_price_spectrum.csv`
- **Source**: USGS Minerals Yearbook 2022, Table 4 ('Representative Yearend Graphite Prices') and industry benchmarks.
- **Fields**:
  - `grade_id` (string): Unique identifier (e.g., `AMORPHOUS`, `FINE_FLAKE`, `MEDIUM_FLAKE`, `LARGE_FLAKE`, `UNCOATED_SPG`, `US_IMPORT_SPG`, `SYNTHETIC_ANODE_IMPORT`, `COATED_CSPG_ESTIMATE`).
  - `carbon_purity_mid` (float): Midpoint fixed carbon fraction (0.0 to 1.0).
  - `price_mid_usd_t` (float): Midpoint market transaction price in USD per metric ton.
  - `is_primary_source` (integer): Flag (1 = official USGS Minerals Yearbook statistical table; 0 = secondary trade-press estimate).

## 4. `graphite_process_energy_lca.csv`
- **Source**: Argonne National Laboratory GREET Model (Report ANL-22/74 Tables 2 & 3), Engels et al. (2022), and Surovtseva et al. (2022).
- **Fields**:
  - `route` (string): Processing pathway (`Natural_Chemical_HF`, `Natural_Thermal`, `Synthetic_Acheson`, `Synthetic_LWG_Castner`).
  - `stage` (string): Distinct value chain transformation step.
  - `electricity_intermediate_kwh` (float): Specific electricity consumption per kg of intermediate stage output.
  - `electricity_cumulative_kwh` (float): Cumulative electricity consumption required per kg of finished coated battery anode material (accounting for upstream stage mass yields).
  - `thermal_energy_mj_per_kg` (float): Direct thermal fuel consumption in MJ per kg.
  - `mass_yield_stage_pct` (float): Percentage mass yield of primary product through the stage.
  - `cumulative_mass_factor` (float): Kilograms of starting raw material required per kilogram of stage output.
  - `acid_reagent_kg_per_t` (float): Chemical acid and neutralizing reagent consumption in kg per metric ton.

## 5. `graphite_supply_chain_flows.csv`
- **Source**: Physical mass-balance accounting across 4 functional supply tiers.
- **Fields**:
  - `tier` (string): Functional supply tier (`Ore_Extraction_Partition`, `Spheronization_Mass_Partition`, `Synthetic_Precursor_Partition`, `Global_AAM_Market_Allocation`).
  - `source` (string): Precursor material or sector node.
  - `target` (string): Output stream or allocation partition.
  - `value` (float): Mass in kg (per 1,000 kg input) or market share in percent.
  - `unit` (string): Measurement unit (`kg` or `pct`).

## 6. `literature_empirical_benchmarks.csv`
- **Source**: Verbatim quotes, table coordinates, and SHA-256 verified PDF sources in `literature/`.
