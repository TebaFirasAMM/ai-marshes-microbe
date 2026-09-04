import streamlit as st
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder


# ============================================================
# AMM - AI Marshes Microbial
# AI-Assisted Microbial Genomic Analysis and Maternal-Fetal
# Risk Assessment
# Research / Educational Prototype
# ============================================================


st.set_page_config(
    page_title="AMM - AI Marshes Microbial",
    page_icon="🧬",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title("🧬 AI Marshes Microbial (AMM)")
st.caption(
    "AI-Assisted Computational Platform for Microbial Genomic "
    "Analysis and Maternal-Fetal Risk Assessment"
)

st.info(
    "⚠️ Research and educational prototype only. "
    "This system is not a clinical diagnostic device and does not "
    "replace professional medical judgment."
)


# ============================================================
# FUNCTIONS
# ============================================================

def clean_sequence(sequence):
    """
    Clean DNA sequence and keep only valid nucleotides.
    """
    sequence = sequence.upper().replace(" ", "")
    sequence = sequence.replace("\n", "")
    sequence = sequence.replace("\r", "")

    valid = set("ATGCN")

    cleaned = "".join(
        nucleotide for nucleotide in sequence
        if nucleotide in valid
    )

    return cleaned


def calculate_sequence_features(sequence):
    """
    Calculate basic genomic features.
    """

    sequence = clean_sequence(sequence)

    length = len(sequence)

    if length == 0:
        return None

    A = sequence.count("A")
    T = sequence.count("T")
    G = sequence.count("G")
    C = sequence.count("C")
    N = sequence.count("N")

    gc_content = ((G + C) / length) * 100

    return {
        "sequence": sequence,
        "length": length,
        "A": A,
        "T": T,
        "G": G,
        "C": C,
        "N": N,
        "A_percent": (A / length) * 100,
        "T_percent": (T / length) * 100,
        "G_percent": (G / length) * 100,
        "C_percent": (C / length) * 100,
        "GC_content": gc_content
    }


def sequence_to_features(sequence, k=2):
    """
    Convert DNA sequence into k-mer frequency features.

    This can later be used as input to a real ML classifier.
    """

    sequence = clean_sequence(sequence)

    nucleotides = ["A", "T", "G", "C"]

    kmers = [
        a + b
        for a in nucleotides
        for b in nucleotides
    ]

    features = {}

    for kmer in kmers:
        features[kmer] = 0

    for i in range(len(sequence) - k + 1):

        kmer = sequence[i:i+k]

        if kmer in features:
            features[kmer] += 1

    total = sum(features.values())

    if total > 0:

        for kmer in features:
            features[kmer] /= total

    return features


# ============================================================
# DEMONSTRATION ML MODEL
# ============================================================

def build_demo_microbial_model():

    """
    Demonstration model architecture.

    IMPORTANT:
    The data below are synthetic examples ONLY.
    They must NOT be presented as clinical validation.
    """

    training_sequences = [
        "ATGCGCGATCGCGATCGCGATCG",
        "ATGCGATCGATCGATCGATCGAT",
        "AATTATTAATTAATTATTAATTA",
        "AATTAATTAATTATTAATTAATT",
        "ATGCCGATGCCGATGCCGATGCC",
        "AATATTAATATTAATATTAATAT"
    ]

    labels = [
        "Example_Bacterium_A",
        "Example_Bacterium_A",
        "Example_Bacterium_B",
        "Example_Bacterium_B",
        "Example_Bacterium_C",
        "Example_Bacterium_C"
    ]

    X = []

    for seq in training_sequences:

        features = sequence_to_features(seq)

        X.append(
            list(features.values())
        )

    X = np.array(X)

    encoder = LabelEncoder()

    y = encoder.fit_transform(labels)
model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(X, y)

    return model, encoder


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("⚙️ AMM Input Panel")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Clinical Microbiology",
        "Environmental Cyanobacteria"
    ]
)


# ============================================================
# CLINICAL MODULE
# ============================================================

if module == "Clinical Microbiology":

    st.header("🧫 Clinical Microbiology Module")

    st.write(
        "Enter a bacterial DNA sequence obtained from a clinical "
        "sample such as urine or vaginal swab."
    )

    sequence_input = st.text_area(
        "🧬 Bacterial DNA Sequence",
        placeholder="Example: ATGCGATCGATCGATCG..."
    )

    st.subheader("🤰 Maternal Clinical Information")

    col1, col2, col3 = st.columns(3)

    with col1:

        gestational_age = st.number_input(
            "Gestational Age (weeks)",
            min_value=1.0,
            max_value=45.0,
            value=20.0,
            step=0.1
        )

    with col2:

        crp_input = st.number_input(
            "Maternal CRP (mg/L)",
            min_value=0.0,
            max_value=500.0,
            value=5.0,
            step=0.1
        )

    with col3:

        ultrasound_status = st.selectbox(
            "Ultrasound Assessment",
            [
                "Normal",
                "Abnormal",
                "Not Available"
            ]
        )

    execute = st.button(
        "🚀 EXECUTE AMM ANALYSIS",
        type="primary"
    )


    # ========================================================
    # EXECUTION
    # ========================================================

    if execute:

        if not sequence_input.strip():

            st.warning(
                "Please enter a DNA sequence before running the analysis."
            )

        else:

            sequence_features = calculate_sequence_features(
                sequence_input
            )

            if sequence_features is None:

                st.error(
                    "No valid DNA sequence was detected."
                )

            else:

                # ====================================================
                # SECTION 1 - GENOMIC ANALYSIS
                # ====================================================

                st.subheader(
                    "🧬 1. Microbial Genomic Analysis"
                )

                col1, col2, col3, col4 = st.columns(4)

                with col1:

                    st.metric(
                        "Sequence Length",
                        f"{sequence_features['length']} bp"
                    )

                with col2:

                    st.metric(
                        "GC Content",
                        f"{sequence_features['GC_content']:.2f}%"
                    )

                with col3:

                    st.metric(
                        "Adenine (A)",
                        f"{sequence_features['A_percent']:.2f}%"
                    )

                with col4:

                    st.metric(
                        "Guanine (G)",
                        f"{sequence_features['G_percent']:.2f}%"
                    )


                st.write("### Nucleotide Composition")

                composition = pd.DataFrame(
                    {
                        "Nucleotide": [
                            "A",
                            "T",
                            "G",
                            "C",
                            "N"
                        ],
 "Count": [
                            sequence_features["A"],
                            sequence_features["T"],
                            sequence_features["G"],
                            sequence_features["C"],
                            sequence_features["N"]
                        ]
                    }
                )

                st.dataframe(
                    composition,
                    use_container_width=True,
                    hide_index=True
                )


                # ====================================================
                # SECTION 2 - MICROBIAL AI CLASSIFICATION
                # ====================================================

                st.subheader(
                    "🤖 2. Microbial AI Classification"
                )

                model, encoder = build_demo_microbial_model()

                sequence_ml_features = sequence_to_features(
                    sequence_features["sequence"]
                )

                X_input = np.array(
                    [
                        list(
                            sequence_ml_features.values()
                        )
                    ]
                )

                prediction = model.predict(
                    X_input
                )[0]

                probabilities = model.predict_proba(
                    X_input
                )[0]

                predicted_label = encoder.inverse_transform(
                    [prediction]
                )[0]

                confidence = probabilities[prediction] * 100


                st.write(
                    f"Predicted Class: "
                    f"{predicted_label}"
                )

                st.write(
                    f"Model Classification Probability: "
                    f"{confidence:.2f}%"
                )

                st.caption(
                    "⚠️ The current classifier uses synthetic demonstration "
                    "training data. It is not clinically validated and "
                    "must be replaced with a properly curated microbial "
                    "sequence dataset for research conclusions."
                )


                # ====================================================
                # FEATURE IMPORTANCE
                # ====================================================

                st.write(
                    "### 🔍 Model Feature Importance"
                )

                feature_names = list(
                    sequence_ml_features.keys()
                )

                importance_df = pd.DataFrame(
                    {
                        "Feature": feature_names,
                        "Importance": model.feature_importances_
                    }
                )

                importance_df = importance_df.sort_values(
                    "Importance",
                    ascending=False
                )

                st.dataframe(
                    importance_df.head(10),
                    use_container_width=True,
                    hide_index=True
                )


                # ====================================================
                # SECTION 3 - MATERNAL INFORMATION
                # ====================================================

                st.subheader(
                    "🤰 3. Maternal Clinical Information"
                )

                clinical_data = pd.DataFrame(
                    {
                        "Parameter": [
                            "Gestational Age",
                            "Maternal CRP",
                            "Ultrasound Assessment"
                        ],

                        "Value": [
                            f"{gestational_age:.1f} weeks",
                            f"{crp_input:.2f} mg/L",
                            ultrasound_status
                        ]
                    }
                )

st.dataframe(
                    clinical_data,
                    use_container_width=True,
                    hide_index=True
                )


                # ====================================================
                # SECTION 4 - COMPUTATIONAL RISK ASSESSMENT
                # ====================================================

                st.subheader(
                    "📊 4. Integrated Computational Risk Assessment"
                )

                st.write(
                    "This section provides a research-oriented "
                    "computational assessment. It is not a validated "
                    "clinical prediction model."
                )


                # ----------------------------------------------------
                # Research indicators
                # ----------------------------------------------------

                risk_indicators = []

                if crp_input > 10:

                    risk_indicators.append(
                        "CRP is above the selected research threshold."
                    )

                if ultrasound_status == "Abnormal":

                    risk_indicators.append(
                        "Abnormal ultrasound assessment was reported."
                    )

                if ultrasound_status == "Not Available":

                    risk_indicators.append(
                        "Ultrasound information is unavailable."
                    )


                # ----------------------------------------------------
                # Risk category
                # ----------------------------------------------------

                indicator_count = len(
                    risk_indicators
                )

                if indicator_count >= 2:

                    risk_category = "HIGH COMPUTATIONAL RISK"

                    st.error(
                        f"🔴 {risk_category}"
                    )

                elif indicator_count == 1:

                    risk_category = "MODERATE COMPUTATIONAL RISK"

                    st.warning(
                        f"🟠 {risk_category}"
                    )

                else:

                    risk_category = "LOW COMPUTATIONAL RISK"

                    st.success(
                        f"🟢 {risk_category}"
                    )


                # ----------------------------------------------------
                # Indicators
                # ----------------------------------------------------

                st.write(
                    "### Contributing Research Indicators"
                )

                if risk_indicators:

                    for indicator in risk_indicators:

                        st.write(
                            f"• {indicator}"
                        )

                else:

                    st.write(
                        "• No predefined research indicators were triggered."
                    )


                st.caption(
                    "Important: The risk category above is a "
                    "computational prototype based on predefined "
                    "research criteria. It does not predict miscarriage "
                    "and must not be used for patient management."
                )


                # ====================================================
                # FINAL REPORT
                # ====================================================

                st.subheader(
                    "📋 5. AMM Computational Report"
                )

                report = {
                    "Sequence Length": (
                        f"{sequence_features['length']} bp"
                    ),

                    "GC Content": (
                        f"{sequence_features['GC_content']:.2f}%"
                    ),

                    "Predicted Microbial Class": (
                        predicted_label
                    ),
 "Classification Probability": (
                        f"{confidence:.2f}%"
                    ),

                    "Gestational Age": (
                        f"{gestational_age:.1f} weeks"
                    ),

                    "CRP": (
                        f"{crp_input:.2f} mg/L"
                    ),

                    "Ultrasound": (
                        ultrasound_status
                    ),

                    "Computational Risk": (
                        risk_category
                    )
                }

                report_df = pd.DataFrame(
                    list(report.items()),
                    columns=[
                        "Parameter",
                        "Result"
                    ]
                )

                st.dataframe(
                    report_df,
                    use_container_width=True,
                    hide_index=True
                )


# ============================================================
# ENVIRONMENTAL CYANOBACTERIA MODULE
# ============================================================

else:

    st.header(
        "🌊 Environmental Cyanobacteria Module"
    )

    st.write(
        "This module is separated from the clinical UTI workflow "
        "and is intended for environmental water/marsh research."
    )

    water_sequence = st.text_area(
        "🧬 Environmental DNA Sequence",
        placeholder="Enter environmental microbial DNA sequence..."
    )

    col1, col2 = st.columns(2)

    with col1:

        salinity = st.number_input(
            "Water Salinity (ppt)",
            min_value=0.0,
            max_value=100.0,
            value=1.0
        )

    with col2:

        cyanotoxin_index = st.number_input(
            "Measured Cyanotoxin Concentration (µg/L)",
            min_value=0.0,
            max_value=10000.0,
            value=0.0
        )


    environmental_execute = st.button(
        "🌊 EXECUTE ENVIRONMENTAL ANALYSIS",
        type="primary"
    )


    if environmental_execute:

        if not water_sequence.strip():

            st.warning(
                "Please enter an environmental DNA sequence."
            )

        else:

            environmental_features = calculate_sequence_features(
                water_sequence
            )

            if environmental_features is None:

                st.error(
                    "No valid DNA sequence detected."
                )

            else:

                # ====================================================
                # ENVIRONMENTAL GENOMIC ANALYSIS
                # ====================================================

                st.subheader(
                    "🧬 1. Environmental Genomic Analysis"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Sequence Length",
                        f"{environmental_features['length']} bp"
                    )

                with col2:

                    st.metric(
                        "GC Content",
                        f"{environmental_features['GC_content']:.2f}%"
                    )


                # ====================================================
                # ENVIRONMENTAL DATA
                # ====================================================

                st.subheader(
                    "🌊 2. Environmental Profile"
                )

                environmental_data = pd.DataFrame(
                    {
                        "Parameter": [
                            "Water Salinity",
                            "Measured Cyanotoxin"
                        ],

                        "Value": [
                            f"{salinity:.2f} ppt",
                            f"{cyanotoxin_index:.2f} µg/L"
                        ]
                    }
                )
 st.dataframe(
                    environmental_data,
                    use_container_width=True,
                    hide_index=True
                )


                # ====================================================
                # ENVIRONMENTAL ASSESSMENT
                # ====================================================

                st.subheader(
                    "🤖 3. Environmental Computational Assessment"
                )

                st.write(
                    "The cyanotoxin value is displayed as a measured "
                    "environmental parameter. No unsupported clinical "
                    "prediction is generated."
                )


                if cyanotoxin_index > 0:

                    st.warning(
                        "⚠️ Detectable cyanotoxin concentration reported."
                    )

                else:

                    st.success(
                        "🟢 No cyanotoxin concentration was entered."
                    )


                st.caption(
                    "Environmental cyanobacteria findings should not "
                    "be interpreted as evidence of urinary tract "
                    "infection or direct pregnancy outcome prediction."
                )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style='text-align:center; color:gray; font-size:12px;'>
    <i>
    AMM is a research and educational computational prototype.
    Results are not intended to diagnose, treat, predict miscarriage,
    or replace professional medical judgment.
    Clinical use requires appropriate datasets, independent validation,
    performance evaluation, and regulatory assessment.
    </i>
    </div>
    """,
    unsafe_allow_html=True
)
