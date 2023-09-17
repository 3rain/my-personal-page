from dash import register_page, dcc, callback, Output, Input
from utils import priprava_dat
import dash_mantine_components as dmc
from plotly.express import bar

register_page(__name__, path='/analyza')

df = priprava_dat()  # Dataframe
print(df[["uzemi_txt", "vzdelani_txt", "hodnota"]])

layout = dmc.Stack([
    dmc.Select(
        id="vyber-uzemi",
        value="Česká republika",
        label="Vyberte oblast",
        data=[
            {"value": moznost, "label": moznost}
            for moznost in df['uzemi_txt'].drop_duplicates().sort_values()  # Vyplní slovník z hodnot v datech
        ]
    ),
    dcc.Graph(id='graf-vzdelani')
])


@callback(
    Output("graf-vzdelani", "figure"),
    Input("vyber-uzemi", "value")
)
def zobraz_graf(uzemi):
    w_df = df.copy()
    w_df = w_df[w_df["uzemi_txt"] == uzemi]
    w_df = w_df.groupby(by=["vzdelani_txt"])["hodnota"].sum().reset_index()

    fig = bar(w_df, x="vzdelani_txt", y="hodnota")
    return fig
