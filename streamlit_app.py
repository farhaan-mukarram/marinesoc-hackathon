import streamlit as st
import pandas as pd

df = pd.read_csv("./data.csv")

# drop 2nd and 3rd column (decimal month and figure name)
cols_to_drop = [2, 3]

data = df.drop(df.columns[cols_to_drop], axis=1)


agg_data_by_year_region = (
    data.groupby(["Year", "Sea_Area"])[
        "Monthly_Average_Sea_Surface_Temperature_degrees_C"
    ]
    .mean()
    .reset_index()
)

sea_areas = sorted(list(pd.unique(agg_data_by_year_region["Sea_Area"])))

st.header("Sea Temperature Variation by Region")
selected_sea_area = st.selectbox(
    "Region",
    sea_areas,
)

is_selected_sea_area = agg_data_by_year_region["Sea_Area"] == selected_sea_area

if selected_sea_area:
    filtered_agg_yearly_data_by_region = agg_data_by_year_region[
        is_selected_sea_area
    ].drop(["Sea_Area"], axis=1)

    st.line_chart(
        filtered_agg_yearly_data_by_region,
        x="Year",
        y="Monthly_Average_Sea_Surface_Temperature_degrees_C",
        y_label="Avg. Sea Surface Temp",
    )


st.header("Credits")
st.markdown(
    "Data source: [Scottish Marine Directorate Coastal Observatory Data](https://data.marine.gov.scot/dataset/scottish-coastal-observatory-data/resource/7d3483aa-c8ad-4652-91fc-b0ca84d496b7#{view-graph:{graphOptions:{hooks:{processOffset:{},bindEvents:{}}}},graphOptions:{hooks:{processOffset:{},bindEvents:{}}}})"
)
