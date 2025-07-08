# 🧠 Smart Phishing Detector (URL + Email)

A Python-based phishing detection tool with a graphical user interface (GUI). It uses feature extraction and machine learning (Random Forest) to classify URLs and emails as phishing or legitimate.

---

## 📄 Description

This tool helps users identify phishing threats by analyzing URLs and email content using simple features. It has a clean GUI built with Tkinter and supports real-time detection.

---

## 🚀 Features

- 🔍 Detects phishing **URLs** using:
  - Length, digits, dots, hyphens, `@` symbols
  - Suspicious TLDs (e.g., `.tk`, `.ga`, `.cf`, etc.)
- 📧 Detects phishing **emails** using:
  - Keywords like “urgent”, “verify”, “password”
  - Presence of links, login prompts, etc.
- 🧠 Trained with a Random Forest Classifier from `scikit-learn`
- 🖥️ Easy-to-use GUI built in `Tkinter`
- 💡 Educational and beginner-friendly

---

## 🔧 Requirements

Install all dependencies using:

```bash
pip install -r requirements.txt

---

## 🖥️ How to Run

Make sure you're in the project directory, then run:

```bash
python phishing_gui.py


---

### 🧑‍💻 Author  
Made with ❤️ by Haider Amin
