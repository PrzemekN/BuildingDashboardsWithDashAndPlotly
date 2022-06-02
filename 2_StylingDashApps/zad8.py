# Styling a Dash app with CSS

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
ecom_sales_df = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_category_df = ecom_sales_df.groupby(['Major Category', 'Minor Category']).size().reset_index(
    name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
top_category = ecom_category_df.iloc[0]['Minor Category']

# sekcja przygotowań wykresów
ecom_bar_fig = px.bar(data_frame=ecom_category_df, x='Total Orders', y='Minor Category', color='Major Category')
ecom_bar_fig.update_layout(
    {'yaxis': {'dtick': 1, 'categoryorder': 'total ascending'}, 'paper_bgcolor': 'rgb(224, 255, 252)'})

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link, style={'width': '215px', 'height': '240px'}),
    html.H1('TopSales Categories'),
    html.Div(dcc.Graph(figure=ecom_bar_fig, style={'width': '500px', 'height': '350px', 'margin': 'auto'})),
    html.Br(),
    html.Span(children=[
        'The top category was: ',
        html.B(top_category),
        html.Br(),
        html.I('Copyright Pymon 2022', style={'background-color': 'lightgray'})
    ])
], style={'text-align': 'center', 'font-size': '22px', 'background-color': 'rgb(224,255,252)'})

if __name__ == '__main__':
    app.run_server(debug=True)
