# cbc_predictor.py

import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# === Load trained model and encoder
model = joblib.load("cbc_rf_model.pkl")
le_combo = joblib.load("combo_encoder.pkl")

# === Subject list (must match training)
SUBJECTS = ["Math", "English", "Kiswahili", "Science", "SocialStudies", "CRE",
            "Business", "Agriculture", "Computer", "Geography"]

# === Example input: Replace with real student scores (Avg from Grade 4 to 9)
new_student = {
    "Math_Avg": 70,
    "English_Avg": 72,
    "Kiswahili_Avg": 70,
    "Science_Avg": 78,
    "SocialStudies_Avg": 60,
    "CRE_Avg": 55,
    "Business_Avg": 65,
    "Agriculture_Avg": 60,
    "Computer_Avg": 85,
    "Geography_Avg": 70
}

# === Convert to DataFrame
input_df = pd.DataFrame([new_student])

# === Predict subject combo
prediction = model.predict(input_df)
predicted_combo = le_combo.inverse_transform(prediction)[0]

# === Output
print("🔮 Recommended Subject Combination:")
print(f"👉 {predicted_combo}")
