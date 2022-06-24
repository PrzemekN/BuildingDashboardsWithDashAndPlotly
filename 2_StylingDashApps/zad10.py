# A refined sales dashboard
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
ecom_line = ecom_sales.groupby('Year-Month')['OrderValue'].agg('sum').reset_index(name='TotalSales')
ecom_bar = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='TotalSales')

# sekcja przygotowań wykresów
line_fig = px.line(data_frame=ecom_line, x='Year-Month', y='TotalSales', title='Total Sales by Month')
line_fig.update_layout({'paper_bgcolor': 'rgb(224,255, 252)'})
bar_fig = px.bar(data_frame=ecom_bar, x='TotalSales', y='Country', orientation='h', title='Total Sales by Country')
bar_fig.update_layout(
    {'yaxis': {'dtick': 1, 'categoryorder': 'total ascending'}, 'paper_bgcolor': 'rgb(224, 255, 252)'})

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div(children=[
    html.Div(children=[
        html.Img(src=logo_link, style={'display': 'inline-block', 'margin': '25px'}),
        html.H1(children=[
            'Sales Figures'
        ], style={'display': 'inline-block'}),
        html.Img(src=logo_link, style={'display': 'inline-block', 'margin': '25px'})
    ]),
    html.Div(
        dcc.Graph(figure=line_fig), style={'width': '500px', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.Div(
        dcc.Graph(figure=bar_fig), style={'width': '350px', 'display': 'inline-block', 'margin': '5px'}
    ),
    html.H3(f'The largest order quantity was {ecom_sales.Quantity.max()}')
], style={'text-align': 'center', 'font-size': 22, 'background-color': 'rgb(224, 255, 252)'})

if __name__ == '__main__':
    app.run_server(debug=True)
