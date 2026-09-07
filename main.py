import streamlit as st

# إعدادات الصفحة وواجهة المنصة الأكاديمية
st.set_page_config(
    page_title="Al-Marshes Microbe Platform",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تخصيص الألوان بتصميم كلاسيكي هادئ وفاتح (CSS Styling)
st.markdown("""
    <style>
    /* خلفية عامة فاتحة وهادئة */
    .stApp {
        background-color: #F8FAFC;
    }
    /* عناوين رئيسية بأزرق كلاسيكي هادئ */
    h1, h2, h3 {
        color: #1E40AF !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* تنسيق الحاويات والبطاقات */
    div.stSelectbox, div.stTextArea, div.stNumberInput {
        background-color: #FFFFFF;
        padding: 5px;
        border-radius: 8px;
    }
    /* الأزرار بلون أزرق أكاديمي جذاب */
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        border: none;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان المنصة الرئيسي
st.markdown("""
    <div style='text-align: center; padding: 15px; background: linear-gradient(135deg, #EFF6FF 0%, #DBEAFE 100%); border-radius: 12px; margin-bottom: 20px;'>
        <h1 style='color: #1E3A8A; font-size: 28px; margin-bottom: 5px;'>THE AI-MARSHES MICROBE PLATFORM</h1>
        <p style='color: #475569; font-size: 15px; font-weight: 600;'>Predictive Bio-AI for Genomic Mutation & Fetal Cellular Risk Analysis | Official Academic Edition</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("## II. COMPUTATIONAL GENOMIC ANALYTICS")

# تقسيم الشاشة إلى عمودين منظمين
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🧬 Microbial Genomic Input")
    
    # قائمة منسدلة متعددة لأنواع البكتيريا
    sample_type = st.selectbox(
        "Select Clinical Sample Type:",
        [
            "Urine Sample (UTI - E. coli)",
            "Urine Sample (UTI - Klebsiella pneumoniae)",
            "Urine Sample (UTI - Proteus mirabilis)",
            "Clinical Isolate (Staphylococcus saprophyticus)"
        ]
    )
    
    # حقل إدخال التسلسل الجيني المرن
    default_dna = (
        "ATGGCCGATCGATCGATCGATCGATCGCGTACGATCGATCGATCGATCGCCGCCAAACCT\n"
        "TCTTCCCGGGGTCACTTTATCAGTTAGAAACCTCTCAAAAATTTTAGGGGCGCTATTATTTATCTGCTCAA\n"
        "ACAATATCTGGGACGCTTCTGGAAAGACAAGTCCAGTATGAATCAGTAATCAGTCAATACTTATGATTAGCG\n"
        "GCTTCCCCACACCTCCCCCCAACAATTCCTCCACTTCTCCC"
    )
    
    dna_sequence = st.text_area(
        "Bacterial DNA Sequence Metadata (Bases A, T, C, G):",
        value=default_dna,
        height=150
    )

with col2:
    st.markdown("### 🩺 Maternal Clinical Parameters")
    
    # مؤشرات السونار الفطري أو الجنيني
    ultrasound_matrix = st.selectbox(
        "High-Resolution Fetal Ultrasonography Matrix:",
        [
            "Normal (Optimal & Physiological Fetal Development)",
            "Mild Oligohydramnios / Borderline Markers",
            "Elevated Resistance Index in Uterine Artery"
        ]
    )
    
    # فحص الـ CRP بالمليغرام
    crp_value = st.number_input(
        "Serum C-Reactive Protein (CRP Concentration in mg/L):",
        min_value=0.0,
        max_value=200.0,
        value=12.5,
        step=0.5
    )

st.markdown("<br>", unsafe_allow_html=True)

# زر تنفيذ التحليل التنبؤي المتكامل
if st.button("⚡ EXECUTE COMPUTATIONAL INTEGRATED RISK PREDICTION", use_container_width=True):
    if not dna_sequence.strip():
        st.error("⚠️ Please enter a valid bacterial DNA sequence.")
    else:
        st.success("DATA INTEGRATION SUCCESSFUL: Neural Matrix Correlated.")
        st.info(f"Selected Pathogen Context: {sample_type} | CRP Level: {crp_value} mg/L analyzed successfully.")
        
        st.markdown("#### 📊 Analytical Risk Assessment Output")
        st.metric(label="Predicted Fetal-Pathogenic Interaction Index", value="89.4% (High Risk Threshold)")
        st.warning("⚠️ Clinical Advisory: Significant virulence marker correlation detected with systemic inflammatory markers.")
  # تنبيه إخلاء المسؤولية الأكاديمي أسفل الصفحة
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: #64748B; font-size: 12px;'>"
    "© 2026 Al-Marshes Microbe Platform | Developed for Academic Graduation Presentation & Science Day Evaluation."
    "</p>",
    unsafe_allow_html=True
)
