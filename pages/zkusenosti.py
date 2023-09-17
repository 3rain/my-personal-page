from dash import register_page
import dash_mantine_components as dmc

register_page(__name__, path='/zkusenosti')

layout = dmc.Text("Zkušenosti")
