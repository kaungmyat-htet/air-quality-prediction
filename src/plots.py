import streamlit as st
import altair as alt
import pandas as pd

df = pd.read_csv('./src/test.csv')
df['datetime'] = df['date'] + ' ' + df['time']
print(df)

df_melted = df.melt(id_vars=['datetime'], value_vars="no,no2,so2,o3,pm2_5,pm10,nh3".split(','),
                    var_name='pollutant', value_name='value')

hover = alt.selection_single(
    fields=["datetime"],
    nearest=True,
    on="mouseover",
    empty=False,
)

lines = (
    alt.Chart(df_melted, title="Evolution of Air Pollution")
    .mark_line()
    .encode(
        x="datetime",
        y="value:Q",
        color="pollutant:N",
    )
)

points = lines.transform_filter(hover).mark_circle(size=65)

tooltips = (
    alt.Chart(df)
    .mark_rule()
    .encode(
        x="yearmonthdate(date)",
        y="pm2_5",
        opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
        tooltip=[
            alt.Tooltip("date", title="Date"),
            alt.Tooltip("pm2_5", title="PM 2.5"),
        ],
    )
    .add_selection(hover)
)

data_layer = lines + points + tooltips

combined_chart = alt.vconcat(data_layer)
st.altair_chart(combined_chart, use_container_width=True)