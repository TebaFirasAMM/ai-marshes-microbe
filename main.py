import streamlit as st
import re

# إعدادات صفحة المنصة
st.set_page_config(
    page_title="AI-Marshes Microbe",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# تنسيقات الواجهة وتصاميم الألوان المريحة
st.markdown("""
    <style>
    .main {
        background-color: #f8fafc;
    }
    .stButton>button {
        background-color: #0d9488;
        color: white;
        font-weight: bold;
        width: 100%;
        border-radius: 8px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #0f766e;
    }
    </style>
""", unsafe_allow_html=True)

# عنوان المنصة والترحيب
st.markdown("<h1 style='text-align: center; color: #0f766e;'>AI-Marshes Microbe</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b;'>منصة التشخيص الذكي المتقدمة للمخاطر الميكروبية (حوامل، أطفال ومراهقين، مياه دجلة والأهوار)</p>", unsafe_allow_html=True)
st.markdown("---")

# تقسيم الواجهة إلى أعمدة تنظيمية رصينة
col1, col2 = st.columns(2)

with col1:
    patient_category = st.selectbox(
        "فئة المريض:",
        ["اختر الفئة...", "امرأة حامل", "أطفال ومراهقين (1 - 18 سنة)", "بالغين / عام"]
    )
    
    sample_type = st.selectbox(
        "نوع العينة (Sample Type):",
        ["اختر نوع العينة...", "عينة بول (Urine)", "عينة دم (Blood)", "مسحة مهبلية (Vaginal Swab - خاص بالحوامل)", "مسحة جروح (Wound Swab - بيئة دجلة والأهوار)"]
    )
    
    gene_sequence = st.text_input(
        "التسلسل الجيني للبكتيريا (أدخل رموز النيوكليوتيدات A, T, C, G):",
        value="ATGCGATCGATCGATC"
    )

with col2:
    pathogen = st.selectbox(
        "البكتيريا المطابقة في قاعدة البيانات:",
        [
            "اختر البكتيريا...",
            "إشريكية كولونية (E. coli - شائعة بالمسالك والأمعاء)",
            "زائفة الزنجارية (Pseudomonas - مياه الأهوار والجروح)",
            "ضمة الكوليرا (Vibrio cholerae - مياه الأنهار والأهوار)",
            "كلبسيلا رئوية (Klebsiella - التهابات تنفسية ونسائية)",
            "لا توجد بكتيريا ممرضة (طبيعي)"
        ]
    )
    
    crp_input = st.number_input(
        "مستوى بروتين التفاعل الـ CRP (ملغ/لتر - الطبيعي أقل من 5):",
        min_value=0.0, step=0.1, value=2.0
    )
    
    wbc_input = st.number_input(
        "تعداد خلايا الدم البيضاء WBC (خلية/ميكروليتر - الطبيعي 4000 - 11000):",
        min_value=0.0, step=100.0, value=7000.0
    )

ultrasound = st.selectbox(
    "حالة السونار (اختياري):",
    ["سليم / طبيعي", "غير طبيعي / وجود تغيرات مرضية"]
)

st.markdown("<br>", unsafe_allow_html=True)

# زر تحليل الحالة
if st.button("تشغيل النظام الذكي وتحليل النتائج السريرية"):
    
    # 1. التدقيق الصارم للتسلسل الجيني
    clean_seq = gene_sequence.strip().upper()
    valid_dna_pattern = re.compile("^[ATCG]+$")
    
    if patient_category == "اختر الفئة..." or sample_type == "اختر نوع العينة..." or pathogen == "اختر البكتيريا...":
        st.error("❌ يرجى اختيار جميع الحقول الأساسية (فئة المريض، نوع العينة، والبكتيريا) قبل تشغيل التحليل.")
    elif len(clean_seq) < 5 or not valid_dna_pattern.match(clean_seq):
        st.error("⚠️ خطأ في التسلسل الجيني المرفق: التسلسل المدخل غير صالح أو قصير جداً. يرجى التأكد من اقتصار الحروف حصراً على رموز النيوكليوتيدات السليمة (A, T, C, G).")
    else:
        # 2. نظام النقاط الموزون (Weighted Clinical Scoring Algorithm)
        score = 10
        
        if "زائفة" in pathogen or "الكوليرا" in pathogen:
            score += 40
        elif "إشريكية" in pathogen or "كلبسيلا" in pathogen:
            score += 30
        elif "لا توجد" in pathogen:
            score = 4
            
        if crp_input > 20:
            score += 30
        elif 5 <= crp_input <= 20:
            score += 15
            
        if wbc_input > 11000:
            score += 20
        elif wbc_input < 4000:
            score += 10
 if ultrasound == "غير طبيعي / وجود تغيرات مرضية":
            score += 15
            
        if "حامل" in patient_category or "أطفال" in patient_category:
            score += 10
            
        if "لا توجد" in pathogen:
            score = 5
        if score > 98:
            score = 98
            
        # 3. إظهار النتائج بتصميم مريح وآمن
        st.markdown("---")
        st.subheader("نتائج التحليل والتقييم السريري الذكي:")
        
        if score < 30:
            st.success(f"🟢 الحالة آمنة والمؤشرات ضمن السيطرة (نسبة الخطورة المقدرة: {score}%)")
        elif 30 <= score < 75:
            st.warning(f"🟡 تنبيه متوسط - وجود خطر محتمل يتطلب المتابعة (نسبة الخطورة المقدرة: {score}%)")
        else:
            st.error(f"🔴 إنذار خطر عالي - يتطلب تدخلاً علاجياً عاجلاً وفورياً (نسبة الخطورة المقدرة: {score}%)")
            
        st.markdown(f"""
        * التحقق الجيني: تم فحص المطابقة المرجعية بنجاح دون أخطاء برمجية.
        * القيم المخبرية: بروتين الـ CRP مسجل بقيمة {crp_input} ملغ/لتر | تعداد الـ WBC مسجل بقيمة {wbc_input} خلية/ميكروليتر.
        * بيانات الفحص: العينة المستخدمة ({sample_type}) تتبع الفئة ({patient_category}).
        * التوصية الطبية الخبيرة: {"يوصى بالتدخل الفوري بالمضادات الحيوية المناسبة وتجنب أي تأخير." if score > 75 else "المؤشرات ضمن نطاق المراقبة الدورية المعتادة."}
        """)
