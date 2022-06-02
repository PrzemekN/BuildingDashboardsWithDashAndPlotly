import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
ecom_sales_df = pd.read_csv('./dataset/ecom_sales.csv', sep=';')

ecom_line_df = ecom_sales_df.groupby('Year-Month')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
ecom_bar_df = ecom_sales_df.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

max_country = ecom_bar_df.sort_values(by='Total Sales ($)', ascending=False).loc[0]['Country']

# sekcja przygotowań wykresów
line_fig = px.line(data_frame=ecom_line_df, x='Year-Month', y='Total Sales ($)', title='TotalSales by Month')
bar_fig = px.bar(data_frame=ecom_bar_df, x='Total Sales ($)', y='Country', orientation='h',
                 title='Total Sales by Country')


app = Dash(__name__)

#sekcja rozmieszczenia elementów graficznych
app.layout = html.Div(children=[
    html.H1('Sales Figure'),
 html.H3(f'The largest country by sales was: {max_country}'),
    html.Div(dcc.Graph(id='line-figure', figure=line_fig)),
    html.Div(dcc.Graph(id='bar-figure', figure=bar_fig))
])

if __name__ == '__main__':
    app.run_server(debug=True)
