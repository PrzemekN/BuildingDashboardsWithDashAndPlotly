# Adding an HTML list to Dash

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# sekcja przygotowań danych
...
# sekcja przygotowań wykresów
...

app = Dash(__name__)

# sekcja rozmieszczenia elementów graficznych
app.layout = html.Div(children=[])

if __name__ == '__main__':
    app.run_server(debug=True)
