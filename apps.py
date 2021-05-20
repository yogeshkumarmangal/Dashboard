import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import dropbox
# Step 1. Launch the application
app = dash.Dash(__name__)
# Step 2. Import the dataset
dbx = dropbox.Dropbox("5uSdWA0gd2UAAAAAAAAAAauPVaO_t_nlwRgP3YzwZ8-2HlxYFWRLUrmTAgk4F4b7")
for entry in dbx.files_list_folder('').entries:
   aa=entry.name
   dd=entry.name
   if aa=='Dashboards.csv':
       bb=entry.id
       resultresult =dbx.files_get_temporary_link(bb)
       cc=resultresult.link
   if dd=="DasboardTable.csv":
      ee=entry.id
      resultresult =dbx.files_get_temporary_link(ee)
      ff=resultresult.link
      
st = pd.read_csv(cc)
df = pd.read_csv(ff)
# dropdown options
features = ['Count','Critical']
opts = [{'label' : i, 'value' : i} for i in features]

# range slider options
st['Date'] = pd.to_datetime(st.Date)
# Step 3. Create a plotly figure
fig = go.Figure(data=[
    go.Bar(name='Total Test', x=st.Date, y=st['Count']),
    go.Bar(name='Critical', x=st.Date, y=st['Critical'])])
fig.update_layout(barmode='group')
# Step 4. Create a Dash layout
app.layout = html.Div([
                # adding a header and a paragraph
                html.Div([
                    html.H1("Acculi Labs Pvt. Ltd."),
                    html.P("Lyfas")
                         ], 
                    style = {'padding' : '50px' , 
                             'backgroundColor' : '#3aaab2'}),
# adding a plot        
                dcc.Graph(id = 'plot', figure = fig),
                html.Div(
                    children=[
                        html.Div(
                            children="Date Range",
                            className="menu-title"
                            ),
                        dcc.DatePickerRange(
                            id="date-range",
                            min_date_allowed=st.Date.min().date(),
                            max_date_allowed=st.Date.max().date(),
                            start_date=st.Date.min().date(),
                            end_date=st.Date.max().date(),
                        ),
                        dash_table.DataTable(
                           id='table',
                           columns=[{"name":i,"id":i} for i in df.columns],
                           data=df.to_dict('records')
                           )
                     
                    ]
                ),
                      ])
                            
                

# Step 5. Add callback functions
@app.callback(Output('plot', 'figure'),
             [ Input("date-range", "start_date"),
        Input("date-range", "end_date"),])
def update_charts(start_date, end_date):
    mask = (
        (st.Date >= start_date)
        & (st.Date <= end_date)
    )
    filtered_data = st.loc[mask, :]
    fig = go.Figure(data=[
    go.Bar(name='Total Test', x=filtered_data['Date'], y=filtered_data['Count']),
    go.Bar(name='Critical', x=filtered_data['Date'], y=filtered_data['Critical'])])
    fig.update_layout(barmode='group')
    return fig
    # updating the plot
  
# Step 6. Add the server clause
if __name__ == "__main__":
        app.run_server(debug=False)
