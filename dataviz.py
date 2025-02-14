# Streamlit (st): Dashboard banane ke liye.
# Pandas (pd): Data manipulation aur filtering ke liye.
# Plotly Express (px): Interactive charts (bar charts, line graphs) banane ke liye.

import streamlit as st
import pandas as pd
import plotly.express as px

# st.title: Dashboard ka main heading.
# st.write: Description ya instructions likhne ke liye.
# Title and Description
st.title("Interactive Data Visualization Dashboard")
st.write("Explore datasets with interactive visualizations!")

# st.sidebar.header: Sidebar mein ek section banata hai.
# st.sidebar.file_uploader: CSV file upload karne ka widget deta hai.
st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your CSV file", type="csv")

def load_data(file):
    try:
        # pd.read_csv: File ko DataFrame (table format) mein load karta hai.
        # st.error: Agar file load karne mein error aaye, toh user ko dikhata hai.
        return pd.read_csv(file)
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None
# load_data function use karke data load karo.
# st.dataframe: Data ka preview (top 5 rows) dikhao.

if uploaded_file:
    df = load_data(uploaded_file)

    if df is not None:
        st.write("### Dataset Preview")
        st.dataframe(df.head())

# select_dtypes: Numeric (numbers) aur categorical (text) columns ko alag-alag detect karta hai.
        st.sidebar.header("Filter Options")
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        categorical_cols = df.select_dtypes(include=['object']).columns
# selectbox: Dropdown se ek numeric column select karte hain.
# slider: User ko range (min-max) select karne ka option deta hai.
# Filtering Logic: Sirf wahi rows rakhte hain jo selected range mein fall karti hain.

        if not numeric_cols.empty:
            st.sidebar.subheader("Filter by Numeric Column")
            num_col = st.sidebar.selectbox("Select Column", options=numeric_cols)
            min_val = float(df[num_col].min())
            max_val = float(df[num_col].max())
            range_values = st.sidebar.slider("Select Range", min_val, max_val, (min_val, max_val))
            df = df[(df[num_col] >= range_values[0]) & (df[num_col] <= range_values[1])]
# multiselect: User ek ya multiple values select kar sakta hai.
# Filtering Logic: Sirf wahi rows rakhte hain jo selected values ke saath match karti hain.
        if not categorical_cols.empty:
            st.sidebar.subheader("Filter by Categorical Column")
            cat_col = st.sidebar.selectbox("Select Column", options=categorical_cols)
            unique_values = df[cat_col].unique()
            selected_values = st.sidebar.multiselect("Select Values", unique_values, default=unique_values)
            df = df[df[cat_col].isin(selected_values)]

# chart_type: User ko choose karne ka option dete hain ki Bar Chart ya Line Graph banana hai.
# x_axis, y_axis: User select karta hai ki kis column ko x aur y axis pe plot karna hai.

        st.sidebar.header("Visualization Options")
        chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Graph"])
        x_axis = st.sidebar.selectbox("X-Axis", options=df.columns)
        y_axis = st.sidebar.selectbox("Y-Axis", options=numeric_cols)

# Bar Chart: px.bar function use hota hai.
# Line Graph: px.line function use hota hai.
# st.plotly_chart: Chart ko dashboard pe dikhata hai.

        if chart_type == "Bar Chart":
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"Bar Chart: {y_axis} vs {x_axis}")
        else:
            fig = px.line(df, x=x_axis, y=y_axis, title=f"Line Graph: {y_axis} vs {x_axis}")

        st.plotly_chart(fig)
else:
    st.info("Please upload a CSV file to start.")
