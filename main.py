import streamlit as st
import re

# Page Configuration
st.set_page_config(
    page_title="AI-Marshes Microbe",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (Darker, Richer & Cleaner UI)
st.markdown("""
    <style>
    .main {
        background-color: #e2e8f0;
    }
    .stButton>button {
        background-color: #0f766e;
        color: white;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
        padding: 12px;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #115e59;
    }
    h1, h2, h3 {
        color: #134e4a;
    }
    </style>
""", unsafe_allow_html=True)

# App Title & Header
st.markdown("<h1 style='text-align: center; color: #134e4a;'>🧬 AI-Marshes Microbe 🧬</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #334155; font-weight: bold;'>Advanced Microbial Risk Diagnostic Platform (Pregnant Women, Pediatrics, Tigris & Marshes Ecosystem)</p>", unsafe_allow_html=True)
st.markdown("---")

# Layout Columns
col1, col2 = st.columns(2)

with col1:
    patient_category = st.selectbox(
        "👤 Patient Category:",
        ["Select Category...", "🤰 Pregnant Woman", "👶 Pediatrics & Adolescents (1 - 18 yrs)", "🧑 Adults / General"]
    )
    
    sample_type = st.selectbox(
        "🧪 Sample Type:",
        ["Select Sample Type...", "💧 Urine Sample", "🩸 Blood Sample", "🧬 Vaginal Swab (Pregnant Specific)", "🩹 Wound Swab (Marshes/Tigris Environment)"]
    )
    
    gene_sequence = st.text_input(
        "🔬 Bacterial Gene Sequence (Enter A, T, C, G):",
        value="ATGCGATCGATCGATC"
    )

with col2:
    pathogen = st.selectbox(
        "🦠 Matched Pathogen in Database:",
        [
            "Select Pathogen...",
            "Escherichia coli (UTI & Enteric)",
            "Pseudomonas aeruginosa (Marshes & Wounds)",
            "Vibrio cholerae (River & Marshes Water)",
            "Klebsiella pneumoniae (Respiratory & Gynecological)",
            "No Pathogenic Bacteria Detected (Normal)"
        ]
    )
    
    crp_input = st.number_input(
        "📊 C-Reactive Protein (CRP) Level (mg/L - Normal < 5):",
        min_value=0.0, step=0.1, value=2.0
    )
    
    wbc_input = st.number_input(
        "🩸 White Blood Cells (WBC) Count (cells/μL - Normal 4000-11000):",
        min_value=0.0, step=100.0, value=7000.0
    )

ultrasound = st.selectbox(
    "🩺 Ultrasound Status:",
    ["Normal / Clear", "Abnormal / Pathological Changes Detected"]
)

st.markdown("<br>", unsafe_allow_html=True)

# Run Analysis Button
if st.button("🚀 Run Smart Diagnostic Analysis"):
    
    clean_seq = gene_sequence.strip().upper()
    valid_dna_pattern = re.compile("^[ATCG]+$")
    
    if patient_category == "Select Category..." or sample_type == "Select Sample Type..." or pathogen == "Select Pathogen...":
        st.error("❌ Please select all required fields before running the analysis.")
    elif len(clean_seq) < 5 or not valid_dna_pattern.match(clean_seq):
        st.error("⚠️ Invalid Gene Sequence: Ensure it contains only valid nucleotide symbols (A, T, C, G).")
    else:
        # Precise Risk Score Calculation (1% to 100%)
        risk_score = 10  # Base score
        
        # Pathogen impact
        if "Pseudomonas" in pathogen or "Vibrio" in pathogen:
            risk_score += 35
        elif "Escherichia" in pathogen or "Klebsiella" in pathogen:
            risk_score += 25
        elif "No Pathogenic" in pathogen:
            risk_score = 5
            
        # CRP impact
        if crp_input > 40:
            risk_score += 30
        elif 10 <= crp_input <= 40:
            risk_score += 20
        elif 5 <= crp_input < 10:
            risk_score += 10
            
        # WBC impact
        if wbc_input > 15000:
            risk_score += 20
        elif 11000 < wbc_input <= 15000:
            risk_score += 10
        elif wbc_input < 4000:
            risk_score += 15
            
        # Ultrasound impact
        if ultrasound == "Abnormal / Pathological Changes Detected":
            risk_score += 15
            
        # Patient sensitivity category impact
        if "Pregnant" in patient_category or "Pediatrics" in patient_category:
            risk_score += 10
            
        # Final boundary check (1% to 100%)
        if "No Pathogenic" in pathogen and crp_input < 5 and wbc_input <= 11000:
            risk_score = 8  # Safe baseline
            
        if risk_score > 98:
            risk_score = 98
        elif risk_score < 5:
            risk_score = 5
            
        st.markdown("---")
        st.subheader("📋 Diagnostic Results & Risk Assessment:")
        
        # Display Results with Exact Percentage (1% - 100%)
        if risk_score < 30:
            st.success(f"🟢 Safe Condition & Under Control (Calculated Risk Rate: {risk_score}%)")
        elif 30 <= risk_score < 70:
            st.warning(f"🟡 Moderate Alert - Potential Risk Requiring Follow-up (Calculated Risk Rate: {risk_score}%)")
        else:
            st.error(f"🔴 High Risk Warning - Immediate Medical Intervention Required (Calculated Risk Rate: {risk_score}%)")
            
        st.markdown(f"""
        * Lab Summary: CRP: {crp_input} mg/L | WBC: {wbc_input} cells/μL
        * Clinical Note: {"Immediate medical attention & appropriate antibiotic therapy required." if risk_score >= 70 else "Condition stable; regular monitoring and preventive care advised."}
        """)
