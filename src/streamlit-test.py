import streamlit as st
import altair as alt
import pandas as pd
from vega_datasets import data

df = pd.read_csv('./test.csv')
df['datetime'] = df['date'] + ' ' + df['time']
print(df)

df_melted = df.melt(id_vars=['datetime'], value_vars="no,no2,so2,o3,pm2_5,pm10,nh3".split(','),
                    var_name='pollutant', value_name='value')

# @st.cache_data
# def get_data():
#     source = data.stocks()
#     source = source[source.date.gt("2004-01-01")]
#     return source

# stock_data = get_data()
# print(stock_data, 'stock data')

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

lines1 = (
    alt.Chart(df, title="Evolution of Air Pollution")
    .mark_line()
    .encode(
        x="datetime",
        y="co",
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

# ANNOTATIONS = [
#     ("Sep 01, 2007", 450, "🙂", "Something's going well for GOOG & AAPL."),
#     ("Nov 01, 2008", 220, "🙂", "The market is recovering."),
#     ("Dec 01, 2007", 750, "😱", "Something's going wrong for GOOG & AAPL."),
#     ("Dec 01, 2009", 680, "😱", "A hiccup for GOOG."),
# ]
# annotations_df = pd.DataFrame(
#     ANNOTATIONS, columns=["date", "price", "marker", "description"]
# )
# annotations_df.date = pd.to_datetime(annotations_df.date)

# annotation_layer = (
#     alt.Chart(annotations_df)
#     .mark_text(size=20, dx=-10, dy=0, align="left")
#     .encode(x="date:T", y=alt.Y("price:Q"), text="marker", tooltip="description")
# )

combined_chart = alt.vconcat(data_layer, lines1)
st.altair_chart(combined_chart, use_container_width=True)