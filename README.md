# 🩺 Diabetes Prediction App

A simple, clean, and powerful **Machine Learning Web App** built using **Streamlit** — now deployed and live!

👉 **Live App:** https://diabetes-prediction-app-ksutmhh8zn8kq3slr7ttgk.streamlit.app/

---

# 🚀 How to Deploy This Streamlit App

Follow these steps to deploy your own Streamlit ML application from scratch.

---

## ✅ Step 1: Create a GitHub Repository

1. Go to GitHub: [https://github.com/](https://github.com/)
2. Click **New Repository**.
3. Name it (example): `diabetes-prediction-app`.
4. Click **Create Repository**.

---

## ✅ Step 2: Add Your Project Files to GitHub

Inside your project folder (example: `Python_model/`) make sure you include:

📁 **Required Files:**

* `Predictive_System.py` — Your Streamlit app
* `trained_model.sav` — Saved ML model
* `requirements.txt` — List of all libraries needed by your app

📌 **Important:** Create the `requirements.txt` inside your virtual environment using:

```bash
pip freeze > requirements.txt
```

This ensures Streamlit Cloud installs the correct versions.

---

## ✅ Step 3: Push Your Code to GitHub

Use the following commands:

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

Your folder will now be uploaded to GitHub.

---

## ✅ Step 4: Deploy on Streamlit Community Cloud

1. Go to: [https://share.streamlit.io](https://share.streamlit.io)
2. Click **New App**
3. Select your GitHub Repository

### Choose the following:

* **Repo:** `diabetes-prediction-app`
* **Branch:** `main`
* **File Path:** `Predictive_System.py`

4. Click **Deploy** 🚀

Streamlit will now install dependencies, set up the environment, and host your app publicly.

---

# 🎉 Your App is Live!

Once deployment completes, Streamlit provides a public URL you can share anywhere.

This is how your ML project becomes a real web application! 🌍

Need help improving your README or adding screenshots/badges? Just let me know! 😊
