# A dropdown for sales by country - additionla version

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'

# sekcja przygotowań danych
...

# sekcja przygotowań wykresów
...

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link),
    html.H1('Sales Breakdown'),
    html.Div(children=[
        html.H2('Controls'),
        html.Br(),
        html.H3('Country select'),

        html.Label('Choose proper country:'),
        dcc.Dropdown(id='country_dd', options=['United Kindgdom', 'Germany', 'France', 'Australia', 'Hong Kong'] )
    ]),
    html.Div(children=[
        dcc.Graph(id='major_cat'),
        html.H2('Major category')
    ])
])


@app.callback(
    Output(component_id='major_cat', component_property='figure'),
    Input(component_id='country_dd', component_property='value')
)
def update_plot(input_country):
    country_filter = 'All Countries'
    sales = ecom_sales.copy(deep=True)
    if input_country:
        country_filter = input_country
        sales = sales[sales['Country'] == country_filter]
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(
        title=f'Sales in {country_filter}', data_frame=ecom_bar_major_cat,
        x='Total Sales ($)', y='Major Category', color='Major Category'
    )
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)
