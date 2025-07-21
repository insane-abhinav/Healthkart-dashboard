import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(page_title="INFLUENCER CAMPAIGN ROI DASHBOARD", layout="wide")

# Custom theme using provided color palette
st.markdown("""
    <style>
        .stApp {
            background-color: #BDDDFC;
            font-family: 'Segoe UI', sans-serif;
            color: #384959;
        }
        .stDataFrame thead tr th {
            background-color: #6A89A7 !important;
            color: white !important;
        }
        .stDataFrame tbody tr td {
            color: #384959;
        }
        .metric-container, .stMetric {
            background-color: #88BDF2;
            padding: 10px;
            border-radius: 8px;
            color: #384959 !important;
        }
        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Load data
influencers = pd.read_csv("data/influencers.csv")
posts = pd.read_csv("data/posts.csv")
tracking = pd.read_csv("data/tracking_data.csv")
payouts = pd.read_csv("data/payouts.csv")

st.title("📊 INFLUENCER CAMPAIGN DASHBOARD")
st.markdown("Use this tool to explore ROAS, Top Personas, and Campaign impact by Platform, Location, and Influencer traits.")

# Sidebar filters
with st.sidebar:
    st.header("🔍 FILTERS")
    selected_brand = st.selectbox("SELECT BRAND", options=sorted(tracking["brand"].unique()))
    selected_platform = st.multiselect("SELECT PLATFORMS", options=sorted(posts["platform"].unique()), default=posts["platform"].unique())

# Merge and calculate metrics
roi_df = (
    tracking[tracking["brand"] == selected_brand]
    .groupby("influencer_id")["revenue"].sum()
    .reset_index()
    .merge(payouts, on="influencer_id")
    .merge(influencers, left_on="influencer_id", right_on="id")
)
roi_df["ROAS"] = roi_df["revenue"] / roi_df["total_payout"]
roi_df["INCREMENTAL_ROAS"] = (roi_df["revenue"] * np.random.uniform(0.3, 0.7)) / roi_df["total_payout"]

# Filter posts by platform
platform_posts = posts[posts["platform"].isin(selected_platform)]

# METRICS
st.subheader(f"📈 PERFORMANCE SUMMARY: {selected_brand.upper()}")
st.metric("AVERAGE ROAS", f"{roi_df['ROAS'].mean():.2f}")
st.metric("TOP INFLUENCER ROAS", f"{roi_df['ROAS'].max():.2f}")

# TOP INFLUENCERS TABLE
st.markdown("### 🏆 TOP PERFORMING INFLUENCERS")
st.dataframe(roi_df.sort_values("ROAS", ascending=False).head(5)[["name", "persona", "platform", "ROAS", "total_payout"]], use_container_width=True)

# INSIGHT: PERSONAS
persona_insight = roi_df.groupby("persona")["ROAS"].mean().sort_values(ascending=False)
st.markdown("### 👥 ROI BY INFLUENCER PERSONA")
st.bar_chart(persona_insight)

# INSIGHT: CITIES
city_insight = roi_df.groupby("city")["ROAS"].mean().sort_values(ascending=False)
st.markdown("### 🏙️ ROAS BY CITY")
st.bar_chart(city_insight)

# LOW PERFORMANCE
st.markdown("### 🚨 LOW PERFORMING INFLUENCERS (BOTTOM 10%)")
st.dataframe(roi_df.sort_values("ROAS").head(int(len(roi_df)*0.1))["name city platform ROAS".split()], use_container_width=True)
