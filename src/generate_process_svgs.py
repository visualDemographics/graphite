#!/usr/bin/env python3
"""Parametric Vector SVG Engineering Cross-Section Generator for Global Graphite.

Generates 6 publication-grade, resolution-independent vector technical drawings
adhering to ISO 128 engineering cross-sectioning and hatching conventions:
1. machine_01_froth_flotation_cell.svg
2. machine_02_spheronization_acm_mill.svg
3. machine_03_hf_acid_leaching_reactor.svg
4. machine_04_acheson_vs_lwg_furnace.svg
5. material_01_natural_flake_to_cspg_morphology.svg
6. material_02_turbostratic_to_hexagonal_crystal_lattice.svg

Every mass flow, yield, reagent dosage, and energy metric is strictly derived
from audited literature in ANL-22/74, Surovtseva et al. (2022), and Engels et al. (2022).
"""

import os
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SVG_DIR = os.path.join(ROOT, "docs", "svg")


def common_svg_defs():
    """Generates reusable patterns, markers, and gradients for engineering drawings."""
    return """
  <defs>
    <!-- Blueprint Subtle Engineering Grid -->
    <pattern id="blueprintGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#E5E8E8" stroke-width="0.6" />
      <path d="M 20 0 L 20 40 M 0 20 L 40 20" fill="none" stroke="#F2F4F4" stroke-width="0.4" />
    </pattern>

    <!-- Steel Hatching Pattern (ISO 128 45 deg lines) -->
    <pattern id="steelHatch" width="8" height="8" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <rect width="8" height="8" fill="#D5D8DC" fill-opacity="0.35" />
      <line x1="0" y1="0" x2="0" y2="8" stroke="#566573" stroke-width="1.2" />
    </pattern>

    <!-- Elastomer / Polyurethane Wear Liner Pattern (Cross-hatch) -->
    <pattern id="rubberLiner" width="6" height="6" patternTransform="rotate(45 0 0)" patternUnits="userSpaceOnUse">
      <rect width="6" height="6" fill="#2C3E50" fill-opacity="0.18" />
      <line x1="0" y1="0" x2="0" y2="6" stroke="#1F618D" stroke-width="1.0" />
      <line x1="0" y1="0" x2="6" y2="0" stroke="#1F618D" stroke-width="1.0" />
    </pattern>

    <!-- Refractory Brick Masonry Pattern -->
    <pattern id="refractoryBrick" width="24" height="12" patternUnits="userSpaceOnUse">
      <rect width="24" height="12" fill="#D35400" fill-opacity="0.25" stroke="#BA4A00" stroke-width="1" />
      <line x1="0" y1="6" x2="24" y2="6" stroke="#BA4A00" stroke-width="1" />
      <line x1="12" y1="0" x2="12" y2="6" stroke="#BA4A00" stroke-width="1" />
      <line x1="0" y1="6" x2="0" y2="12" stroke="#BA4A00" stroke-width="1" />
      <line x1="24" y1="6" x2="24" y2="12" stroke="#BA4A00" stroke-width="1" />
    </pattern>

    <!-- PTFE / Fluoropolymer Corrosion Lining Pattern -->
    <pattern id="ptfeHatch" width="8" height="8" patternTransform="rotate(-45 0 0)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="8" stroke="#16A085" stroke-width="1.5" />
      <line x1="0" y1="4" x2="8" y2="4" stroke="#16A085" stroke-width="0.8" stroke-dasharray="2,2" />
    </pattern>

    <!-- Granular Resistor Coke Bed Pattern -->
    <pattern id="cokeBed" width="16" height="16" patternUnits="userSpaceOnUse">
      <rect width="16" height="16" fill="#2C3E50" fill-opacity="0.15" />
      <circle cx="4" cy="4" r="2.2" fill="#34495E" />
      <circle cx="12" cy="12" r="2.8" fill="#2C3E50" />
      <circle cx="13" cy="4" r="1.8" fill="#1A252F" />
      <circle cx="4" cy="12" r="2.0" fill="#2C3E50" />
    </pattern>

    <!-- Polyhedral Mineralized Froth Cellular Pattern -->
    <pattern id="frothCells" width="18" height="16" patternUnits="userSpaceOnUse">
      <rect width="18" height="16" fill="#EAEDED" />
      <polygon points="9,1 17,5 17,11 9,15 1,11 1,5" fill="#F8F9F9" stroke="#566573" stroke-width="1.2" />
      <circle cx="9" cy="8" r="3.5" fill="#FFFFFF" opacity="0.8" />
      <path d="M 1,5 L 9,1 L 17,5" fill="none" stroke="#1C2833" stroke-width="1.6" stroke-dasharray="3,1" />
    </pattern>

    <!-- Thermal Plume & Incandescent Gradients -->
    <radialGradient id="heatGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF9C4" stop-opacity="1" />
      <stop offset="45%" stop-color="#F39C12" stop-opacity="0.85" />
      <stop offset="85%" stop-color="#C0392B" stop-opacity="0.5" />
      <stop offset="100%" stop-color="#7B241C" stop-opacity="0" />
    </radialGradient>

    <radialGradient id="bubbleGrad" cx="35%" cy="30%" r="65%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.98" />
      <stop offset="55%" stop-color="#D6EAF8" stop-opacity="0.85" />
      <stop offset="90%" stop-color="#85C1E9" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#2E86C1" stop-opacity="0.9" />
    </radialGradient>

    <linearGradient id="metallicCyl" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#7F8C8D" />
      <stop offset="30%" stop-color="#ECF0F1" />
      <stop offset="55%" stop-color="#BDC3C7" />
      <stop offset="85%" stop-color="#566573" />
      <stop offset="100%" stop-color="#7F8C8D" />
    </linearGradient>

    <linearGradient id="slurryGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#D6DBDF" stop-opacity="0.72" />
      <stop offset="35%" stop-color="#AEB6BF" stop-opacity="0.84" />
      <stop offset="75%" stop-color="#5D6D7E" stop-opacity="0.92" />
      <stop offset="100%" stop-color="#2C3E50" stop-opacity="0.98" />
    </linearGradient>

    <linearGradient id="frothGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#2C3E50" stop-opacity="0.85" />
      <stop offset="30%" stop-color="#5D6D7E" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#D5D8DC" stop-opacity="0.9" />
    </linearGradient>

    <!-- Arrow Markers -->
    <marker id="arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2C3E50" />
    </marker>
    <marker id="arrowRed" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#C0392B" />
    </marker>
    <marker id="arrowBlue" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#2980B9" />
    </marker>
    <marker id="arrowGreen" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#27AE60" />
    </marker>
    <marker id="arrowOrange" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="5.5" markerHeight="5.5" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#D35400" />
    </marker>
    <marker id="dimTick" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 2 L 8 5 L 0 8 z" fill="#34495E" />
    </marker>
  </defs>
"""


def render_title_block(dwg_no, title_text, unit_op, key_metrics, lit_ref):
    """Embeds an ISO 7200 compliant technical engineering title block in the lower-right."""
    t_text = title_text.replace("&", "&amp;")
    u_text = unit_op.replace("&", "&amp;")
    m_text = key_metrics.replace("&", "&amp;")
    l_text = lit_ref.replace("&", "&amp;")
    # Adjust font-size if title_text is long to prevent collision with dwg_no column
    title_font_size = "9.5" if len(title_text) > 42 else ("10.5" if len(title_text) > 32 else "11.5")
    return f"""
    <!-- ISO 7200 Technical Title Block -->
    <g transform="translate(680, 672)" id="iso_title_block">
      <rect x="0" y="0" width="500" height="108" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.8" />
      <rect x="0" y="0" width="500" height="28" fill="#F2F4F4" stroke="#1C2833" stroke-width="1.2" />
      <line x1="0" y1="56" x2="500" y2="56" stroke="#1C2833" stroke-width="1.0" />
      <line x1="0" y1="82" x2="500" y2="82" stroke="#1C2833" stroke-width="1.0" />
      <line x1="375" y1="0" x2="375" y2="56" stroke="#1C2833" stroke-width="1.0" />
      <line x1="435" y1="28" x2="435" y2="56" stroke="#1C2833" stroke-width="1.0" />

      <!-- First-Angle Projection Symbol -->
      <circle cx="482" cy="14" r="6" fill="none" stroke="#1C2833" stroke-width="1.1" />
      <circle cx="482" cy="14" r="2.5" fill="none" stroke="#1C2833" stroke-width="1.1" />
      <polygon points="452,10 470,7 470,21 452,18" fill="none" stroke="#1C2833" stroke-width="1.1" />

      <!-- Field Content -->
      <text x="10" y="19" font-family="Helvetica, Arial, sans-serif" font-size="{title_font_size}" font-weight="bold" fill="#1C2833">{t_text}</text>
      <text x="383" y="19" font-family="Courier, monospace" font-size="10.5" font-weight="bold" fill="#C0392B">{dwg_no}</text>

      <text x="10" y="45" font-family="Helvetica, Arial, sans-serif" font-size="9" fill="#566573">UNIT OP:</text>
      <text x="58" y="45" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#1C2833">{u_text}</text>
      <text x="383" y="45" font-family="Helvetica, Arial, sans-serif" font-size="8.5" fill="#566573">STD: ISO 128</text>
      <text x="442" y="45" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">REV 2.0</text>

      <text x="10" y="73" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#117A65">AUDIT METRICS: {m_text}</text>
      <text x="10" y="98" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-style="italic" fill="#5D6D7E">PRIMARY PROVENANCE: {l_text}</text>
    </g>
"""


def render_drawing_header(title, subtitle):
    """Draws upper header with ISO/ASME drawing sheet frame and blueprint aesthetics."""
    t = title.replace("&", "&amp;")
    st = subtitle.replace("&", "&amp;")
    title_font_size = "12" if len(title) > 70 else ("13" if len(title) > 58 else ("14.5" if len(title) > 45 else "16"))
    sub_font_size = "9" if len(subtitle) > 105 else "9.5"
    return f"""
    <!-- Background Blueprint Grid & ISO Drawing Sheet Frame -->
    <rect x="12" y="12" width="1176" height="776" fill="url(#blueprintGrid)" stroke="#1C2833" stroke-width="2" />
    <rect x="16" y="16" width="1168" height="768" fill="none" stroke="#566573" stroke-width="0.8" />

    <!-- Upper Blueprint Header -->
    <rect x="20" y="20" width="1160" height="52" fill="#1C2833" rx="3" />
    <rect x="20" y="68" width="1160" height="4" fill="#C0392B" />
    <text x="36" y="43" font-family="Helvetica, Arial, sans-serif" font-size="{title_font_size}" font-weight="bold" fill="#ECF0F1">{t}</text>
    <text x="36" y="60" font-family="Helvetica, Arial, sans-serif" font-size="{sub_font_size}" font-weight="normal" fill="#BDC3C7">{st}</text>
    <line x1="855" y1="26" x2="855" y2="64" stroke="#566573" stroke-width="1" />
    <text x="1165" y="42" font-family="Courier, monospace" font-size="9.5" font-weight="bold" fill="#F39C12" text-anchor="end">BASIS: 1,000 kg FINISHED cSPG (24,300 kg ROM ORE)</text>
    <text x="1165" y="58" font-family="Courier, monospace" font-size="8.5" fill="#ABB2B9" text-anchor="end">CAD SECTION VIEW A-A | P&amp;ID INSTRUMENTED</text>
"""


# =====================================================================
# Drawing 1: Mechanical Froth Flotation Cell
# =====================================================================
def create_svg_froth_flotation():
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">',
        common_svg_defs(),
        '  <rect width="1200" height="800" fill="#F8F9F9" />',
        render_drawing_header(
            "FORCED-AIR MECHANICAL FROTH FLOTATION CELL (TANKCELL ARCHITECTURE)",
            "Stage 1 Beneficiation: Hydrophobic Natural Flake Attachment vs. Depressed Silicate Gangue (ISO 10628 / ANL-22/74 Table 3)"
        ),
        """
    <!-- ================================================================= -->
    <!-- LEFT PANEL: REALISTIC CAD CROSS-SECTION OF FLOTATION CELL         -->
    <!-- ================================================================= -->
    <g id="flotation_cell_assembly">

      <!-- Structural Support I-Beam Legs & Concrete Plinths -->
      <rect x="175" y="535" width="22" height="115" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <rect x="523" y="535" width="22" height="115" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <rect x="155" y="650" width="60" height="14" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.5" />
      <rect x="505" y="650" width="60" height="14" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.5" />
      <!-- Anchor Bolts -->
      <line x1="168" y1="644" x2="168" y2="668" stroke="#1C2833" stroke-width="2" />
      <line x1="202" y1="644" x2="202" y2="668" stroke="#1C2833" stroke-width="2" />
      <line x1="518" y1="644" x2="518" y2="668" stroke="#1C2833" stroke-width="2" />
      <line x1="552" y1="644" x2="552" y2="668" stroke="#1C2833" stroke-width="2" />

      <!-- Outer Welded Carbon-Steel Shell (ISO 128 Section Hatching) -->
      <path d="M 170 205 L 170 495 L 265 585 L 455 585 L 550 495 L 550 205 Z" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="2.2" />
      <!-- Top & Side Bolted Reinforcing Flanges -->
      <rect x="162" y="200" width="16" height="8" fill="#566573" stroke="#1C2833" stroke-width="1" />
      <rect x="542" y="200" width="16" height="8" fill="#566573" stroke="#1C2833" stroke-width="1" />
      <rect x="162" y="340" width="8" height="12" fill="#566573" stroke="#1C2833" stroke-width="1" />
      <rect x="550" y="340" width="8" height="12" fill="#566573" stroke="#1C2833" stroke-width="1" />

      <!-- Internal Polyurethane / Elastomer Abrasion Liner (6 mm) -->
      <path d="M 184 205 L 184 488 L 272 573 L 448 573 L 536 488 L 536 205 Z" fill="url(#rubberLiner)" stroke="#1F618D" stroke-width="1.5" />
      <path d="M 190 205 L 190 484 L 276 567 L 444 567 L 530 484 L 530 205 Z" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.2" />

      <!-- HYDRODYNAMIC ZONE 1: Quiescent Separation & Active Pulp Zone (30-35% Solids) -->
      <path d="M 190 265 L 190 484 L 276 567 L 444 567 L 530 484 L 530 265 Z" fill="url(#slurryGradient)" />

      <!-- Pulp-Froth Interface Meniscus (Turbulence-Damped Transition) -->
      <path d="M 190 265 Q 235 261, 280 265 T 360 265 T 445 265 T 530 265" fill="none" stroke="#1F618D" stroke-width="2" stroke-dasharray="6,3" />
      <text x="488" y="278" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1F618D" text-anchor="end">PULP-FROTH INTERFACE</text>

      <!-- HYDRODYNAMIC ZONE 2: Mineralized Polyhedral Froth Bed (205 to 265) -->
      <rect x="190" y="205" width="340" height="60" fill="url(#frothCells)" opacity="0.92" />
      <rect x="190" y="205" width="340" height="60" fill="url(#frothGradient)" opacity="0.55" stroke="#566573" stroke-width="1" />

      <!-- Coalescing Froth Bubbles Coated with Black Graphite Platelets -->
      <g id="froth_bubbles">
        <circle cx="212" cy="222" r="8" fill="#D6EAF8" stroke="#1C2833" stroke-width="2" stroke-dasharray="4,2" />
        <circle cx="232" cy="236" r="10" fill="#D6EAF8" stroke="#1C2833" stroke-width="2.2" stroke-dasharray="5,2" />
        <circle cx="255" cy="218" r="11" fill="#EBF5FB" stroke="#1C2833" stroke-width="2.4" stroke-dasharray="5,2" />
        <circle cx="282" cy="242" r="9" fill="#D6EAF8" stroke="#1C2833" stroke-width="2" stroke-dasharray="4,2" />
        <circle cx="308" cy="224" r="10" fill="#EBF5FB" stroke="#1C2833" stroke-width="2.2" stroke-dasharray="5,2" />
        <circle cx="412" cy="224" r="10" fill="#EBF5FB" stroke="#1C2833" stroke-width="2.2" stroke-dasharray="5,2" />
        <circle cx="438" cy="242" r="9" fill="#D6EAF8" stroke="#1C2833" stroke-width="2" stroke-dasharray="4,2" />
        <circle cx="465" cy="218" r="11" fill="#EBF5FB" stroke="#1C2833" stroke-width="2.4" stroke-dasharray="5,2" />
        <circle cx="488" cy="236" r="10" fill="#D6EAF8" stroke="#1C2833" stroke-width="2.2" stroke-dasharray="5,2" />
        <circle cx="508" cy="222" r="8" fill="#D6EAF8" stroke="#1C2833" stroke-width="2" stroke-dasharray="4,2" />
      </g>

      <!-- Internal Froth Crowder Cones (Accelerates Radial Froth Transport to Launder) -->
      <polygon points="315,205 335,205 335,262 325,262" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <polygon points="405,205 385,205 385,262 395,262" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <text x="292" y="254" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#1C2833" text-anchor="end">FROTH CROWDER</text>

      <!-- Wall Anti-Swirl Radial Baffles (4 vertical baffles eliminating vortexing) -->
      <rect x="192" y="290" width="18" height="175" fill="#2C3E50" fill-opacity="0.65" stroke="#1C2833" stroke-width="1.2" />
      <rect x="510" y="290" width="18" height="175" fill="#2C3E50" fill-opacity="0.65" stroke="#1C2833" stroke-width="1.2" />
      <text x="215" y="340" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#ECF0F1">WALL BAFFLE</text>

      <!-- Internal Draft-Tube & False Bottom Circulation Cone -->
      <polygon points="245,380 265,380 295,465 280,465" fill="#95A5A6" stroke="#1C2833" stroke-width="1.2" />
      <polygon points="475,380 455,380 425,465 440,465" fill="#95A5A6" stroke="#1C2833" stroke-width="1.2" />
      <!-- False Bottom Deflector Apron -->
      <path d="M 220 515 L 295 495 M 500 515 L 425 495" stroke="#95A5A6" stroke-width="3.5" stroke-linecap="round" />

      <!-- Peripheral Froth Overflow Lip, Rotary Skimmer Paddles & Sloped Launders -->
      <path d="M 190 205 L 138 205 L 138 252 L 170 268 L 170 222 L 190 222 Z" fill="#BDC3C7" stroke="#1C2833" stroke-width="1.6" />
      <path d="M 530 205 L 582 205 L 582 252 L 550 268 L 550 222 L 530 222 Z" fill="#BDC3C7" stroke="#1C2833" stroke-width="1.6" />
      <!-- Froth Overflow Cascades -->
      <path d="M 190 204 Q 168 196, 155 225 L 145 245 L 166 255 Z" fill="#2C3E50" opacity="0.85" />
      <path d="M 530 204 Q 552 196, 565 225 L 575 245 L 554 255 Z" fill="#2C3E50" opacity="0.85" />
      <!-- Motorized Rotary Froth Skimmer Paddles (Left & Right) -->
      <circle cx="184" cy="198" r="9" fill="#E67E22" stroke="#1C2833" stroke-width="1.5" />
      <line x1="172" y1="198" x2="196" y2="198" stroke="#1C2833" stroke-width="2" />
      <line x1="184" y1="186" x2="184" y2="210" stroke="#1C2833" stroke-width="2" />
      <circle cx="536" cy="198" r="9" fill="#E67E22" stroke="#1C2833" stroke-width="1.5" />
      <line x1="524" y1="198" x2="548" y2="198" stroke="#1C2833" stroke-width="2" />
      <line x1="536" y1="186" x2="536" y2="210" stroke="#1C2833" stroke-width="2" />
      <text x="155" y="182" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#B9770E" text-anchor="middle">SKIMMER PADDLE</text>
    </g>

    <!-- ================================================================= -->
    <!-- SUPERSTRUCTURE: MOTOR, V-BELT PULLEY, STANDPIPE & ROTOR-STATOR    -->
    <!-- ================================================================= -->
    <g id="drive_and_rotor_stator">
      <!-- Top Structural Bridge I-Beam across Cell -->
      <rect x="150" y="162" width="420" height="14" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.6" />
      <line x1="150" y1="166" x2="570" y2="166" stroke="#1C2833" stroke-width="0.8" />
      <line x1="150" y1="172" x2="570" y2="172" stroke="#1C2833" stroke-width="0.8" />

      <!-- Finned TEFC Squirrel-Cage Induction Motor (Offset Left on Bridge) -->
      <rect x="242" y="92" width="64" height="54" fill="#1F618D" stroke="#154360" stroke-width="1.8" rx="4" />
      <!-- Cooling Fins on Motor Stator -->
      <line x1="248" y1="102" x2="300" y2="102" stroke="#85C1E9" stroke-width="1.2" />
      <line x1="248" y1="110" x2="300" y2="110" stroke="#85C1E9" stroke-width="1.2" />
      <line x1="248" y1="118" x2="300" y2="118" stroke="#85C1E9" stroke-width="1.2" />
      <line x1="248" y1="126" x2="300" y2="126" stroke="#85C1E9" stroke-width="1.2" />
      <line x1="248" y1="134" x2="300" y2="134" stroke="#85C1E9" stroke-width="1.2" />
      <text x="274" y="86" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#154360" text-anchor="middle">TEFC MOTOR (45 kW)</text>

      <!-- V-Belt Guard & Driven Sheave Box -->
      <rect x="268" y="146" width="110" height="16" fill="#F39C12" fill-opacity="0.85" stroke="#9C640C" stroke-width="1.4" rx="2" />
      <line x1="274" y1="152" x2="360" y2="152" stroke="#1C2833" stroke-width="1.5" stroke-dasharray="4,2" />
      <line x1="274" y1="157" x2="360" y2="157" stroke="#1C2833" stroke-width="1.5" stroke-dasharray="4,2" />

      <!-- Upper Cylindrical Bearing Cartridge & Air Plenum Manifold -->
      <rect x="338" y="114" width="44" height="48" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.6" />
      <!-- Forced Air Side Blow-In Nozzle & Butterfly Damper (FIC-102) -->
      <rect x="382" y="122" width="42" height="16" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.4" />
      <line x1="424" y1="118" x2="424" y2="142" stroke="#1C2833" stroke-width="2.5" />

      <!-- Concentric Air Standpipe & Inner Solid Impeller Drive Shaft -->
      <!-- Outer Air Standpipe Sleeve -->
      <rect x="342" y="176" width="36" height="292" fill="url(#metallicCyl)" fill-opacity="0.88" stroke="#1C2833" stroke-width="1.5" />
      <!-- Internal Annular Air Downflow Arrows -->
      <line x1="348" y1="195" x2="348" y2="445" stroke="#27AE60" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arrowGreen)" />
      <line x1="372" y1="195" x2="372" y2="445" stroke="#27AE60" stroke-width="1.5" stroke-dasharray="5,3" marker-end="url(#arrowGreen)" />
      <!-- Inner High-Tensile Steel Drive Shaft -->
      <rect x="355" y="110" width="10" height="370" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />

      <!-- High-Shear Multi-Blade Rotor & Slotted Dispersion Stator Cage (Outotec FloatForce Style) -->
      <!-- Stator Hood Ring -->
      <rect x="296" y="465" width="128" height="10" fill="#34495E" stroke="#17202A" stroke-width="1.5" rx="2" />
      <!-- Slotted Stator Dispersion Bars (Left & Right) -->
      <rect x="298" y="475" width="10" height="42" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />
      <rect x="314" y="475" width="8" height="42" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />
      <rect x="398" y="475" width="8" height="42" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />
      <rect x="412" y="475" width="10" height="42" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />
      <!-- Central Shaped Rotor Impeller (Pumping Slurry + Air Radially Outward) -->
      <path d="M 332 472 L 388 472 L 396 512 L 372 518 L 348 518 L 324 512 Z" fill="#C0392B" stroke="#641E16" stroke-width="1.6" />
      <!-- Rotor Internal Air/Pulp Channels -->
      <path d="M 352 472 L 332 504 M 368 472 L 388 504" stroke="#FADBD8" stroke-width="2" />
      <text x="360" y="532" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#FADBD8" text-anchor="middle">ROTOR-STATOR IMPELLER (v_tip = 6.5 m/s)</text>

      <!-- Hydrodynamic Double-Toroidal Flow Loops & Micro-Bubble Plume -->
      <!-- Lower Radial Pumping & Recirculation Loop -->
      <path d="M 294 496 C 235 496, 215 440, 255 395 C 280 370, 315 420, 325 468" fill="none" stroke="#E74C3C" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrowRed)" />
      <path d="M 426 496 C 485 496, 505 440, 465 395 C 440 370, 405 420, 395 468" fill="none" stroke="#E74C3C" stroke-width="2" stroke-dasharray="5,3" marker-end="url(#arrowRed)" />
      <!-- Rising Bubble-Particle Aggregate Streamlines -->
      <path d="M 285 460 Q 250 380, 265 272" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-dasharray="3,3" marker-end="url(#arrowBlue)" />
      <path d="M 435 460 Q 470 380, 455 272" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-dasharray="3,3" marker-end="url(#arrowBlue)" />

      <!-- Rising Micro-Bubble Swarm carrying Black Graphite Flakes -->
      <g id="rising_bubble_swarm">
        <circle cx="275" cy="445" r="4.5" fill="url(#bubbleGrad)" /><rect x="271" y="449" width="8" height="2.2" fill="#17202A" />
        <circle cx="255" cy="410" r="5.5" fill="url(#bubbleGrad)" /><rect x="250" y="415" width="10" height="2.5" fill="#17202A" />
        <circle cx="290" cy="375" r="6.0" fill="url(#bubbleGrad)" /><rect x="284" y="381" width="11" height="2.5" fill="#17202A" />
        <circle cx="245" cy="340" r="6.5" fill="url(#bubbleGrad)" /><rect x="239" y="346" width="12" height="2.5" fill="#17202A" />
        <circle cx="280" cy="305" r="7.0" fill="url(#bubbleGrad)" /><rect x="273" y="312" width="13" height="2.8" fill="#17202A" />

        <circle cx="445" cy="445" r="4.5" fill="url(#bubbleGrad)" /><rect x="441" y="449" width="8" height="2.2" fill="#17202A" />
        <circle cx="465" cy="410" r="5.5" fill="url(#bubbleGrad)" /><rect x="460" y="415" width="10" height="2.5" fill="#17202A" />
        <circle cx="430" cy="375" r="6.0" fill="url(#bubbleGrad)" /><rect x="424" y="381" width="11" height="2.5" fill="#17202A" />
        <circle cx="475" cy="340" r="6.5" fill="url(#bubbleGrad)" /><rect x="469" y="346" width="12" height="2.5" fill="#17202A" />
        <circle cx="440" cy="305" r="7.0" fill="url(#bubbleGrad)" /><rect x="433" y="312" width="13" height="2.8" fill="#17202A" />
      </g>

      <!-- Settling Hydrophilic Silicate Gangue Grains (Quartz / Mica sinking to underflow) -->
      <g fill="#D35400" stroke="#78281F" stroke-width="0.8">
        <polygon points="235,480 242,485 238,492 230,488" />
        <polygon points="278,525 286,530 282,538 274,534" />
        <polygon points="315,548 323,552 319,560 311,556" />
        <polygon points="405,548 413,552 409,560 401,556" />
        <polygon points="442,525 450,530 446,538 438,534" />
        <polygon points="485,480 492,485 488,492 480,488" />
      </g>

      <!-- Bottom Tailings Dart Valve / Pneumatic Control Valve (LCV-101) -->
      <rect x="342" y="573" width="36" height="32" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <!-- Dart Plug inside Cone -->
      <polygon points="348,572 372,572 360,552" fill="#E74C3C" stroke="#641E16" stroke-width="1.4" />
      <!-- P&ID Control Valve Bowtie & Diaphragm Dome (LCV-101) -->
      <polygon points="344,612 376,628 376,612 344,628" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.5" />
      <path d="M 392 610 A 10 10 0 0 1 392 630 Z" fill="#27AE60" stroke="#1C2833" stroke-width="1.4" />
      <line x1="360" y1="620" x2="384" y2="620" stroke="#1C2833" stroke-width="1.5" />
    </g>

    <!-- ================================================================= -->
    <!-- P&ID INSTRUMENTATION LOOP & ENGINEERING DIMENSION CALLOUTS        -->
    <!-- ================================================================= -->
    <g id="pid_and_dimensions">
      <!-- Ultrasonic Froth Level Transmitter (LT-101) & Controller (LIC-101) -->
      <circle cx="495" cy="122" r="14" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.5" />
      <line x1="481" y1="122" x2="509" y2="122" stroke="#1C2833" stroke-width="1" />
      <text x="495" y="119" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833" text-anchor="middle">LIC</text>
      <text x="495" y="131" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833" text-anchor="middle">101</text>
      <!-- Sensor Probe into Froth -->
      <line x1="495" y1="136" x2="495" y2="215" stroke="#1C2833" stroke-width="1.2" stroke-dasharray="2,2" />
      <!-- Pneumatic / 4-20mA Signal Line from LIC-101 to LCV-101 -->
      <path d="M 509 122 L 602 122 L 602 620 L 392 620" fill="none" stroke="#27AE60" stroke-width="1.2" stroke-dasharray="4,3" />

      <!-- Forced Air Flow Controller (FIC-102) -->
      <circle cx="452" cy="95" r="13" fill="#FFFFFF" stroke="#27AE60" stroke-width="1.5" />
      <line x1="439" y1="95" x2="465" y2="95" stroke="#27AE60" stroke-width="1" />
      <text x="452" y="93" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#1E8449" text-anchor="middle">FIC</text>
      <text x="452" y="103" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#1E8449" text-anchor="middle">102</text>

      <!-- CAD Dimension Line: Cell Active Diameter -->
      <line x1="170" y1="598" x2="332" y2="598" stroke="#34495E" stroke-width="1" marker-start="url(#dimTick)" />
      <line x1="550" y1="598" x2="388" y2="598" stroke="#34495E" stroke-width="1" marker-start="url(#dimTick)" />
      <text x="255" y="594" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#34495E" text-anchor="middle">D_cell = 3,200 mm</text>
    </g>

    <!-- ================================================================= -->
    <!-- PROCESS STREAM CALLOUT BOXES (STRICT MASS & ENERGY BALANCE)       -->
    <!-- ================================================================= -->
    <g id="process_streams">
      <!-- 1. Conditioned Pulp Feed Inlet (Lower-Left Tangential Nozzle) -->
      <rect x="135" y="368" width="35" height="18" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.4" />
      <line x1="40" y1="377" x2="132" y2="377" stroke="#2980B9" stroke-width="3.5" marker-end="url(#arrowBlue)" />
      <rect x="26" y="302" width="136" height="66" fill="#EBF5FB" stroke="#2980B9" stroke-width="1.2" rx="3" />
      <text x="32" y="316" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#1B4F72">1. CONDITIONED PULP FEED</text>
      <text x="32" y="329" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• ROM Ore: 24,300 kg (10.43% C)</text>
      <text x="32" y="341" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Pulp Density: 32 wt% solids</text>
      <text x="32" y="353" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#154360">• Kerosene: 150 g/t | MIBC: 60 g/t</text>
      <text x="32" y="364" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#5D6D7E">• Na2SiO3 Depressant: 400 g/t</text>

      <!-- 2. Froth Concentrate Overflow (Upper-Left Launder Discharge) -->
      <line x1="145" y1="258" x2="65" y2="258" stroke="#C0392B" stroke-width="3.5" marker-end="url(#arrowRed)" />
      <rect x="26" y="182" width="124" height="68" fill="#FDEDEC" stroke="#C0392B" stroke-width="1.2" rx="3" />
      <text x="32" y="196" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#900C3F">2. FLAKE CONCENTRATE</text>
      <text x="32" y="209" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#78281F">• Mass: 2,534 kg (104.3 kg/t)</text>
      <text x="32" y="221" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Mass Yield: 10.43% of ROM</text>
      <text x="32" y="233" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Grade: 94-97% C (+80/-100#)</text>
      <text x="32" y="245" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#900C3F">• Market Price: $793-$830/t</text>

      <!-- 3. Forced Low-Pressure Blower Air Inlet -->
      <line x1="468" y1="130" x2="428" y2="130" stroke="#27AE60" stroke-width="3" marker-end="url(#arrowGreen)" />
      <text x="474" y="150" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1E8449">3. BLOWER AIR (25 kPa)</text>
      <text x="474" y="161" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32">J_g = 1.2 cm/s (0.9 m3/m2·min)</text>

      <!-- 4. Silicate Gangue Tailings Underflow -->
      <line x1="360" y1="630" x2="360" y2="695" stroke="#566573" stroke-width="3.5" marker-end="url(#arrow)" />
      <rect x="26" y="675" width="320" height="62" fill="#F2F4F4" stroke="#566573" stroke-width="1.2" rx="3" />
      <text x="34" y="690" font-family="Helvetica, Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#2C3E50">4. HYDROPHILIC SILICATE GANGUE TAILINGS UNDERFLOW</text>
      <text x="34" y="704" font-family="Helvetica, Arial, sans-serif" font-size="8.5" fill="#1C2833">• Depressed Quartz (SiO2), Mica &amp; Feldspar: 21,730 kg (894.2 kg/t ore | 89.42%)</text>
      <text x="34" y="717" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#5D6D7E">• Unallocated Slimes / Handling Residual: 36 kg (1.5 kg/t ore | 0.15% &lt; 5% Audit Cap)</text>
      <text x="34" y="730" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#117A65">• Stage 1 Energy: 0.484 kWh/kg conc (1.352 kWh/kg cSPG) + 2.88 MJ/kg Thermal</text>

      <!-- Hydrodynamic Zone Legend Box (Left Middle) -->
      <rect x="26" y="420" width="136" height="105" fill="#FFFFFF" stroke="#7F8C8D" stroke-width="1.2" rx="3" />
      <rect x="26" y="420" width="136" height="18" fill="#34495E" rx="2" />
      <text x="94" y="432" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#FFFFFF" text-anchor="middle">CELL ZONE PROFILE</text>
      <text x="32" y="450" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#2C3E50">Zone I: Froth Drainage</text>
      <text x="32" y="461" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#5D6D7E">H_f = 150-350 mm; gangue dropback</text>
      <text x="32" y="476" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#1F618D">Zone II: Quiescent Collection</text>
      <text x="32" y="487" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#5D6D7E">Laminar bubble-flake rise</text>
      <text x="32" y="502" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#C0392B">Zone III: Intense Shear</text>
      <text x="32" y="513" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#5D6D7E">Turbulent dissipation eps = 15 W/kg</text>
    </g>

    <!-- ================================================================= -->
    <!-- RIGHT PANEL: DIDACTIC THREE-PHASE PHYSICOCHEMICAL INSET           -->
    <!-- ================================================================= -->
    <g transform="translate(650, 88)" id="micro_inset">
      <rect x="0" y="0" width="530" height="572" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.8" rx="5" />
      <rect x="0" y="0" width="530" height="28" fill="#1C2833" rx="4" />
      <text x="14" y="18" font-family="Helvetica, Arial, sans-serif" font-size="11" font-weight="bold" fill="#ECF0F1">PHYSICOCHEMICAL INSET: THREE-PHASE CONTACT &amp; CRYSTALLOGRAPHIC SELECTIVITY</text>

      <!-- SUB-PANEL A: Young-Dupre Three-Phase Contact Line & Interfacial Tension Vectors -->
      <rect x="14" y="38" width="502" height="238" fill="#F4F9FD" stroke="#85C1E9" stroke-width="1.2" rx="4" />
      <text x="24" y="55" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#1B4F72">A. YOUNG-DUPRE THREE-PHASE CONTACT MECHANICS (HYDROPHOBIC GRAPHITE BASAL PLANE)</text>

      <!-- Layered Natural Graphite Flake Substrate (Showing sp2 Basal Sheets vs Polar Edge) -->
      <g transform="translate(35, 185)">
        <!-- Stacked Graphene Layers inside Flake -->
        <rect x="0" y="0" width="320" height="8" fill="#1C2833" stroke="#000000" stroke-width="0.8" />
        <rect x="4" y="10" width="316" height="8" fill="#2C3E50" stroke="#000000" stroke-width="0.8" />
        <rect x="0" y="20" width="320" height="8" fill="#1C2833" stroke="#000000" stroke-width="0.8" />
        <rect x="6" y="30" width="314" height="8" fill="#34495E" stroke="#000000" stroke-width="0.8" />
        <text x="160" y="52" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833" text-anchor="middle">NATURAL CRYSTALLINE GRAPHITE FLAKE (sp2 Basal Cleavage Plane {0001} — Non-Polar Hydrophobic)</text>

        <!-- Adsorbed Kerosene Collector Hydrocarbon Chains (C12-C16 Alkanes on Basal Plane) -->
        <path d="M 30 0 L 34 -6 L 30 -12 L 34 -18 M 50 0 L 54 -6 L 50 -12 L 54 -18 M 70 0 L 74 -6 L 70 -12 L 74 -18 M 250 0 L 254 -6 L 250 -12 L 254 -18 M 270 0 L 274 -6 L 270 -12 L 274 -18" fill="none" stroke="#D35400" stroke-width="1.6" />
        <text x="16" y="-23" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#BA4A00">Kerosene C12-C16 Collector Film</text>
        <text x="16" y="-13" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#78281F">(pi-alkyl van der Waals adsorption)</text>

        <!-- Reactive Prismatic Edge Defect (Right Edge of Flake with -COOH / -OH groups) -->
        <circle cx="324" cy="4" r="3.5" fill="#E74C3C" />
        <circle cx="324" cy="24" r="3.5" fill="#E74C3C" />
        <text x="334" y="12" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#C0392B">Polar Prismatic Edge {10-10}</text>
        <text x="334" y="23" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#78281F">(-COOH / -OH groups; Kerosene</text>
        <text x="334" y="33" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#78281F">masks edge hydration defects)</text>
      </g>

      <!-- Attached Air Bubble Dome on Graphite Basal Surface (Contact Point at x=125, y=185 and x=265, y=185) -->
      <path d="M 125 185 A 75 75 0 1 1 265 185 Z" fill="url(#bubbleGrad)" stroke="#2980B9" stroke-width="2.5" />
      <text x="195" y="132" font-family="Helvetica, Arial, sans-serif" font-size="11" font-weight="bold" fill="#154360" text-anchor="middle">AIR BUBBLE (GAS)</text>
      <text x="195" y="146" font-family="Helvetica, Arial, sans-serif" font-size="8.5" fill="#1F618D" text-anchor="middle">d_32 = 0.8 - 1.5 mm</text>
      <text x="195" y="158" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#117A65" text-anchor="middle">MIBC Frother @ Gas-Liquid Interface</text>

      <!-- Three-Phase Contact Angle (theta_c = 82 deg) & Surface Tension Vectors at Left Contact Point (125, 185) -->
      <!-- Arc for Contact Angle inside Gas Phase -->
      <path d="M 155 185 A 30 30 0 0 0 130 156" fill="none" stroke="#C0392B" stroke-width="2.2" />
      <text x="160" y="176" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#C0392B">theta_c = 75°-86°</text>
      <!-- Vector gamma_SG (Solid-Gas, pointing right into bubble base) -->
      <line x1="125" y1="185" x2="175" y2="185" stroke="#27AE60" stroke-width="2.2" marker-end="url(#arrowGreen)" />
      <text x="165" y="198" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1E8449">gamma_SG</text>
      <!-- Vector gamma_SL (Solid-Liquid, pointing left into slurry) -->
      <line x1="125" y1="185" x2="78" y2="185" stroke="#2980B9" stroke-width="2.2" marker-end="url(#arrowBlue)" />
      <text x="82" y="198" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1F618D">gamma_SL</text>
      <!-- Vector gamma_LG (Liquid-Gas tangent along bubble wall) -->
      <line x1="125" y1="185" x2="138" y2="120" stroke="#C0392B" stroke-width="2.4" marker-end="url(#arrowRed)" />
      <text x="108" y="114" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#C0392B">gamma_LG</text>

      <!-- Thermodynamic Equations Box (Top Right of Sub-Panel A) -->
      <rect x="335" y="64" width="172" height="106" fill="#FFFFFF" stroke="#2980B9" stroke-width="1" rx="3" />
      <text x="343" y="79" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1B4F72">THERMODYNAMIC CRITERIA:</text>
      <text x="343" y="94" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#1C2833">gamma_SL - gamma_SG =</text>
      <text x="355" y="106" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#1C2833">gamma_LG * cos(theta_c)</text>
      <line x1="343" y1="113" x2="498" y2="113" stroke="#BDC3C7" stroke-width="0.8" />
      <text x="343" y="126" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#C0392B">Work of Adhesion (Delta G_att):</text>
      <text x="343" y="139" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#900C3F">W_a = gamma_LG(1 - cos theta_c)</text>
      <text x="343" y="152" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32">• Native Flake: theta_c = 75°-82°</text>
      <text x="343" y="163" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32">• +Kerosene: theta_c = 85°-92°</text>

      <!-- SUB-PANEL B: Silicate Gangue Depression vs. Flake Collection Kinetics -->
      <rect x="14" y="286" width="502" height="142" fill="#FEF9E7" stroke="#F39C12" stroke-width="1.2" rx="4" />
      <text x="24" y="303" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#B9770E">B. ELECTROSTATIC DEPRESSION OF QUARTZ / MICA GANGUE (SODIUM SILICATE MECHANISM)</text>

      <!-- Depressed Quartz Grain surrounded by Hydrated H2SiO3 / SiO3(2-) Double Layer -->
      <circle cx="95" cy="358" r="34" fill="#D6EAF8" stroke="#2980B9" stroke-width="1.5" stroke-dasharray="3,2" />
      <polygon points="75,342 115,338 122,368 92,382 68,365" fill="#D35400" stroke="#78281F" stroke-width="1.5" />
      <text x="95" y="358" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">SiO2 / Mica</text>
      <text x="95" y="369" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#FADBD8" text-anchor="middle">Gangue</text>
      <!-- Negative Zeta Potential Charges around Quartz -->
      <text x="95" y="319" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#1F618D" text-anchor="middle">-  SiO3(2-)  H2O  -</text>
      <text x="95" y="404" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#1F618D" text-anchor="middle">-  zeta = -45 mV  -</text>
      <!-- Gravity Settling Arrow -->
      <line x1="145" y1="335" x2="145" y2="385" stroke="#C0392B" stroke-width="2.5" marker-end="url(#arrowRed)" />
      <text x="154" y="362" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#C0392B">SINKS</text>

      <!-- Explanation of Selectivity & Collection Probability -->
      <text x="198" y="324" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">1. Hydrophilic Hydration Shell (theta_c &lt; 15°):</text>
      <text x="206" y="337" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">Na2SiO3 adsorbs as polymeric silicic acid on quartz/mica,</text>
      <text x="206" y="349" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">creating a repulsive negative electrical double layer (zeta = -45 mV).</text>
      <text x="198" y="366" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">2. Flotation Collection Probability (P_col = P_c * P_a * (1 - P_d)):</text>
      <text x="206" y="379" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">Coarse flakes (+80 mesh, 180 um) require quiescent froth zone</text>
      <text x="206" y="391" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">to prevent turbulent detachment (P_d) while multi-stage cleaner</text>
      <text x="206" y="403" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">re-grinding liberates locked interlamellar silicate ash to 94-97% C.</text>
      <text x="206" y="418" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#900C3F">• Rejects 894.2 kg gangue per 1,000 kg ROM ore at Stage 1!</text>

      <!-- SUB-PANEL C: Stage 1 Industrial Operating & LCI Ledger Table -->
      <rect x="14" y="438" width="502" height="122" fill="#EAFAF1" stroke="#27AE60" stroke-width="1.2" rx="4" />
      <text x="24" y="455" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#0E6251">C. VERIFIED STAGE 1 MASS, REAGENT &amp; ENERGY LEDGER (ANL-22/74 TABLE 3; USGS 2025)</text>
      <line x1="24" y1="462" x2="504" y2="462" stroke="#27AE60" stroke-width="0.8" />

      <!-- Two-Column Ledger -->
      <text x="24" y="477" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Run-of-Mine (ROM) Ore Feed:</text>
      <text x="185" y="477" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">24.30 t ore / t cSPG</text>
      <text x="24" y="492" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Flake Concentrate Output:</text>
      <text x="185" y="492" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">2.534 t conc / t cSPG</text>
      <text x="24" y="507" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Concentrate Mass Yield:</text>
      <text x="185" y="507" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">10.43% (104.3 kg/t ore)</text>
      <text x="24" y="522" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Tailings + Loss Partition:</text>
      <text x="185" y="522" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#C0392B">894.2 + 1.5 kg/t ore</text>
      <text x="24" y="537" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Flotation Circuit Config:</text>
      <text x="185" y="537" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">1 Rougher + 3-4 Cleaners</text>
      <text x="24" y="552" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Concentrate Market Value:</text>
      <text x="185" y="552" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#1B4F72">$793-$830/t (-100 mesh)</text>

      <line x1="298" y1="465" x2="298" y2="555" stroke="#A3E4D7" stroke-width="1" />

      <text x="308" y="477" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Stage Elec (per kg conc):</text>
      <text x="442" y="477" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">0.484 kWh/kg</text>
      <text x="308" y="492" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Cumul. Elec (per kg cSPG):</text>
      <text x="442" y="492" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">1.352 kWh/kg</text>
      <text x="308" y="507" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Stage Thermal Fuel:</text>
      <text x="442" y="507" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#D35400">2.880 MJ/kg</text>
      <text x="308" y="522" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Kerosene Collector:</text>
      <text x="442" y="522" font-family="Courier, monospace" font-size="8.5" fill="#34495E">150 g/t ore</text>
      <text x="308" y="537" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• MIBC / Pine Oil Frother:</text>
      <text x="442" y="537" font-family="Courier, monospace" font-size="8.5" fill="#34495E">60 g/t ore</text>
      <text x="308" y="552" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Global Mining Chokepoint:</text>
      <text x="442" y="552" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#C0392B">79.38% China</text>
    </g>
"""
    ]
    lines.append(render_title_block(
        "DWG-MCH-01",
        "MECHANICAL FROTH FLOTATION CELL (SECTION A-A)",
        "Comminution & Froth Flotation (Stage 1)",
        "Elec: 0.484 kWh/kg conc (1.352 kWh/kg cSPG) | Yield: 10.43% | 94-97% C",
        "ANL GREET ANL-22/74 Table 3; Surovtseva (2022); USGS MCS (2025)"
    ))
    lines.append("</svg>")
    return "\n".join(lines)


# =====================================================================
# Drawing 2: Impact Spheronization Air-Classifier Mill (ACM)
# =====================================================================
def create_svg_acm_mill():
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">',
        common_svg_defs(),
        '  <rect width="1200" height="800" fill="#F8F9F9" />',
        render_drawing_header(
            "AIR-CLASSIFIER IMPACT MILL (ACM): MECHANICAL SPHERONIZATION OF FLAKE GRAPHITE",
            "Stage 2 Flake Rounding: High-Shear Folding in a Pin-Rotor Chamber + Centrifugal Classifier Size Cut (ISO 10628 / ANL-22/74 Table 3)"
        ),
        """
    <!-- ================================================================= -->
    <!-- LEFT PANEL: CAD CROSS-SECTION OF THE ACM (SECTION A-A)            -->
    <!-- ================================================================= -->
    <g id="acm_machine_body">

      <!-- Foundation plinth & anti-vibration mounts -->
      <rect x="170" y="676" width="340" height="14" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.5" />
      <rect x="190" y="660" width="26" height="16" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.2" />
      <rect x="464" y="660" width="26" height="16" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.2" />

      <!-- Lower grinding chamber: cast-iron shell (ISO 128 hatching) -->
      <path d="M 200 330 L 200 560 L 245 598 L 435 598 L 480 560 L 480 330 Z" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="2.2" />
      <!-- Upper classifier housing -->
      <rect x="230" y="168" width="220" height="162" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="2.2" />
      <!-- Bolted split flange between chambers -->
      <rect x="192" y="324" width="296" height="10" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <g fill="#1C2833">
        <circle cx="204" cy="329" r="2" /><circle cx="236" cy="329" r="2" /><circle cx="444" cy="329" r="2" /><circle cx="476" cy="329" r="2" />
      </g>

      <!-- Inner cavity (white) -->
      <path d="M 216 334 L 216 552 L 252 584 L 428 584 L 464 552 L 464 334 Z" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.2" />
      <rect x="244" y="182" width="192" height="152" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.2" />

      <!-- Serrated stator impact liner (tungsten-carbide / hardened steel) -->
      <path d="M 216 372 L 232 380 L 216 388 L 232 396 L 216 404 L 232 412 L 216 420 L 232 428 L 216 436 L 232 444 L 216 452 L 232 460 L 216 468 L 232 476 L 216 484 L 232 492 L 216 500 L 232 508 L 216 516 Z" fill="#E67E22" stroke="#9C640C" stroke-width="1.2" />
      <path d="M 464 372 L 448 380 L 464 388 L 448 396 L 464 404 L 448 412 L 464 420 L 448 428 L 464 436 L 448 444 L 464 452 L 448 460 L 464 468 L 448 476 L 464 484 L 448 492 L 464 500 L 448 508 L 464 516 Z" fill="#E67E22" stroke="#9C640C" stroke-width="1.2" />
      <text x="224" y="362" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#9C640C">SERRATED LINER</text>

      <!-- Air-borne particle cloud (dark flakes) filling the grinding chamber -->
      <rect x="236" y="340" width="208" height="150" fill="#2C3E50" fill-opacity="0.07" />

      <!-- Rotor disc with impact pins -->
      <rect x="248" y="500" width="184" height="18" fill="#C0392B" stroke="#641E16" stroke-width="1.8" rx="2" />
      <g fill="#922B21" stroke="#1C2833" stroke-width="1">
        <rect x="256" y="474" width="10" height="26" /><rect x="282" y="474" width="10" height="26" />
        <rect x="308" y="474" width="10" height="26" /><rect x="362" y="474" width="10" height="26" />
        <rect x="388" y="474" width="10" height="26" /><rect x="414" y="474" width="10" height="26" />
      </g>
      <!-- Rotor hub & main shaft -->
      <rect x="326" y="486" width="28" height="14" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <rect x="333" y="518" width="14" height="150" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />
      <!-- Bearing housing & V-belt sheave -->
      <rect x="312" y="618" width="56" height="34" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <rect x="296" y="652" width="88" height="10" fill="#F39C12" fill-opacity="0.85" stroke="#9C640C" stroke-width="1.2" rx="2" />
      <text x="340" y="674" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#1C2833" text-anchor="middle">ROTOR DRIVE (VFD)</text>
      <!-- Labyrinth seal -->
      <rect x="326" y="598" width="28" height="12" fill="#95A5A6" stroke="#1C2833" stroke-width="1" />

      <!-- Tip-speed dimension on rotor -->
      <line x1="340" y1="534" x2="432" y2="534" stroke="#34495E" stroke-width="1" marker-start="url(#dimTick)" marker-end="url(#dimTick)" />
      <text x="388" y="546" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#34495E" text-anchor="middle">R_rotor</text>
      <text x="468" y="533" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#C0392B">v_tip = 15-25 m/s</text>

      <!-- Classifier wheel (squirrel-cage rotor with vanes) -->
      <rect x="296" y="210" width="88" height="56" fill="#2980B9" fill-opacity="0.9" stroke="#154360" stroke-width="1.8" />
      <g stroke="#FFFFFF" stroke-width="2.4">
        <line x1="306" y1="210" x2="306" y2="266" /><line x1="318" y1="210" x2="318" y2="266" /><line x1="330" y1="210" x2="330" y2="266" />
        <line x1="350" y1="210" x2="350" y2="266" /><line x1="362" y1="210" x2="362" y2="266" /><line x1="374" y1="210" x2="374" y2="266" />
      </g>
      <rect x="333" y="150" width="14" height="60" fill="#2C3E50" stroke="#17202A" stroke-width="1.2" />
      <!-- Classifier motor -->
      <rect x="306" y="96" width="68" height="46" fill="#1F618D" stroke="#154360" stroke-width="1.8" rx="4" />
      <g stroke="#85C1E9" stroke-width="1.1">
        <line x1="312" y1="106" x2="368" y2="106" /><line x1="312" y1="114" x2="368" y2="114" /><line x1="312" y1="122" x2="368" y2="122" /><line x1="312" y1="130" x2="368" y2="130" />
      </g>
      <rect x="322" y="142" width="36" height="10" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.2" />
      <text x="340" y="90" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#154360" text-anchor="middle">CLASSIFIER MOTOR (VFD: sets cut size)</text>
      <text x="340" y="296" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#FFFFFF" text-anchor="middle">CLASSIFIER WHEEL</text>

      <!-- Fines outlet duct (right of classifier) to cyclone / baghouse -->
      <rect x="450" y="212" width="120" height="30" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="1.8" />
      <rect x="436" y="218" width="134" height="18" fill="#FFFFFF" stroke="#1C2833" stroke-width="1" />
      <!-- Product discharge (coarse spheroids) right side of hopper -->
      <rect x="480" y="528" width="90" height="26" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="1.8" />
      <rect x="464" y="534" width="106" height="14" fill="#FFFFFF" stroke="#1C2833" stroke-width="1" />
      <!-- Carrier air inlet (left of hopper) -->
      <rect x="110" y="548" width="100" height="26" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="1.8" />
      <rect x="110" y="554" width="116" height="14" fill="#FFFFFF" stroke="#1C2833" stroke-width="1" />
      <!-- Feed screw conveyor (left) -->
      <rect x="100" y="412" width="116" height="30" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="1.8" />
      <rect x="100" y="418" width="116" height="18" fill="#FFFFFF" stroke="#1C2833" stroke-width="1" />
      <rect x="110" y="422" width="100" height="10" fill="#566573" />
      <g stroke="#17202A" stroke-width="1.4">
        <line x1="118" y1="420" x2="124" y2="434" /><line x1="136" y1="420" x2="142" y2="434" /><line x1="154" y1="420" x2="160" y2="434" /><line x1="172" y1="420" x2="178" y2="434" /><line x1="190" y1="420" x2="196" y2="434" />
      </g>
      <path d="M 100 412 L 70 340 L 190 340 L 160 412 Z" fill="#D5D8DC" stroke="#1C2833" stroke-width="1.5" />
      <text x="130" y="372" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833" text-anchor="middle">FLAKE HOPPER</text>
    </g>

    <!-- ================================================================= -->
    <!-- FLOW: TOROIDAL RECIRCULATION, CLASSIFICATION & PARTICLES          -->
    <!-- ================================================================= -->
    <g id="flow_pathways">
      <!-- Toroidal recirculation loops (particle-wall-pin collisions) -->
      <path d="M 262 470 C 232 420, 240 372, 290 366 C 318 364, 318 420, 306 468" fill="none" stroke="#E74C3C" stroke-width="2.2" stroke-dasharray="5,3" marker-end="url(#arrowRed)" />
      <path d="M 418 470 C 448 420, 440 372, 390 366 C 362 364, 362 420, 374 468" fill="none" stroke="#E74C3C" stroke-width="2.2" stroke-dasharray="5,3" marker-end="url(#arrowRed)" />
      <text x="340" y="400" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#C0392B" text-anchor="middle">TOROIDAL</text>
      <text x="340" y="411" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#C0392B" text-anchor="middle">RECIRCULATION</text>
      <text x="340" y="422" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#7B241C" text-anchor="middle">8-16 passes</text>

      <!-- Upward air + fines stream through classifier wheel -->
      <path d="M 340 330 L 340 300" stroke="#27AE60" stroke-width="2.2" stroke-dasharray="4,3" marker-end="url(#arrowGreen)" />
      <path d="M 262 330 Q 262 290, 296 245" fill="none" stroke="#27AE60" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrowGreen)" />
      <path d="M 418 330 Q 418 290, 384 245" fill="none" stroke="#27AE60" stroke-width="1.8" stroke-dasharray="4,3" marker-end="url(#arrowGreen)" />
      <!-- Rejected coarse particles fall back (classifier rejects) -->
      <path d="M 288 275 Q 262 305, 272 345" fill="none" stroke="#7F8C8D" stroke-width="1.6" stroke-dasharray="3,3" marker-end="url(#arrow)" />
      <path d="M 392 275 Q 418 305, 408 345" fill="none" stroke="#7F8C8D" stroke-width="1.6" stroke-dasharray="3,3" marker-end="url(#arrow)" />
      <text x="262" y="318" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#566573" text-anchor="end">oversize rejected</text>

      <!-- Fines exit arrow along duct -->
      <line x1="440" y1="227" x2="585" y2="227" stroke="#C0392B" stroke-width="3.2" marker-end="url(#arrowRed)" />
      <!-- Product exit arrow -->
      <line x1="470" y1="541" x2="585" y2="541" stroke="#27AE60" stroke-width="3.2" marker-end="url(#arrowGreen)" />
      <!-- Feed arrow -->
      <line x1="40" y1="427" x2="98" y2="427" stroke="#2980B9" stroke-width="3.2" marker-end="url(#arrowBlue)" />
      <!-- Air arrow -->
      <line x1="40" y1="561" x2="108" y2="561" stroke="#27AE60" stroke-width="3.2" marker-end="url(#arrowGreen)" />

      <!-- Particles: flat flakes (left of chamber), spheroids near product exit -->
      <g fill="#17202A">
        <rect x="240" y="440" width="12" height="2.5" /><rect x="262" y="392" width="12" height="2.5" /><rect x="410" y="445" width="12" height="2.5" /><rect x="395" y="395" width="12" height="2.5" />
      </g>
      <g fill="#2C3E50" stroke="#17202A" stroke-width="0.8">
        <circle cx="300" cy="560" r="4" /><circle cx="324" cy="568" r="3.4" /><circle cx="356" cy="566" r="4" /><circle cx="384" cy="558" r="3.4" /><circle cx="412" cy="548" r="4" />
      </g>
    </g>

    <!-- ================================================================= -->
    <!-- STREAM CALLOUT BOXES (STRICT MASS BALANCE, BASIS 2,534 kg FLAKE)  -->
    <!-- ================================================================= -->
    <g id="process_streams">
      <rect x="22" y="196" width="152" height="86" fill="#EBF5FB" stroke="#2980B9" stroke-width="1.2" rx="3" />
      <text x="28" y="211" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#1B4F72">1. FLAKE CONCENTRATE FEED</text>
      <text x="28" y="225" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Mass: 2,534 kg (2.22 t / t uSPG)</text>
      <text x="28" y="238" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Grade: 94-97% C, +80/-100 mesh</text>
      <text x="28" y="251" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• D50 = 150-300 um flat platelets</text>
      <text x="28" y="264" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#154360">• Aspect ratio 1:20 to 1:50</text>
      <text x="28" y="276" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#5D6D7E">Pneumatic / screw injection</text>

      <rect x="22" y="582" width="86" height="40" fill="#E8F8F5" stroke="#27AE60" stroke-width="1.2" rx="3" />
      <text x="28" y="596" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1E8449">2. CARRIER AIR</text>
      <text x="28" y="609" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32">Dry, ambient; fan-driven</text>
      <text x="28" y="619" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32">(closed circuit w/ baghouse)</text>

      <rect x="456" y="128" width="150" height="76" fill="#FDEDEC" stroke="#C0392B" stroke-width="1.2" rx="3" />
      <text x="462" y="143" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#900C3F">3. CLEAVAGE FINES TO CYCLONE</text>
      <text x="462" y="157" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Mass: 1,387 kg (54.73%)</text>
      <text x="462" y="170" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• 1.215 t fines / t uSPG</text>
      <text x="462" y="183" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• D50 &lt; 5 um, non-spherical</text>
      <text x="462" y="196" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#900C3F">• Sold ~$468/t (refractory/recarb)</text>

      <rect x="456" y="570" width="186" height="64" fill="#E8F8F5" stroke="#27AE60" stroke-width="1.2" rx="3" />
      <text x="462" y="585" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#0E6251">4. SPHERICAL uSPG PRODUCT</text>
      <text x="462" y="599" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Mass: 1,141 kg (45.05% yield)</text>
      <text x="462" y="612" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• D50 = 15 um | tap &gt;= 0.95 g/cm3</text>
      <text x="462" y="625" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32">• Purity ~95% C (pre-purification)</text>

      <rect x="22" y="640" width="200" height="30" fill="#FEF9E7" stroke="#F39C12" stroke-width="1" rx="3" />
      <text x="28" y="653" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#B9770E">Baghouse filter dust: 6 kg (0.22%)</text>
      <text x="28" y="664" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#7E5109">Handling loss, within 5% residual cap</text>
    </g>

    <!-- ================================================================= -->
    <!-- RIGHT PANEL: DIDACTIC INSET                                       -->
    <!-- ================================================================= -->
    <g transform="translate(650, 88)" id="spheronization_mechanism_inset">
      <rect x="0" y="0" width="530" height="572" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.8" rx="5" />
      <rect x="0" y="0" width="530" height="28" fill="#1C2833" rx="4" />
      <text x="14" y="18" font-family="Helvetica, Arial, sans-serif" font-size="11" font-weight="bold" fill="#ECF0F1">MECHANISM INSET: FROM PLATELET TO SPHEROID, AND WHERE THE MASS GOES</text>

      <!-- SUB-PANEL A: 4-step morphology evolution -->
      <rect x="14" y="38" width="502" height="248" fill="#F4F9FD" stroke="#85C1E9" stroke-width="1.2" rx="4" />
      <text x="24" y="55" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#1B4F72">A. MORPHOLOGY EVOLUTION IN THE PIN-ROTOR CHAMBER (SIDE VIEW, NOT TO SCALE)</text>

      <!-- Step 1: flat flake -->
      <g transform="translate(24, 64)">
        <rect x="0" y="0" width="114" height="150" fill="#FFFFFF" stroke="#BDC3C7" stroke-width="1" rx="3" />
        <text x="57" y="14" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#2C3E50" text-anchor="middle">1. RAW FLAKE</text>
        <g fill="#34495E" stroke="#17202A" stroke-width="0.8">
          <rect x="10" y="62" width="94" height="6" /><rect x="8" y="70" width="98" height="6" /><rect x="10" y="78" width="94" height="6" /><rect x="8" y="86" width="98" height="6" />
        </g>
        <line x1="10" y1="104" x2="104" y2="104" stroke="#34495E" stroke-width="1" marker-start="url(#dimTick)" marker-end="url(#dimTick)" />
        <text x="57" y="116" font-family="Courier, monospace" font-size="7.5" fill="#34495E" text-anchor="middle">150-300 um</text>
        <text x="57" y="132" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#566573" text-anchor="middle">Exposed prismatic edges</text>
        <text x="57" y="142" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#566573" text-anchor="middle">Tap 0.35-0.45 g/cm3</text>
      </g>
      <!-- Step 2: buckling + delamination -->
      <g transform="translate(150, 64)">
        <rect x="0" y="0" width="114" height="150" fill="#FFFFFF" stroke="#BDC3C7" stroke-width="1" rx="3" />
        <text x="57" y="14" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#B9770E" text-anchor="middle">2. IMPACT + BUCKLING</text>
        <path d="M 10 80 Q 30 52, 52 80 T 98 74" fill="none" stroke="#E67E22" stroke-width="6" stroke-linecap="round" />
        <path d="M 12 92 Q 32 70, 54 92 T 98 88" fill="none" stroke="#34495E" stroke-width="5" stroke-linecap="round" />
        <polygon points="86,46 96,42 94,52" fill="#C0392B" /><polygon points="100,58 108,56 105,64" fill="#C0392B" /><polygon points="20,48 28,44 27,53" fill="#C0392B" />
        <line x1="57" y1="26" x2="57" y2="48" stroke="#C0392B" stroke-width="2" marker-end="url(#arrowRed)" />
        <text x="57" y="118" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#B9770E" text-anchor="middle">Pin / wall impact</text>
        <text x="57" y="132" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#C0392B" text-anchor="middle">Edge shear sheds</text>
        <text x="57" y="142" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#C0392B" text-anchor="middle">&lt; 5 um fines</text>
      </g>
      <!-- Step 3: folding -->
      <g transform="translate(276, 64)">
        <rect x="0" y="0" width="114" height="150" fill="#FFFFFF" stroke="#BDC3C7" stroke-width="1" rx="3" />
        <text x="57" y="14" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1F618D" text-anchor="middle">3. CABBAGE FOLD</text>
        <path d="M 22 92 C 22 52, 92 52, 92 88 C 92 112, 36 112, 36 86 C 36 68, 78 68, 78 86" fill="none" stroke="#2980B9" stroke-width="5" stroke-linecap="round" />
        <path d="M 30 100 C 50 118, 80 112, 88 98" fill="none" stroke="#34495E" stroke-width="3" stroke-linecap="round" />
        <text x="57" y="132" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1B4F72" text-anchor="middle">Lamellae wrap core,</text>
        <text x="57" y="142" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1B4F72" text-anchor="middle">trapping micro-voids</text>
      </g>
      <!-- Step 4: sphere -->
      <g transform="translate(402, 64)">
        <rect x="0" y="0" width="100" height="150" fill="#FFFFFF" stroke="#27AE60" stroke-width="1.2" rx="3" />
        <text x="50" y="14" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1E8449" text-anchor="middle">4. uSPG SPHEROID</text>
        <circle cx="50" cy="78" r="34" fill="#2C3E50" stroke="#17202A" stroke-width="1.6" />
        <path d="M 22 78 C 22 54, 78 54, 78 78 C 78 98, 30 98, 30 78 C 30 64, 70 64, 70 78" fill="none" stroke="#95A5A6" stroke-width="2.4" stroke-linecap="round" />
        <circle cx="50" cy="78" r="12" fill="none" stroke="#BDC3C7" stroke-width="1.4" />
        <circle cx="50" cy="78" r="3.5" fill="#16A085" />
        <text x="50" y="128" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#1E8449" text-anchor="middle">D50 = 15 um</text>
        <text x="50" y="140" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#145A32" text-anchor="middle">Tap 0.95-1.02 g/cm3</text>
      </g>
      <!-- Arrows between steps -->
      <g stroke="#2C3E50" stroke-width="2" fill="none">
        <line x1="140" y1="140" x2="148" y2="140" marker-end="url(#arrow)" /><line x1="266" y1="140" x2="274" y2="140" marker-end="url(#arrow)" /><line x1="392" y1="140" x2="400" y2="140" marker-end="url(#arrow)" />
      </g>
      <rect x="24" y="226" width="482" height="50" fill="#FFFFFF" stroke="#BDC3C7" stroke-width="1" rx="3" />
      <text x="32" y="240" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#2C3E50">WHY IT MATTERS:</text>
      <text x="32" y="252" font-family="Helvetica, Arial, sans-serif" font-size="7.8" fill="#34495E">Rounding raises tap density (about 2.3x vs. flake), improves electrode packing and Li+ pathways, and hides reactive</text>
      <text x="32" y="263" font-family="Helvetica, Arial, sans-serif" font-size="7.8" fill="#34495E">edge planes. The price is mechanical: each pass sheds edge material, so more than half of the feed leaves as fines.</text>
      <text x="32" y="273" font-family="Helvetica, Arial, sans-serif" font-size="7.8" fill="#C0392B">Remaining BET area is still 6.5-9.0 m2/g (too high) until pitch coating (Stage 4).</text>

      <!-- SUB-PANEL B: mass-balance stacked bar -->
      <rect x="14" y="296" width="502" height="124" fill="#FEF9E7" stroke="#F39C12" stroke-width="1.2" rx="4" />
      <text x="24" y="313" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#B9770E">B. MASS BALANCE OF THE FLAKE FEED (2,534 kg = 100%)</text>
      <rect x="24" y="326" width="216" height="30" fill="#27AE60" stroke="#1C2833" stroke-width="1.2" />
      <rect x="240" y="326" width="262" height="30" fill="#C0392B" stroke="#1C2833" stroke-width="1.2" />
      <rect x="502" y="326" width="2" height="30" fill="#F39C12" stroke="#1C2833" stroke-width="1" />
      <text x="132" y="346" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">uSPG 1,141 kg (45.05%)</text>
      <text x="371" y="346" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Fines scrap 1,387 kg (54.73%)</text>
      <line x1="503" y1="326" x2="503" y2="372" stroke="#B9770E" stroke-width="1" />
      <text x="500" y="384" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#7E5109" text-anchor="end">Dust 6 kg (0.22%)</text>
      <text x="24" y="376" font-family="Courier, monospace" font-size="8" fill="#34495E">1,141 + 1,387 + 6 = 2,534 kg (closed balance)</text>
      <text x="24" y="396" font-family="Helvetica, Arial, sans-serif" font-size="8.2" fill="#1C2833">Feed multiplier 2.22 t flake per t uSPG; scrap output 1.215 t per t uSPG (ANL-22/74 Table 3).</text>
      <text x="24" y="410" font-family="Helvetica, Arial, sans-serif" font-size="8.2" font-weight="bold" fill="#900C3F">Fines are not waste: sold at ~$468/t, credited back against the cSPG cost (-$649/t).</text>

      <!-- SUB-PANEL C: ledger -->
      <rect x="14" y="430" width="502" height="132" fill="#EAFAF1" stroke="#27AE60" stroke-width="1.2" rx="4" />
      <text x="24" y="447" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#0E6251">C. STAGE 2 ENERGY &amp; COST LEDGER (ANL-22/74 TABLE 3; DATASET graphite_process_energy_lca.csv)</text>
      <line x1="24" y1="454" x2="504" y2="454" stroke="#27AE60" stroke-width="0.8" />
      <text x="24" y="470" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Stage electricity (per kg uSPG)</text>
      <text x="196" y="470" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">1.899 kWh/kg</text>
      <text x="24" y="486" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Per kg cSPG (cumulative stage)</text>
      <text x="196" y="486" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">2.167 kWh/kg</text>
      <text x="24" y="502" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Thermal fuel</text>
      <text x="196" y="502" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">0.0 MJ/kg (all electric)</text>
      <text x="24" y="518" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Cumulative with Stage 1</text>
      <text x="196" y="518" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">3.519 kWh/kg cSPG</text>
      <line x1="334" y1="458" x2="334" y2="552" stroke="#A3E4D7" stroke-width="1" />
      <text x="344" y="470" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Milling power + liner wear</text>
      <text x="344" y="482" font-family="Courier, monospace" font-size="8.5" fill="#34495E">+$550 / t cSPG</text>
      <text x="344" y="498" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• Yield-loss penalty (2.22x feed)</text>
      <text x="344" y="510" font-family="Courier, monospace" font-size="8.5" fill="#34495E">+$1,200 / t cSPG</text>
      <text x="344" y="526" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">• China share of spheronization</text>
      <text x="344" y="538" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#C0392B">99.0% (IEA 2024)</text>
      <text x="24" y="546" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#145A32">Stage 2 = 27.4% of HF-route electricity: the single biggest cost lever before purification.</text>
    </g>
"""
    ]
    lines.append(render_title_block(
        "DWG-MCH-02",
        "AIR-CLASSIFIER IMPACT MILL (SECTION A-A)",
        "Mechanical Spheronization (Stage 2)",
        "Elec: 1.899 kWh/kg uSPG | Core Yield: 45.05% | Fines: 54.73%",
        "ANL GREET ANL-22/74 Table 3; Engels (2022); IEA (2024)"
    ))
    lines.append("</svg>")
    return "\n".join(lines)


# =====================================================================
# Drawing 3: Agitated HF/HCl Acid Leaching Reactor
# =====================================================================
def create_svg_acid_reactor():
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">',
        common_svg_defs(),
        '  <rect width="1200" height="800" fill="#F8F9F9" />',
        render_drawing_header(
            "PTFE-LINED HF / HCl ACID DIGESTION REACTOR: CHEMICAL PURIFICATION",
            "Stage 3A Leaching: Dissolution of Interlamellar Silicate & Metal Oxide Ash (95.0% -> >=99.95% C | ANL-22/74 Table 3)"
        ),
        """
    <!-- ================================================================= -->
    <!-- LEFT PANEL: CAD CROSS-SECTION OF PTFE-LINED ACID DIGESTION VESSEL -->
    <!-- ================================================================= -->
    <g id="reactor_vessel">

      <!-- Structural Support Skirt / I-Beam Legs & Concrete Plinths -->
      <rect x="200" y="555" width="20" height="105" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <rect x="500" y="555" width="20" height="105" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <rect x="180" y="660" width="58" height="12" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.5" />
      <rect x="482" y="660" width="58" height="12" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.5" />

      <!-- External Half-Pipe / Welded Steam Heating Jacket (60-90 °C, 0.955 MJ/kg) -->
      <path d="M 164 250 L 164 495 C 164 598, 556 598, 556 495 L 556 250 L 538 250 L 538 492 C 538 576, 182 576, 182 492 L 182 250 Z" fill="#F5B041" fill-opacity="0.38" stroke="#BA4A00" stroke-width="1.8" />
      <!-- Internal Steam Baffle Spiral Rings in Jacket -->
      <g fill="#D35400" stroke="#A04000" stroke-width="1">
        <rect x="164" y="290" width="18" height="6" /><rect x="538" y="290" width="18" height="6" />
        <rect x="164" y="345" width="18" height="6" /><rect x="538" y="345" width="18" height="6" />
        <rect x="164" y="400" width="18" height="6" /><rect x="538" y="400" width="18" height="6" />
        <rect x="164" y="455" width="18" height="6" /><rect x="538" y="455" width="18" height="6" />
      </g>
      <!-- Steam Inlet Nozzle (Upper Left Jacket) & Condensate Trap Drain (Lower Right Jacket) -->
      <rect x="136" y="264" width="28" height="14" fill="url(#metallicCyl)" stroke="#BA4A00" stroke-width="1.4" />
      <rect x="556" y="476" width="28" height="14" fill="url(#metallicCyl)" stroke="#BA4A00" stroke-width="1.4" />
      <line x1="584" y1="483" x2="622" y2="483" stroke="#D35400" stroke-width="2.2" marker-end="url(#arrowOrange)" />
      <text x="586" y="473" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#BA4A00">CONDENSATE</text>
      <text x="586" y="496" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#78281F">Steam Trap</text>

      <!-- Carbon-Steel Pressure Vessel Shell & Torispherical Dished Head (ISO 128 Hatching) -->
      <path d="M 182 214 C 182 158, 538 158, 538 214 L 538 492 C 538 576, 182 576, 182 492 Z" fill="url(#steelHatch)" stroke="#1C2833" stroke-width="2.2" />

      <!-- Bolted Main Vessel Body Flange (Splits Top Dished Head from Shell at y=215) -->
      <rect x="168" y="210" width="384" height="12" fill="#566573" stroke="#1C2833" stroke-width="1.4" />
      <g fill="#ECF0F1" stroke="#1C2833" stroke-width="0.8">
        <rect x="174" y="206" width="6" height="20" /><rect x="192" y="206" width="6" height="20" />
        <rect x="522" y="206" width="6" height="20" /><rect x="540" y="206" width="6" height="20" />
      </g>

      <!-- Heavy-Duty PTFE / PVDF Fluoropolymer Corrosion Barrier Lining (8 mm Isostatic Liner) -->
      <path d="M 196 216 C 196 170, 524 170, 524 216 L 524 488 C 524 560, 196 560, 196 488 Z" fill="url(#ptfeHatch)" stroke="#0E6251" stroke-width="2" />
      <path d="M 204 218 C 204 178, 516 178, 516 218 L 516 485 C 516 550, 204 550, 204 485 Z" fill="#FFFFFF" stroke="#16A085" stroke-width="1.5" />
      <text x="488" y="242" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#0E6251" text-anchor="end">PTFE LINER (HF-Inert)</text>

      <!-- Corrosive Acid-Graphite Slurry Fill (HF + HCl + HNO3 + uSPG Cores at 60-90 °C) -->
      <path d="M 204 268 L 516 268 L 516 485 C 516 550, 204 550, 204 485 Z" fill="#A3E4D7" fill-opacity="0.65" />
      <path d="M 204 268 L 516 268 L 516 485 C 516 550, 204 550, 204 485 Z" fill="url(#slurryGradient)" opacity="0.45" />
      <!-- Agitated Liquid Vortex Meniscus -->
      <path d="M 204 268 Q 280 262, 360 274 Q 440 262, 516 268" fill="none" stroke="#0E6251" stroke-width="2" />
      <!-- Corrosive Acid Vapor Headspace (SiF4, HF, NOx fumes above liquid) -->
      <path d="M 204 218 C 204 178, 516 178, 516 218 L 516 268 L 204 268 Z" fill="#E8DAEF" fill-opacity="0.32" />
      <text x="445" y="258" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-style="italic" fill="#6C3483" text-anchor="middle">SiF4(g) + HF(g) Vapor Headspace</text>

      <!-- Internal PTFE-Encapsulated Anti-Vortex Wall Baffles (4x90 deg) -->
      <rect x="208" y="278" width="14" height="205" fill="#117A65" fill-opacity="0.8" stroke="#0E6251" stroke-width="1.2" />
      <rect x="498" y="278" width="14" height="205" fill="#117A65" fill-opacity="0.8" stroke="#0E6251" stroke-width="1.2" />
      <text x="226" y="476" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#FFFFFF">PTFE BAFFLE</text>
    </g>

    <!-- ================================================================= -->
    <!-- AGITATION DRIVE, DOUBLE MECHANICAL SEAL, DIP-TUBES & IMPELLERS    -->
    <!-- ================================================================= -->
    <g id="agitator_and_internals">
      <!-- Explosion-Proof Variable-Speed Drive Motor & Helical Gearbox (Positioned well below header) -->
      <text x="360" y="98" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#154360" text-anchor="middle">AGITATOR DRIVE</text>
      <rect x="326" y="103" width="68" height="36" fill="#1F618D" stroke="#154360" stroke-width="1.8" rx="4" />
      <g stroke="#85C1E9" stroke-width="1.1">
        <line x1="332" y1="111" x2="388" y2="111" /><line x1="332" y1="118" x2="388" y2="118" /><line x1="332" y1="125" x2="388" y2="125" /><line x1="332" y1="132" x2="388" y2="132" />
      </g>

      <!-- Pressurized Double Cartridge Mechanical Seal (N2 Barrier Gas Purge) -->
      <rect x="336" y="139" width="48" height="22" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <rect x="328" y="161" width="64" height="15" fill="#566573" stroke="#1C2833" stroke-width="1.4" />
      <text x="331" y="153" font-family="Helvetica, Arial, sans-serif" font-size="7" font-weight="bold" fill="#1C2833" text-anchor="end">DOUBLE SEAL</text>

      <!-- PTFE-Sleeved Central Agitator Shaft -->
      <rect x="353" y="176" width="14" height="329" fill="#16A085" stroke="#0E6251" stroke-width="1.5" />
      <line x1="360" y1="176" x2="360" y2="505" stroke="#0E6251" stroke-width="1" stroke-dasharray="6,3" />

      <!-- Upper 4-Blade Pitched-Blade Turbine (45 deg Axial Down-Pumping) -->
      <polygon points="282,352 353,358 353,372 276,366" fill="#0E6251" stroke="#1C2833" stroke-width="1.4" />
      <polygon points="438,352 367,358 367,372 444,366" fill="#0E6251" stroke="#1C2833" stroke-width="1.4" />
      <rect x="348" y="354" width="24" height="20" fill="#117A65" stroke="#1C2833" stroke-width="1.4" />

      <!-- Lower 4-Blade Pitched-Blade / Hydrofoil Turbine (Solids Suspension off Dish Bottom) -->
      <polygon points="272,468 353,475 353,490 266,482" fill="#0E6251" stroke="#1C2833" stroke-width="1.4" />
      <polygon points="448,468 367,475 367,490 454,482" fill="#0E6251" stroke="#1C2833" stroke-width="1.4" />
      <rect x="348" y="471" width="24" height="22" fill="#117A65" stroke="#1C2833" stroke-width="1.4" />

      <!-- Axial-Radial Circulation Loops & Rising SiF4 Gas Micro-Bubbles -->
      <path d="M 325 380 C 280 420, 245 420, 245 365 C 245 315, 295 315, 330 348" fill="none" stroke="#0E6251" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrowGreen)" />
      <path d="M 395 380 C 440 420, 475 420, 475 365 C 475 315, 425 315, 390 348" fill="none" stroke="#0E6251" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrowGreen)" />
      <path d="M 325 492 C 270 532, 232 510, 248 455" fill="none" stroke="#0E6251" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrowGreen)" />
      <path d="M 395 492 C 450 532, 488 510, 472 455" fill="none" stroke="#0E6251" stroke-width="1.8" stroke-dasharray="5,3" marker-end="url(#arrowGreen)" />

      <!-- Suspended uSPG Graphite Spheroids & Evolving SiF4(g) Bubbles -->
      <g fill="#1C2833">
        <circle cx="265" cy="395" r="3.2" /><circle cx="295" cy="435" r="3.2" /><circle cx="320" cy="515" r="3.2" />
        <circle cx="455" cy="395" r="3.2" /><circle cx="425" cy="435" r="3.2" /><circle cx="400" cy="515" r="3.2" />
      </g>
      <g fill="#FFFFFF" stroke="#8E44AD" stroke-width="1">
        <circle cx="285" cy="330" r="3.5" /><circle cx="305" cy="295" r="4" /><circle cx="430" cy="325" r="3.5" /><circle cx="415" cy="290" r="4" />
      </g>

      <!-- Submerged PTFE Acid Injection Dip-Tube (Delivers HF/HCl/HNO3 directly to Impeller Zone) -->
      <rect x="236" y="182" width="20" height="14" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <rect x="242" y="196" width="8" height="234" fill="#E74C3C" stroke="#922B21" stroke-width="1.2" />
      <text x="254" y="302" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#922B21">PTFE DIP-TUBE</text>

      <!-- Submerged PTFE Thermowell Probe (TIC-301) -->
      <rect x="283" y="176" width="18" height="14" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <rect x="289" y="190" width="6" height="205" fill="#2980B9" stroke="#154360" stroke-width="1.2" />

      <!-- Solids Feed Nozzle & Scrubber Off-Gas Nozzle on Top Head -->
      <rect x="404" y="176" width="20" height="14" fill="#566573" stroke="#1C2833" stroke-width="1.2" />
      <rect x="456" y="182" width="18" height="14" fill="#566573" stroke="#1C2833" stroke-width="1.2" />

      <!-- Bottom Flush-Seated Ram Discharge Valve & Slurry Outlet -->
      <rect x="342" y="548" width="36" height="36" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <polygon points="348,548 372,548 360,532" fill="#16A085" stroke="#0E6251" stroke-width="1.4" />
      <!-- P&ID Control Valve Symbol on Bottom Slurry Line -->
      <polygon points="344,592 376,608 376,592 344,608" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.5" />
    </g>

    <!-- ================================================================= -->
    <!-- P&ID INSTRUMENTATION: TIC-301 STEAM LOOP & SCRUBBER VENT          -->
    <!-- ================================================================= -->
    <g id="pid_instrumentation">
      <!-- Temperature Indicator Controller (TIC-301) coupled to Steam Control Valve (TCV-301) -->
      <circle cx="292" cy="120" r="14" fill="#FFFFFF" stroke="#2980B9" stroke-width="1.5" />
      <line x1="278" y1="120" x2="306" y2="120" stroke="#2980B9" stroke-width="1" />
      <text x="292" y="117" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#154360" text-anchor="middle">TIC</text>
      <text x="292" y="128" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#154360" text-anchor="middle">301</text>
      <line x1="292" y1="134" x2="292" y2="176" stroke="#2980B9" stroke-width="1.4" />

      <!-- Steam Control Valve (TCV-301) on Jacket Inlet -->
      <polygon points="96,263 118,279 118,263 96,279" fill="#FFFFFF" stroke="#BA4A00" stroke-width="1.5" />
      <path d="M 97 253 A 10 10 0 0 1 117 253 Z" fill="#D35400" stroke="#BA4A00" stroke-width="1.2" />
      <line x1="107" y1="253" x2="107" y2="271" stroke="#BA4A00" stroke-width="1.4" />
      <text x="107" y="292" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#BA4A00" text-anchor="middle">TCV-301</text>
      <!-- Signal Line from TIC-301 to TCV-301 routed cleanly below Box 1 -->
      <path d="M 278 120 L 188 120 L 188 196 L 107 196 L 107 244" fill="none" stroke="#2980B9" stroke-width="1.1" stroke-dasharray="4,3" />
    </g>

    <!-- ================================================================= -->
    <!-- PROCESS STREAM CALLOUT BOXES (STRICT MASS & REAGENT LEDGER)       -->
    <!-- ================================================================= -->
    <g id="process_streams">
      <!-- 1. Mixed Acid Reagent Feed (HF + HCl + HNO3) -->
      <path d="M 174 152 L 246 152 L 246 182" fill="none" stroke="#C0392B" stroke-width="3" marker-end="url(#arrowRed)" />
      <rect x="22" y="98" width="152" height="84" fill="#FDEDEC" stroke="#C0392B" stroke-width="1.2" rx="3" />
      <text x="28" y="112" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#900C3F">1. ACID REAGENT FEED</text>
      <text x="28" y="125" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#78281F">• Total: 480 kg / t cSPG</text>
      <text x="28" y="138" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• HF (40%): 180 kg (~$215)</text>
      <text x="28" y="150" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• HCl (31%): 200 kg (~$45)</text>
      <text x="28" y="162" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• HNO3 (68%): 100 kg (~$40)</text>
      <text x="28" y="174" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#900C3F">ANL-22/74 Table 3 LCI</text>

      <!-- 2. Uncoated Spherical Graphite (uSPG) Solids Feed (Right of Drive Motor) -->
      <path d="M 442 128 L 414 128 L 414 176" fill="none" stroke="#2C3E50" stroke-width="3" marker-end="url(#arrow)" />
      <rect x="442" y="96" width="146" height="58" fill="#EBF5FB" stroke="#2980B9" stroke-width="1.2" rx="3" />
      <text x="448" y="110" font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="bold" fill="#1B4F72">2. uSPG SOLIDS INLET</text>
      <text x="448" y="123" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Mass: 1,141 kg (95.0% C)</text>
      <text x="448" y="135" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• D50 = 15.0 um spheroids</text>
      <text x="448" y="147" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#154360">• Interstitial Ash: ~5.0 wt%</text>

      <!-- 3. Steam Jacket Thermal Input (Placed lower-left below vessel midline) -->
      <line x1="22" y1="385" x2="84" y2="385" stroke="#D35400" stroke-width="2.5" />
      <path d="M 84 385 L 118 385 L 118 271 L 136 271" fill="none" stroke="#D35400" stroke-width="2.5" marker-end="url(#arrowOrange)" />
      <rect x="22" y="396" width="134" height="58" fill="#FEF9E7" stroke="#F39C12" stroke-width="1.2" rx="3" />
      <text x="28" y="410" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#B9770E">3. PROCESS STEAM</text>
      <text x="28" y="423" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Temp: 60 - 90 °C</text>
      <text x="28" y="435" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• Fuel: 0.955 MJ/kg</text>
      <text x="28" y="446" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#7E5109">(0.965 MJ/kg cSPG)</text>

      <!-- 4. Off-Gas Vent to Alkaline Wet Scrubber (Far-right upper corner) -->
      <path d="M 465 182 L 465 166 L 512 166" fill="none" stroke="#8E44AD" stroke-width="2.5" marker-end="url(#arrow)" />
      <rect x="516" y="158" width="124" height="56" fill="#F5EEF8" stroke="#8E44AD" stroke-width="1.2" rx="3" />
      <text x="522" y="172" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#6C3483">4. TO WET SCRUBBER</text>
      <text x="522" y="185" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1C2833">• SiF4(g), HF(g), NOx</text>
      <text x="522" y="197" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#5B2C6F">• Alkaline Ca(OH)2 wash</text>
      <text x="522" y="208" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#5B2C6F">captures fluorides</text>

      <!-- 5. Purified Slurry Discharge to Counter-Current Filtration & Lime Neutralization -->
      <line x1="360" y1="608" x2="360" y2="656" stroke="#16A085" stroke-width="3.5" marker-end="url(#arrowGreen)" />
      <rect x="22" y="662" width="644" height="118" fill="#E8F8F5" stroke="#16A085" stroke-width="1.4" rx="3" />
      <text x="32" y="678" font-family="Helvetica, Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#0E6251">5. PURIFIED SLURRY TO COUNTER-CURRENT FILTER PRESS &amp; LIME NEUTRALIZATION</text>
      <text x="32" y="694" font-family="Helvetica, Arial, sans-serif" font-size="8.5" fill="#1C2833">• Purified Graphite Filter Cake: 1,010 kg (&gt;= 99.95% C | Stage Mass Yield: 88.5%)</text>
      <text x="32" y="708" font-family="Helvetica, Arial, sans-serif" font-size="8.5" fill="#1C2833">• Counter-Current Deionized Wash Water: 15 - 25 m3/t | Slaked Lime: 400 kg CaO (~$60/t)</text>
      <text x="32" y="722" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#900C3F">• Precipitated Sludge: ~650 kg CaF2 / CaCl2 / SiF4 cake (Waste disposal ~$320/t | Stage 3A: +$1,100/t)</text>
      <text x="32" y="736" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#117A65">• Stage 3A Electricity: 0.276 kWh/kg | Total Natural cSPG Chemical Route Power: 7.91 kWh/kg</text>
      <text x="32" y="749" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#5D6D7E">• Environmental Regulatory Audit: Zero toxic fluoride discharge via complete CaF2 precipitation.</text>
      <text x="32" y="762" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#5D6D7E">• Quality Lot Spec: Trace Fe &lt; 20 ppm, Ash &lt;= 0.05% for battery cell safety qualification.</text>
    </g>

    <!-- ================================================================= -->
    <!-- RIGHT PANEL: DIDACTIC CHEMICAL & THERMODYNAMIC INSET              -->
    <!-- ================================================================= -->
    <g transform="translate(650, 94)" id="chemistry_reactions_inset">
      <rect x="0" y="0" width="530" height="566" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.8" rx="5" />
      <rect x="0" y="0" width="530" height="28" fill="#1C2833" rx="4" />
      <text x="14" y="18" font-family="Helvetica, Arial, sans-serif" font-size="11" font-weight="bold" fill="#ECF0F1">CHEMICAL INSET: PORE-DIFFUSION LEACHING, STOICHIOMETRY &amp; THERMAL TRADE-OFF</text>

      <!-- SUB-PANEL A: Intra-Particle Pore Diffusion & Ash Dissolution inside uSPG Sphere -->
      <rect x="14" y="38" width="502" height="172" fill="#F4F9FD" stroke="#85C1E9" stroke-width="1.2" rx="4" />
      <text x="24" y="55" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#1B4F72">A. INTRA-PARTICLE PORE DIFFUSION IN CABBAGE-FOLDED uSPG (D50 = 15.0 um)</text>

      <!-- Cross-Section of uSPG Sphere under Acid Attack -->
      <g transform="translate(95, 130)">
        <circle cx="0" cy="0" r="54" fill="#2C3E50" stroke="#17202A" stroke-width="1.8" />
        <path d="M -44 0 C -44 -32, 44 -32, 44 0 C 44 34, -34 34, -34 0 C -34 -20, 30 -20, 30 0" fill="none" stroke="#95A5A6" stroke-width="2.5" stroke-linecap="round" />
        <!-- Trapped Ash Inclusions being dissolved -->
        <circle cx="-18" cy="-12" r="6" fill="#E74C3C" stroke="#FFFFFF" stroke-width="1" />
        <text x="-18" y="-10" font-family="Helvetica, Arial, sans-serif" font-size="6.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">SiO2</text>
        <circle cx="16" cy="14" r="6" fill="#F39C12" stroke="#FFFFFF" stroke-width="1" />
        <text x="16" y="16" font-family="Helvetica, Arial, sans-serif" font-size="6.5" font-weight="bold" fill="#1C2833" text-anchor="middle">Fe</text>
        <!-- Acid Diffusion Inward Arrows (HF / HCl) -->
        <line x1="-72" y1="-22" x2="-28" y2="-14" stroke="#C0392B" stroke-width="2" marker-end="url(#arrowRed)" />
        <text x="-74" y="-26" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#C0392B">HF / HCl</text>
        <!-- Dissolved Product Diffusion Outward Arrows (SiF6^2-, FeCl3) -->
        <line x1="24" y1="12" x2="72" y2="24" stroke="#16A085" stroke-width="2" marker-end="url(#arrowGreen)" />
        <text x="58" y="38" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#0E6251">H2SiF6 / FeCl3</text>
      </g>

      <!-- Explanation of Why Flotation Cannot Reach 99.95% C -->
      <text x="182" y="76" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#1C2833">Why Mechanical Flotation Stops at 94-97% C:</text>
      <text x="182" y="90" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">• Residual 3-5% ash (SiO2, Fe2O3, Al2O3) is crystallographically locked</text>
      <text x="182" y="102" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">  between graphene lamellae and folded inside uSPG micro-cavities.</text>
      <text x="182" y="118" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#900C3F">Why HF Acid Is Required in Route 3A:</text>
      <text x="182" y="132" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">• HCl and HNO3 dissolve metallic oxides (Fe, Al, Ca) but CANNOT break</text>
      <text x="182" y="144" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#34495E">  the strong covalent Si-O bond (452 kJ/mol) of quartz (SiO2).</text>
      <text x="182" y="158" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#0E6251">• Only HF forms stable hexafluorosilicate [SiF6]2- complexes at 60-90 °C,</text>
      <text x="182" y="170" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#0E6251">  leaving clean internal pores ready for Stage 4 pitch sealing.</text>
      <text x="182" y="196" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#1B4F72">• Battery Spec: Fe &lt; 20 ppm (prevents internal lithium-dendrite shorting).</text>

      <!-- SUB-PANEL B: Stoichiometric Leaching & Neutralization Equations -->
      <rect x="14" y="218" width="502" height="196" fill="#FEF9E7" stroke="#F39C12" stroke-width="1.2" rx="4" />
      <text x="24" y="235" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#B9770E">B. STOICHIOMETRIC DIGESTION &amp; EFFLUENT NEUTRALIZATION REACTIONS</text>

      <!-- Box 1: Silicate Dissolution -->
      <rect x="24" y="244" width="482" height="50" fill="#FADBD8" stroke="#E74C3C" stroke-width="1" rx="3" />
      <text x="32" y="258" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#900C3F">1. QUARTZ &amp; ALUMINOSILICATE DISSOLUTION (180 kg HF / t cSPG):</text>
      <text x="32" y="273" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#78281F">SiO2(s) + 4 HF(aq)  ---&gt;  SiF4(g)^ + 2 H2O(l)       [Gas to Wet Scrubber]</text>
      <text x="32" y="287" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#78281F">SiO2(s) + 6 HF(aq)  ---&gt;  H2[SiF6](aq) + 2 H2O(l)   [Soluble Fluosilicate]</text>

      <!-- Box 2: Metal Oxide Leaching -->
      <rect x="24" y="300" width="482" height="50" fill="#FCF3CF" stroke="#D4AC0D" stroke-width="1" rx="3" />
      <text x="32" y="314" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#7D6608">2. TRANSITION METAL OXIDE &amp; SULFIDE LEACHING (200 kg HCl + 100 kg HNO3 / t cSPG):</text>
      <text x="32" y="329" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#7E5109">Fe2O3(s) + 6 HCl(aq) ---&gt; 2 FeCl3(aq) + 3 H2O(l)    [Soluble Ferric Chloride]</text>
      <text x="32" y="343" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#7E5109">Al2O3(s) + 6 HCl(aq) ---&gt; 2 AlCl3(aq) + 3 H2O(l)    [HNO3 oxidizes FeS2 pyrite]</text>

      <!-- Box 3: Lime Slaking & Fluoride Precipitation -->
      <rect x="24" y="356" width="482" height="50" fill="#E8F8F5" stroke="#16A085" stroke-width="1" rx="3" />
      <text x="32" y="370" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#0E6251">3. WASTEWATER LIME NEUTRALIZATION &amp; SLUDGE PRECIPITATION (400 kg CaO / t cSPG):</text>
      <text x="32" y="385" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#145A32">2 HF(aq) + Ca(OH)2(aq)     ---&gt; CaF2(s)v + 2 H2O(l)   [Insoluble Fluorspar Cake]</text>
      <text x="32" y="399" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#145A32">H2SiF6(aq) + 3 Ca(OH)2(aq) ---&gt; 3 CaF2(s)v + SiO2(s)v + 4 H2O(l)</text>

      <!-- SUB-PANEL C: Route 3A (Chemical HF) vs. Route 3B (Thermal 2,800 °C) Comparison Ledger -->
      <rect x="14" y="422" width="502" height="138" fill="#EAFAF1" stroke="#27AE60" stroke-width="1.2" rx="4" />
      <text x="24" y="439" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#0E6251">C. PURIFICATION PATHWAY BENCHMARK: CHEMICAL HF (3A) VS. THERMAL 2,800 °C (3B)</text>
      <line x1="24" y1="446" x2="504" y2="446" stroke="#27AE60" stroke-width="0.8" />

      <!-- Table Headers -->
      <text x="24" y="460" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#566573">PARAMETER (BASIS: 1.0 t cSPG)</text>
      <text x="215" y="460" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#900C3F">ROUTE 3A: HF ACID (99% SHARE)</text>
      <text x="372" y="460" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1B4F72">ROUTE 3B: THERMAL (&lt;1% SHARE)</text>
      <line x1="24" y1="465" x2="504" y2="465" stroke="#A3E4D7" stroke-width="0.8" />

      <text x="24" y="479" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Operating Temperature:</text>
      <text x="215" y="479" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#0E6251">60 - 90 °C (Steam Jacket)</text>
      <text x="372" y="479" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#C0392B">2,800 - 3,000 °C (Furnace)</text>

      <text x="24" y="493" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Stage Electricity:</text>
      <text x="215" y="493" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#0E6251">0.276 kWh/kg (0.279/cSPG)</text>
      <text x="372" y="493" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#C0392B">9.50 kWh/kg (34.4x HF!)</text>

      <text x="24" y="507" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Stage Thermal Fuel:</text>
      <text x="215" y="507" font-family="Courier, monospace" font-size="8" fill="#34495E">0.955 MJ/kg (0.965/cSPG)</text>
      <text x="372" y="507" font-family="Courier, monospace" font-size="8" fill="#34495E">0.0 MJ/kg (All-Electric)</text>

      <text x="24" y="521" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Stage Mass Yield &amp; Purity:</text>
      <text x="215" y="521" font-family="Courier, monospace" font-size="8" fill="#34495E">88.5% -&gt; &gt;= 99.95% C</text>
      <text x="372" y="521" font-family="Courier, monospace" font-size="8" fill="#34495E">90.0% -&gt; &gt;= 99.99% C</text>

      <text x="24" y="535" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Step Conversion Cost:</text>
      <text x="215" y="535" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#0E6251">+$1,100 / t cSPG</text>
      <text x="372" y="535" font-family="Courier, monospace" font-size="8" font-weight="bold" fill="#C0392B">+$1,650 to +$2,500 / t</text>

      <text x="24" y="550" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Total Route Electricity:</text>
      <text x="215" y="550" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#0E6251">7.91 kWh/kg cSPG</text>
      <text x="372" y="550" font-family="Courier, monospace" font-size="8.5" font-weight="bold" fill="#C0392B">17.18 kWh/kg cSPG (+117%)</text>
    </g>
"""
    ]
    lines.append(render_title_block(
        "DWG-MCH-03",
        "PTFE-LINED HF/HCl ACID DIGESTION REACTOR (SECTION A-A)",
        "Chemical Purification (Stage 3A)",
        "Elec: 0.276 kWh/kg | Acids: 480 kg/t + 400 kg CaO | Yield: 88.5% | >=99.95% C",
        "ANL GREET ANL-22/74 Table 3; Surovtseva (2022)"
    ))
    lines.append("</svg>")
    return "\n".join(lines)


# =====================================================================
# Drawing 4: Acheson Batch vs. Longitudinal Graphitization (LWG)
# =====================================================================
def create_svg_graphitization_furnaces():
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">',
        common_svg_defs(),
        '  <rect width="1200" height="800" fill="#F8F9F9" />',
        render_drawing_header(
            "ULTRA-HIGH-TEMPERATURE GRAPHITIZATION FURNACES: ACHESON VS. LWG (2,800 - 3,000 °C)",
            "Synthetic Anode Stage 3: Indirect Resistor-Bed Batch Heating (12.50 kWh/kg) vs. Direct Axial Joule Heating (7.40 kWh/kg | ANL-22/74 Table 2)"
        ),
        """
    <!-- ================================================================= -->
    <!-- TOP-LEFT PANEL: ARCHITECTURE A — BATCH ACHESON RESISTANCE FURNACE -->
    <!-- ================================================================= -->
    <g transform="translate(22, 92)" id="acheson_furnace_panel">
      <rect x="0" y="0" width="564" height="418" fill="#FFFFFF" stroke="#C0392B" stroke-width="1.8" rx="5" />
      <rect x="0" y="0" width="564" height="28" fill="#900C3F" rx="4" />
      <text x="12" y="18" font-family="Helvetica, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#FFFFFF">A. TRADITIONAL BATCH ACHESON RESISTANCE FURNACE (INDIRECT COKE-BED HEATING)</text>

      <!-- Exhaust Fume Extraction Hood (Captures CO, SO2, and SiO2/S Puffing Volatiles) -->
      <polygon points="150,36 414,36 444,54 120,54" fill="#D5D8DC" stroke="#566573" stroke-width="1.2" />
      <line x1="282" y1="54" x2="282" y2="38" stroke="#7F8C8D" stroke-width="2" marker-end="url(#arrow)" />
      <text x="282" y="49" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#2C3E50" text-anchor="middle">OFF-GAS HOOD: CO(g) + SO2(g) + SiO(g) Volatiles to Scrubber</text>

      <!-- Concrete Foundation Piers & Under-Floor Air-Cooling Channels -->
      <rect x="54" y="316" width="456" height="14" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.4" />
      <g fill="#FFFFFF" stroke="#1C2833" stroke-width="1">
        <rect x="92" y="319" width="36" height="8" /><rect x="172" y="319" width="36" height="8" /><rect x="264" y="319" width="36" height="8" />
        <rect x="356" y="319" width="36" height="8" /><rect x="436" y="319" width="36" height="8" />
      </g>
      <text x="282" y="341" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#1F618D" text-anchor="middle">UNDER-BED CONVECTIVE AIR-COOLING CHANNELS (Prevents Concrete Foundation Meltdown)</text>

      <!-- U-Trough Refractory Brick Enclosure & Removable Side Blocks -->
      <path d="M 62 64 L 502 64 L 502 300 L 472 316 L 92 316 L 62 300 Z" fill="url(#refractoryBrick)" stroke="#BA4A00" stroke-width="1.8" />
      <path d="M 78 64 L 486 64 L 486 292 L 460 304 L 104 304 L 78 292 Z" fill="#FDFEFE" stroke="#BA4A00" stroke-width="1.2" />

      <!-- Outer Thermal Insulation Blanket (SiC + Quartz Sand + Coke Breeze + Sawdust) -->
      <rect x="78" y="64" width="408" height="40" fill="#BDC3C7" fill-opacity="0.7" stroke="#7F8C8D" stroke-width="1" />
      <rect x="78" y="266" width="408" height="38" fill="#BDC3C7" fill-opacity="0.7" stroke="#7F8C8D" stroke-width="1" />
      <text x="282" y="80" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#2C3E50" text-anchor="middle">TOP THERMAL INSULATION BLANKET (250 mm SiO2 Sand + SiC + Coke Breeze)</text>
      <text x="282" y="93" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#78281F" text-anchor="middle">Parasitic Side-Reaction at 1,700°C: SiO2(s) + 3C(s) -&gt; beta-SiC(s) + 2CO(g) (Consumes Energy)</text>

      <!-- Granular Metallurgical Coke Resistor Packing Bed (Indirect Joule Heating Medium) -->
      <rect x="94" y="104" width="376" height="162" fill="url(#cokeBed)" stroke="#34495E" stroke-width="1.2" />
      <text x="282" y="118" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833" text-anchor="middle">METALLURGICAL COKE RESISTOR PACKING BED (Indirect Heating: Q = I^2 * R_bed)</text>

      <!-- Water-Cooled Graphite Head Electrodes & Copper Busbars (Left & Right) -->
      <rect x="16" y="152" width="46" height="68" fill="#D35400" stroke="#78281F" stroke-width="1.5" rx="2" />
      <rect x="62" y="146" width="32" height="80" fill="#2C3E50" stroke="#17202A" stroke-width="1.8" />
      <text x="35" y="144" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#900C3F" text-anchor="middle">Cu BUSBAR</text>
      <text x="35" y="234" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#1F618D" text-anchor="middle">H2O Cooled</text>

      <rect x="470" y="146" width="32" height="80" fill="#2C3E50" stroke="#17202A" stroke-width="1.8" />
      <rect x="502" y="152" width="46" height="68" fill="#D35400" stroke="#78281F" stroke-width="1.5" rx="2" />
      <text x="531" y="144" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#900C3F" text-anchor="middle">ELECTRODE</text>
      <text x="531" y="234" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#1C2833" text-anchor="middle">60 - 100 kA</text>

      <!-- Incandescent Core Thermal Plume (2,800 - 3,000 °C) -->
      <ellipse cx="282" cy="188" rx="176" ry="66" fill="url(#heatGlow)" />

      <!-- Transverse Cylindrical Graphite Sagger Crucibles Packed with Needle Coke Anode Powder -->
      <g stroke="#F39C12" stroke-width="1.6" fill="#1C2833">
        <rect x="116" y="142" width="42" height="88" rx="3" />
        <rect x="184" y="142" width="42" height="88" rx="3" />
        <rect x="252" y="142" width="42" height="88" rx="3" />
        <rect x="320" y="142" width="42" height="88" rx="3" />
        <rect x="388" y="142" width="42" height="88" rx="3" />
      </g>
      <!-- Crucible Caps & Internal Anode Powder -->
      <g fill="#566573" stroke="#1C2833" stroke-width="1">
        <rect x="114" y="138" width="46" height="6" /><rect x="182" y="138" width="46" height="6" /><rect x="250" y="138" width="46" height="6" />
        <rect x="318" y="138" width="46" height="6" /><rect x="386" y="138" width="46" height="6" />
      </g>
      <text x="273" y="182" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">SAGGER CRUCIBLES (x50-80)</text>
      <text x="273" y="194" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#FAD7A0" text-anchor="middle">1,020 kg Green Coke -&gt; 1,000 kg Anode</text>

      <!-- Radial Thermal Gradient Annotation (Core 3,000°C vs Wall 2,600°C) -->
      <path d="M 92 248 L 472 248" stroke="#C0392B" stroke-width="1.2" stroke-dasharray="4,2" />
      <text x="282" y="260" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#900C3F" text-anchor="middle">Steep Radial Delta-T (~250 °C Core-to-Wall Gradient) -&gt; Batch-to-Batch d002 Variance</text>
      <text x="282" y="286" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#2C3E50" text-anchor="middle">BOTTOM SILICON CARBIDE &amp; SAND BED (300 mm Thermal Barrier above Concrete Floor)</text>

      <!-- Bottom Metrics Summary Strip -->
      <rect x="10" y="348" width="544" height="62" fill="#FDEDEC" stroke="#C0392B" stroke-width="1.2" rx="3" />
      <text x="18" y="362" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#900C3F">ACHESON BATCH OPERATING LEDGER (ANL-22/74 TABLE 2; SUROVTSEVA 2022):</text>
      <text x="18" y="376" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Stage 3 Electricity: 12.50 kWh/kg (90.6% of total 13.79 kWh/kg Synthetic Acheson Route)</text>
      <text x="18" y="389" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#78281F">• Thermal Efficiency: ~28 - 32% (~70% heat wasted in 3:1 resistor coke &amp; sand pack; 12-18 day cycle)</text>
      <text x="18" y="402" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#900C3F">• Coal-Grid Footprint: 19.65 kg CO2e/kg (Inner Mongolia) vs. 4.60 kg CO2e/kg (Hydro Grid) | Cost: +$2,100/t</text>
    </g>

    <!-- ================================================================= -->
    <!-- TOP-RIGHT PANEL: ARCHITECTURE B — LONGITUDINAL LWG (CASTNER)      -->
    <!-- ================================================================= -->
    <g transform="translate(604, 92)" id="lwg_furnace_panel">
      <rect x="0" y="0" width="576" height="418" fill="#FFFFFF" stroke="#27AE60" stroke-width="1.8" rx="5" />
      <rect x="0" y="0" width="576" height="28" fill="#0E6251" rx="4" />
      <text x="12" y="18" font-family="Helvetica, Arial, sans-serif" font-size="10.5" font-weight="bold" fill="#FFFFFF">B. LONGITUDINAL GRAPHITIZATION FURNACE — LWG / CASTNER (DIRECT JOULE HEATING)</text>

      <!-- Optical Pyrometer & Argon Purge Hood on Top -->
      <circle cx="288" cy="48" r="11" fill="#FFFFFF" stroke="#2980B9" stroke-width="1.4" />
      <text x="288" y="46" font-family="Helvetica, Arial, sans-serif" font-size="6.5" font-weight="bold" fill="#154360" text-anchor="middle">TI</text>
      <text x="288" y="54" font-family="Helvetica, Arial, sans-serif" font-size="6.5" fill="#154360" text-anchor="middle">402</text>
      <line x1="288" y1="59" x2="288" y2="132" stroke="#2980B9" stroke-width="1.2" stroke-dasharray="3,2" />
      <text x="304" y="48" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#154360">Optical Pyrometer Sight Tube (T_core = 2,950 °C)</text>
      <text x="304" y="58" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#5D6D7E">Closed Hood + Low-Flow N2/Ar Blanket (Minimizes Carbon Oxidation Loss)</text>

      <!-- Concrete Piers & Air-Cooled Steel Support Frame -->
      <rect x="64" y="316" width="448" height="14" fill="#7F8C8D" stroke="#1C2833" stroke-width="1.4" />
      <text x="288" y="341" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#0E6251" text-anchor="middle">MODULAR SEGMENTED SHELL (3 - 5 Day Fast Cooling &amp; Automated Crane Discharge)</text>

      <!-- Insulated U-Frame Refractory Shell -->
      <rect x="74" y="68" width="428" height="248" fill="url(#refractoryBrick)" stroke="#BA4A00" stroke-width="1.8" />
      <rect x="90" y="82" width="396" height="220" fill="#FDFEFE" stroke="#BA4A00" stroke-width="1.2" />

      <!-- Stationary Graphitized Carbon Black Insulation Layer (Zero Resistor Coke!) -->
      <rect x="90" y="82" width="396" height="44" fill="#D5D8DC" fill-opacity="0.75" stroke="#7F8C8D" stroke-width="1" />
      <rect x="90" y="256" width="396" height="46" fill="#D5D8DC" fill-opacity="0.75" stroke="#7F8C8D" stroke-width="1" />
      <text x="288" y="100" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833" text-anchor="middle">STATIONARY CARBON BLACK INSULATION BLANKET (Low k_th = 0.4 W/m·K)</text>
      <text x="288" y="114" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#0E6251" text-anchor="middle">ZERO INTER-CRUCIBLE RESISTOR COKE BED -&gt; Eliminates 40.8% Parasitic Thermal Mass!</text>

      <!-- Left & Right Hydraulic Axial Clamping Rams (10-30 MPa Contact Pressure) -->
      <rect x="12" y="164" width="34" height="54" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <line x1="18" y1="191" x2="40" y2="191" stroke="#C0392B" stroke-width="3" marker-end="url(#arrowRed)" />
      <rect x="46" y="152" width="44" height="78" fill="#2C3E50" stroke="#17202A" stroke-width="1.8" />
      <text x="38" y="136" font-family="Helvetica, Arial, sans-serif" font-size="7.2" font-weight="bold" fill="#C0392B" text-anchor="middle">HYDRAULIC RAM</text>
      <text x="38" y="146" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#1C2833" text-anchor="middle">P = 10-30 MPa</text>

      <rect x="486" y="152" width="44" height="78" fill="#2C3E50" stroke="#17202A" stroke-width="1.8" />
      <rect x="530" y="164" width="34" height="54" fill="url(#metallicCyl)" stroke="#1C2833" stroke-width="1.5" />
      <line x1="558" y1="191" x2="536" y2="191" stroke="#C0392B" stroke-width="3" marker-end="url(#arrowRed)" />
      <text x="538" y="136" font-family="Helvetica, Arial, sans-serif" font-size="7.2" font-weight="bold" fill="#C0392B" text-anchor="middle">TAIL ELECTRODE</text>
      <text x="538" y="146" font-family="Helvetica, Arial, sans-serif" font-size="7" fill="#1F618D" text-anchor="middle">80-150 kA DC</text>

      <!-- Incandescent Axial Carbon Column (Direct Self-Heating) -->
      <rect x="90" y="130" width="396" height="122" fill="url(#heatGlow)" rx="4" />

      <!-- End-to-End Clamped Conductive Graphite Box-Crucibles / Anode Columns -->
      <g fill="#1C2833" stroke="#F1C40F" stroke-width="2">
        <rect x="96" y="146" width="90" height="90" />
        <rect x="192" y="146" width="92" height="90" />
        <rect x="290" y="146" width="92" height="90" />
        <rect x="388" y="146" width="90" height="90" />
      </g>
      <!-- Inter-Column Contact Interfaces (High J^2 * R_contact Heating) -->
      <g stroke="#F39C12" stroke-width="3">
        <line x1="189" y1="146" x2="189" y2="236" />
        <line x1="287" y1="146" x2="287" y2="236" />
        <line x1="385" y1="146" x2="385" y2="236" />
      </g>

      <!-- Direct Axial DC Current Path Vector through the Carbon Column -->
      <line x1="92" y1="191" x2="478" y2="191" stroke="#F1C40F" stroke-width="3.5" stroke-dasharray="8,4" marker-end="url(#arrowOrange)" />
      <text x="288" y="176" font-family="Helvetica, Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#FFFFFF" text-anchor="middle">DIRECT AXIAL DC CURRENT (I = 80 - 150 kA THROUGH ANODE COLUMN)</text>
      <text x="288" y="212" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#FAD7A0" text-anchor="middle">Self-Heating: q&apos;&apos;&apos; = J^2 * rho(T) | Uniform Axial Temp (2,900 ± 40 °C)</text>
      <text x="288" y="226" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#F9E79F" text-anchor="middle">Graphite Box-Crucibles act as the electrical conductor (No resistor bed)</text>

      <text x="288" y="280" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#2C3E50" text-anchor="middle">REUSABLE GRAPHITE FOIL &amp; CARBON BLACK BASE INSULATION (250 mm)</text>

      <!-- Bottom Metrics Summary Strip -->
      <rect x="10" y="348" width="556" height="62" fill="#E8F8F5" stroke="#16A085" stroke-width="1.2" rx="3" />
      <text x="18" y="362" font-family="Helvetica, Arial, sans-serif" font-size="8.5" font-weight="bold" fill="#0E6251">LWG / CASTNER OPERATING LEDGER (SUROVTSEVA ET AL. 2022; IEA 2024):</text>
      <text x="18" y="376" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">• Stage 3 Electricity: 7.40 kWh/kg (-40.8% vs. Acheson | Total Route: 8.69 kWh/kg, -37.0%)</text>
      <text x="18" y="389" font-family="Helvetica, Arial, sans-serif" font-size="8" fill="#145A32">• Thermal Efficiency: ~50 - 60% (Direct Joule heating of column; rapid 3-5 day turnover)</text>
      <text x="18" y="402" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#0E6251">• Coal-Grid Footprint: 12.40 kg CO2e/kg (-36.9% vs. Acheson) vs. 2.90 kg CO2e/kg (Hydro) | Cost: +$1,250/t</text>
    </g>

    <!-- ================================================================= -->
    <!-- BOTTOM-LEFT PANEL: THERMAL REGIMES & ENERGY WATERFALL LEDGER      -->
    <!-- ================================================================= -->
    <g transform="translate(22, 522)" id="thermal_physics_and_ledger">
      <rect x="0" y="0" width="642" height="258" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.6" rx="5" />
      <rect x="0" y="0" width="642" height="26" fill="#1C2833" rx="4" />
      <text x="12" y="17" font-family="Helvetica, Arial, sans-serif" font-size="10" font-weight="bold" fill="#ECF0F1">THERMODYNAMIC &amp; CRYSTALLOGRAPHIC REGIMES (800 -&gt; 3,000 °C) &amp; HEAT-BALANCE BREAKDOWN</text>

      <!-- Left Sub-Box: 4 Temperature Regimes from Green Coke to ABAB Graphite -->
      <rect x="10" y="32" width="308" height="218" fill="#F4F9FD" stroke="#85C1E9" stroke-width="1.1" rx="3" />
      <text x="18" y="47" font-family="Helvetica, Arial, sans-serif" font-size="8.8" font-weight="bold" fill="#1B4F72">1. TEMPERATURE-STAGE REACTION ZONES (NEEDLE COKE)</text>

      <!-- Zone 1 -->
      <rect x="16" y="54" width="296" height="42" fill="#EBF5FB" stroke="#5DADE2" stroke-width="0.9" rx="2" />
      <text x="22" y="66" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#154360">Zone I: 800 - 1,350 °C | Calcination &amp; Pitch Binder Coking</text>
      <text x="22" y="78" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#1C2833">• Coal-tar pitch (150 kg/t) carbonizes; C-H volatiles (CH4, H2) evolve.</text>
      <text x="22" y="89" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#5D6D7E">• Stage 1-2 Inputs: 1.288 kWh/kg elec + 8.69 MJ/kg natural gas/fuel oil.</text>

      <!-- Zone 2 -->
      <rect x="16" y="100" width="296" height="44" fill="#FEF9E7" stroke="#F39C12" stroke-width="0.9" rx="2" />
      <text x="22" y="112" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#B9770E">Zone II: 1,400 - 2,000 °C | Heteroatom &quot;Puffing&quot; &amp; Desulfurization</text>
      <text x="22" y="124" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#1C2833">• Irreversible expansion as thiophenic S &amp; N2 erupt (CS2, H2S, SO2).</text>
      <text x="22" y="135" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#7E5109">• Requires low-S needle coke (&lt;0.5% S) + Fe2O3 puffing inhibitor.</text>

      <!-- Zone 3 -->
      <rect x="16" y="148" width="296" height="44" fill="#FDEDEC" stroke="#E74C3C" stroke-width="0.9" rx="2" />
      <text x="22" y="160" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#900C3F">Zone III: 2,000 - 2,500 °C | Thermal Ash Volatilization (No HF!)</text>
      <text x="22" y="172" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#1C2833">• Metallic &amp; silicate impurities (Fe, Si, Al, Ca, V) boil off as vapors.</text>
      <text x="22" y="183" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#78281F">• Intrinsic purity reaches &gt;= 99.95% C with zero chemical acid waste.</text>

      <!-- Zone 4 -->
      <rect x="16" y="196" width="296" height="48" fill="#E8F8F5" stroke="#16A085" stroke-width="0.9" rx="2" />
      <text x="22" y="208" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#0E6251">Zone IV: 2,500 - 3,000 °C | 3D ABAB Hexagonal Graphitization</text>
      <text x="22" y="220" font-family="Helvetica, Arial, sans-serif" font-size="7.4" fill="#1C2833">• Turbostratic d002 = 0.3440 nm (g=0%) -&gt; 0.3356-0.3360 nm (g=88-95%).</text>
      <text x="22" y="232" font-family="Helvetica, Arial, sans-serif" font-size="7.4" font-weight="bold" fill="#145A32">• Crystallite L_c grows 2-&gt;45 nm; unlocks 355-365 mAh/g LiC6 capacity.</text>

      <!-- Right Sub-Box: Energy Heat-Balance Bars & Comparative Ledger -->
      <rect x="326" y="32" width="306" height="218" fill="#FEF9E7" stroke="#F39C12" stroke-width="1.1" rx="3" />
      <text x="334" y="47" font-family="Helvetica, Arial, sans-serif" font-size="8.8" font-weight="bold" fill="#B9770E">2. SPECIFIC ENERGY PARTITION (PER kg SYNTHETIC ANODE)</text>

      <!-- Acheson Stacked Bar (12.50 kWh/kg = 280 px wide) -->
      <text x="334" y="62" font-family="Helvetica, Arial, sans-serif" font-size="7.8" font-weight="bold" fill="#900C3F">Acheson Batch: 12.50 kWh/kg (45.0 MJ/kg Electrical Input)</text>
      <rect x="334" y="66" width="85" height="18" fill="#27AE60" stroke="#1C2833" stroke-width="1" />
      <rect x="419" y="66" width="110" height="18" fill="#E74C3C" stroke="#1C2833" stroke-width="1" />
      <rect x="529" y="66" width="85" height="18" fill="#F39C12" stroke="#1C2833" stroke-width="1" />
      <text x="376" y="78" font-family="Helvetica, Arial, sans-serif" font-size="7" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3.8 kWh Anode</text>
      <text x="474" y="78" font-family="Helvetica, Arial, sans-serif" font-size="7" font-weight="bold" fill="#FFFFFF" text-anchor="middle">4.9 kWh Coke Bed</text>
      <text x="571" y="78" font-family="Helvetica, Arial, sans-serif" font-size="7" font-weight="bold" fill="#1C2833" text-anchor="middle">3.8 kWh Wall</text>

      <!-- LWG Stacked Bar (7.40 kWh/kg = 166 px wide) -->
      <text x="334" y="98" font-family="Helvetica, Arial, sans-serif" font-size="7.8" font-weight="bold" fill="#0E6251">LWG Longitudinal: 7.40 kWh/kg (26.6 MJ/kg, -40.8% Savings)</text>
      <rect x="334" y="102" width="85" height="18" fill="#27AE60" stroke="#1C2833" stroke-width="1" />
      <rect x="419" y="102" width="47" height="18" fill="#F39C12" stroke="#1C2833" stroke-width="1" />
      <rect x="466" y="102" width="34" height="18" fill="#85C1E9" stroke="#1C2833" stroke-width="1" />
      <text x="376" y="114" font-family="Helvetica, Arial, sans-serif" font-size="7" font-weight="bold" fill="#FFFFFF" text-anchor="middle">3.8 kWh Anode</text>
      <text x="442" y="114" font-family="Helvetica, Arial, sans-serif" font-size="6.8" font-weight="bold" fill="#1C2833" text-anchor="middle">2.1 Ins</text>
      <text x="506" y="114" font-family="Helvetica, Arial, sans-serif" font-size="7" font-weight="bold" fill="#0E6251">-5.10 kWh/kg Saved!</text>

      <!-- Comparison Table -->
      <line x1="334" y1="128" x2="622" y2="128" stroke="#D4AC0D" stroke-width="0.9" />
      <text x="334" y="140" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#566573">BENCHMARK METRIC</text>
      <text x="466" y="140" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#900C3F">ACHESON</text>
      <text x="552" y="140" font-family="Helvetica, Arial, sans-serif" font-size="7.5" font-weight="bold" fill="#0E6251">LWG / CASTNER</text>

      <text x="334" y="154" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Green Coke + Pitch Feed:</text>
      <text x="466" y="154" font-family="Courier, monospace" font-size="7.5" fill="#1C2833">1,020 + 150 kg</text>
      <text x="552" y="154" font-family="Courier, monospace" font-size="7.5" fill="#1C2833">1,020 + 150 kg</text>

      <text x="334" y="168" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Stage 3 Mass Yield:</text>
      <text x="466" y="168" font-family="Courier, monospace" font-size="7.5" fill="#1C2833">98.0% (1.0 t)</text>
      <text x="552" y="168" font-family="Courier, monospace" font-size="7.5" fill="#1C2833">98.0% (1.0 t)</text>

      <text x="334" y="182" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Stage 3 Electricity:</text>
      <text x="466" y="182" font-family="Courier, monospace" font-size="7.5" font-weight="bold" fill="#C0392B">12.50 kWh/kg</text>
      <text x="552" y="182" font-family="Courier, monospace" font-size="7.5" font-weight="bold" fill="#0E6251">7.40 kWh/kg</text>

      <text x="334" y="196" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Total Route Power:</text>
      <text x="466" y="196" font-family="Courier, monospace" font-size="7.5" font-weight="bold" fill="#C0392B">13.79 kWh/kg</text>
      <text x="552" y="196" font-family="Courier, monospace" font-size="7.5" font-weight="bold" fill="#0E6251">8.69 kWh/kg</text>

      <text x="334" y="210" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Total Route Thermal Fuel:</text>
      <text x="466" y="210" font-family="Courier, monospace" font-size="7.5" fill="#34495E">8.69 MJ/kg</text>
      <text x="552" y="210" font-family="Courier, monospace" font-size="7.5" fill="#34495E">8.69 MJ/kg</text>

      <text x="334" y="224" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Batch Cycle Duration:</text>
      <text x="466" y="224" font-family="Courier, monospace" font-size="7.5" fill="#C0392B">12 - 18 days</text>
      <text x="552" y="224" font-family="Courier, monospace" font-size="7.5" fill="#0E6251">3 - 5 days</text>

      <text x="334" y="238" font-family="Helvetica, Arial, sans-serif" font-size="7.5" fill="#1C2833">• Step Conversion Cost:</text>
      <text x="466" y="238" font-family="Courier, monospace" font-size="7.5" font-weight="bold" fill="#C0392B">+$2,100 / t</text>
      <text x="552" y="238" font-family="Courier, monospace" font-size="7.5" font-weight="bold" fill="#0E6251">+$1,250 / t</text>
    </g>

    <!-- ================================================================= -->
    <!-- MIDDLE-RIGHT PANEL: GRID CARBON INTENSITY & SUPPLY CHAIN LEDGER   -->
    <!-- ================================================================= -->
    <g transform="translate(675, 522)" id="grid_decarbonization_panel">
      <rect x="0" y="0" width="505" height="138" fill="#EAFAF1" stroke="#27AE60" stroke-width="1.5" rx="5" />
      <rect x="0" y="0" width="505" height="24" fill="#0E6251" rx="4" />
      <text x="12" y="16" font-family="Helvetica, Arial, sans-serif" font-size="9.5" font-weight="bold" fill="#FFFFFF">GRID CARBON SENSITIVITY &amp; SYNTHETIC ANODE LCA (HYPOTHESIS H1 VERIFIED)</text>

      <text x="12" y="39" font-family="Helvetica, Arial, sans-serif" font-size="8" font-weight="bold" fill="#1C2833">Why Grid Electricity Mix Governs Synthetic Graphite Climate Impact:</text>
      <text x="12" y="52" font-family="Helvetica, Arial, sans-serif" font-size="7.6" fill="#34495E">• Graphitization consumes 90.6% (Acheson) to 85.2% (LWG) of all synthetic route electricity.</text>
      <text x="12" y="65" font-family="Helvetica, Arial, sans-serif" font-size="7.6" font-weight="bold" fill="#900C3F">• 1. Inner Mongolia Coal Grid (~1,050 g CO2e/kWh): Acheson = 19.65 kg CO2e/kg | LWG = 12.40 kg CO2e/kg</text>
      <text x="12" y="78" font-family="Helvetica, Arial, sans-serif" font-size="7.6" font-weight="bold" fill="#1B4F72">• 2. US Average Grid Mix (~380 g CO2e/kWh):      Acheson = 8.90 kg CO2e/kg  | LWG = 5.95 kg CO2e/kg</text>
      <text x="12" y="91" font-family="Helvetica, Arial, sans-serif" font-size="7.6" font-weight="bold" fill="#0E6251">• 3. Sichuan / Nordic Hydro (~25 g CO2e/kWh):   Acheson = 4.60 kg CO2e/kg  | LWG = 2.90 kg CO2e/kg (-85%!)</text>
      <line x1="12" y1="98" x2="493" y2="98" stroke="#A3E4D7" stroke-width="1" />
      <text x="12" y="112" font-family="Helvetica, Arial, sans-serif" font-size="7.6" fill="#1C2833">• Residual ~2.6-2.9 kg CO2e/kg floor on 100% hydro comes from direct process CO2 during baking/calcination</text>
      <text x="12" y="124" font-family="Helvetica, Arial, sans-serif" font-size="7.6" font-weight="bold" fill="#145A32">  and upstream petroleum needle coke production (Surovtseva et al. 2022; ANL-22/74 Table 2).</text>
    </g>
"""
    ]
    lines.append(render_title_block(
        "DWG-MCH-04",
        "ACHESON VS. LWG GRAPHITIZATION FURNACES (2,800-3,000 °C)",
        "High-Temp Thermal Graphitization (Stage 3)",
        "Acheson: 12.50 kWh/kg (eff ~30%) | LWG: 7.40 kWh/kg (eff ~55%, -40.8%)",
        "ANL GREET ANL-22/74 Table 2; Surovtseva (2022); IEA (2024)"
    ))
    lines.append("</svg>")
    return "\n".join(lines)


# =====================================================================
# Drawing 5: Material Cross-Section (Flake -> uSPG -> cSPG)
# =====================================================================
def _t(x, y, text, size=9, fill="#5D6D7E", weight="normal", anchor="start", family="Helvetica, Arial, sans-serif", style="normal"):
    """Compact helper emitting one escaped SVG text element."""
    s = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" '
            f'font-style="{style}" fill="{fill}" text-anchor="{anchor}">{s}</text>')


def _morph_panel(tx, color, bg, title, subtitle, illustration, rows, spec_title, spec_fill):
    """Builds one 380 x 408 morphology panel: header, SEM-style illustration, property ledger."""
    out = [f'<g transform="translate({tx}, 92)">',
           f'<rect x="0" y="0" width="380" height="408" fill="#FFFFFF" stroke="{color}" stroke-width="1.8" rx="5" />',
           f'<rect x="0" y="0" width="380" height="28" fill="{bg}" rx="4" />',
           _t(12, 19, title, 10.5, color, "bold"),
           _t(12, 44, subtitle, 8, "#566573", style="italic"),
           illustration,
           f'<rect x="12" y="252" width="356" height="148" fill="{spec_fill}" stroke="#BDC3C7" stroke-width="1" rx="4" />',
           _t(22, 268, spec_title, 9.5, color, "bold")]
    y = 285
    for label, value, vcol, bold in rows:
        out.append(_t(22, y, label, 8.5, "#34495E"))
        out.append(_t(358, y, value, 8.5, vcol, "bold" if bold else "normal", "end", "Courier, monospace"))
        y += 15
    out.append('</g>')
    return "\n".join(out)


def create_svg_flake_to_cspg_morphology():
    fold = ('M -85 0 C -85 -55, 85 -55, 85 0 C 85 60, -70 60, -70 0 '
            'C -70 -40, 60 -40, 60 0 C 60 30, -40 30, -40 0')
    fold2 = 'M 0 -85 C 55 -85, 55 85, 0 85 C -50 85, -50 -60, 0 -60 C 35 -60, 35 40, 0 40'

    # ---- Panel 1 illustration: planar flake side-view with exposed polar edges ----
    flake = ['<g transform="translate(190, 140)">']
    for i in range(8):
        y = -52 + i * 13
        x0 = -132 + (i % 2) * 8
        w = 264 - (i % 2) * 14
        flake.append(f'<rect x="{x0}" y="{y}" width="{w}" height="10" fill="{"#34495E" if i % 2 == 0 else "#2C3E50"}" stroke="#17202A" stroke-width="1" />')
        flake.append(f'<circle cx="{x0 + w + 4}" cy="{y + 5}" r="3" fill="#E74C3C" />')
    flake += [
        '<circle cx="-50" cy="-6" r="7" fill="#E74C3C" stroke="#922B21" />',
        _t(-50, -14, "SiO2", 7.5, "#C0392B", "bold", "middle"),
        '<rect x="24" y="-22" width="14" height="9" fill="#E67E22" stroke="#B9770E" />',
        _t(31, -26, "Fe2O3", 7.5, "#B9770E", "bold", "middle"),
        '<line x1="-132" y1="64" x2="132" y2="64" stroke="#34495E" stroke-width="1" marker-start="url(#dimTick)" marker-end="url(#dimTick)" />',
        _t(0, 78, "150 - 300 um flake width (+80 mesh)", 8, "#34495E", "bold", "middle", "Courier, monospace"),
        _t(140, -66, "Polar prismatic edges", 7.5, "#C0392B", "bold", "end"),
        _t(-132, -66, "sp2 basal planes (non-polar)", 7.5, "#1C2833", "bold"),
        _t(0, 98, "Interlamellar silicate / iron-oxide ash locked between sheets", 7.5, "#922B21", "normal", "middle"),
        '</g>']
    p1 = _morph_panel(22, "#2C3E50", "#EAEDED", "1. RAW NATURAL FLAKE (94 - 97% C)",
                      "Stage 1 output: froth-flotation concentrate", "\n".join(flake), [
        ("Morphology", "planar platelet", "#2C3E50", False),
        ("D50 particle size", "150 - 300 um", "#2C3E50", False),
        ("Carbon purity", "94.0 - 97.0 % C", "#2C3E50", False),
        ("Tap density", "0.35 - 0.45 g/cm3", "#C0392B", True),
        ("BET surface area", "1.5 - 2.5 m2/g", "#2C3E50", False),
        ("Battery suitability", "INCOMPATIBLE", "#C0392B", True),
        ("Failure mode", "delaminates on Li+ uptake", "#922B21", False),
        ("", "", "#000000", False)],
        "PHYSICAL & CHEMICAL AUDIT", "#F8F9F9")

    # ---- Panel 2 illustration: uncoated spherical graphite, open edge terminations ----
    usp = ['<g transform="translate(190, 140)">',
           '<circle cx="0" cy="0" r="86" fill="#2C3E50" stroke="#1A252F" stroke-width="2" />',
           f'<path d="{fold}" transform="scale(0.84)" fill="none" stroke="#7F8C8D" stroke-width="4.5" stroke-linecap="round" />',
           f'<path d="{fold2}" transform="scale(0.84)" fill="none" stroke="#BDC3C7" stroke-width="3.2" stroke-linecap="round" />',
           '<circle cx="-30" cy="-22" r="7" fill="#EBF5FB" stroke="#2980B9" /><circle cx="34" cy="26" r="9" fill="#EBF5FB" stroke="#2980B9" />',
           '<circle cx="8" cy="-40" r="4.5" fill="#EBF5FB" stroke="#2980B9" />']
    import math
    for k in range(16):
        a = k * math.pi / 8
        x1, y1 = 86 * math.cos(a), 86 * math.sin(a)
        x2, y2 = 95 * math.cos(a), 95 * math.sin(a)
        usp.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#E74C3C" stroke-width="2.2" />')
    usp += [
        _t(-118, -92, "Open edge terminations", 7.5, "#C0392B", "bold"),
        _t(118, -92, "Acid-cleaned pores", 7.5, "#2980B9", "bold", "end"),
        _t(0, 112, "Concentric 'cabbage-fold' lamellae (D50 = 15 um)", 8, "#2980B9", "bold", "middle"),
        _t(0, 126, "Folded edges still reach the surface -> high BET", 7.5, "#7E5109", "normal", "middle"),
        '</g>']
    p2 = _morph_panel(410, "#1B4F72", "#EBF5FB", "2. UNCOATED SPHERICAL (uSPG)",
                      "Stages 2-3A: impact spheronization + HF/HCl leaching", "\n".join(usp), [
        ("Morphology", "folded quasi-sphere", "#1B4F72", False),
        ("D50 particle size", "15.0 - 16.0 um", "#1B4F72", False),
        ("Carbon purity", ">= 99.95 % C", "#1B4F72", False),
        ("Tap density", "0.95 - 1.02 g/cm3", "#117A65", True),
        ("BET surface area", "6.5 - 9.0 m2/g", "#C0392B", True),
        ("Limitation", "high 1st-cycle loss", "#B9770E", False),
        ("1st-cycle irrev. capacity", "> 15 %", "#C0392B", True),
        ("", "", "#000000", False)],
        "PHYSICAL & CHEMICAL AUDIT", "#F8F9F9")

    # ---- Panel 3 illustration: pitch-coated core-shell sphere ----
    csp = ['<g transform="translate(190, 140)">',
           '<circle cx="0" cy="0" r="96" fill="#27AE60" fill-opacity="0.35" stroke="#27AE60" stroke-width="3" />',
           '<circle cx="0" cy="0" r="86" fill="#1C2833" stroke="#16A085" stroke-width="2" />',
           f'<path d="{fold}" transform="scale(0.84)" fill="none" stroke="#566573" stroke-width="4" stroke-linecap="round" />',
           f'<path d="{fold2}" transform="scale(0.84)" fill="none" stroke="#7F8C8D" stroke-width="3" stroke-linecap="round" />',
           '<circle cx="-30" cy="-22" r="7" fill="#117A65" stroke="#27AE60" /><circle cx="34" cy="26" r="9" fill="#117A65" stroke="#27AE60" />',
           '<line x1="84" y1="-62" x2="114" y2="-92" stroke="#27AE60" stroke-width="1.6" marker-end="url(#arrowGreen)" />',
           _t(-118, -100, "Amorphous pitch shell (5 wt%, 20-50 nm)", 7.5, "#0E6251", "bold"),
           _t(0, 112, "Crystalline graphite core + sealed carbon skin", 8, "#0E6251", "bold", "middle"),
           _t(0, 126, "Edge planes and open pores are hermetically covered", 7.5, "#145A32", "normal", "middle"),
           '</g>']
    p3 = _morph_panel(798, "#0E6251", "#E8F8F5", "3. COATED FINISHED (cSPG, BATTERY GRADE)",
                      "Stage 4: pitch coating + carbonization", "\n".join(csp), [
        ("Morphology", "core-shell sphere", "#0E6251", False),
        ("D50 / D10 / D90", "15.5 / 8.5 / 27 um", "#0E6251", False),
        ("Carbon purity", ">= 99.95 % C", "#0E6251", False),
        ("Tap density", "1.00 - 1.10 g/cm3", "#117A65", True),
        ("BET surface area", "1.8 - 2.5 m2/g", "#117A65", True),
        ("Reversible capacity", "355 - 365 mAh/g", "#117A65", False),
        ("Initial coulombic eff. (ICE)", ">= 92.5 %", "#0E6251", True),
        ("", "", "#000000", False)],
        "BATTERY QUALIFICATION SPEC", "#E8F8F5")

    # ---- Stage chevrons between panels ----
    chev = ('<polygon points="398,128 418,140 398,152" fill="#C0392B" stroke="#FFFFFF" stroke-width="1.5" />'
            '<polygon points="786,128 806,140 786,152" fill="#C0392B" stroke="#FFFFFF" stroke-width="1.5" />')

    # ---- Bottom-left: normalized property bar charts (range midpoints) ----
    def bars(x0, vals, cols, scale, fmt):
        o = []
        for i, (v, c) in enumerate(zip(vals, cols)):
            h = v * scale
            bx = x0 + i * 80
            o.append(f'<rect x="{bx}" y="{740 - h:.1f}" width="50" height="{h:.1f}" fill="{c}" stroke="#1C2833" stroke-width="1" />')
            o.append(_t(bx + 25, 734 - h, fmt.format(v), 8.5, "#1C2833", "bold", "middle", "Courier, monospace"))
        return "\n".join(o)

    chart = [
        '<rect x="22" y="512" width="640" height="268" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.6" rx="5" />',
        '<rect x="22" y="512" width="640" height="26" fill="#1C2833" rx="4" />',
        _t(34, 529, "PROPERTY EVOLUTION ALONG THE ROUTE (MIDPOINTS OF THE RANGES ABOVE)", 10, "#ECF0F1", "bold"),
        _t(44, 558, "TAP DENSITY (g/cm3): packing & volumetric energy", 8.5, "#1B4F72", "bold"),
        _t(364, 558, "BET SURFACE AREA (m2/g): SEI-forming interface", 8.5, "#900C3F", "bold"),
        '<line x1="40" y1="740" x2="300" y2="740" stroke="#1C2833" stroke-width="1.4" />',
        '<line x1="360" y1="740" x2="620" y2="740" stroke="#1C2833" stroke-width="1.4" />',
        bars(60, [0.40, 0.985, 1.05], ["#566573", "#2980B9", "#27AE60"], 125, "{:.2f}"),
        bars(380, [2.0, 7.75, 2.15], ["#566573", "#C0392B", "#27AE60"], 16.67, "{:.2f}"),
    ]
    for bx in (60, 140, 220, 380, 460, 540):
        names = {60: "Flake", 140: "uSPG", 220: "cSPG", 380: "Flake", 460: "uSPG", 540: "cSPG"}
        chart.append(_t(bx + 25, 754, names[bx], 8.5, "#1C2833", "bold", "middle"))
    chart += [
        _t(280, 766, "+160% vs flake", 8, "#117A65", "bold", "end"),
        _t(600, 766, "-72% vs uSPG (coating seals pores)", 8, "#117A65", "bold", "end"),
        _t(40, 776, "Rounding fixes packing (Stage 2); coating fixes the surface (Stage 4).", 7.5, "#5D6D7E", "normal", "start", style="italic"),
    ]

    # ---- Bottom-right: SEI schematic (uncoated vs coated surface) ----
    sei = [
        '<g transform="translate(680, 512)">',
        '<rect x="0" y="0" width="500" height="150" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.6" rx="5" />',
        '<rect x="0" y="0" width="500" height="26" fill="#1C2833" rx="4" />',
        _t(12, 17, "WHY THE COATING MATTERS: SEI FORMATION AT THE PARTICLE SURFACE", 10, "#ECF0F1", "bold"),
        # left: uncoated
        _t(14, 44, "uSPG: open edge planes", 8.5, "#C0392B", "bold"),
        '<rect x="14" y="98" width="214" height="34" fill="#2C3E50" stroke="#17202A" />',
        '<path d="M 14 98 L 40 98 L 40 90 L 52 90 L 52 98 L 120 98 L 120 90 L 132 90 L 132 98 L 228 98" fill="none" stroke="#E74C3C" stroke-width="2.2" />',
        '<rect x="14" y="80" width="214" height="16" fill="#E67E22" fill-opacity="0.75" stroke="#B9770E" />',
        _t(121, 92, "thick, unstable SEI", 8, "#FFFFFF", "bold", "middle"),
        '<g fill="#FFFFFF" stroke="#2980B9" stroke-width="1"><circle cx="40" cy="60" r="4" /><circle cx="90" cy="54" r="4" /><circle cx="150" cy="62" r="4" /><circle cx="200" cy="56" r="4" /></g>',
        '<g stroke="#2980B9" stroke-width="1.2"><line x1="90" y1="60" x2="90" y2="78" marker-end="url(#arrowBlue)" /><line x1="150" y1="66" x2="150" y2="78" marker-end="url(#arrowBlue)" /></g>',
        _t(121, 146, "Li+ consumed -> irrev. loss > 15%", 8, "#922B21", "bold", "middle"),
        # right: coated
        _t(262, 44, "cSPG: sealed carbon shell", 8.5, "#0E6251", "bold"),
        '<rect x="262" y="98" width="224" height="34" fill="#2C3E50" stroke="#17202A" />',
        '<rect x="262" y="92" width="224" height="6" fill="#27AE60" stroke="#145A32" />',
        '<rect x="262" y="86" width="224" height="6" fill="#85C1E9" fill-opacity="0.9" stroke="#2980B9" />',
        _t(374, 80, "thin, stable SEI", 8, "#0E6251", "bold", "middle"),
        '<g fill="#FFFFFF" stroke="#2980B9" stroke-width="1"><circle cx="290" cy="56" r="4" /><circle cx="350" cy="52" r="4" /><circle cx="410" cy="58" r="4" /><circle cx="462" cy="54" r="4" /></g>',
        '<g stroke="#2980B9" stroke-width="1.2"><line x1="350" y1="58" x2="350" y2="76" marker-end="url(#arrowBlue)" /><line x1="410" y1="64" x2="410" y2="76" marker-end="url(#arrowBlue)" /></g>',
        _t(374, 146, "Li+ preserved -> ICE >= 92.5%", 8, "#0E6251", "bold", "middle"),
        '</g>',
    ]

    body = "\n".join([p1, p2, p3, chev] + chart + sei)
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">',
        common_svg_defs(),
        '  <rect width="1200" height="800" fill="#F8F9F9" />',
        render_drawing_header(
            "MORPHOLOGY EVOLUTION: NATURAL FLAKE TO BATTERY-GRADE cSPG",
            "Particle cross-sections (schematic, not to scale): planar flake -> folded uSPG -> pitch-coated cSPG | ANL-22/74 Table 3"
        ),
        body,
    ]
    lines.append(render_title_block(
        "DWG-MAT-01",
        "FLAKE TO BATTERY cSPG PARTICLE CROSS-SECTIONS",
        "Material Evolution (Stages 1-4)",
        "Flake (0.4 g/cm3) -> uSPG (0.95 g/cm3) -> cSPG (1.05 g/cm3, ICE >= 92.5%)",
        "ANL GREET ANL-22/74 Table 3; Engels (2022)"
    ))
    lines.append("</svg>")
    return "\n".join(lines)


# =====================================================================
# Drawing 6: Crystallographic Lattice (Turbostratic -> Hexagonal ABAB)
# =====================================================================
def _hex_points(cx, cy, r):
    """Returns SVG polygon points for a flat-top hexagon centered at (cx, cy)."""
    import math
    pts = []
    for k in range(6):
        ang = math.radians(60 * k)
        pts.append(f"{cx + r * math.cos(ang):.1f},{cy + r * math.sin(ang):.1f}")
    return " ".join(pts)


def create_svg_turbostratic_to_lattice():
    import math

    # ---- TOP-LEFT PANEL: Turbostratic Disordered Carbon (1,000 - 1,350 °C) ----
    turbo = [
        '<g transform="translate(22, 92)" id="panel_turbostratic">',
        '<rect x="0" y="0" width="564" height="408" fill="#FFFFFF" stroke="#D35400" stroke-width="1.8" rx="5" />',
        '<rect x="0" y="0" width="564" height="28" fill="#FEF5E7" rx="4" />',
        _t(12, 19, "1. TURBOSTRATIC CARBON: ROTATIONAL STACKING DISORDER (1,000 - 1,350 °C)", 10.5, "#9C640C", "bold"),
        # Left Sub-View: Side-View HRTEM Stacking Profile
        '<rect x="12" y="36" width="322" height="202" fill="#FDFEFE" stroke="#F5B041" stroke-width="1.1" rx="4" />',
        _t(20, 51, "A. SIDE VIEW (c-AXIS): WAVY, CROSS-LINKED GRAPHENE RIBBONS", 8.2, "#B9770E", "bold"),
        # Wavy graphene ribbons (4 layers with curvature & defects)
        '<path d="M 26 78 Q 88 58, 152 80 Q 214 100, 262 72" fill="none" stroke="#2C3E50" stroke-width="4.2" stroke-linecap="round" />',
        '<path d="M 24 118 Q 96 138, 162 110 Q 218 92, 264 122" fill="none" stroke="#34495E" stroke-width="4.2" stroke-linecap="round" />',
        '<path d="M 28 160 Q 92 142, 156 168 Q 216 188, 260 156" fill="none" stroke="#2C3E50" stroke-width="4.2" stroke-linecap="round" />',
        '<path d="M 24 202 Q 100 220, 166 196 Q 222 178, 264 204" fill="none" stroke="#34495E" stroke-width="4.2" stroke-linecap="round" />',
        # sp3 & heteroatom (S, N) cross-link bridges pinning layers
        '<line x1="102" y1="73" x2="108" y2="124" stroke="#C0392B" stroke-width="2.2" stroke-dasharray="3,2" />',
        '<circle cx="105" cy="98" r="5.5" fill="#E74C3C" stroke="#922B21" stroke-width="1" />',
        _t(114, 101, "S / N Bridge", 7.2, "#C0392B", "bold"),
        '<line x1="194" y1="104" x2="188" y2="172" stroke="#C0392B" stroke-width="2.2" stroke-dasharray="3,2" />',
        '<circle cx="191" cy="138" r="5.5" fill="#E67E22" stroke="#9C640C" stroke-width="1" />',
        _t(130, 141, "sp3 Defect", 7.2, "#B9770E", "bold"),
        # Blocked / Trapped Li+ Ion
        '<circle cx="58" cy="139" r="6.5" fill="#F1C40F" stroke="#9C640C" stroke-width="1.2" />',
        _t(58, 142, "Li+", 6.5, "#1C2833", "bold", "middle"),
        '<path d="M 66 139 L 86 139" stroke="#C0392B" stroke-width="1.8" marker-end="url(#arrowRed)" />',
        _t(26, 228, "Steric bottleneck: high Li+ diffusion barrier (E_a > 0.65 eV)", 7.3, "#922B21", "bold"),
        # d002 dimension callout inside box (x=272..328)
        '<line x1="274" y1="72" x2="274" y2="122" stroke="#C0392B" stroke-width="1.6" marker-start="url(#arrowRed)" marker-end="url(#arrowRed)" />',
        _t(280, 93, "d002 >=", 7.5, "#C0392B", "bold"),
        _t(280, 104, "0.3440 nm", 7.5, "#C0392B", "bold", "start", "Courier, monospace"),
        _t(280, 116, "(g = 0%)", 7.2, "#922B21", "bold"),
        '<line x1="274" y1="156" x2="274" y2="204" stroke="#566573" stroke-width="1.4" marker-start="url(#dimTick)" marker-end="url(#dimTick)" />',
        _t(280, 178, "L_c < 5 nm", 7.2, "#34495E", "bold"),
        _t(280, 189, "L_a < 10 nm", 7.2, "#34495E"),

        # Right Sub-View: Top-View Rotational Moiré Misorientation
        '<rect x="342" y="36" width="210" height="202" fill="#FDFEFE" stroke="#F5B041" stroke-width="1.1" rx="4" />',
        _t(350, 51, "B. BASAL PLAN VIEW: MOIRE TWIST", 8.2, "#B9770E", "bold"),
        '<g transform="translate(447, 128)">',
    ]
    # Layer 1 hexagons (unrotated)
    for dx, dy in [(-27, -15.6), (0, -31.2), (27, -15.6), (-27, 15.6), (0, 0), (27, 15.6), (0, 31.2)]:
        turbo.append(f'<polygon points="{_hex_points(dx, dy, 18)}" fill="none" stroke="#2C3E50" stroke-width="1.6" />')
    # Layer 2 hexagons (rotated by 22 deg - incommensurate turbostratic stacking)
    turbo.append('<g transform="rotate(22)">')
    for dx, dy in [(-27, -15.6), (0, -31.2), (27, -15.6), (-27, 15.6), (0, 0), (27, 15.6), (0, 31.2)]:
        turbo.append(f'<polygon points="{_hex_points(dx, dy, 18)}" fill="none" stroke="#E67E22" stroke-width="1.4" stroke-dasharray="3,2" />')
    turbo += [
        '</g>',
        '</g>',
        _t(447, 198, "Random rotation angle theta != 0°, 60°", 7.4, "#9C640C", "bold", "middle"),
        _t(447, 211, "Incommensurate stacking destroys", 7.2, "#5D6D7E", "normal", "middle"),
        _t(447, 222, "aligned LiC6 intercalation sites", 7.2, "#922B21", "bold", "middle"),

        # Bottom Quantitative Crystallographic & XRD Audit Table
        '<rect x="12" y="246" width="540" height="152" fill="#FEF9E7" stroke="#F5B041" stroke-width="1.1" rx="4" />',
        _t(22, 262, "TURBOSTRATIC CRYSTALLOGRAPHIC & ELECTROCHEMICAL AUDIT (T = 1,000 - 1,350 °C):", 9, "#9C640C", "bold"),
        '<line x1="22" y1="268" x2="542" y2="268" stroke="#F5B041" stroke-width="0.9" />',
    ]
    turbo_rows = [
        ("• Layer Stacking Sequence:", "Random rotational & translational disorder (1D diffraction)"),
        ("• Interlayer Spacing d002:", "0.3440 - 0.3550 nm (Franklin non-graphitized threshold >= 0.3440 nm)"),
        ("• XRD (002) Bragg Reflection:", "2-theta = 25.4° - 25.8° (Cu-Ka) | Broad asymmetric peak (FWHM > 1.2°)"),
        ("• Crystallite Coherence Lengths:", "Stacking height L_c = 2 - 5 nm | In-plane domain L_a = 4 - 10 nm"),
        ("• Degree of Graphitization (g):", "g = 0.0%  [Mering-Maire: g = (0.3440 - d002) / (0.3440 - 0.3354)]"),
        ("• Raman Spectroscopy (532 nm):", "High D-band (1,350 cm-1) defect intensity: I_D / I_G = 0.85 - 1.25"),
        ("• Reversible Li+ Capacity:", "180 - 230 mAh/g (Sloping voltage curve, high hysteresis, no LiC6 plateau)"),
    ]
    for idx, (k, v) in enumerate(turbo_rows):
        yy = 282 + idx * 16
        turbo.append(_t(22, yy, k, 7.8, "#1C2833", "bold"))
        turbo.append(_t(198, yy, v, 7.8, "#922B21" if idx in (1, 4, 6) else "#34495E", "bold" if idx in (1, 4, 6) else "normal"))
    turbo.append('</g>')

    # ---- TOP-RIGHT PANEL: Bernal Hexagonal 2H ABAB Graphite (2,800 - 3,000 °C) ----
    hexag = [
        '<g transform="translate(604, 92)" id="panel_hexagonal">',
        '<rect x="0" y="0" width="576" height="408" fill="#FFFFFF" stroke="#27AE60" stroke-width="1.8" rx="5" />',
        '<rect x="0" y="0" width="576" height="28" fill="#E8F8F5" rx="4" />',
        _t(12, 19, "2. BERNAL HEXAGONAL 2H GRAPHITE: ORDERED ABAB REGISTRY (2,800 - 3,000 °C)", 10.5, "#0E6251", "bold"),
        # Left Sub-View: Side-View ABAB Registry & Stage-1 LiC6 Intercalation
        '<rect x="12" y="36" width="330" height="202" fill="#FDFEFE" stroke="#76D7C4" stroke-width="1.1" rx="4" />',
        _t(20, 51, "A. SIDE VIEW (c-AXIS): ABAB STACKING & STAGE-1 LiC6 GALLERIES", 8.2, "#0E6251", "bold"),
    ]
    # 4 flat ordered graphene planes: A (y=74), B (y=116), A (y=158), B (y=200)
    layer_specs = [
        (74, "A", "#1B4F72", 42),
        (116, "B", "#117A65", 56),
        (158, "A", "#1B4F72", 42),
        (200, "B", "#117A65", 56),
    ]
    for ly, lbl, col, x_start in layer_specs:
        hexag.append(_t(22, ly + 4, lbl, 10, col, "bold"))
        hexag.append(f'<line x1="36" y1="{ly}" x2="236" y2="{ly}" stroke="{col}" stroke-width="4" />')
        for cx in range(x_start, 232, 28):
            hexag.append(f'<circle cx="{cx}" cy="{ly}" r="3.2" fill="#FFFFFF" stroke="{col}" stroke-width="1.4" />')
    # Vertical dashed alignment lines demonstrating ABAB half-hexagon shift
    for cx in range(42, 220, 56):
        hexag.append(f'<line x1="{cx}" y1="74" x2="{cx}" y2="200" stroke="#AED6F1" stroke-width="0.9" stroke-dasharray="2,2" />')
    # Intercalated Li+ ions in Stage-1 LiC6 galleries (y=95, 137, 179)
    for gy in (95, 137, 179):
        for lx in (63, 119, 175, 217):
            hexag.append(f'<circle cx="{lx}" cy="{gy}" r="6.5" fill="#F1C40F" stroke="#B7950B" stroke-width="1.2" />')
            hexag.append(_t(lx, gy + 2.5, "Li+", 6, "#1C2833", "bold", "middle"))
    hexag += [
        # Precision dimension callouts strictly inside x=242..338
        '<line x1="246" y1="74" x2="246" y2="116" stroke="#27AE60" stroke-width="1.6" marker-start="url(#arrowGreen)" marker-end="url(#arrowGreen)" />',
        _t(252, 91, "d002 =", 7.5, "#0E6251", "bold"),
        _t(252, 102, "0.3354 nm", 7.5, "#0E6251", "bold", "start", "Courier, monospace"),
        _t(252, 113, "(0.370 LiC6)", 6.8, "#117A65"),
        '<line x1="246" y1="116" x2="246" y2="200" stroke="#2980B9" stroke-width="1.5" marker-start="url(#arrowBlue)" marker-end="url(#arrowBlue)" />',
        _t(252, 155, "c = 2*d002", 7.3, "#1B4F72", "bold"),
        _t(252, 166, "= 0.6708 nm", 7.3, "#1B4F72", "bold", "start", "Courier, monospace"),
        _t(252, 182, "L_c: 25-45nm", 7.0, "#0E6251", "bold"),
        _t(22, 228, "Stage-1 LiC6: rapid 2D Li+ diffusion (D_Li ~ 10^-8 cm2/s) -> 372 mAh/g", 7.3, "#0E6251", "bold"),

        # Right Sub-View: Top-View Bernal ABAB Registry & LiC6 Superlattice
        '<rect x="350" y="36" width="214" height="202" fill="#FDFEFE" stroke="#76D7C4" stroke-width="1.1" rx="4" />',
        _t(358, 51, "B. BASAL PLAN VIEW: ABAB + LiC6", 8.2, "#0E6251", "bold"),
        '<g transform="translate(457, 126)">',
    ]
    # Layer A hexagons (solid navy)
    hex_centers = [(-27, -15.6), (0, -31.2), (27, -15.6), (-27, 15.6), (0, 0), (27, 15.6), (0, 31.2)]
    for dx, dy in hex_centers:
        hexag.append(f'<polygon points="{_hex_points(dx, dy, 18)}" fill="none" stroke="#1B4F72" stroke-width="1.6" />')
    # Layer B shifted hexagons (shifted by a/sqrt(3) = 18px along x)
    for dx, dy in [(-27, -15.6), (0, -31.2), (0, 0), (-27, 15.6)]:
        hexag.append(f'<polygon points="{_hex_points(dx + 18, dy, 18)}" fill="none" stroke="#16A085" stroke-width="1.2" stroke-dasharray="3,2" />')
    # Golden Li+ ions occupying (sqrt(3) x sqrt(3))R30° superlattice centers
    for lx, ly in [(0, 0), (0, -31.2), (0, 31.2), (-27, -15.6), (27, 15.6)]:
        hexag.append(f'<circle cx="{lx}" cy="{ly}" r="5.5" fill="#F1C40F" stroke="#B7950B" stroke-width="1.1" />')
    hexag += [
        '</g>',
        _t(457, 198, "Layer B shifted by a_C-C = 0.1421 nm", 7.4, "#0E6251", "bold", "middle"),
        _t(457, 211, "Golden Li+ ions occupy aligned", 7.2, "#34495E", "normal", "middle"),
        _t(457, 222, "(sqrt(3) x sqrt(3))R30° LiC6 sites", 7.2, "#145A32", "bold", "middle"),

        # Bottom Quantitative Crystallographic & XRD Audit Table
        '<rect x="12" y="246" width="552" height="152" fill="#E8F8F5" stroke="#76D7C4" stroke-width="1.1" rx="4" />',
        _t(22, 262, "BERNAL HEXAGONAL CRYSTALLOGRAPHIC & ELECTROCHEMICAL AUDIT (T = 2,800 - 3,000 °C):", 9, "#0E6251", "bold"),
        '<line x1="22" y1="268" x2="554" y2="268" stroke="#76D7C4" stroke-width="0.9" />',
    ]
    hex_rows = [
        ("• Space Group & Polytype:", "P6_3/mmc (2H Hexagonal ABAB Bernal registry; <10% 3R ABC rhombohedral)"),
        ("• Interlayer Spacing d002:", "0.3354 nm (ideal crystal) | 0.3356 - 0.3360 nm (synthetic LWG/Acheson)"),
        ("• XRD (002) Bragg Reflection:", "2-theta = 26.55° (Cu-Ka) | Sharp symmetric reflection + (101)/(112) 3D peaks"),
        ("• Crystallite Coherence Lengths:", "Stacking height L_c = 25 - 45 nm | In-plane domain L_a = 50 - 120 nm"),
        ("• Degree of Graphitization (g):", "g = 90.0 - 97.7% (Synthetic anode spec >= 93%; Natural flake ~ 98-100%)"),
        ("• Raman Spectroscopy (532 nm):", "Dominant G-band (1,580 cm-1) sp2 stretching: I_D / I_G = 0.08 - 0.22"),
        ("• Reversible Li+ Capacity:", "355 - 365 mAh/g (95-98% of 372 mAh/g Stage-1 LiC6 theoretical limit)"),
    ]
    for idx, (k, v) in enumerate(hex_rows):
        yy = 282 + idx * 16
        hexag.append(_t(22, yy, k, 7.8, "#1C2833", "bold"))
        hexag.append(_t(198, yy, v, 7.8, "#0E6251" if idx in (1, 4, 6) else "#34495E", "bold" if idx in (1, 4, 6) else "normal"))
    hexag.append('</g>')

    # ---- Transition Chevron between Top Panels ----
    chev = '<polygon points="586,282 604,294 586,306" fill="#C0392B" stroke="#FFFFFF" stroke-width="1.2" />'

    # ---- BOTTOM-LEFT PANEL: Mering-Maire Curve (d002 & g vs T) & Li+ Staging Curve ----
    bot_left = [
        '<g transform="translate(22, 512)" id="crystallographic_curves">',
        '<rect x="0" y="0" width="642" height="268" fill="#FFFFFF" stroke="#1C2833" stroke-width="1.6" rx="5" />',
        '<rect x="0" y="0" width="642" height="26" fill="#1C2833" rx="4" />',
        _t(12, 17, "MERING-MAIRE GRAPHITIZATION TRAJECTORY (d002 VS. T) & DAUMAS-HEROLD Li+ STAGING", 9.8, "#ECF0F1", "bold"),

        # Sub-Chart 1: d002 & g vs Furnace Temperature (1,000 -> 3,000 °C)
        '<rect x="10" y="34" width="308" height="224" fill="#F4F9FD" stroke="#85C1E9" stroke-width="1" rx="3" />',
        _t(18, 49, "A. INTERLAYER CONTRACTION d002(T) & MERING-MAIRE g", 8.2, "#1B4F72", "bold"),
        # Axes: x from 54 (1,000°C) to 294 (3,000°C); y from 68 (0.3440 nm, g=0%) to 188 (0.3354 nm, g=100%)
        '<line x1="54" y1="68" x2="54" y2="192" stroke="#1C2833" stroke-width="1.3" />',
        '<line x1="54" y1="192" x2="300" y2="192" stroke="#1C2833" stroke-width="1.3" />',
        # Horizontal dashed gridlines
        '<line x1="54" y1="68" x2="300" y2="68" stroke="#E74C3C" stroke-width="0.9" stroke-dasharray="3,2" />',
        _t(50, 71, "0.3440", 6.8, "#C0392B", "bold", "end", "Courier, monospace"),
        '<line x1="54" y1="128" x2="300" y2="128" stroke="#BDC3C7" stroke-width="0.8" stroke-dasharray="2,2" />',
        _t(50, 131, "0.3397", 6.8, "#566573", "normal", "end", "Courier, monospace"),
        '<line x1="54" y1="188" x2="300" y2="188" stroke="#27AE60" stroke-width="0.9" stroke-dasharray="3,2" />',
        _t(50, 191, "0.3354", 6.8, "#0E6251", "bold", "end", "Courier, monospace"),
        # Temperature ticks: 1000, 1500, 2000, 2500, 3000 °C
        _t(54, 204, "1,000°C", 6.8, "#34495E", "normal", "middle"),
        _t(114, 204, "1,500°C", 6.8, "#34495E", "normal", "middle"),
        _t(174, 204, "2,000°C", 6.8, "#34495E", "normal", "middle"),
        _t(234, 204, "2,500°C", 6.8, "#34495E", "normal", "middle"),
        _t(294, 204, "3,000°C", 6.8, "#0E6251", "bold", "middle"),
        # Sigmoidal d002 contraction curve:
        # (1000°C, 0.3440 -> 54,68), (1500°C, 0.3440 -> 114,68), (1800°C, 0.3435 -> 150,75),
        # (2000°C, 0.3415 -> 174,103), (2300°C, 0.3385 -> 210,145), (2600°C, 0.3364 -> 246,174),
        # (2900°C, 0.3356 -> 282,185), (3000°C, 0.3355 -> 294,187)
        '<path d="M 54 68 L 114 68 L 150 75 L 174 103 L 210 145 L 246 174 L 282 185 L 294 187" fill="none" stroke="#C0392B" stroke-width="2.4" />',
        '<circle cx="114" cy="68" r="3" fill="#C0392B" />',
        '<circle cx="174" cy="103" r="3" fill="#E67E22" />',
        '<circle cx="210" cy="145" r="3" fill="#F39C12" />',
        '<circle cx="246" cy="174" r="3.2" fill="#27AE60" />',
        '<circle cx="282" cy="185" r="3.8" fill="#0E6251" />',
        _t(108, 62, "Turbostratic (g=0%)", 6.8, "#C0392B", "bold"),
        _t(182, 100, "g = 29%", 6.8, "#B9770E", "bold"),
        _t(218, 142, "g = 64%", 6.8, "#B9770E", "bold"),
        _t(236, 166, "2,600°C (g=88%)", 6.8, "#117A65", "bold", "end"),
        _t(280, 178, "2,900°C (g=95%)", 6.8, "#0E6251", "bold", "end"),
        # Mering-Maire formula callout box at bottom of Sub-Chart 1
        '<rect x="18" y="212" width="292" height="40" fill="#FFFFFF" stroke="#85C1E9" stroke-width="0.9" rx="2" />',
        _t(24, 225, "Mering-Maire Equation (Franklin 1951):", 7.5, "#1B4F72", "bold"),
        _t(24, 238, "g = (0.3440 - d002) / (0.3440 - 0.3354) x 100%", 7.5, "#1C2833", "bold", "start", "Courier, monospace"),
        _t(24, 248, "Threshold: T >= 2,500 °C required to reach g >= 88%.", 7.0, "#5D6D7E"),

        # Sub-Chart 2: Daumas-Hérold Li+ Intercalation Staging Curve (V vs Capacity)
        '<rect x="326" y="34" width="306" height="224" fill="#FEF9E7" stroke="#F39C12" stroke-width="1" rx="3" />',
        _t(334, 49, "B. Li+ STAGING POTENTIAL PROFILE (V vs. Li/Li+)", 8.2, "#B9770E", "bold"),
        # Axes: x from 366 (0 mAh/g) to 612 (372 mAh/g); y from 68 (1.0 V) to 192 (0.0 V)
        '<line x1="366" y1="68" x2="366" y2="192" stroke="#1C2833" stroke-width="1.3" />',
        '<line x1="366" y1="192" x2="618" y2="192" stroke="#1C2833" stroke-width="1.3" />',
        _t(362, 73, "1.0V", 6.8, "#34495E", "normal", "end", "Courier, monospace"),
        _t(362, 132, "0.5V", 6.8, "#34495E", "normal", "end", "Courier, monospace"),
        _t(362, 169, "0.2V", 6.8, "#0E6251", "bold", "end", "Courier, monospace"),
        _t(362, 191, "0.0V", 6.8, "#C0392B", "bold", "end", "Courier, monospace"),
        _t(366, 204, "0", 6.8, "#34495E", "normal", "middle"),
        _t(432, 204, "100", 6.8, "#34495E", "normal", "middle"),
        _t(498, 204, "200", 6.8, "#34495E", "normal", "middle"),
        _t(564, 204, "300", 6.8, "#34495E", "normal", "middle"),
        _t(612, 204, "372 mAh/g", 6.8, "#0E6251", "bold", "end"),
        # Sloping Turbostratic Curve (stops at ~200 mAh/g, x=498)
        '<path d="M 368 74 Q 410 125, 455 155 Q 480 175, 498 188" fill="none" stroke="#C0392B" stroke-width="2.2" stroke-dasharray="4,2" />',
        _t(452, 122, "Turbostratic (g=0%)", 7.2, "#C0392B", "bold"),
        _t(452, 132, "Sloping, ~200 mAh/g", 6.8, "#922B21"),
        # Stepped ABAB Hexagonal Graphite Curve (Stage IV -> III -> II -> I plateaus)
        '<path d="M 368 74 L 382 166 L 408 166 L 414 174 L 464 174 L 470 182 L 604 182 L 608 190" fill="none" stroke="#0E6251" stroke-width="2.5" />',
        _t(395, 161, "IV/III", 6.5, "#0E6251", "bold", "middle"),
        _t(440, 169, "Stage II (LiC12)", 6.5, "#0E6251", "bold", "middle"),
        _t(542, 177, "Stage I (LiC6, 0.08 V)", 6.8, "#0E6251", "bold", "middle"),
        # Explanation box at bottom of Sub-Chart 2
        '<rect x="334" y="212" width="290" height="40" fill="#FFFFFF" stroke="#F5B041" stroke-width="0.9" rx="2" />',
        _t(340, 225, "Daumas-Herold Staging Mechanism:", 7.5, "#B9770E", "bold"),
        _t(340, 237, "Ordered ABAB galleries fill sequentially (LiC36 -> LiC12 -> LiC6)", 7.1, "#1C2833"),
        _t(340, 248, "at 0.20 - 0.08 V vs Li/Li+, maximizing cell voltage & energy.", 7.1, "#0E6251", "bold"),
        '</g>',
    ]

    # ---- MIDDLE-RIGHT PANEL: Geological vs Synthetic Crystallinity & Energy Trade-Off ----
    mid_right = [
        '<g transform="translate(680, 512)" id="thermodynamic_crystallinity_comparison">',
        '<rect x="0" y="0" width="500" height="150" fill="#EAFAF1" stroke="#27AE60" stroke-width="1.6" rx="5" />',
        '<rect x="0" y="0" width="500" height="24" fill="#0E6251" rx="4" />',
        _t(12, 16, "GEOLOGICAL METAMORPHISM VS. ELECTRO-THERMAL GRAPHITIZATION", 9.5, "#FFFFFF", "bold"),
        _t(12, 39, "Why Natural cSPG Uses 42.6% Less Electricity Than Acheson Synthetic Graphite:", 8.2, "#1C2833", "bold"),
        _t(12, 54, "• 1. Natural Flake Route (7.91 kWh/kg cSPG): Geological metamorphism (700-850 °C, 5-8 kbar", 7.6, "#0E6251", "bold"),
        _t(12, 66, "  over ~10^7 yr) provides d002 = 0.3354 nm (g ~ 100%) for free; only the 5 wt% amorphous", 7.5, "#34495E"),
        _t(12, 78, "  pitch coating requires 1,100 °C carbonization (Stage 4: 2.07 kWh/kg).", 7.5, "#34495E"),
        _t(12, 94, "• 2. Synthetic Route (13.79 kWh/kg Acheson | 8.69 kWh/kg LWG): Must overcome the", 7.6, "#900C3F", "bold"),
        _t(12, 106, "  260 kJ/mol C-C rearrange activation barrier at 2,800-3,000 °C to convert turbostratic", 7.5, "#34495E"),
        _t(12, 118, "  needle coke (d002 = 0.3440 nm) into ABAB graphite (d002 = 0.3356 nm, g = 93-97%).", 7.5, "#34495E"),
        '<line x1="12" y1="125" x2="488" y2="125" stroke="#A3E4D7" stroke-width="0.9" />',
        _t(12, 139, "• Trade-Off: Synthetic has lower swelling & longer cycle life (>2,000 cycles vs ~1,200 natural).", 7.6, "#1B4F72", "bold"),
        '</g>',
    ]

    body = "\n".join(turbo + hexag + [chev] + bot_left + mid_right)
    lines = [
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 800" width="1200" height="800">',
        common_svg_defs(),
        '  <rect width="1200" height="800" fill="#F8F9F9" />',
        render_drawing_header(
            "CRYSTALLOGRAPHIC EVOLUTION: TURBOSTRATIC CARBON TO BERNAL ABAB LATTICE",
            "Atomic-Scale Phase Transition (1,000 -> 3,000 °C): d002 Contraction, Mering-Maire Graphitization & Stage-1 LiC6 Intercalation"
        ),
        body,
    ]
    lines.append(render_title_block(
        "DWG-MAT-02",
        "TURBOSTRATIC TO BERNAL ABAB CRYSTAL LATTICE",
        "Crystallographic Phase Transition (Stage 3)",
        "d002: >=0.3440 nm (g=0%) -> 0.3354 nm (g>93%) | Stage-1 LiC6: 372 mAh/g",
        "Franklin (1951); Surovtseva et al. (2022); ANL-22/74"
    ))
    lines.append("</svg>")
    return "\n".join(lines)


# =====================================================================
# Main Execution Pipeline
# =====================================================================
def main():
    print("=" * 70)
    print("PARAMETRIC VECTOR SVG TECHNICAL CROSS-SECTION GENERATOR")
    print("=" * 70)

    os.makedirs(SVG_DIR, exist_ok=True)

    drawings = [
        ("machine_01_froth_flotation_cell.svg", create_svg_froth_flotation),
        ("machine_02_spheronization_acm_mill.svg", create_svg_acm_mill),
        ("machine_03_hf_acid_leaching_reactor.svg", create_svg_acid_reactor),
        ("machine_04_acheson_vs_lwg_furnace.svg", create_svg_graphitization_furnaces),
        ("material_01_natural_flake_to_cspg_morphology.svg", create_svg_flake_to_cspg_morphology),
        ("material_02_turbostratic_to_hexagonal_crystal_lattice.svg", create_svg_turbostratic_to_lattice),
    ]

    for fname, generator_fn in drawings:
        svg_content = generator_fn()
        # Verify strict XML well-formedness
        try:
            ET.fromstring(svg_content)
        except ET.ParseError as err:
            print(f"✗ XML Validation Error in {fname}: {err}")
            raise err

        out_path = os.path.join(SVG_DIR, fname)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(svg_content)
        print(f"✓ Generated & Validated XML: docs/svg/{fname} ({len(svg_content):,} bytes)")

    print("=" * 70)
    print("VECTOR SVG GENERATION COMPLETE: 6/6 Technical Drawings Created.")
    print("=" * 70)


if __name__ == "__main__":
    main()
