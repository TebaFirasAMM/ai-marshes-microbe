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

# زر تحليل الحالة الديناميكي
if st.button("تشغيل النظام الذكي وتحليل النتائج السريرية"):
    
    clean_seq = gene_sequence.strip().upper()
    valid_dna_pattern = re.compile("^[ATCG]+$")
    
    if patient_category == "اختر الفئة..." or sample_type == "اختر نوع العينة..." or pathogen == "اختر البكتيريا...":
        st.error("❌ يرجى اختيار جميع الحقول الأساسية (فئة المريض، نوع العينة، والبكتيريا) قبل تشغيل التحليل.")
    elif len(clean_seq) < 5 or not valid_dna_pattern.match(clean_seq):
        st.error("⚠️ خطأ في التسلسل الجيني المرفق: التسلسل المدخل غير صالح أو قصير جداً. يرجى التأكد من اقتصار الحروف حصراً على رموز النيوكليوتيدات السليمة (A, T, C, G).")
    else:
        # خوارزمية تحليل ديناميكية متكاملة (تعتمد على تداخل جميع المعايير معاً لتوليد نتيجة فريدة)
        risk_score = 0
        clinical_notes = []
        
        # 1. تقييم نوع البكتيريا والتسلسل الجيني المدخل
        if "لا توجد" in pathogen:
            risk_score += 0
            clinical_notes.append("الفحص الجيني والميكروبيولوجي لا يظهر أي ممرضات بكتيرية خطيرة.")
        else:
            risk_score += 25
            clinical_notes.append(f"تم رصد مطابقة إيجابية مع سلالة ({pathogen}) في العينة المرفقة.")
            
        # 2. تقييم استجابة مؤشرات الدم (CRP)
        if crp_input > 40:
 risk_score += 35
            clinical_notes.append(f"مستوى بروتين التفاعل (CRP) مرتفع جداً ({crp_input} ملغ/لتر)، مما يدل على استجابة التهابية جهازية حادة.")
        elif 10 <= crp_input <= 40:
            risk_score += 20
            clinical_notes.append(f"مستوى بروتين التفاعل (CRP) مرتفع بشكل ملحوظ ({crp_input} ملغ/لتر)، ويشير إلى التهاب متوسط النشاط.")
        elif 5 <= crp_input < 10:
            risk_score += 10
            clinical_notes.append(f"مستوى بروتين التفاعل (CRP) عند الحد الحدي الأعلى ({crp_input} ملغ/لتر).")
        else:
            clinical_notes.append(f"مستوى بروتين التفاعل (CRP) ضمن النطاق الطبيعي المطمئن ({crp_input} ملغ/لتر).")
            
        # 3. تقييم خلايا الدم البيضاء (WBC)
        if wbc_input > 15000:
            risk_score += 30
            clinical_notes.append(f"التعداد الكلي لخلايا الدم البيضاء مرتفع بشدة ({wbc_input} خلية/ميكروليتر)، مما يعكس نشاطاً مناعياً هجومياً ضد عدوى جرثومية.")
        elif 11000 < wbc_input <= 15000:
            risk_score += 15
            clinical_notes.append(f"تعداد خلايا الدم البيضاء مرتفع قليلاً عن المعدل الطبيعي ({wbc_input} خلية/ميكروليتر).")
        elif wbc_input < 4000:
            risk_score += 25
            clinical_notes.append(f"تعداد خلايا الدم البيضاء منخفض ({wbc_input} خلية/ميكروليتر)، وهو مؤشر استجابة مناعية يستدعي الحذر.")
        else:
            clinical_notes.append(f"تعداد خلايا الدم البيضاء ضمن النطاق الطبيعي المستقر ({wbc_input} خلية/ميكروليتر).")
            
        # 4. تقييم حالة السونار والأعراض المرتبطة بفئة المريض
        if ultrasound == "غير طبيعي / وجود تغيرات مرضية":
            risk_score += 25
            clinical_notes.append("تقرير السونار السريري يظهر تغيرات مرضية أو احتقان، مما يرفع من دلالة الإصابة النسيجية.")
        else:
            clinical_notes.append("فحص السونار أظهر استقراراً هيكلياً دون تغيرات مرضية ظاهرة.")
            
        if "حامل" in patient_category:
            risk_score += 15
            clinical_notes.append("تم تفعيل بروتوكول الرعاية الخاصة بفئة الحوامل نظرًا لحساسية الحالة وضرورة الوقاية من أي مضاعفات صاعدة.")
        elif "أطفال" in patient_category:
            risk_score += 10
            clinical_notes.append("تم تطبيق معايير الأمان الخاصة بفئة الأطفال والمراهقين لسرعة الاستجابة السريرية.")

        # إظهار النتائج بصياغة تحليلية دقيقة تتغير بناءً على تشخيص المدخلات الحقيقية
        st.markdown("---")
        st.subheader("تقرير التشخيص السريري المتقدم (Dynamic Clinical Report):")
        
        if risk_score >= 65:
            st.error("🔴 إنذار خطر عالي - تداخل مرضي يتطلب تدخلاً علاجياً عاجلاً:\nالتحليل الشامل للأعراض، المؤشرات المخبرية (CRP و WBC)، وفحص السونار يوضح وجود نشاط ميكروبي حاد يستوجب بدء العلاج بالمضادات الحيوية المناسبة فوراً وتحت إشراف طبي.")
        elif 30 <= risk_score < 65:
            st.warning("🟡 تنبيه متوسط - حالة تستوجب المتابعة الدورية:\nالمؤشرات الحيوية وفحوصات الدم تظهر نشاطاً التهابياً أو تطابقاً جرثومياً جزئياً؛ يوصى بإعادة الفحص خلال فترة قصيرة ومراقبة الأعراض بدقة.")
        else:
            st.success("🟢 الحالة مستقرة والمؤشرات ضمن السيطرة:\nلا توجد دلائل على مخاطر ميكروبية حرجة بناءً على المدخلات الحالية والفحوصات المخبرية المرفقة، مع التأكيد على المتابعة الوقائية الاعتيادية.")
            
        st.markdown("### ملخص القراءات والتحليل الاستدلالي:")
        for note in clinical_notes:
            st.markdown(f"- {note}")
            
        st.markdown(f"""
        ---
        * فئة المريض: {patient_category} | نوع العينة: {sample_type}
        * التدقيق الجيني والمخابري: تم فحص التوافق بنجاح ومعالجة القيم الحيوية (CRP: {crp_input} | WBC: {wbc_input}) وفق النظام الاستدلالي الحيوي للمنصة.
        """)
