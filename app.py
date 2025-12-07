import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Product Metrics Dashboard", layout="wide")

# ------------------------
# LOAD DATA
# ------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("user_behavior_dataset.csv")
    return df

df = load_data()

st.title("📱 Product Metrics Dashboard")
st.markdown("Analyze usage patterns, device performance & user behavior segmentation.")

# ------------------------
# CLEAN COLUMN NAMES
# ------------------------
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("(", "").str.replace(")", "").str.replace("/", "_")

# Now your columns become:
# User_ID
# Device_Model
# Operating_System
# App_Usage_Time_min_day
# Screen_On_Time_hours_day
# Battery_Drain_mAh_day
# Number_of_Apps_Installed
# Data_Usage_MB_day
# Age
# Gender
# User_Behavior_Class

numeric_cols = [
    "App_Usage_Time_min_day",
    "Screen_On_Time_hours_day",
    "Battery_Drain_mAh_day",
    "Number_of_Apps_Installed",
    "Data_Usage_MB_day",
    "Age"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Custom user intensity score
df["Usage_Intensity_Score"] = (
    df["App_Usage_Time_min_day"] * 0.4 +
    df["Screen_On_Time_hours_day"] * 0.3 +
    df["Data_Usage_MB_day"] * 0.2 +
    df["Number_of_Apps_Installed"] * 0.1
)

# ------------------------
# SIDEBAR FILTERS
# ------------------------
st.sidebar.header("Filters")

gender_filter = st.sidebar.multiselect(
    "Gender",
    df["Gender"].unique(),
    df["Gender"].unique()
)

os_filter = st.sidebar.multiselect(
    "Operating System",
    df["Operating_System"].unique(),
    df["Operating_System"].unique()
)

filtered_df = df[
    (df["Gender"].isin(gender_filter)) &
    (df["Operating_System"].isin(os_filter))
]

# ------------------------
# KPI CARDS
# ------------------------
st.subheader("📊 Key Product Metrics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Avg Usage (min/day)", f"{filtered_df['App_Usage_Time_min_day'].mean():.1f}")
col2.metric("Avg Screen Time (hrs/day)", f"{filtered_df['Screen_On_Time_hours_day'].mean():.2f}")
col3.metric("Avg Battery Drain (mAh)", f"{filtered_df['Battery_Drain_mAh_day'].mean():.0f}")
col4.metric("Avg Data Usage (MB/day)", f"{filtered_df['Data_Usage_MB_day'].mean():.1f}")
col5.metric("Avg Apps Installed", f"{filtered_df['Number_of_Apps_Installed'].mean():.1f}")

st.markdown("---")

# ------------------------
# TABS
# ------------------------
tab1, tab2, tab3, tab4 = st.tabs(["Engagement", "Device Insights", "Demographics", "Behavior Segmentation"])

# ------------------------
# TAB 1 – ENGAGEMENT
# ------------------------
with tab1:
    st.subheader("📈 User Engagement Analysis")

    fig1 = px.histogram(filtered_df, x="App_Usage_Time_min_day", nbins=30,
                        title="Distribution of App Usage Time (min/day)")
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.scatter(filtered_df, x="App_Usage_Time_min_day", y="Battery_Drain_mAh_day",
                      trendline="ols", title="Usage vs Battery Drain (per day)")
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.imshow(filtered_df[numeric_cols].corr(), text_auto=True,
                     title="Correlation Heatmap")
    st.plotly_chart(fig3, use_container_width=True)

# ------------------------
# TAB 2 – DEVICE INSIGHTS
# ------------------------
with tab2:
    st.subheader("📱 Device Performance Insights")

    fig4 = px.box(filtered_df, x="Operating_System", y="App_Usage_Time_min_day",
                  title="Usage Time by Operating System")
    st.plotly_chart(fig4, use_container_width=True)

    device_battery = filtered_df.groupby("Device_Model")["Battery_Drain_mAh_day"].mean().reset_index()
    device_battery = device_battery.sort_values("Battery_Drain_mAh_day", ascending=False).head(10)

    fig5 = px.bar(device_battery, x="Device_Model", y="Battery_Drain_mAh_day",
                  title="Top 10 Devices with Highest Battery Drain")
    st.plotly_chart(fig5, use_container_width=True)

# ------------------------
# TAB 3 – DEMOGRAPHICS
# ------------------------
with tab3:
    st.subheader("👥 Demographic Insights")

    fig6 = px.bar(filtered_df, x="Age", y="App_Usage_Time_min_day",
                  title="Usage Time by Age")
    st.plotly_chart(fig6, use_container_width=True)

    gender_usage = filtered_df.groupby("Gender")["App_Usage_Time_min_day"].mean().reset_index()
    fig7 = px.bar(gender_usage, x="Gender", y="App_Usage_Time_min_day",
                  title="Average Usage by Gender")
    st.plotly_chart(fig7, use_container_width=True)

# ------------------------
# TAB 4 – BEHAVIOR SEGMENTATION
# ------------------------
with tab4:
    st.subheader("🧭 User Behavior Segmentation")

    fig8 = px.pie(filtered_df, names="User_Behavior_Class",
                  title="User Behavior Class Distribution")
    st.plotly_chart(fig8, use_container_width=True)

    fig9 = px.box(filtered_df, x="User_Behavior_Class", y="App_Usage_Time_min_day",
                  title="Usage Time by Behavior Class")
    st.plotly_chart(fig9, use_container_width=True)
