# Switching to Darkmode

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
logo_link = 'https://assets.datacamp.com/production/repositories/5893/datasets/1c95273e21a54b5ca48e0b03cc0c1faeafb3d7cd/e-comlogo_white.png'
ecom_category_df = ecom_sales.groupby(['Major Category', 'Minor Category']).size().reset_index(
    name='Total Orders').sort_values(by='Total Orders', ascending=False).reset_index(drop=True)
top_category = ecom_category_df.loc[0]['Minor Category']

# sekcja przygotowań wykresów
ecom_bar_fig = px.bar(data_frame=ecom_category_df, x='Total Orders', y='Minor Category', color='Major Category')
# Set the font color of the bar chart
ecom_bar_fig.update_layout(
    {'yaxis': {'dtick': 1, 'categoryorder': 'total ascending'}, 'paper_bgcolor': 'black', 'font': {'color': 'white'}})

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div([
    # Set the new white-text image
    html.Img(src=logo_link, style={'width': '165px', 'height': '50px'}),
    html.Div(dcc.Graph(figure=ecom_bar_fig, style={'width': '500px', 'height': '350px', 'margin': 'auto'})),
    html.Br(),
    html.Span(children=[
        'The Topcategory was: ',
        html.B(top_category),
        html.Br(),
        html.I('Copyright Pymon 2022')
    ])
], style={'text-align': 'center', 'font-size': 22,
          # Update the background color to the entire app
          'background-color': 'black',
          # Change the text color for the whole app
          'color': 'white'
          })

if __name__ == '__main__':
    app.run_server(debug=True)
