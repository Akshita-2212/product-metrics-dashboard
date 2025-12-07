📱 Product Metrics Dashboard

A Product Analytics Dashboard for Understanding User Engagement, Device Performance & Behavioral Segmentation

---

🚀 Overview

This interactive dashboard enables Product Analysts, Data Analysts, and AI/ML professionals to explore key mobile usage metrics using real-world behavioral data.

The goal of this project is to analyze user engagement and device performance and extract insights that could guide:

Feature prioritization

User retention strategies

Device optimization

Performance monitoring

Product decision-making

It is built using Streamlit, Pandas, and Plotly for a clean and intuitive analytics experience.

---

🎯 Key Questions This Dashboard Answers

✔ Which user segment is the most active?
✔ How does device type (Android/iOS) influence usage?
✔ Which devices cause more battery drain?
✔ How does age/gender affect engagement?
✔ What factors correlate most with heavy usage?
✔ How do different behavior classes behave?

---

📊 Features
🔹 1. Key Product Metrics

Average daily usage time

Screen-on time

Data consumption

Battery drain

Number of installed apps

🔹 2. Engagement Insights

Usage time distribution

Usage vs battery drain (correlation)

Correlation heatmap

🔹 3. Device Insights

OS-level usage comparison

Battery drain by device model

Top 10 battery-draining devices

🔹 4. Demographic Insights

Usage by age groups

Usage comparison across genders

🔹 5. Behavior Segmentation

Behavioral class distribution (1–5)

Usage comparison by class

---

🔥 Custom Metric: Usage Intensity Score

A weighted composite metric designed to identify heavy vs casual users.

Usage_Intensity_Score =
0.4 \* App_Usage_Time

- 0.3 \* Screen_On_Time
- 0.2 \* Data_Usage
- 0.1 \* Number_of_Apps_Installed

This helps PMs instantly differentiate high-engagement and low-engagement user segments.

---

📈 Business Insights Extracted

✨ Heavy users install more apps and consume more data
→ Suggests upselling opportunities & premium features.

✨ Battery drain strongly correlates with screen-on time
→ Can guide performance optimization for specific models.

✨ Android devices show higher variance in usage
→ Indicates need for OS-specific UX optimization.

✨ Usage differs significantly across age groups
→ Helpful for feature targeting & personalization.

✨ Behavior Class 5 users are the most active
→ Useful for identifying power users or beta testers.

---

🗂️ Dataset

Mobile Device Usage & User Behavior Dataset – Kaggle
Contains:

User ID

Device model

OS (Android/iOS)

Age & gender

Daily usage time

Screen-on hours

Mobile data consumption

Number of installed apps

Battery drain

Behavior class (1–5)

---

⚙️ Tech Stack
Component Technology
Dashboard Streamlit
Data Processing Pandas, NumPy
Visualizations Plotly Express
Language Python

---

🛠️ Project Structure
product-metrics-dashboard/
│── app.py
│── user_behavior_dataset.csv
│── requirements.txt
│── README.md

▶️ Run the App Locally
1️⃣ Clone repo
git clone https://github.com/Akshita-2212/product-metrics-dashboard.git
cd product-metrics-dashboard

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run Streamlit
streamlit run app.py

---

🌐 Live Demo (Coming Soon)

To view the dashboard online with no setup:

👉 Deployment link will appear here once hosted on Streamlit Cloud.

---

🚀 Deployment Options

You can deploy this on:

Streamlit Cloud (Recommended)

HuggingFace Spaces

Render

Deployment guide is provided below.

---

📌 Future Improvements

🔹 Add DAU/MAU + Retention Cohorts
🔹 Add churn prediction model
🔹 Add clustering for user segmentation
🔹 Add anomaly detection
🔹 Add real-time monitoring with APIs
🔹 Support SQL data sources

---

✨ Author

Akshita Sharma
Machine Learning & Product Analytics
📧 Akshita03coder@gmail.com
🔗 GitHub: Akshita-2212
