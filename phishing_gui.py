import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# --- Feature Extraction Functions ---

def extract_url_features(url):
    return {
        "url_length": len(url),
        "count_dots": url.count("."),
        "count_hyphens": url.count("-"),
        "count_at": url.count("@"),
        "has_https": int(url.startswith("https")),
        "count_digits": sum(char.isdigit() for char in url),
        "has_suspicious_tld": int(any(tld in url for tld in [".tk", ".ml", ".ga", ".cf", ".gq"]))
    }

def extract_email_features(email):
    email = email.lower()
    return {
        "contains_urgent": int(any(word in email for word in ["urgent", "immediately", "suspended", "verify", "warning"])),
        "contains_login": int("login" in email or "log in" in email),
        "contains_update": int("account update" in email),
        "contains_password": int("password" in email),
        "contains_link": int("http://" in email or "https://" in email or "www." in email),
        "length": len(email),
    }

# --- Training Datasets ---

# URLs
url_data = [
    {"url": "http://paypal-login.tk", "label": 1},
    {"url": "https://secure-facebook.com-login", "label": 1},
    {"url": "http://apple.support.account-update.ga", "label": 1},
    {"url": "https://google.com", "label": 0},
    {"url": "https://haideramin989.medium.com", "label": 0},
    {"url": "https://amazon.com", "label": 0},
    {"url": "http://verify-apple.com-login.tk", "label": 1},
    {"url": "https://facebook.com", "label": 0},
    {"url": "https://paypal.com", "label": 0},
    {"url": "http://malicious-verify-id.cf", "label": 1},
]
df_urls = pd.DataFrame(url_data)
X_url = pd.DataFrame([extract_url_features(url) for url in df_urls["url"]])
y_url = df_urls["label"]
model_url = RandomForestClassifier(n_estimators=100)
model_url.fit(X_url, y_url)

# Emails
email_data = [
    {"email": "Your account is suspended. Please verify immediately at http://suspicious.tk", "label": 1},
    {"email": "Click here to update your password: http://fake-login.com", "label": 1},
    {"email": "Important: Log in to your account now to avoid closure", "label": 1},
    {"email": "Meeting confirmed for tomorrow. Please find agenda attached.", "label": 0},
    {"email": "Here is the receipt for your recent purchase", "label": 0},
    {"email": "Your Amazon order has been shipped", "label": 0},
]
df_emails = pd.DataFrame(email_data)
X_email = pd.DataFrame([extract_email_features(email) for email in df_emails["email"]])
y_email = df_emails["label"]
model_email = RandomForestClassifier(n_estimators=100)
model_email.fit(X_email, y_email)

# --- GUI Logic ---
def check_input():
    text = input_entry.get("1.0", "end").strip()
    if not text:
        messagebox.showwarning("Input Error", "Please enter a URL or email.")
        return

    if selected_mode.get() == "URL":
        features = pd.DataFrame([extract_url_features(text)])
        prediction = model_url.predict(features)[0]
        if prediction == 1:
            result_label.config(text="⚠️ Phishing URL Detected!", fg="red")
        else:
            result_label.config(text="✅ This URL seems safe.", fg="green")

    elif selected_mode.get() == "Email":
        features = pd.DataFrame([extract_email_features(text)])
        prediction = model_email.predict(features)[0]
        if prediction == 1:
            result_label.config(text="⚠️ Phishing Email Detected!", fg="red")
        else:
            result_label.config(text="✅ This Email seems safe.", fg="green")

    input_entry.delete("1.0", "end")

# --- GUI Setup ---
root = tk.Tk()
root.title("Smart Phishing Detector (URL + Email)")
root.geometry("500x360")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="🧠 Smart Phishing Detector", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

mode_frame = tk.Frame(root, bg="#f0f0f0")
mode_frame.pack()

selected_mode = tk.StringVar(value="URL")
tk.Radiobutton(mode_frame, text="URL", variable=selected_mode, value="URL", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=20)
tk.Radiobutton(mode_frame, text="Email", variable=selected_mode, value="Email", font=("Helvetica", 12), bg="#f0f0f0").pack(side=tk.LEFT, padx=20)

input_entry = tk.Text(root, height=5, width=58, font=("Helvetica", 12))
input_entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("Helvetica", 12), command=check_input, bg="#4caf50", fg="white", width=15)
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0")
result_label.pack(pady=20)

root.mainloop()
