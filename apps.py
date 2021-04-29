import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
data=pd.read_csv("Dashboards.csv")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
app = dash.Dash(__name__)
server=app.server
app.layout = html.Div(
    children=[
        html.H1(children="Acculi Lbas Pvt.Ltd.",),
        html.H2(children="Lyfas",),
        html.P(
            children=""
            ""
            " ",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Count"],
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Test Number"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Critical"],
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Critical Patient Number"},
            },
        ),
    ]
)

