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

logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/2bac9433b0e904735feefa26ca913fba187c0d55/e_com_logo.png'
# sekcja przygotowań danych
ecom_sales = pd.read_csv('..\dataset\ecom_sales.csv', sep=';')

ecom_bar_df = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)').sort_values(
    by='Total Sales ($)', ascending=False)
top_country = ecom_bar_df.loc[0]['Country']

# sekcja przygotowań wykresów
bar_fig_country = px.bar(data_frame=ecom_bar_df, x='Total Sales ($)', y='Country', color='Country',
                         color_discrete_map={'United Kingdom': 'lightblue', 'Germany': 'orange', 'France': 'darkblue',
                                             'Australia': 'green', 'Hong Kong': 'red'})

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div(children=[
    html.Img(src= logo_link),
    html.H1('Sales by Country'),
    html.Div(dcc.Graph(figure=bar_fig_country), style={'width':'750px', 'margin':'auto'}),
    html.Span(children=[
        'This year, the most sales came from:',
        html.B(top_country),
        html.I(' Copyright E-Com INC')
    ])
],
style={'text-align': 'center', 'fontsize': 22})

if __name__ == '__main__':
    app.run_server(debug=True)
