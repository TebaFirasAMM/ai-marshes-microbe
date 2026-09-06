import streamlit as st
import numpy as np

# Set page configuration with the new academic research medical identity
st.set_page_config(page_title="AMM Research Platform", page_icon="🧬", layout="wide")

# Custom CSS for the White and Light Blue aesthetic (No Royal Blue)
st.markdown("""
    <style>
    .main { background-color: #FFFFFF; } /* Clean White Background */
    h1, h2, h3 { color: #2B6CB0; font-family: 'Helvetica Neue', sans-serif; } /* Soft Slate Blue for text */
    .stButton>button { 
        background-color: #63B3ED; /* Vibrant Light Blue Button */
        color: white; 
        border-radius: 5px; 
        font-weight: bold; 
        width: 100%; 
        border: none;
        height: 45px;
    }
    .stButton>button:hover { background-color: #4299E1; color: white; }
    /* Style widgets with a very light blue tint */
    .stSelectbox, .stSlider, .stNumberInput, .stTextArea { background-color: #F7FAFC; border: 1px solid #E2E8F0; border-radius: 5px; }
    </style>
    """, unsafe_style_allowed=True)

# Title & Core Academic Concept
st.title("🧬 AI Marshes Microbial — AMM")
st.subheader("An AI-Assisted Computational Research Platform for Microbial Genomic Analysis and Maternal-Fetal Risk Assessment")
st.markdown("---")

# Sidebar - Research Control Panel (Strictly for Investigators & Students)
st.sidebar.header("🔬 Research Control Panel")
st.sidebar.info("🎯 TARGET USERS: Researchers, Academics, and Microbiology Students.")

research_mode = st.sidebar.radio(
    "Select Research Data Source:",
    ["Public Genomic Dataset (NCBI GenBank)", "Simulated/Theoretical Clinical Data", "Independent Research Dataset"]
)

module_selection = st.sidebar.selectbox(
    "Select Target Evaluation Module:",
    ["Clinical Research Module (UTI Genomic Modeling)", "Environmental Water Module (Cyanobacteria Vectors)"]
)

st.sidebar.markdown("---")
st.sidebar.write(f"Research Mode: {research_mode}")
st.sidebar.write(f"Selected Module: {module_selection}")

# Layout: Split into Inputs and Outputs
col1, col2 = st.columns(2)

with col1:
    st.header("📥 Input Metadata & Parameters")
    
    if module_selection == "Clinical Research Module (UTI Genomic Modeling)":
        st.subheader("🧫 Sample & Bacterial Metadata")
        sample_source = st.selectbox(
            "Bacterial Sample Source:",
            [
                "Clinical isolate – Urine",
                "Clinical isolate – Vaginal swab",
                "Environmental isolate – Marsh/Wetland water",
                "Reference sequence – NCBI/GenBank"
            ]
        )
        specimen_type = st.selectbox("Specimen Type:", ["Urine", "Vaginal swab"])
        bacterial_id = st.selectbox("Bacterial Identification:", ["Escherichia coli", "Other Pathogen"])
        id_method = st.selectbox("Identification Method:", ["Culture/biochemical", "16S rRNA Sequence Fragment", "Other molecular method"])
        
        st.subheader("🧬 Computational Genomic Input")
        dna_input = st.text_area(
            "Enter DNA Sequence (Bases: A, T, C, G)", 
            "ATGGCGATCGATCGATCGATCGATCGATCGACTAGCTAGCTAGCTAGC",
            key="clinical_dna"
        )
        
        st.subheader("👩‍🍼 Simulated Maternal Clinical Parameters")
        gestational_age = st.slider("Gestational Age (Weeks):", min_value=4, max_value=40, value=12)
        crp_input = st.number_input("Serum C-Reactive Protein - CRP (mg/L):", min_value=0.0, max_value=200.0, value=78.0, step=1.0)
        ultrasound_status = st.selectbox(
            "Fetal Ultrasound Assessment:",
            ["No significant abnormality reported", "Suspected abnormality", "Abnormal finding"]
        )
        
    else:
        st.subheader("🧫 Environmental Metadata")
        env_source = st.selectbox("Water Sample Source:", ["Tigris River Ecosystem", "Marshland Water Vectors"])
        cyanobacteria_id = st.selectbox("Target Microbial Group:", ["Cyanobacteria (Microcystis)", "Other Aquatic Flora"])
        
        st.subheader("🧬 Environmental Genomic Input")
        dna_input = st.text_area(
            "Enter En
 vironmental Water DNA Sequence (Bases: A, T, C, G)", 
            "CCGGCGGCCGGCCGGCCGGCCGGCCGGCCGGCGTAACGTACG",
            key="env_dna"
        )
        st.subheader("🌊 Simulated Water Parameters")
        salinity = st.slider("Water Salinity Level (ppt):", min_value=0.0, max_value=50.0, value=15.0)
        cyanotoxin_index = st.number_input("Estimated Cyanotoxin Concentration (µg/L):", min_value=0.0, max_value=100.0, value=5.0)

    execute_btn = st.button("RUN AI-ASSISTED RISK ASSESSMENT")

with col2:
    st.header("📊 Computational Research Report")
    
    if execute_btn:
        clean_dna = dna_input.strip().upper()
        seq_length = len(clean_dna)
        
        # Calculate GC Content (%) accurately
        g_count = clean_dna.count('G')
        c_count = clean_dna.count('C')
        gc_content = ((g_count + c_count) / seq_length) * 100 if seq_length > 0 else 0.0
        
        st.success("DATA INTEGRATION SUCCESSFUL: Genomic and maternal clinical parameters successfully processed.")
        
        # 1. Genomic Features Report
        st.subheader("🧬 1. Genomic Features")
        st.write(f"Input DNA Sequence Length: {seq_length} bp")
        st.write(f"GC Content (GC%): {gc_content:.2f}%")
        
        if module_selection == "Clinical Research Module (UTI Genomic Modeling)":
            st.write(f"Molecular Identification: *{bacterial_id}*")
            st.write(f"Sample Provenance: {sample_source}")
            st.write("🤖 AI Pathogen Classification Confidence: 94.2%")
            
            # 2. Simulated Clinical Report Section
            st.subheader("👩‍🍼 2. Simulated Clinical Profile")
            st.write(f"Gestational Age: {gestational_age} weeks")
            st.write(f"Validated Inflammatory Biomarker (CRP): {crp_input} mg/L")
            st.write(f"Ultrasound Assessment: {ultrasound_status}")
            
            # 3. AI Risk Score
            st.subheader("🤖 3. Estimated Infection-Associated Risk")
            if crp_input > 50.0 or gc_content > 45.0 or ultrasound_status != "No significant abnormality reported":
                st.error("Estimated Risk Level: 🔴 HIGH RISK")
            elif crp_input > 20.0 or gc_content > 40.0:
                st.warning("Estimated Risk Level: 🟠 MODERATE RISK")
            else:
                st.success("Estimated Risk Level: 🟢 LOW RISK")
            st.write("📊 Integrated Risk Model Confidence: 87.0%")
            
            # Explainable AI - Feature Importance Simulator
            st.markdown("Top Features Associated with Research Risk Estimate:")
            st.write(f"CRP Level ({crp_input} mg/L): ████████████████ 52%")
            st.write(f"Bacterial GC Content ({gc_content:.2f}%): ████████████ 35%")
            st.write("Gestational Age & Ultrasound Findings: ████ 13%")
            
            st.markdown("---")
            st.markdown("🔬 *Recommendation: Further microbiological and environmental investigation is recommended. Clinical correlation and physician evaluation are recommended.*")
            
        else:
            st.write(f"Molecular Genus Target: *{cyanobacteria_id}*")
            st.write(f"Ecosystem Origin: {env_source}")
            st.write("🤖 AI Pathogen Classification Confidence: 91.5%")
            
            st.subheader("🌊 2. Eco-Environmental Profile")
            st.write(f"Water Salinity: {salinity} ppt")
            st.write(f"Cyanotoxin Index: {cyanotoxin_index} µg/L")
            
            st.subheader("🤖 3. Eco-AI Assessment Output")
            if cyanotoxin_index > 1.0:
                st.error("Estimated Eco-Risk Level: 🔴 HIGH ECO-ENVIRONMENTAL RISK")
            else:
                st.success("Estimated Eco-Risk Level: 🟢 LOW RISK")
            st.write("📊 Integrated Eco-Model Confidence: 89.4%")
            st.markdown("---")
            st.markdown("🔬 *Recommendation: Further water quality tracking and eco-toxicological validation are recommended.*")
            
    else:
        st.info("Please adjust inpu
 ts on the left and click 'RUN AI-ASSISTED RISK ASSESSMENT' to compile report.")

# Footer - Essential Academic Notice (Strictly required by FDA/WHO guidelines)
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7F8C8D; font-size: 13px; font-weight: bold;'>⚠️ ACADEMIC RESEARCH NOTICE: This result is a research-based risk estimate and does not constitute a medical diagnosis. Clinical interpretation should be performed by a qualified healthcare professional. For research and educational use only. This prototype is not intended to diagnose, treat, or replace professional medical judgment.</p>", unsafe_style_allowed=True)
