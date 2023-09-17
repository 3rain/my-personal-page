from dash import Dash, html, Input, Output, State, callback
import dash_mantine_components as dmc

app = Dash(__name__)

app.layout = html.Div([
    dmc.NumberInput(
        id="input-1",
        label="First Number",
    ),
    dmc.NumberInput(
        id="input-2",
        label="Second number",
    ),
    dmc.Button(
        "Click me",
        id='button-1'
    ),
    dmc.Text(id="result")
])


@callback(
    Output("result", "children"),
    Input("button-1", "n_clicks"),
    State("input-1", "value"),
    State("input-2", "value"),
    prevent_initial_call=True
)
def summ(n_clicks, result1, result2):
    return result1+result2


if __name__ == "__main__":
    app.run(debug=True)
