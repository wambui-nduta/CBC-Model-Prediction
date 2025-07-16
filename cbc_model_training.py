# cbc_model_training.py

import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib

# === Constants ===
SUBJECTS = ["Math", "English", "Kiswahili", "Science", "SocialStudies", "CRE",
            "Business", "Agriculture", "Computer", "Geography"]
GRADES = ["G4", "G5", "G6", "G7", "G8", "G9"]

COMBO_MAP = {
    "STEM": "Advanced Mathematics, Biology, Chemistry",
    "SCIENCE_APPLIED": "Biology, Chemistry, Agriculture",
    "TECHNICAL": "Computer Studies, Business studies, Physics",
    "BUSINESS": "Business Studies, History & Citizenship, French",
    "ARTS": "Fine Arts, Theatre & Film, Geography",
    "LANGUAGES": "Mandarin, French, Business Studies"
}

# === Subject emphasis per combo ===
COMBO_SUBJECT_WEIGHTS = {
    "STEM": {
        "Math": (80, 95),
        "Science": (80, 95),
        "Computer": (70, 85),
        "Business": (40, 60),
        "CRE": (40, 60),
        "Kiswahili": (50, 65),
    },
    "SCIENCE_APPLIED": {
        "Biology": (80, 95),
        "Agriculture": (80, 95),
        "Math": (70, 85),
        "Business": (45, 60),
        "CRE": (40, 55),
    },
    "TECHNICAL": {
        "Computer": (80, 95),
        "Business": (80, 95),
        "Math": (75, 90),
        "Science": (70, 85),
        "English": (50, 65),
    },
    "BUSINESS": {
        "Business": (80, 95),
        "Math": (70, 85),
        "English": (75, 90),
        "Kiswahili": (75, 90),
        "Science": (50, 65),
    },
    "ARTS": {
        "SocialStudies": (80, 95),
        "CRE": (80, 95),
        "English": (75, 90),
        "Geography": (75, 90),
        "Math": (40, 60),
    },
    "LANGUAGES": {
        "English": (85, 100),
        "Kiswahili": (85, 100),
        "CRE": (70, 85),
        "Geography": (70, 85),
        "Math": (50, 65),
    }
}

# === Realistic Data Generator ===
def generate_combo_students(combo_name, n=833):
    students = []
    strong_subjects = COMBO_SUBJECT_WEIGHTS[combo_name]

    for _ in range(n):
        student = {}

        for subject in SUBJECTS:
            for grade in GRADES:
                if subject in strong_subjects:
                    score_range = strong_subjects[subject]
                else:
                    score_range = (50, 70)  # neutral default

                student[f"{subject}_{grade}"] = random.randint(*score_range)

        student["Subject_Combo"] = COMBO_MAP[combo_name]
        students.append(student)

    return students

# === Combine all combos
def generate_final_dataset():
    all_students = []
    for combo_key in COMBO_MAP.keys():
        all_students += generate_combo_students(combo_key, n=833)  # ~5000 total
    return pd.DataFrame(all_students)

# === Train the model
def train_model(df):
    for subject in SUBJECTS:
        df[f"{subject}_Avg"] = df[[f"{subject}_G{i}" for i in range(4, 10)]].mean(axis=1)

    le_combo = LabelEncoder()
    df["Combo_Code"] = le_combo.fit_transform(df["Subject_Combo"])

    X = df[[f"{s}_Avg" for s in SUBJECTS]]
    y = df["Combo_Code"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"\n✅ Accuracy: {round(acc * 100, 2)}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred, target_names=le_combo.classes_))

    joblib.dump(model, "cbc_rf_model.pkl")
    joblib.dump(le_combo, "combo_encoder.pkl")
    print("💾 Model and encoder saved.")

# === Run it
if __name__ == "__main__":
    df = generate_final_dataset()
    df.to_csv("cbc_dataset.csv", index=False)
    print("📁 Dataset saved as 'cbc_dataset.csv'")
    train_model(df)
