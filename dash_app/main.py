# -*- coding: utf-8 -*-
# Simple callback function to see changes in UI, 
# Run this file over terminal with command as 'gunicorn --workers 4 dash_app.main:server'


from dash import Dash, dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.run_server(debug=True)

df = pd.DataFrame({
  'student_id' : range(1, 11),
  'score' : [1, 5, 2, 5, 2, 3, 1, 5, 1, 5]
})

app.layout = html.Div([
    dcc.Dropdown(list(range(1, 6)), 1, id='score'),
	'was scored by this many students:',
	html.Div(id='output'),
])

@app.callback(Output('output', 'children'), Input('score', 'value'))
def update_output(value):
	filtered_df = df[df['score'] == value]
	return len(filtered_df)


# if __name__ == '__main__':
#     app.run_server(debug=True)