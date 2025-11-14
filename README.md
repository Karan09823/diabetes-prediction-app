# Diabetes-Prediction-App
 Check the streamlit app here - https://diabetes-prediction-app-dows8kblfwusi9gtfcwwji.streamlit.app/

# Steps for deploying the App
✅ Step 1: Create a GitHub Repository
- Go to https://github.com/
- Click New Repository
- Name it something like: diabetes-prediction-app
- Click Create Repository

✅ Step 2: Add Your Project Files to GitHub
- Inside your project folder (folder:Python_model/):
- Your folder must include:
- Predictive_System.py
- trained_model.sav
- requirements.txt   (VERY IMPORTANT)
*** Create a requirements.txt(inside environment) - pip freeze > requirements.txt
  
✅ Step 3: Push Your Code to GitHub

✅ Step 4: Deploy on Streamlit Cloud
- Go to https://share.streamlit.io
- Click New App
- Select your GitHub repo
  Choose:
   - Repo: diabetes-prediction-app
   - Branch: main
   - File path: Predictive_System.py
   - Click Deploy

💥 Streamlit will build & host your app online.
