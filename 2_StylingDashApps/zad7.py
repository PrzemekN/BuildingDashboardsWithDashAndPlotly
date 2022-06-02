# Adding an HTML list to Dash
'''
    tags:
    .Br() - new line break,
    .Img() - insert an image, zarówno loklalny plik jaki z servera np htlm.Img(src='www.website.com/logo.png')
    .Ul() - for unordered lists,
    .Ol() - for ordered list (ponumerowane punkty),
    .Li() - for each liest element ??,
    .P() - for insert plain text - moze zawierac children,
    .Span() - for insert plain text - moze zawierac children,
    .B() - bold some text
    .I() - Italizice some text
'''

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
ecom_category_df = ecom_sales.groupby(['Major Category', 'Minor Category']).size().reset_index(
    name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
num1_category, num1_salesvol = ecom_category_df.loc[0].tolist()[1:3]
num2_category, num2_salesvol = ecom_category_df.loc[1].tolist()[1:3]

# sekcja przygotowań wykresów
ecom_bar = px.bar(data_frame=ecom_category_df, x='Total Orders', y='Minor Category', color='Major Category')
ecom_bar.update_layout({'yaxis': {'dtick': 1, 'categoryorder': 'total ascending'}})

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    html.Img(src=logo_link),
    html.H1('Top Sales Category'),
    html.Div(dcc.Graph(figure=ecom_bar)),
    html.Span(children=[
        html.Ol(children=[
            html.Li(children=[num1_category, ' with ', num1_salesvol, ' sales volume']),
            html.Li(children=[num2_category, ' with ', num2_salesvol, ' sales volume'])
        ], style={'width': '350px', 'margin': 'auto'}),
        html.Br(),
        html.I('Copyright Pymon Sp.z o.o.')
    ])
], style={'text-align': 'center', 'font-size': 22})

if __name__ == '__main__':
    app.run_server(debug=True)
