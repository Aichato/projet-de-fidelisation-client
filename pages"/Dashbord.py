import streamlit as st  # web development
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import time  # to simulate a real time data, time loop
import plotly.express as px  # interactive charts

# read csv
df = pd.read_csv("churn_modeling.csv")
df = df.replace(to_replace=["Spain", "Germany", "France"], value=["Niamey", "Maradi", "Tahoua"])
df = df.drop(['RowNumber', 'Surname'], axis=1)
df = df.set_index('CustomerId')

st.set_page_config(
    page_title='Real-Time Client Dashboard',
    page_icon='✅',
    layout='wide'
)

# dashboard title

st.title("Tableau de Bord")

# top-level filters

geo_filter = st.selectbox("Selectionner la region", pd.unique(df['Geography']))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter

df = df[df['Geography'] == geo_filter]

# near real-time / live feed simulation

for seconds in range(200):
    # while True:

    df['age_new'] = df['Age'] * np.random.choice(range(1, 5))
    df['balance_new'] = df['Balance'] * np.random.choice(range(1, 5))

    # creating KPIs
    avg_age = np.mean(df['age_new'])

    count_gender = int(df[(df["Gender"] == 'Female')]['Gender'].count() + np.random.choice(range(1, 30)))

    balance = np.mean(df['balance_new'])

    with placeholder.container():
        # create three columns
        kpi1, kpi2, kpi3 = st.columns(3)

        # fill in those three columns with respective metrics or KPIs
        kpi1.metric(label="Age ⏳", value=round(avg_age), delta=round(avg_age) - 10)
        kpi2.metric(label="Female Count ", value=int(count_gender), delta=- 10 + count_gender)
        kpi3.metric(label=" Balance ", value=f"$ {round(balance, 2)} ",
                    delta=- round(balance / count_gender) * 100)

        # create two columns for charts

        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig = px.density_heatmap(data_frame=df, y='age_new', x='Gender')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x='age_new')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)
