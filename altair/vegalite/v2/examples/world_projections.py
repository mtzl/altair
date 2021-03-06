"""
World Projections
-----------------
This example shows a map of the countries of the world using four available
geographic projections. For more details on the projections available in
Altair, see https://vega.github.io/vega-lite/docs/projection.html
"""
# category: geographic

import altair as alt
from vega_datasets import data

countries = alt.topo_feature(data.world_110m.url, 'countries')

base = alt.Chart(countries).mark_geoshape(
    fill='#666666',
    stroke='white'
).properties(
    width=300,
    height=180
)

projections = ['equirectangular', 'mercator', 'orthographic', 'gnomonic']
charts = [base.properties(title=proj, projection={'type': proj})
          for proj in projections]

alt.vconcat(
    alt.hconcat(*charts[:2]),
    alt.hconcat(*charts[2:])
)
