#!/bin/env python3
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash
import dash_table
import pandas as pd

df = pd.read_csv('./export_jira_dataframe.csv')

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True)
