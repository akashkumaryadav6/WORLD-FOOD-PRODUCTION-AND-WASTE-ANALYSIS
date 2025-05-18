import dash
import dash_bootstrap_components as dbc
from dash import *

explore_btn = html.Div([
        dbc.Button([
            "EXPLORE MORE"
        ], className="bttn shadow")
], className="text-center")

save_report = html.Button(
                        'Save Report', 
                        className="btn large btn-success"
                    )
save_datasetorg = html.Button([
                        'Save Dataset'
                        ], id='org', className="btn large btn-dark")
save_datasetdemo = html.Button([
                        'Save Dataset'
                        ], id='demo', className="btn large btn-dark")
                        

