#10a
import plotly.graph_objects as go
import pandas as pd
data={
    'Date':pd.date_range(start='2023-01-01',periods=10,freq='D'),
    'Value':[10,12,13,15,17,18,20,22,23,26]
}
df=pd.DataFrame(data)
fig=go.Figure()
fig.add_trace(go.Scatter(x=df['Date'],y=df['Value'],mode='lines+markers',name='Time series'))
fig.update_layout(
    title='Time series plot',
    xaxis_title='Date',
    yaxis_title='Value'
)
fig.show()

#10b
import plotly.express as px
import pandas as pd
data=pd.read_csv('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv')
data=data.dropna(subset=['mag'])
data=data[data.mag>=0]
fig=px.scatter_geo(data,lat='latitude',lon='longitude',color='mag',hover_name='place',title='Earth quake around world')
fig.show()
