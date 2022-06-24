# A dropdown for sales by country - POWTÓRKA

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# sekcja przygotowań danych
ecom_sales = pd.read_csv("../dataset/ecom_sales.csv", sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link),
    html.H1("Sales breakdowns"),
    html.Div(children=[
        html.H2('Controls'),
        html.Br(),
        html.H3("Country Select"),
        # adding dropdown with id
        dcc.Dropdown(id='country_dropdown',
                     options=[{'label': 'UK', 'value': 'United Kingdom'},
                              {'label': 'GM', 'value': 'Germany'},
                              {'label': 'FR', 'value': 'France'},
                              {'label': 'AUS', 'value': 'Australia'},
                              {'label': 'HK', 'value': 'Hong Kong'}
                              ]
                     ),
        html.Div(children=[
            dcc.Graph(id='major_cat'),
            html.H2('Major Category')
        ])
    ]
    )
])


@app.callback(
    Output(component_id='major_cat', component_property='figure'),
    Input(component_id='country_dropdown', component_property='value')
)
def update_plot(input_country):
    country_filter = 'All Countries'
    sales = ecom_sales.copy(deep=True)
    if input_country:
        country_filter = input_country
        sales = sales[sales['Country'] == country_filter]
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(title=f'Sales in {country_filter}', data_frame=ecom_bar_major_cat, x='Total Sales ($)',
                               y='Major Category', color='Major Category',
                               color_discrete_map={'Clothes': 'blue', 'Kitchen': 'red', 'Garden': 'green',
                                                   'Household': 'yellow'})
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)
