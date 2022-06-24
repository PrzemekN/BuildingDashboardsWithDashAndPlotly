# Controlling object layout

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_bar_major_cat = ecom_sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
ecom_bar_minor_cat = ecom_sales.groupby('Minor Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

# sekcja przygotowań wykresów
bar_fig_major_cat = px.bar(data_frame=ecom_bar_major_cat, x='Total Sales ($)', y='Major Category',
                           color='Major Category',
                           color_discrete_map={'Clothes': 'blue', 'Kitchen': 'red', 'Garden': 'green',
                                               'Household': 'yellow'})
bar_fig_minor_cat = px.bar(data_frame=ecom_bar_minor_cat, x='Total Sales ($)', y='Minor Category')

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link,
             # Add margin to the logo
             style={'margin': '30px 0px 0px 0px'}),
    html.H1('Sales breakdowns'),
    html.Div(children=[
        dcc.Graph(
            # Style the graphs to appear side-by-side
            figure=bar_fig_major_cat,
            style={'display': 'inline-block'}),
        dcc.Graph(
            figure=bar_fig_minor_cat,
            style={'display': 'inline-block'}),
    ]),
    html.H2('Major Category',
            # Style the titles to appear side-by-side with a 2 pixel border
            style={'display': 'inline-block', 'border': '2px solid black',
                   # Style the titles to have the correct spacings
                   'padding': '10px', 'margin': '10px 220px'}),
    html.H2('Minor Category',
            # Style the titles to appear side-by-side with a 2 pixel border
            style={'display': 'inline-block', 'border': '2px solid black',
                   # Style the titles to have the correct spacings
                   'padding': '10px', 'margin': '10px 220px'}),

], style={'text-align': 'center', 'font-size': 22})

if __name__ == '__main__':
    app.run_server(debug=True)
