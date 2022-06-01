import dash
# import dash_core_components as dcc - DEPRECATED !
from dash import dcc
import pandas as pd
import plotly.express as px

ecom_sales = pd.read_csv('./dataset/ecom_sales.csv', sep=';')
ecom_sales = ecom_sales.groupby(['Year-Month', 'Country'])['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
line_fig = px.line(data_frame=ecom_sales, x='Year-Month', y='Total Sales ($)', title='Total Sales by month',
                   color='Country')

app = dash.Dash(__name__)
app.layout = dcc.Graph(id='my_first_graph', figure=line_fig)

if __name__ == '__main__':
    app.run_server(debug=True)
