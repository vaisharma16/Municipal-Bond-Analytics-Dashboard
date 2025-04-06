import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv("muni_bonds_2000.csv")  # Update path if needed

# Sidebar filters
st.sidebar.header("🔎 Filter Bonds")
state_filter = st.sidebar.multiselect("Select State(s):", df["State"].unique(), default=df["State"].unique())
rating_filter = st.sidebar.multiselect("Select Credit Rating(s):", df["CreditRating"].unique(), default=df["CreditRating"].unique())
sector_filter = st.sidebar.multiselect("Select Sector(s):", df["Sector"].unique(), default=df["Sector"].unique())

# Filtered data
filtered_df = df[
    df["State"].isin(state_filter) &
    df["CreditRating"].isin(rating_filter) &
    df["Sector"].isin(sector_filter)
]

# Title
st.title("📊 Municipal Bond Dashboard")
st.markdown("Explore synthetic municipal bond data and uncover insights by state, sector, and credit rating.")

# KPIs
col1, col2, col3 = st.columns(3)
col1.metric("Average Yield (%)", round(filtered_df["Yield"].mean(), 2))
col2.metric("Average Price ($)", round(filtered_df["Price"].mean(), 2))
col3.metric("Total Bonds", filtered_df.shape[0])

st.markdown("---")

# Yield by Rating
st.subheader("🎯 Yield Distribution by Credit Rating")
fig1 = px.box(filtered_df, x="CreditRating", y="Yield", color="CreditRating", points="all")
st.plotly_chart(fig1, use_container_width=True)

# Price vs Duration
st.subheader("📈 Price vs Duration (Risk View)")
fig2 = px.scatter(filtered_df, x="Duration", y="Price", color="CreditRating",
                  hover_data=["BondID", "Sector", "Yield"])
st.plotly_chart(fig2, use_container_width=True)

# Yield Curve: Maturity vs Yield
st.subheader("📉 Simulated Yield Curve")
filtered_df["MaturityDate"] = pd.to_datetime(filtered_df["MaturityDate"])
filtered_df["MaturityYear"] = filtered_df["MaturityDate"].dt.year
fig3 = px.scatter(filtered_df, x="MaturityYear", y="Yield", color="CreditRating", trendline="lowess")
st.plotly_chart(fig3, use_container_width=True)

# Sector breakdown
st.subheader("🏢 Bonds by Sector")
sector_counts = filtered_df["Sector"].value_counts().reset_index()
sector_counts.columns = ["Sector", "Count"]
fig4 = px.bar(sector_counts, x="Sector", y="Count", color="Sector")
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.markdown("👩‍💻 Built by Vaibhav Sharma — Data + Applied Science Enthusiast | GitHub: [vaisharma16](https://github.com/vaisharma16)")
