# cbc_streamlit_app.py

import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# === Load model and encoder
model = joblib.load("cbc_rf_model.pkl")
le_combo = joblib.load("combo_encoder.pkl")

# === Subject list (must match model training)
SUBJECTS = [
    "Math", "English", "Kiswahili", "Science", "SocialStudies", "CRE",
    "Business", "Agriculture", "Computer", "Geography"
]

# === Career path mapping
CAREER_PATHS = {
    "Advanced Mathematics, Biology, Chemistry": ["🩺 Doctor", "🔧 Engineer", "💊 Pharmacist", "📈 Data Analyst"],
    "Biology, Chemistry, Agriculture": ["🐄 Veterinarian", "🌾 Agricultural Officer", "🧬 Biotechnologist"],
    "Computer Studies, Business studies, Physics": ["💻 Software Developer", "🧠 Systems Analyst", "🔌 ICT Technician"],
    "Business Studies, History & Citizenship, French": ["📊 Economist", "⚖️ Lawyer", "🌍 Diplomat", "💼 Business Consultant"],
    "Fine Arts, Theatre & Film, Geography": ["🎨 Artist", "🎭 Theatre Director", "🎬 Filmmaker", "🧭 Geographer"],
    "Mandarin, French, Business Studies": ["🗣️ Translator", "🌐 International Business Manager", "✈️ Tourism Officer"]
}

# === Page Setup
st.set_page_config(page_title="CBC Career Recommender", layout="centered")
st.title("🎓 CBC Subject & Career Recommender")
st.markdown("Helping students explore their best-fit career paths based on their strengths and interests.")

st.divider()

# === Collect Subject Averages
st.subheader("📋 Enter Subject Averages (Grades 4–9)")
student_data = {}
cols = st.columns(2)

for idx, subject in enumerate(SUBJECTS):
    with cols[idx % 2]:
        student_data[f"{subject}_Avg"] = st.slider(f"{subject}", 40, 100, 70)

# === Predict Button
if st.button("🚀 Predict My Path"):
    input_df = pd.DataFrame([student_data])
    prediction = model.predict(input_df)
    predicted_combo = le_combo.inverse_transform(prediction)[0]

    st.success(f"✅ **Recommended CBC Subject Combination:**\n\n🎯 _{predicted_combo}_")

    # === Suggested Careers
    careers = CAREER_PATHS.get(predicted_combo, ["🎓 Career info coming soon"])
    st.subheader("💼 Suggested Career Paths:")
    for career in careers:
        st.markdown(f"- {career}")

    # === Bar Chart: Subject Performance
    st.subheader("📊 Subject Performance Overview")
    st.bar_chart(input_df.T)

    # === Pie Chart: Subject Area Strengths
    st.subheader("📈 Subject Area Strengths")
    subject_areas = {
        "Languages": student_data["English_Avg"] + student_data["Kiswahili_Avg"],
        "Sciences": student_data["Math_Avg"] + student_data["Science_Avg"],
        "Humanities": student_data["SocialStudies_Avg"] + student_data["CRE_Avg"],
        "Tech & Business": student_data["Computer_Avg"] + student_data["Business_Avg"],
        "Environmental": student_data["Geography_Avg"] + student_data["Agriculture_Avg"]
    }

    fig, ax = plt.subplots()
    ax.pie(subject_areas.values(), labels=subject_areas.keys(), autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    st.info("✅ _Tip: Encourage students to explore co-curriculars aligned with their career paths._")

# === Footer
st.divider()
st.caption("Built with ❤️ by Elizabeth | CBC Career Intelligence Tool")
