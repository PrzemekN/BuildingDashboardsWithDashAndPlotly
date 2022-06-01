import pandas as pd
import plotly_express as px
ecom_sales = pd.read_csv('./dataset/ecom_sales.csv', sep=';')
print(ecom_sales.head(10))
print(ecom_sales.columns)
# ecom_sales = ecom_sales.groupby(['Year-Month', 'Country'])['OrderValue'].agg('sum')
ecom_sales = ecom_sales.groupby(['Year-Month', 'Country'])['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')
print(ecom_sales)
print(ecom_sales.info())

line_graph = px.line(data_frame=ecom_sales, x='Year-Month', y='Total Sales ($)', color='Country')
line_graph.show()
