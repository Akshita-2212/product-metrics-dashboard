📱 Product Metrics Dashboard

A data analytics dashboard built using Streamlit, Pandas, and Plotly to analyze user behavior, device performance, and engagement patterns from mobile usage data.

🚀 Project Overview

This dashboard provides insights on:

User engagement (App usage time, screen time, data usage)

Device performance (Battery drain, OS comparison)

Demographics analysis

User behavior segmentation

Custom "Usage Intensity Score"

The goal of this project is to showcase Product Analytics skills using real data and interactive visualizations.

📊 Features
✅ 1. Key Product Metrics

Average usage time per day

Average screen-on time

Average data consumption

Average battery drain

Average number of apps installed

✅ 2. Engagement Insights

Usage distribution

Usage vs battery drain scatter plot

Correlation heatmap

✅ 3. Device Insights

Usage time by operating system (iOS vs Android)

Top devices with the highest battery drain

✅ 4. Demographic Insights

Usage by age

Usage comparison by gender

✅ 5. Behavior Segmentation

Distribution of behavior classes (1–5)

Usage comparison across classes

🧮 Usage Intensity Score (Custom Metric)

A composite metric designed to represent how “heavy” the user is:

Usage_Intensity_Score =
    0.4 * App_Usage_Time
  + 0.3 * Screen_On_Time
  + 0.2 * Data_Usage
  + 0.1 * Number_of_Apps_Installed

🗂️ Tech Stack

Streamlit – UI & dashboard

Pandas – Data processing

Plotly – Interactive charts

Python – Logic & calculations

▶️ How to Run Locally
1. Clone the repo
git clone https://github.com/<your-username>/product-metrics-dashboard.git
cd product-metrics-dashboard

2. Install dependencies
pip install -r requirements.txt

3. Run the app
streamlit run app.py

📁 Dataset

Dataset used:
Mobile Device Usage and User Behavior Dataset (Kaggle)
Includes user ID, device model, OS, age, gender, app usage, screen time, data usage & behavior class.

🌐 Deployment

The project is compatible with:

Streamlit Cloud

HuggingFace Spaces

Render

🏁 Author

Akshita Sharma
Machine Learning & Data Analytics