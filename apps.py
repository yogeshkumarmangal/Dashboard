import flask
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
data=pd.read_xlsx("Dashboard.xlsx")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d")
data.sort_values("Date", inplace=True)
app = dash.Dash(__name__)
server=app.server
app.layout = html.Div(
    children=[
        html.H1(children="Acculi Lbas Pvt.Ltd.",),
        html.H2(children="March Data Analytics",),
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
                "layout": {"title": "Total Test in March"},
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
                "layout": {"title": "Total Test in March"},
            },
        ),
    ]
)

