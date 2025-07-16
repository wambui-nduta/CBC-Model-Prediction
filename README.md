
# 🎓 CBC Career & Subject Combination Predictor

This project is an intelligent **ML-powered tool** that recommends the most suitable CBC subject combinations and career paths for Kenyan learners based on their academic performance from Grades 4–9.

It uses student subject averages to predict ideal learning pathways aligned with the **Ministry of Education's CBC framework**, helping learners and educators make informed decisions early.

---

## 🚀 Features

- ✅ Predicts best-fit **CBC subject combination**
- 💼 Recommends related **career paths**
- 📊 Visualizes student performance via **bar & pie charts**
- 🎨 Engaging **Streamlit web app** for easy interaction
- 🔮 Powered by **Random Forest Classifier** trained on smart, realistic data

---

## 🧠 How It Works

1. **Generate or input student data** (subject averages from Grades 4–9)
2. Trained model analyzes subject strengths
3. Outputs:
   - ✅ The recommended CBC subject combination
   - 💼 Possible career paths
   - 📈 Graphs showing subject area performance

The model was trained on over **5,000 simulated learners** with logical scoring aligned to CBC pathways.

---

## 📁 Project Structure

```

📦 CBC-Career-Predictor
│
├── cbc\_model\_training.py         # Generates dataset, trains the ML model
├── cbc\_streamlit\_app.py          # The interactive Streamlit prediction app
├── cbc\_rf\_model.pkl              # Trained Random Forest model (auto-generated)
├── combo\_encoder.pkl             # Label encoder for subject combos
├── cbc\_dataset.csv               # Dataset of 5,000 smart learners
├── README.md                     # You're here!

````

---

## 🌐 Try It Yourself

1. **Install dependencies**
   ```bash
   pip install streamlit pandas scikit-learn matplotlib joblib
````

2. **Train the model**

   ```bash
   python cbc_model_training.py
   ```

3. **Run the web app**

   ```bash
   streamlit run cbc_streamlit_app.py
   ```

---

## 📷 Screenshots

| 📊 Prediction UI     | 📈 Subject Charts          |
| -------------------- | -------------------------- |
| ![ui](assets/ui.png) | ![chart](assets/chart.png) |

---

## 📚 Sample Subject Combinations (From MoE)

| Track     | Sample Subjects                                 |
| --------- | ----------------------------------------------- |
| STEM      | Advanced Mathematics, Biology, Chemistry        |
| TECHNICAL | Computer Studies, Business studies, Physics     |
| BUSINESS  | Business Studies, History & Citizenship, French |
| LANGUAGES | Mandarin, French, Business Studies              |

---

## ✨ Future Improvements

* 📄 Export prediction as **PDF report**
* 📁 Bulk CSV uploads for **whole classes**
* 🧑‍🏫 Dashboard for teachers and admins
* 🌍 Localization for Kiswahili interface
* 🔐 Login system for student profiles

---

## 👩🏽‍💻 Author

**Elizabeth Nduta Wambui**
Engineer • Data Science Enthusiast • Educator
🔗 [LinkedIn](https://www.linkedin.com/) | 🌐 [Portfolio](https://your-portfolio-link.com)

---

## ❤️ Acknowledgements

* Kenya Ministry of Education — for the CBC subject pathways framework
* Streamlit — for an amazing interactive UI framework
* Scikit-learn — for machine learning tools

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).

```

---

### 🔧 Next Step (Optional)

- Save the file as `README.md`
- Add screenshots in a folder called `assets/` if you'd like
- Push to GitHub




