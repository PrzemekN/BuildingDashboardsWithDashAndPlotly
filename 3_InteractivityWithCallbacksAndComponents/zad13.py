# Date picker for sales data

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from datetime import datetime, date

# sekcja przygotowań danych
ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'

# zmieniamy kolumne z luzną datą na typ datowy:
ecom_sales['InvoiceDate'] = pd.to_datetime(ecom_sales['InvoiceDate'])

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link, style={'margin': '30px 0px 0px 0px'}),
    html.H1('Sales breakdowns'),
    html.Div(children=[
        html.Div(children=[
            html.H2('Controls'),
            html.Br(),
            html.H3('Sale Date Select'),
            # Tworzymy komponent 'single date picker' z identyfikatorem
            dcc.DatePickerSingle(
                id='sale_date',
                # ustawiamy min i maximum dla datepicera jako najmniejsza i najwieksza wartosc z dataframe
                min_date_allowed=ecom_sales['InvoiceDate'].min(),  # zawezamy pole wyboru do min
                max_date_allowed=ecom_sales['InvoiceDate'].max(),  # zaweżamy pole wyboru do max
                # ustawiamy date ktora pokarze sie jako startowa date
                date=date(2011, 4, 11),  # jaka data będzie ustawiona/wybrana na początku.
                initial_visible_month=date(2011, 4, 11),  # po kliknięciu na date pojawi sie popup z kalendarzem
                # i ta zmienna mowi nam jaki miesiac pojawi sie.To pobiera/extraktuje miesiac wiec mozna podac
                # datetime.now i samo zadba o pobranie miesiaca.
                style={'width': '200px', 'margin': '0 auto'}
            )
        ], style={'width': '350px', 'height': '350px', 'display': 'inline-block', 'vertical-align': 'top',
                  'border': '1px solid black', 'padding': '20px'}),
        html.Div(children=[
            dcc.Graph(id='sales_cat'),
            html.H2('Daily sales by Major Category',
                    style={'border': '2px solid black', 'width': '400px', 'margin': '0 auto'}),
        ], style={'width': '700px', 'display': 'inline-block'})
    ])
], style={'text-align': 'center', 'display': 'inline-block', 'width': '100%'})


@app.callback(
    # output wskazuje ktory element zostanie zmieniony przy uzyciu zwroconej wartosci wyzwalanej funkcji.
    Output(component_id='sales_cat', component_property='figure'),
    Input(component_id='sale_date', component_property='date')
)
def update_plot(input_date):
    sales = ecom_sales.copy(deep=True)
    if input_date:
        sales = sales[sales['InvoiceDate'] == input_date]

    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
    bar_fig_major_cat = px.bar(title=f'Sales on: {input_date}', data_frame=ecom_bar_major_cat, orientation='h',
                               x='Total Sales ($)', y='Major Category')
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)
