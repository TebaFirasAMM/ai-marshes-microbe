import streamlit as st
import re
import streamlit.components.v1 as components

components.html(
    '<meta name="google-site-verification" content="WvWqpxPre8eh9xRCdG52RG19FPSg_kO_Yg7j3yZ4W88">',
    height=0, width=0
)
# Page Configuration
st.set_page_config(
    page_title="AI-Marshes Microbe - Diagnostic Hub",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Professional Blue Tech & Medical Styling + Clean Animated Banners (No text, moving icons only)
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f6ff;
        color: #0f172a;
    }
    
    h1 {
        color: #1e3a8a !important;
        font-weight: 800 !important;
        font-size: 38px !important;
        text-align: center;
    }
    
    h3, h4 {
        color: #1e40af !important;
        font-weight: 700 !important;
    }
    
    .dashboard-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(30, 58, 138, 0.08);
        margin-bottom: 25px;
    }
    
    label, .stMarkdown p {
        font-size: 17px !important;
        font-weight: 600 !important;
        color: #1e3a8a !important;
    }
    
    .stButton>button {
        background: linear-gradient(135deg, #1e40af 0%, #1d4ed8 100%);
        color: #ffffff;
        font-weight: 700;
        width: 100%;
        border-radius: 10px;
        padding: 15px;
        font-size: 18px;
        border: none;
        box-shadow: 0 6px 20px rgba(29, 78, 216, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e3a8a 100%);
        box-shadow: 0 8px 25px rgba(29, 78, 216, 0.5);
    }

    /* --- شريط ديكوري متحرك بدون أي نصوص، النقشات فقط تتحرك --- */
    .microbe-banner {
        width: 100%;
        height: 38px;
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #008080 100%);
        border-radius: 8px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
        margin-top: 15px;
        margin-bottom: 25px;
    }
    .microbe-banner::before {
        content: "🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠";
        position: absolute;
        top: 0;
        left: 0;
        width: 200%;
        height: 100%;
        font-size: 18px;
        letter-spacing: 20px;
        opacity: 0.25;
        white-space: nowrap;
        animation: slideBanner 20s linear infinite;
        display: flex;
        align-items: center;
        color: white;
    }
    @keyframes slideBanner {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    </style>
""", unsafe_allow_html=True)

# دالة لطباعة الشريط المزخرف الخالي من النصوص
def render_banner():
    st.markdown('<div class="microbe-banner"></div>', unsafe_allow_html=True)

# App Title & Header
st.markdown("<h1>🧬 AI-Marshes Microbe Intelligence Hub</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #334155; font-size: 19px; font-weight: 500;'>Advanced Microbial Risk Diagnostic & Ecosystem Analytics Platform</p>", unsafe_allow_html=True)

# --- الشريط الأول المتحرك تحت العنوان مباشرة ---
render_banner()

# Layout Columns (Main Form Layout)
col1, col2 = st.columns(2, gap="large")

with col1:
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<h3>👤 Patient & Sample Information</h3>", unsafe_allow_html=True)
    
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
    st.markdown("</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
    st.markdown("<h3>📊 Clinical & Laboratory Metrics</h3>", unsafe_allow_html=True)
    
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
    st.markdown("</div>", unsafe_allow_html=True)

# Full-width Ultrasound selection
st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
ultrasound = st.selectbox(
    "🩺 Ultrasound & Imaging Status:",
    ["Normal / Clear", "Abnormal / Pathological Changes Detected"]
)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Run Analysis Button
run_btn = st.button("🚀 Run Smart Diagnostic Analysis")

st.markdown("<br>", unsafe_allow_html=True)

# Analysis Execution Logic
if run_btn:
    clean_seq = gene_sequence.strip().upper()
    valid_dna_pattern = re.compile("^[ATCG]+$")
    
    if "Select" in patient_category or "Select" in sample_type or "Select" in pathogen:
        st.error("❌ Please select all required fields before running the analysis.")
    elif len(clean_seq) < 5 or not valid_dna_pattern.match(clean_seq):
        st.error("⚠️ Invalid Gene Sequence: Ensure it contains only valid nucleotide symbols (A, T, C, G).")
    else:
        risk_score = 10  
        
        if "Pseudomonas" in pathogen or "Vibrio" in pathogen:
            risk_score += 35
        elif "Escherichia" in pathogen or "Klebsiella" in pathogen:
            risk_score += 25
        elif "No Pathogenic" in pathogen:
            risk_score = 5
            
        if crp_input > 40:
            risk_score += 30
        elif 10 <= crp_input <= 40:
            risk_score += 20
        elif 5 <= crp_input < 10:
            risk_score += 10
            
        if wbc_input > 15000:
            risk_score += 20
        elif 11000 < wbc_input <= 15000:
            risk_score += 10
        elif wbc_input < 4000:
            risk_score += 15
            
        if "Abnormal" in ultrasound:
            risk_score += 15
            
        if "Pregnant" in patient_category or "Pediatrics" in patient_category:
            risk_score += 10
            
        if "No Pathogenic" in pathogen and crp_input < 5 and wbc_input <= 11000:
            risk_score = 8  
            
        if risk_score > 98:
            risk_score = 98
        elif risk_score < 5:
            risk_score = 5
            
        st.markdown("<div class='dashboard-card'>", unsafe_allow_html=True)
        st.markdown("<h3>📋 Diagnostic Results & Risk Assessment Report</h3>", unsafe_allow_html=True)
        st.markdown("<hr style='border-color: #cbd5e1;'>", unsafe_allow_html=True)
        
        col_r1, col_r2 = st.columns([1, 2], gap="large")
        
        with col_r1:
            st.metric(label="Calculated Risk Rate", value=f"{risk_score}%", delta="Critical Tier" if risk_score >= 70 else "Stable Tier")
            
        with col_r2:
            if risk_score < 30:
                st.success(f"🟢 Safe Condition & Under Control (Risk Rate: {risk_score}%)")
            elif 30 <= risk_score < 70:
                st.warning(f"🟡 Moderate Alert - Potential Risk Requiring Follow-up (Risk Rate: {risk_score}%)")
            else:
                st.error(f"🔴 High Risk Warning - Immediate Medical Intervention Required (Risk Rate: {risk_score}%)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background-color: #f8fafc; padding: 20px; border-radius: 12px; border: 1px solid #e2e8f0;'>
            <h4 style='color: #1e3a8a; margin-top: 0;'>🔬 Clinical Summary & Protocol</h4>
            <ul style='color: #334155; line-height: 2.0; font-size: 16px;'>
                <li><b>Patient Profile:</b> {patient_category} | <b>Sample:</b> {sample_type}</li>
                <li><b>Pathogen Detected:</b> {pathogen}</li>
                <li><b>Biomarkers:</b> CRP: <code>{crp_input} mg/L</code> | WBC: <code>{wbc_input} cells/μL</code></li>
                <li><b>Clinical Decision:</b> <b>{"Immediate medical attention & appropriate antibiotic therapy required." if risk_score >= 70 else "Condition stable; regular monitoring and preventive care advised."}</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# --- الشريط الثاني المتحرك في نهاية الصفحة ---
render_banner()
# --- إضافة شريط متحرك ذكي في أسفل الصفحة ---
st.markdown("""
    <style>
    .microbe-banner-bottom {
        width: 100%;
        height: 38px;
        background: #f0f6ff;
        position: relative;
        overflow: hidden;
        margin-top: 35px;
        margin-bottom: 15px;
    }
    .microbe-banner-bottom::before {
        content: "🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠 🧬 🔬 🧫 🦠";
        position: absolute;
        top: 0;
        left: 0;
        width: 200%;
        height: 100%;
        font-size: 18px;
        letter-spacing: 20px;
        opacity: 0.85;
        white-space: nowrap;
        animation: slideBannerBottom 20s linear infinite;
        display: flex;
        align-items: center;
        color: #1e3a8a;
    }
    @keyframes slideBannerBottom {
        0% { transform: translateX(0); }
        100% { transform: translateX(-50%); }
    }
    </style>
    <div class="microbe-banner-bottom"></div>
""", unsafe_allow_html=True)
st.markdown("""
    <head>
        <meta name="google-site-verification" content="WvWqpxPre8eh9xRcDgS2RGl9FPSgJiYg_xvbbjUZNHI" />
        <meta name="description" content="AI-Marshes Microbe (AMM) - Advanced Microbial Risk Diagnostic & Ecosystem Analytics Platform.">
        <meta name="keywords" content="AI-Marshes Microbe, AMM, AI Marshes Microbe, amm microbe, microbial diagnostic hub, University of Mosul">
        <meta name="author" content="Microbiology Student Platform">
    </head>
""", unsafe_allow_html=True)
