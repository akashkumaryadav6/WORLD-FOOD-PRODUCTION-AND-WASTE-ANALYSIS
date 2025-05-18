from dash import *
import dash_bootstrap_components as dbc
from datasets_load import *
from Footer import footer

time_line = html.Div([
    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='item-total',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='itemtotal-drop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ]),
    html.Br(),

    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='item-max',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='itemmax-drop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ]),
    html.Br(),

    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='item-avg',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='itemavg-drop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop shadowdrop'
                ),
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ])
]), footer

@callback(
    Output('item-avg','figure'),
    Input('itemavg-drop', 'value')
)
def getTimelineDatamean(value):
    data=value if value else 'Wheat'
    return px.bar(foodorg[foodorg['Item'] == data][cols].mean().T,
    title=data+' Production over the year [1961-2013][Average]',
    labels={'index':'Years', 'value':'Quantity Measure (Tonnes)', 'variable':data},
    color_discrete_sequence=['rgba(72, 219, 251, 0.7)'])

@callback(
    Output('item-total','figure'),
    Input('itemtotal-drop', 'value')
)
def getTimelineDatatotal(value):
    data=value if value else 'Wheat'
    return px.bar(foodorg[foodorg['Item'] == data][cols].sum().T,
    title=data+' Production over the year [1961-2013][Total]',
    labels={'index':'Years', 'value':'Quantity Measure (Tonnes)', 'variable':data},
    color_discrete_sequence=['rgba(72, 219, 251, 0.7)'])

@callback(
    Output('item-max','figure'),
    Input('itemmax-drop', 'value')
)
def getTimelineDatamax(value):
    data=value if value else 'Wheat'
    return px.bar(foodorg[foodorg['Item'] == data][cols].max().T,
    title=data+' Production over the year [1961-2013][Maximum]',
    labels={'index':'Years', 'value':'Quantity Measure (Tonnes)', 'variable':data},
    color_discrete_sequence=['rgba(72, 219, 251, 0.7)'])  

