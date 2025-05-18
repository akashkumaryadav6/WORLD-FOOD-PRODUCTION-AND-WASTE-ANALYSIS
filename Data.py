from dash import *
import pandas as pd
import dash_bootstrap_components as dbc
from buttons import *
from datasets_load import *


datasets =  dbc.Container([
    html.Br(),
    html.Br(),
    html.Div([
        html.Div([
            "(Demo) World Food Production",
            html.Button([
                        'Save Dataset'
                        ], id='org', className="btn large btn-success"),
            dcc.Download(id='ddemo')
        ], className='row bttn'),
        html.Div([
            "(Org) World Food Production",
            html.Button([
                        'Save Dataset'
                        ], id='demo', className="btn large btn-success")
                        ,
            dcc.Download(id='dorg'),
        ], className='row bttn'),
        html.Div([
            "(Org) World Food Waste",
            html.Button([
                'Save Dataset', 
            ], id='worlddownload', className="btn large btn-success"),
            dcc.Download(id='worlddown')
        ], className="row bttn"),
        html.Div([
            "(Org) World Food Waste 2",
            html.Button([
                'Save Dataset', 
            ], id='world2download', className="btn large btn-success"),
            dcc.Download(id='world2down')
        ], className="row bttn"),
        html.Div([
            "India Food Import",
            html.Button([
                'Save Dataset', 
            ], id='importdrop', className="btn large btn-success"),
            dcc.Download(id='import')
        ], className="row bttn"),
        html.Div([
            "India Food Export",
            html.Button([
                'Save Dataset', 
            ], id='exportdrop', className="btn large btn-success"),
            dcc.Download(id='export')
        ], className="row bttn"),
        html.Hr()
    ], className='row text-center')
])

@callback(
    Output('world2down', 'data'),
    Input('world2download', 'n_clicks'),
    prevent_initial_call=True,
)
def waste2dataset(n_clicks):
    return dcc.send_data_frame(waste2.to_csv, 'World Food Waste 2.csv')

@callback(
    Output('worlddown', 'data'),
    Input('worlddownload', 'n_clicks'),
    prevent_initial_call=True,
)
def wastedataset(n_clicks):
    return dcc.send_data_frame(waste.to_csv, 'World Food Waste.csv')

@callback(
    Output('indiadown', 'data'),
    Input('indiadownload', 'n_clicks'),
    prevent_initial_call=True,
)
def wastedataset(n_clicks):
    return dcc.send_data_frame(foodindia.to_csv, 'World Food Waste.csv')

@callback(
    Output ('import', 'data'),
    Input('importdrop', 'n_clicks'),
    prevent_initial_call=True,
)
def demodataset(n_clicks):
    return dcc.send_data_frame(importx.to_csv, 'India Food Import.csv')

@callback(
    Output ('export', 'data'),
    Input('exportdrop', 'n_clicks'),
    prevent_initial_call=True,
)
def orgdataset(n_clicks):
    return dcc.send_data_frame(exportx.to_csv, 'India Food Export.csv')
