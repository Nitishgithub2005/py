#9
import plotly.express as px
df=px.data.iris()
fig=px.scatter_3d(df,x='sepal_width',y='sepal_length',z='petal_width',color='species')
fig.show()
