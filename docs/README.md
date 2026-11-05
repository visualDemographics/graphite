# Technical Process Engineering & Diagrammatic Documentation Suite

This directory contains technical process flow models, batch control state machines, and parametric vector cross-sections illustrating industrial unit operations, machinery, and material transformations across two parallel research tracks:
1. **Global Natural & Synthetic Graphite Value Chains**
2. **Carbon Capture, Utilization, and Storage (CCUS) & Direct Air Capture (DAC)**

All mass flows, chemical reagent dosages, process temperatures, and electrical energy intensities are strictly synchronized with the repository's verified empirical datasets in [`datasets/`](file:///Users/selle/Documents/GitHub/graphite/datasets) and primary literature benchmarks in [`literature_empirical_benchmarks.csv`](file:///Users/selle/Documents/GitHub/graphite/datasets/literature_empirical_benchmarks.csv).

---

# PART I: GRAPHITE PROCESS ENGINEERING

## 1. Text-Based Process Modeling Standards (`docs/puml/`)

The process engineering models in [`docs/puml/`](file:///Users/selle/Documents/GitHub/graphite/docs/puml) are authored in PlantUML adhering to formal industrial standards:

| Diagram File | Standard / Architecture | Operational Scope | Empirical Benchmarks |
| :--- | :--- | :--- | :--- |
| **[`01_global_value_chain_topology.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/01_global_value_chain_topology.puml)** | **SysML Block Definition** (Supply Chain & Chokepoints) | End-to-end geopolitical flow from natural mine extraction ($1{,}600\text{ kt/yr}$) and petroleum needle coke precursors ($1.108\text{ t/t}$) through midstream refining chokepoints to battery gigafactories. | China controls $79.38\%$ of mining, $99.0\%$ of spherical shaping, and $95.86\%$ ($2{,}550\text{ kt}$) of synthetic anode throughput. |
| **[`02_natural_cspg_process_flow.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/02_natural_cspg_process_flow.puml)** | **ISO 10628 Process Flow Diagram (PFD)** | Cradle-to-gate natural coated spherical purified graphite (`cSPG`) flowsheet across 4 stages: Ore comminution & flotation $\rightarrow$ Air-classifier mill spheronization $\rightarrow$ HF/HCl leaching vs. thermal purification $\rightarrow$ Pitch coating & carbonization. | Basis: $1.0\text{ t cSPG}$. Cumulative Flake input: $2.534\text{ t/t}$; Cumulative Run-of-Mine ore: $24.3\text{ t/t}$. Electricity: $7.91\text{ kWh/kg}$ (HF) vs. $17.18\text{ kWh/kg}$ (Thermal). |
| **[`03_synthetic_anode_process_flow.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/03_synthetic_anode_process_flow.puml)** | **ISO 10628 Process Flow Diagram (PFD)** | Cradle-to-gate synthetic anode active material (`AAM`) flowsheet: Rotary kiln calcining ($1{,}300^\circ\text{C}$) $\rightarrow$ Milling & pitch kneading $\rightarrow$ Ring furnace baking ($1{,}000^\circ\text{C}$) $\rightarrow$ Acheson batch vs. LWG continuous graphitization ($3{,}000^\circ\text{C}$) $\rightarrow$ Magnetic de-ironing ($<50\text{ ppb Fe}$). | Basis: $1.0\text{ t AAM}$. Green needle coke: $1.108\text{ t/t}$; Pitch binder: $0.205\text{ t/t}$. Electricity: $13.79\text{ kWh/kg}$ (Acheson) vs. $8.69\text{ kWh/kg}$ (LWG, $-37.0\%$). |
| **[`04_isa88_batch_state_and_thermodynamics.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/04_isa88_batch_state_and_thermodynamics.puml)** | **ANSI/ISA-88 (IEC 61512)** Batch State Machine | Procedural state transitions (`IDLE` $\rightarrow$ `CHARGING` $\rightarrow$ `DEVOLATILIZATION` $\rightarrow$ `ASH_VOLATILIZATION` $\rightarrow$ `GRAPHITIZATION_SOAK` $\rightarrow$ `COOLING` $\rightarrow$ `UNLOADING`) coupled with solid-state carbothermal reactions and $d_{002}$ lattice contraction. | Solid-state reactions: $\text{SiO}_2 + 3\text{C} \to \text{SiC} + 2\text{CO}\uparrow$ ($1{,}600\text{–}1{,}900^\circ\text{C}$); $\text{SiC} \to \text{Si}\uparrow + \text{C}_{\text{graphite}}$ ($>2{,}500^\circ\text{C}$). Peak temp: $2{,}800\text{–}3{,}000^\circ\text{C}$. |

---

## 2. Graphite Vector Engineering Machine Cross-Sections (`docs/svg/`)

The technical drawings in [`docs/svg/`](file:///Users/selle/Documents/GitHub/graphite/docs/svg) are parametric vector graphics ($1200 \times 800\text{ px}$) generated via [`src/generate_process_svgs.py`](file:///Users/selle/Documents/GitHub/graphite/src/generate_process_svgs.py) complying with **ISO 128** cross-section hatching, stream callouts, and **ISO 7200** title blocks:

### 2.1 Mechanical Froth Flotation Cell
- **File**: [`docs/svg/machine_01_froth_flotation_cell.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/machine_01_froth_flotation_cell.svg)
- **Unit Operation**: Stage 1 Beneficiation (Run-of-Mine Ore $\rightarrow$ Flake Concentrate).
- **Engineering Features**: Cylindrical tank with conical bottom, draft-tube standpipe, rotor-stator shearing impeller, radial baffles, froth launders, and bottom tailings cone valve.
- **Microscopic Inset**: Particle-bubble three-phase contact line showing hydrophobic contact angle ($\theta_c = 75^\circ\text{–}85^\circ$) between kerosene-coated $sp^2$ basal graphite planes and air bubbles, contrasting with sinking hydrophilic silicate gangue ($\text{SiO}_2$).
- **Key Metrics**: Pulp feed $10.43\%\text{ C}$ $\rightarrow$ Froth concentrate $104.3\text{ kg/t ore}$ ($94\text{–}97\%\text{ C}$); Tailings underflow $894.2\text{ kg/t}$ ($89.4\%$ gangue loss). Electricity: $0.484\text{ kWh/kg concentrate}$ ($1.352\text{ kWh/kg cSPG}$).

### 2.2 Impact Air-Classifier Mill (ACM)
- **File**: [`docs/svg/machine_02_spheronization_acm_mill.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/machine_02_spheronization_acm_mill.svg)
- **Unit Operation**: Stage 2 Mechanical Spheronization (Flake Concentrate $\rightarrow$ Uncoated Spherical `uSPG`).
- **Engineering Features**: High-speed peripheral hammer/pin rotor disc ($15\text{–}25\text{ m/s}$ tip speed), serrated stator impact ring liner, internal draft tube creating toroidal recirculation loops, and top variable-speed squirrel-cage classifier wheel.
- **Morphology Evolution Inset**: 4-step transformation from flat high-aspect platelet ($1:20$ to $1:50$) through edge cleavage buckling to progressive "cabbage-fold" rolling into $15.0\,\mu\text{m}$ spheres.
- **Key Metrics**: Feed requirement: $2.22\text{ t flake/t uSPG}$. Core shaping yield: $45.05\%$ ($1.00\text{ t uSPG}$); Cleavage scrap fines loss: $54.73\%$ ($1.215\text{ t scrap/t uSPG}$); Filter dust: $0.22\%$. Electricity: $1.899\text{ kWh/kg uSPG}$ ($2.167\text{ kWh/kg cSPG}$).

### 2.3 Agitated HF/HCl Acid Leaching Reactor
- **File**: [`docs/svg/machine_03_hf_acid_leaching_reactor.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/machine_03_hf_acid_leaching_reactor.svg)
- **Unit Operation**: Stage 3A Chemical Purification (`uSPG` $95\%\text{ C} \rightarrow 99.95\%\text{ C}$).
- **Engineering Features**: Carbon-steel pressure shell, steam heating jacket ($60\text{–}90^\circ\text{C}$), corrosion-resistant fluoropolymer lining (PTFE/PVDF), dual pitched-blade turbine impellers, internal anti-vortex baffles, chemical dip-tubes, and top $\text{SiF}_4/\text{HF}$ gas scrubber vent.
- **Chemistry Inset**: Stoichiometric dissolution reactions:
  $$\text{SiO}_2 + 4\text{ HF} \to \text{SiF}_4\uparrow + 2\text{ H}_2\text{O}$$
  $$\text{SiO}_2 + 6\text{ HF} \to \text{H}_2[\text{SiF}_6]_{(\text{aq})} + 2\text{ H}_2\text{O}$$
  $$\text{Fe}_2\text{O}_3 + 6\text{ HCl} \to 2\text{ FeCl}_{3(\text{aq})} + 3\text{ H}_2\text{O}$$
  $$\text{Effluent Neutralization: } 2\text{ HF} + \text{Ca(OH)}_2 \to \text{CaF}_{2(\text{s})}\downarrow + 2\text{ H}_2\text{O}$$
- **Key Metrics**: Reagents per ton `cSPG`: $180\text{ kg HF} + 200\text{ kg HCl} + 100\text{ kg HNO}_3$ + $400\text{ kg CaO}$ slaked lime. Stage yield: $88.5\%$. Electricity: $0.276\text{ kWh/kg}$; Fuel: $0.955\text{ MJ/kg}$.

### 2.4 Acheson Batch vs. Longitudinal Graphitization (LWG) Furnaces
- **File**: [`docs/svg/machine_04_acheson_vs_lwg_furnace.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/machine_04_acheson_vs_lwg_furnace.svg)
- **Unit Operation**: Stage 3 Synthetic High-Temperature Graphitization ($2{,}800\text{–}3{,}000^\circ\text{C}$).
- **Engineering Features**: Dual comparative layout:
  - **Left (Acheson Batch)**: Refractory U-trough, water-cooled end electrodes, cylindrical graphite crucibles embedded in granular resistor coke bed, thick silicon-carbide/sand thermal blanket ($15\text{–}25\text{ day}$ cycle time).
  - **Right (LWG / Castner Continuous)**: Hydraulic ram clamping ($10\text{–}30\text{ MPa}$), direct axial current flow ($50\text{–}120\text{ kA}$) through the active carbon column (Joule self-heating $I^2 R$), stationary carbon black insulation shell ($3\text{–}5\text{ day}$ turnover).
- **Key Metrics**: Acheson Electricity: $12.50\text{ kWh/kg}$ (thermal efficiency $\sim 30\%$, total route $13.79\text{ kWh/kg}$). LWG Electricity: $7.40\text{ kWh/kg}$ (thermal efficiency $50\text{–}60\%$, total route $8.69\text{ kWh/kg}$, a $-40.8\%$ power reduction).

---

## 3. Graphite Material & Microstructural Cross-Sections (`docs/svg/`)

### 3.1 Natural Flake $\rightarrow$ `uSPG` $\rightarrow$ Coated `cSPG` Morphology
- **File**: [`docs/svg/material_01_natural_flake_to_cspg_morphology.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/material_01_natural_flake_to_cspg_morphology.svg)
- **Scale**: SEM Particle Cross-Section ($\mu\text{m}$ scale).
- **Microstructural Progression**:
  1. **Raw Natural Flake ($150\text{–}300\,\mu\text{m}$)**: Flat, crystalline layered platelet with high aspect ratio ($1:20$ to $1:50$), exposed reactive prismatic edges, and interstitial ash defects ($\text{SiO}_2, \text{Fe}_2\text{O}_3$). Tap density: $0.35\text{–}0.45\text{ g/cm}^3$.
  2. **Uncoated Spherical `uSPG` ($D_{50} = 15.0\,\mu\text{m}$)**: Concentric "cabbage/onion-fold" lamellae enclosing micro-cavities; ash defects chemically leached to $\ge 99.95\%\text{ C}$. Tap density: $0.95\text{–}1.02\text{ g/cm}^3$. High BET area ($6.5\text{–}9.0\text{ m}^2\text{/g}$) causes excessive first-cycle capacity loss ($>15\%$).
  3. **Pitch-Coated `cSPG` ($D_{50} = 15.5\,\mu\text{m}$)**: Crystalline folded core hermetically sealed by an isotropic $20\text{–}50\text{ nm}$ amorphous pitch shell ($5\text{ wt\%}$ petroleum pitch at $1{,}100^\circ\text{C}$). BET surface area drops by $-70\%$ ($1.8\text{–}2.5\text{ m}^2\text{/g}$), stabilizing the Solid Electrolyte Interphase (SEI) and achieving Initial Coulombic Efficiency (ICE) $\ge 92.5\%$.

### 3.2 Crystallographic Lattice: Turbostratic to Hexagonal $ABAB$ Registry
- **File**: [`docs/svg/material_02_turbostratic_to_hexagonal_crystal_lattice.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/material_02_turbostratic_to_hexagonal_crystal_lattice.svg)
- **Scale**: Atomic & Nanoscale Lattice Cross-Section ($\text{\AA}$ scale).
- **Crystallographic Transition**:
  - **Turbostratic Carbon ($1{,}000^\circ\text{C}$)**: Curved, wrinkled $sp^2$ ribbons with rotational stacking disorder, heteroatom sulfur/nitrogen cross-links, expanded interlayer distance $d_{002} > 0.3440\text{ nm}$, crystallite dimensions $L_c < 5\text{ nm}, L_a < 10\text{ nm}$, and graphitization degree $g = 0\%$.
  - **Bernal Hexagonal Graphite ($3{,}000^\circ\text{C}$)**: Flat graphene planes aligned in perfect $ABAB$ stacking (Space Group $P6_3/mmc$), $d_{002} = 0.3354\text{ nm}$ ($-2.5\%$ contraction), $c = 0.6708\text{ nm}$, $L_c > 25\text{–}45\text{ nm}, L_a > 50\text{–}100\text{ nm}$, and graphitization degree $g > 93\%$ via the Mering-Maire relationship:
    $$g = \frac{0.3440 - d_{002}}{0.3440 - 0.3354} \times 100\%$$
  - **Lithium Intercalation**: Illustrates Stage-1 $\text{LiC}_6$ stoichiometry ($372\text{ mAh/g}$ theoretical capacity) with golden $\text{Li}^+$ ions accommodated between planar basal sheets.

---

# PART II: CARBON CAPTURE, UTILIZATION & STORAGE (CCUS) & DAC

## 4. Text-Based Process Modeling Standards for CCUS (`docs/puml/`)

The process engineering models in [`docs/puml/`](file:///Users/selle/Documents/GitHub/graphite/docs/puml) for CCUS and Direct Air Capture (DAC) adhere to ISO 10628 PFD, ANSI/ISA-88 batch procedure, and SysML value chain topologies:

| Diagram File | Standard / Architecture | Operational Scope | Empirical Benchmarks |
| :--- | :--- | :--- | :--- |
| **[`ccus_01_global_source_to_sink_topology.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/ccus_01_global_source_to_sink_topology.puml)** | **SysML Block Definition** (Global CCUS Source-to-Sink) | Geopolitical flow from point sources ($51.1\text{ Mt/yr}$) and ambient air ($0.04\text{ Mt/yr}$) through transport pipelines ($>8{,}000\text{ km}$) to geological storage fates and utilization sinks. | Operational capacity is concentrated in low-hanging fruit ($65\%$ gas processing, $12\%$ ammonia); dedicated saline storage expands from $<25\%$ to $>70\%$ ($416\text{ Mt/yr}$) in development pipeline. |
| **[`ccus_02_post_combustion_amine_process_flow.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/ccus_02_post_combustion_amine_process_flow.puml)** | **ISO 10628 Process Flow Diagram (PFD)** | Cradle-to-gate post-combustion chemical absorption flowsheet: DCC quench & NaOH SO2 polish $\rightarrow$ Structured-packing Mellapak absorber $\rightarrow$ Cross-heat exchanger $\rightarrow$ Thermal stripper reboiler $\rightarrow$ Condenser, TEG dehydration $\rightarrow$ 8-stage supercritical compressor ($15.3\text{ MPa}$). | Basis: $1{,}000\text{ kg CO}_2$ captured (NETL Case B12B.90). LP steam reboiler duty: $2.45\text{ GJ}_{\text{th}}\text{/t}$ ($70.4\%$ of thermal energy). Booster fan: $30.9\text{ kWh}_{\text{e}}\text{/t}$. Compressor: $80.1\text{ kWh}_{\text{e}}\text{/t}$. |
| **[`ccus_03_direct_air_capture_ldac_vs_sdac_flow.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/ccus_03_direct_air_capture_ldac_vs_sdac_flow.puml)** | **ISO 10628 Process Flow Diagram (PFD)** | Dual archetype comparison: Left: Liquid KOH / $\text{Ca(OH)}_2$ pellet reactor and $900^\circ\text{C}$ oxy-calciner loop (Keith et al. 2018). Right: Solid sorbent amine nanofibril monolith TVSA matrix (Deutz & Bardow 2021). | Basis: $1{,}000\text{ kg CO}_2$ from $420\text{ ppm}$ air. Liquid DAC: $5.25\text{–}8.81\text{ GJ}_{\text{th}}\text{/t}$ ($900^\circ\text{C}$) + $361\text{–}440\text{ kWh}_{\text{e}}\text{/t}$. Solid DAC: $5.76\text{–}7.50\text{ GJ}_{\text{th}}\text{/t}$ ($100^\circ\text{C}$) + $400\text{–}650\text{ kWh}_{\text{e}}\text{/t}$ + net $+2.0\text{ t H}_2\text{O/t CO}_2$. |
| **[`ccus_04_isa88_tvsa_cycle_and_thermodynamics.puml`](file:///Users/selle/Documents/GitHub/graphite/docs/puml/ccus_04_isa88_tvsa_cycle_and_thermodynamics.puml)** | **ANSI/ISA-88 (IEC 61512)** Batch State Machine | 6-state cyclic TVSA procedure (`IDLE_STANDBY` $\rightarrow$ `ADSORPTION_BLOWING` $\rightarrow$ `CHAMBER_EVACUATION` $\rightarrow$ `STEAM_HEATING_DESORPTION` $\rightarrow$ `COOLING_REPRESSURIZATION` $\rightarrow$ `PURGE_VALVE_RESET`) with thermodynamic Gibbs separation work equations. | Minimum Gibbs work: DAC ($420\text{ ppm}$) $W_{\text{min}} = 20.3\text{ kJ/mol} = 128\text{ kWh/t}$; Flue gas ($12.5\%$) $W_{\text{min}} = 7.57\text{ kJ/mol} = 47.8\text{ kWh/t}$. Second-Law efficiency $\eta_{\text{II}} \approx 6.5\text{–}9.2\%$ (DAC) vs $18.5\text{–}24.0\%$ (Amine). |

---

## 5. CCUS Vector Engineering Machine Cross-Sections (`docs/svg/`)

The technical drawings in [`docs/svg/`](file:///Users/selle/Documents/GitHub/graphite/docs/svg) are parametric vector graphics ($1200 \times 800\text{ px}$) generated via [`src/generate_ccus_svgs.py`](file:///Users/selle/Documents/GitHub/graphite/src/generate_ccus_svgs.py) complying with **ISO 128** cross-section hatching and **ISO 7200** title blocks:

### 5.1 Post-Combustion Amine Packed Absorber & Thermal Stripper
- **File**: [`docs/svg/ccus_machine_01_packed_amine_absorber_stripper.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/ccus_machine_01_packed_amine_absorber_stripper.svg)
- **Unit Operation**: Point-Source Flue Gas Chemical Absorption & Thermal Regeneration (NETL Case B12B.90 / CANSOLV).
- **Engineering Features**: Left: Carbon-steel absorption column ($D = 9\text{ m}$, $H = 45\text{ m}$), bottom gas distributor, two Mellapak 250X structured packing beds, intercooling collector/redistributor to control the $52^\circ\text{C}$ exothermic bulge, top water wash tray for amine aerosol retention ($<1\text{ ppmv}$). Center: Plate-and-frame Lean/Rich cross heat exchanger ($\Delta T_{\text{approach}} = 5^\circ\text{C}$). Right: Thermal stripper column ($D = 6\text{ m}$), kettle steam reboiler bundle ($2.45\text{ GJ}_{\text{th}}\text{/t}$), overhead condenser, and reflux accumulator.
- **Key Metrics**: Capture efficiency: $90.0\%$; Specific steam duty: $2.45\text{ GJ}_{\text{th}}\text{/t CO}_2$; Auxiliary power: $111.0\text{ kWh}_{\text{e}}\text{/t CO}_2$; Solvent loss: $<0.5\text{ kg/t CO}_2$.

### 5.2 Solid Sorbent Direct Air Capture (S-DAC) Modular TVSA Contactor Block
- **File**: [`docs/svg/ccus_machine_02_dac_air_contactor_tvsa_module.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/ccus_machine_02_dac_air_contactor_tvsa_module.svg)
- **Unit Operation**: Direct Air Capture via Temperature-Vacuum Swing Adsorption (Climeworks Orca / Deutz & Bardow 2021).
- **Engineering Features**: Modular shipping-container housing, inlet multi-blade axial fan bank ($1.2\text{ m/s}$ air velocity), front and rear hermetic louvers with pneumatic bladder seals, solid amine-functionalized nanofibrillated cellulose monolith cassettes, internal steam jacket channels ($95\text{–}100^\circ\text{C}$), vacuum header plenum with roots blowers ($0.15\text{ bar}$), and bottom condensed water collector.
- **Key Metrics**: Air processed: $1.6 \times 10^6\text{ m}^3\text{/t CO}_2$; Specific thermal duty: $5.76\text{–}7.50\text{ GJ}_{\text{th}}\text{/t CO}_2$ (low-grade heat @ $100^\circ\text{C}$); Electric consumption: $400\text{–}650\text{ kWh}_{\text{e}}\text{/t CO}_2$; Net water byproduct: $+1.5\text{–}2.5\text{ t H}_2\text{O/t CO}_2$.

### 5.3 Liquid DAC Oxy-Fired Calciner & Fluidized Bed Pellet Reactor
- **File**: [`docs/svg/ccus_machine_03_oxy_calciner_fluidized_bed_pellet_reactor.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/ccus_machine_03_oxy_calciner_fluidized_bed_pellet_reactor.svg)
- **Unit Operation**: High-Temperature Calcite De-carbonation & Causticization (Carbon Engineering / Keith et al. 2018).
- **Engineering Features**: Left: Fluidized-bed pellet reactor with conical bottom, draft tube, recirculating calcite seed sand, and drained spherical $\text{CaCO}_3$ pellet discharge ($0.8\text{–}1.2\text{ mm}$, $90\text{ wt\%}$ solids). Center: Exothermic lime slaker ($\text{CaO} + \text{H}_2\text{O} \to \text{Ca(OH)}_2$, $\Delta H = -65\text{ kJ/mol}$). Right: Oxy-fired circulating fluidized bed calciner ($900^\circ\text{C}$ refractory brick riser, natural gas oxy-combustion in pure $\text{O}_2$ from ASU), cyclone separator, and overhead steam condensing quench.
- **Key Metrics**: Thermal fuel input: $5.25\text{–}8.81\text{ GJ}_{\text{th}}\text{/t CO}_2$; ASU electricity: $110.0\text{ kWh}_{\text{e}}\text{/t CO}_2$; Operating temperature: $900^\circ\text{C}$; LCOC: $\$190\text{–}\$232\text{/t CO}_2$.

### 5.4 Supercritical CO2 Compressor Train & EPA Class VI Geological Storage Well
- **File**: [`docs/svg/ccus_machine_04_supercritical_compressor_and_class_vi_well.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/ccus_machine_04_supercritical_compressor_and_class_vi_well.svg)
- **Unit Operation**: Multi-Stage Dense-Phase Compression & Deep Subsurface Geologic Injection (NETL 2022 / USGS 2013).
- **Engineering Features**: Left: 8-stage integrally geared centrifugal compressor ($0.18 \to 8.0\text{ MPa}$), interstage coolers, TEG dehydration contactor tower ($<50\text{ ppmv H}_2\text{O}$), and dense-phase booster pump discharging at $15.3\text{ MPa}$ ($2{,}217\text{ psia}$, fluid density $820\text{ kg/m}^3$). Right: EPA Class VI injection well cross-section down to $2{,}000\text{ m}$ depth, showing surface casing protecting freshwater USDW aquifers ($0\text{–}150\text{ m}$), $300\text{ m}$ thick impermeable shale caprock confining zone, 13Cr corrosion-resistant tubing, retrievable downhole packer, and perforated saline sandstone reservoir with expanding supercritical plume.
- **Key Metrics**: Discharge pressure: $15.3\text{ MPa}$; Specific compression electricity: $80.1\text{ kWh}_{\text{e}}\text{/t CO}_2$; Reservoir depth: $>1{,}800\text{ m}$; Geological retention probability: $>99\%$ over $1{,}000$ years.

---

## 6. CCUS Material & Chemical Transformations (`docs/svg/`)

### 6.1 Molecular Chemisorption: Amine Speciation vs. Diamine-MOF Isotherm
- **File**: [`docs/svg/ccus_material_01_solid_sorbent_mof_vs_liquid_amine_speciation.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/ccus_material_01_solid_sorbent_mof_vs_liquid_amine_speciation.svg)
- **Scale**: Molecular Reaction Coordinate & Pore Channel Physics.
- **Chemical Progression**:
  - **Pathway 1 (Carbamate)**: $2\text{ R-NH}_2 + \text{CO}_2 \rightleftharpoons \text{R-NHCOO}^- + \text{R-NH}_3^+$ via zwitterion intermediate; stoichiometric limit $\alpha = 0.50\text{ mol CO}_2\text{/mol amine}$, $\Delta H_{\text{abs}} = -84.5\text{ kJ/mol}$, high thermal regeneration barrier at $120^\circ\text{C}$.
  - **Pathway 2 (Bicarbonate)**: $\text{R}_1\text{R}_2\text{R}_3\text{N} + \text{CO}_2 + \text{H}_2\text{O} \rightleftharpoons \text{HCO}_3^- + \text{R}_1\text{R}_2\text{R}_3\text{NH}^+$; stoichiometric limit $\alpha = 1.00\text{ mol/mol}$ ($2\times\text{ MEA}$), $\Delta H_{\text{abs}} = -62\text{ kJ/mol}$, $-25\%$ lower regeneration duty.
  - **Diamine-Appended MOF ($\text{mmen-Mg}_2(\text{dobpdc})$)**: Cooperative 1D ammonium carbamate chain formation along hexagonal pore channels ($d_{\text{pore}} \approx 2.1\text{ nm}$); sharp step-shaped adsorption isotherm at $P_{\text{step}} = 0.42\text{ mbar}$ ($420\text{ ppmv}$); enables $3.2\text{ mmol/g}$ working capacity with mild temperature swing ($\Delta T < 50^\circ\text{C}$).

### 6.2 Subsurface Geological Trapping Chronology & Basaltic Mineral Carbonation
- **File**: [`docs/svg/ccus_material_02_geological_trapping_and_mineral_carbonation_lattice.svg`](file:///Users/selle/Documents/GitHub/graphite/docs/svg/ccus_material_02_geological_trapping_and_mineral_carbonation_lattice.svg)
- **Scale**: Multi-Century Trapping Security Timeline ($10^0\text{–}10^4\text{ yr}$) & Rhombohedral Calcite Crystal Lattice.
- **Trapping Mechanics & Mineralization Kinetics**:
  - **4-Stage Trapping Timeline**: Structural/stratigraphic trapping dominant during injection ($70\text{–}85\%$) decays as capillary residual trapping ($10\text{–}100\text{ yr}$) and solubility dissolution trapping ($100\text{–}1{,}000\text{ yr}$) take over, culminating in permanent mineral trapping ($>10{,}000\text{ yr}$).
  - **Basaltic In-Situ Carbonation (Carbfix / Matter et al. 2016 Science)**: Co-injected water-dissolved $\text{CO}_2$ ($\text{H}_2\text{CO}_3$) rapidly leaches divalent cations ($\text{Ca}^{2+}, \text{Mg}^{2+}, \text{Fe}^{2+}$) from basaltic silicates (olivine, plagioclase), precipitating solid calcite ($\text{CaCO}_3$), magnesite ($\text{MgCO}_3$), and siderite ($\text{FeCO}_3$).
  - **Empirical Benchmark**: $>95\%$ in-situ conversion of injected $\text{CO}_2$ to solid carbonate stone achieved within $<2$ years with $25\text{ t H}_2\text{O/t CO}_2$, eliminating buoyant gas migration and long-term caprock integrity risks.

---

# PART III: DETERMINISTIC RE-GENERATION & PIPELINE AUDIT

## 7. Execution Commands

To recompile all SVG vector drawings across both tracks:
```bash
# Graphite Process SVGs (6 drawings)
.venv/bin/python3 src/generate_process_svgs.py

# CCUS & DAC Process SVGs (6 drawings)
.venv/bin/python3 src/generate_ccus_svgs.py
```

To run the complete automated 9-check research pipeline audit:
```bash
.venv/bin/python3 .agents/skills/responsible-research/scripts/audit_research_pipeline.py
```
