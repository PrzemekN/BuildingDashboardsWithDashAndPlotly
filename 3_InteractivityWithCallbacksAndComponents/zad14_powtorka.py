# A date picker callback

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from datetime import datetime, date

# sekcja przygotowań danych
ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/fdbe0accd2581a0c505dab4b29ebb66cf72a1803/e-comlogo.png'
ecom_sales['InvoiceDate'] = pd.to_datetime(ecom_sales['InvoiceDate'])

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link),
    html.H1('Sales breakdown'),
    html.Div(
        children=[
            html.Div(
                children=[
                    html.H2("Controls"),
                    html.Br(),
                    html.H3('Sale date Select'),
                    dcc.DatePickerSingle(id='sale_date',
                                         min_date_allowed=ecom_sales['InvoiceDate'].min(),
                                         max_date_allowed=ecom_sales['InvoiceDate'].max(),
                                         initial_visible_month=date(2011, 4, 1),
                                         date=date(2011, 4, 11)
                                         )
                ]
            ),
            html.Div(children=[
                dcc.Graph(id='sales_cat'),
                html.H2('daily sales by Major category')
            ])
        ]
    )
])


# sekcja callback
@app.callback(
    Output(component_id='sales_cat', component_property='figure'),
    Input(component_id='sale_date', component_property='date')
)
def update_plot(input_date):
    # Ensure the DataFrame is not overritne
    sales = ecom_sales.copy(deep=True)
    if input_date:
        sales = sales[sales['InvoiceDate'] == input_date]
    ecom_bar_major_cat = sales.groupby('Major Category')['OrderValue'].agg('sum').reset_index(
        name='Total Sales ($)')
    bar_fig_major_cat = px.bar(title=f'Sales on {input_date}', data_frame=ecom_bar_major_cat,
                               orientation='h', x='Total Sales ($)', y='Major Category')
    # return the figure to render
    return bar_fig_major_cat


if __name__ == '__main__':
    app.run_server(debug=True)
