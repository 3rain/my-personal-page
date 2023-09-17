from dash import Dash, html, Input, Output, State, callback, page_container
from utils import navigacny_panel
import dash_mantine_components as dmc

app = Dash(__name__, use_pages=True)

links = {
    "o-mne": {"label": "O mně"},
    "projekty": {"label": "Projekty"},
    "zkusenosti": {"label": "Zkušenosti"},
    "kontakty": {"label": "Kontakty"},
    "analyza": {"label": "Analýza sčítání"},
}

app.layout = dmc.MantineProvider([
    navigacny_panel(links, "tabler:square-rounded-letter-o"),
    html.Div(page_container, style={"margin-top": "40px"}),
],
    theme={"colorScheme": "dark"},
    withGlobalStyles=True,
    id="provider-temy"
)


@callback(
    Output("provider-temy", "theme"),
    Input("tlacidlo-zmena-temy", "n_clicks"),
    State("provider-temy", "theme"),
    prevent_initial_call=True
)
def zmen_temu(n_clicks, tema):
    if tema["colorScheme"] == "dark":
        return {"colorScheme": "light"}
    else:
        return {"colorScheme": "dark"}


if __name__ == "__main__":
    app.run(debug=False)
