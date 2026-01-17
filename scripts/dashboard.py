import streamlit as st
import oracledb
import pandas as pd
import plotly.express as px
import config

# Page Config
st.set_page_config(page_title="Retail Data Warehouse Insights", layout="wide")

@st.cache_data
def get_data():
    conn = oracledb.connect(user=config.DB_USER, password=config.DB_PASS, dsn=config.DB_DSN)
    # Query the view we created earlier
    query = "SELECT * FROM VW_RETAIL_DASHBOARD"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

# Header
st.title("📊 Global Retail Executive Dashboard")
st.markdown("Insights from 1M+ Records Processed via Oracle XE Pipeline")

try:
    data = get_data()

    # --- KPI METRICS ---
    total_rev = f"${data['REVENUE'].sum():,.2f}"
    total_orders = f"{data['TOTAL_ORDERS'].sum():,}"
    top_country = data.iloc[0]['COUNTRY']

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Revenue", total_rev)
    col2.metric("Total Orders", total_orders)
    col3.metric("Top Country", top_country)

    st.divider()

    # --- CHARTS ---
    left_col, right_col = st.columns(2)

    with left_col:
        st.subheader("Revenue by Country (Top 10)")
        fig_rev = px.bar(data.head(10), x='COUNTRY', y='REVENUE', 
                         color='REVENUE', color_continuous_scale='Viridis')
        st.plotly_chart(fig_rev, use_container_width=True)

    with right_col:
        st.subheader("Order Volume Distribution")
        fig_pie = px.pie(data.head(5), values='TOTAL_ORDERS', names='COUNTRY', hole=0.4)
        st.plotly_chart(fig_pie, use_container_width=True)

    # --- DATA TABLE ---
    st.subheader("Detailed Performance Metrics")
    st.dataframe(data, use_container_width=True)

except Exception as e:
    st.error(f"Error connecting to Oracle: {e}")