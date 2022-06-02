import dash
# import dash_core_components as dcc - DEPRECATED !
from dash import dcc
# import dash_html_components as html - DEPRECATED !
from dash import html
import pandas as pd
import plotly.express as px

ecom_sales = pd.read_csv('./dataset/ecom_sales.csv', sep=';')

ecom_line = ecom_sales.groupby(['Year-Month', 'Country'])['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

line_graph = px.line(data_frame=ecom_line, x='Year-Month', y='Total Sales ($)', title='Total Sales by Month',
                     color='Country')
bar_graph = px.bar(data_frame=ecom_bar, x='Total Sales ($)', y='Country', orientation='h',
                   title='Total Sales by Country')

# create the Dash App
app = dash.Dash(__name__)

# Set up the layout using an overall div
app.layout = html.Div(children=[
    # add a H1
    html.H1("Sales by country & Over Time"),
    # add both graphs
    dcc.Graph(id='line_graph', figure=line_graph),
    dcc.Graph(id='bar_graph', figure=bar_graph)
])

if __name__ == '__main__':
    app.run_server(debug=True)
