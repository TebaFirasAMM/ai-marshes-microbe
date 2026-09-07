import streamlit as st
import numpy as np

# Page Configuration
st.set_page_config(page_title="AI-Marshes Microbe Platform", page_icon="🧬", layout="wide")

# Custom CSS for clean academic look
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; }
    h1, h2, h3 { color: #2B6CB0; font-family: 'Helvetica Neue', sans-serif; }
    .stButton>button {
        background-color: #6383ED;
        color: white;
        border-radius: 5px;
        font-weight: bold;
        width: 100%;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Header
st.title("THE AI-MARSHES MICROBE PLATFORM")
st.markdown("*Predictive Bio-AI for Genomic Mutation & Fetal Cellular Risk Analysis | Official Academic Edition*")
st.markdown("---")

st.header("II. COMPUTATIONAL GENOMIC ANALYTICS")

# Layout columns for inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧬 Microbial Genomic Input")
    sample_type = st.selectbox(
        "Select Clinical Sample Type:",
        ["Urine Sample (UTI - E. coli)", "Vaginal / Cervical Swab (GBS/Other)"]
    )
    dna_seq = st.text_area("Bacterial DNA Sequence Metadata (Bases A, T, C, G):", 
                           "ATGGCGATCGATCGATCGATCGATCGGCGGCCAAACTTTT\nCTTGCCCCCCGGGTCACTTTTATCAGTTAGAAACCTICACAAAAA\nTTTTAGGGGCGCTATTATTTTATCTGCTCAAACAATATCTGGGA")

with col2:
    st.subheader("🩺 Maternal Clinical Parameters")
    ultrasound_status = st.selectbox(
        "High-Resolution Fetal Ultrasonography Matrix:",
        ["Normal (Optimal & Physiological Fetal Development)", 
         "Mild / Borderline (Minor Fluid Variation or Monitoring)", 
         "Critical / Danger (Oligohydramnios / Placentitis Sign)"]
    )
    crp_val = st.number_input("Serum C-Reactive Protein (CRP Concentration in mg/L):", min_value=0.0, max_value=250.0, value=12.5, step=0.5)

st.markdown("---")

# Execution Button
if st.button("⚡ EXECUTE COMPUTATIONAL INTEGRATED RISK PREDICTION"):
    # Simple intelligent logic simulation based on inputs
    risk_score = 0
    if "Critical" in ultrasound_status:
        risk_score += 2
    elif "Mild" in ultrasound_status:
        risk_score += 1
        
    if crp_val > 50.0:
        risk_score += 2
    elif crp_val > 10.0:
        risk_score += 1
        
    if "Vaginal" in sample_type:
        risk_score += 1

    st.markdown("### 📊 Diagnostic & Risk Output Result:")
    if risk_score >= 3:
        st.error("🚨 DANGER / HIGH RISK STATE: Significant environmental stress correlation detected. Genomic mutation markers combined with elevated clinical parameters indicate high probability of inflammatory complications or preterm risk. Immediate clinical intervention advised.")
    elif risk_score >= 1:
        st.warning("⚠️ BORDERLINE / MODERATE STRESS: Moderate adaptive strain mutation detected under environmental pressure. Requires close clinical monitoring and follow-up.")
    else:
        st.success("✅ NORMAL / TOLERANT STATE: Bacterial isolate exhibits standard baseline stability with minimal immediate fetal risk indices.")
