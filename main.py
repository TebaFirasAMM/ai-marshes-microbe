import streamlit as st
import re

# Page Configuration
st.set_page_config(
    page_title="AI-Marshes Microbe - Academic Dashboard",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Academic Royal Green & Clean Styling (Enlarged Fonts & Emojis)
st.markdown("""
    <style>
    /* Global Clean Academic Background */
    .stApp {
        background-color: #f4f6f8;
        color: #1e293b;
        font-size: 18px;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #e2e8f0;
    }
    section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] .stMarkdown {
        font-size: 17px !important;
        font-weight: 600 !important;
        color: #064e3b !important;
    }
    
    /* Elegant Academic Cards */
    .academic-card {
        background-color: #ffffff;
        border: 1px solid #cbd5e1;
        padding: 30px;
        border-radius: 16px;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.08);
        margin-bottom: 25px;
    }
    
    /* Royal Green Button Styling */
    .stButton>button {
        background: linear-gradient(135deg, #065f46 0%, #047857 100%);
        color: #ffffff;
        font-weight: 700;
        width: 100%;
        border-radius: 10px;
        padding: 15px;
        font-size: 18px;
        border: none;
        box-shadow: 0 6px 15px rgba(6, 95, 70, 0.25);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #047857 0%, #064e3b 100%);
        box-shadow: 0 8px 20px rgba(6, 95, 70, 0.4);
    }
    
    /* Enlarged Headings & Text */
    h1 {
        color: #064e3b !important;
        font-size: 36px !important;
        font-weight: 800 !important;
    }
    h2, h3 {
        color: #065f46 !important;
        font-weight: 700 !important;
    }
    p, li, span {
        font-size: 17px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Control Panel (Enlarged Emojis & Text)
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #064e3b;'>🎛️ لوحة التحكم المختبري</h2>", unsafe_allow_html=True)
    st.markdown("<hr style='border-color: #cbd5e1;'>", unsafe_allow_html=True)
    
    patient_category = st.selectbox(
        "👤 فئة المريض (Patient Category):",
        ["اختر الفئة...", "🤰 امرأة حامل (Pregnant)", "👶 الأطفال والمراهقين (Pediatrics)", "🧑 بالغين / عام (Adults)"]
    )
    
    sample_type = st.selectbox(
        "🧪 نوع العينة (Sample Type):",
        ["اختر العينة...", "💧 عينة بول (Urine)", "🩸 عينة دم (Blood)", "🧬 مسحة مهبلية (Vaginal Swab)", "🩹 مسحة جروح (Wound Swab)"]
    )
    
    pathogen = st.selectbox(
        "🦠 الممرض المكتشف (Matched Pathogen):",
        [
            "اختر الممرض...",
            "Escherichia coli (UTI & Enteric)",
            "Pseudomonas aeruginosa (Marshes & Wounds)",
            "Vibrio cholerae (River & Marshes Water)",
            "Klebsiella pneumoniae (Respiratory)",
            "No Pathogenic Bacteria Detected (Normal)"
        ]
    )
    
    gene_sequence = st.text_input(
        "🔬 التسلسل الجيني (Gene Sequence A, T, C, G):",
        value="ATGCGATCGATCGATC"
    )
    
    crp_input = st.number_input(
        "📊 مستوى بروتين التفاعل C (CRP mg/L - الطبيعي < 5):",
        min_value=0.0, step=0.1, value=2.0
    )
    
    wbc_input = st.number_input(
        "🩸 تعداد كريات الدم البيضاء (WBC cells/μL):",
        min_value=0.0, step=100.0, value=7000.0
    )

    ultrasound = st.selectbox(
        "🩺 حالة السونار أو التصوير (Ultrasound Status):",
        ["طبيعي / صافي (Normal / Clear)", "غير طبيعي / تغيرات مرضية (Abnormal / Pathological)"]
    )

    st.markdown("<br>", unsafe_allow_html=True)
    run_btn = st.button("🚀 تشغيل التحليل الذكي")
    # Main Dashboard Area
st.markdown("<h1 style='text-align: center;'>🧬 منصة أبحاث الأحياء المجهرية والأهوار</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; font-size: 19px; font-weight: 500;'>منصة التشخيص الأكاديمي المتقدم للمخاطر الميكروبية وتحليلات النظام البيئي</p>", unsafe_allow_html=True)
st.markdown("<hr style='border-color: #cbd5e1; margin-top: 25px; margin-bottom: 30px;'>", unsafe_allow_html=True)

if not run_btn:
    # Initial State Card
    st.markdown("""
        <div class='academic-card' style='text-align: center; border: 2px dashed #94a3b8; padding: 50px;'>
            <h3 style='color: #065f46;'>⏳ النظام في وضع الاستعداد بانتظار المدخلات</h3>
            <p style='color: #475569; font-size: 18px;'>يرجى إدخال بيانات المريض والمؤشرات المخبرية من <b>لوحة التحكم الجانبية على اليسار</b>، ثم الضغط على زر <b>'تشغيل التحليل الذكي'</b> لتوليد التقرير الأكاديمي المفصل.</p>
        </div>
    """, unsafe_allow_html=True)

else:
    clean_seq = gene_sequence.strip().upper()
    valid_dna_pattern = re.compile("^[ATCG]+$")
    
    if "اختر" in patient_category or "اختر" in sample_type or "اختر" in pathogen:
        st.error("❌ يرجى اختيار كافة الحقول المطلوبة من لوحة التحكم الجانبية قبل تشغيل التحليل.")
    elif len(clean_seq) < 5 or not valid_dna_pattern.match(clean_seq):
        st.error("⚠️ خطأ في التسلسل الجيني: يجب أن يحتوي فقط على النيوكليوتيدات الصالحة (A, T, C, G).")
    else:
        # Risk Score Calculation Logic
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
            
        if "حامل" in patient_category or "الأطفال" in patient_category:
            risk_score += 10
            
        if "No Pathogenic" in pathogen and crp_input < 5 and wbc_input <= 11000:
            risk_score = 8  
            
        if risk_score > 98:
            risk_score = 98
        elif risk_score < 5:
            risk_score = 5
            
        # Results Section inside Academic Cards
        st.markdown("<h3 style='margin-bottom: 20px;'>📋 تقرير التقييم التشخيصي والأكاديمي</h3>", unsafe_allow_html=True)
        
        col_r1, col_r2 = st.columns([1, 2])
        
        with col_r1:
            st.metric(label="معدل الخطورة المحسوب (Risk Rate)", value=f"{risk_score}%", delta="حالة حرجة" if risk_score >= 70 else "حالة مستقرة")
            
        with col_r2:
            if risk_score < 30:
                st.success(f"🟢 حالة آمنة وتحت السيطرة (معدل الخطورة: {risk_score}%)")
            elif 30 <= risk_score < 70:
                st.warning(f"🟡 تنبيه متوسط - خطر محتمل يتطلب المتابعة (معدل الخطورة: {risk_score}%)")
            else:
                st.error(f"🔴 تحذير عالي الخطورة - يتطلب تدخلاً طبياً فورياً (معدل الخطورة: {risk_score}%)")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Detailed Summary Card
        st.markdown(f"""
        <div class='academic-card'>
            <h3 style='color: #065f46; margin-top: 0; margin-bottom: 20px;'>🔬 الملخص المخبري الإكلينيكي الشامل</h3>
            <ul style='color: #334155; line-height: 2.2;'>
                <li><b>تصنيف المريض:</b> <span style='color: #0f172a; font-weight: 600;'>{patient_category}</span> | <b>نوع العينة:</b> <span style='color: #0f172a; font-weight: 600;'>{sample_type}</span></li>
                <li><b>الممرض المحدد:</b> <span style='color: #0f172a; font-weight: 600;'>{pathogen}</span></li>
                <li><b>مستويات المؤشرات الحيوية:</b> CRP: <code style='color: #047857; font-size: 18px;'>{crp_input} mg/L</code> | WBC: <code style='color: #047857; font-size: 18px;'>{wbc_input} cells/μL</code></li>
                <li><b>التوصية العلاجية الأكاديمية:</b> <b style='color: #064e3b;'>{"يجب التدخل الطبي العاجل ووصف العلاج المضاد للميكروبات المناسب فوراً." if risk_score >= 70 else "حالة المريض مستقرة؛ يوصى بالمتابعة الدورية وجدولة الفحوصات الاحترازية."}</b></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
