import pandas as pd
import plotly_express as px

ecom_sales = pd.read_csv('../dataset/ecom_sales.csv', sep=';')
ecom_sales = ecom_sales.groupby('Country')['OrderValue'].agg('sum').reset_index(name='Total Sales ($)')

bar_fig = px.bar(data_frame=ecom_sales, x='Total Sales ($)', y='Country', orientation='h', color='Country')
bar_fig.update_layout({'bargap': 0.5})
bar_fig.show()
