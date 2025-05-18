from dash import *
import dash_bootstrap_components as dbc
from buttons import *
from Footer import footer
from datasets_load import *

region = html.Div([
    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='geo1',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='yearlist',
                    placeholder='Select Year',
                    searchable=True,
                    options=list(range(1961,2014)),
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='itemlist',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='optionlist',
                    placeholder='Select Option',
                    searchable=True,
                    options=[{'label':'Open Street Style','value':'open-street-map'}, {'label':'Carto Positron Style','value':'carto-positron'}, {'label':'Carto Darkmatter Style','value':'carto-darkmatter'}],
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
                            id='geowaste',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='wastelist',
                    placeholder='Select Type',
                    searchable=True,
                    options=[{'label':'Food Waste', 'value':'Waste'},{'label':'Organic Waste', 'value':'Organic Waste'}],
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='optionlistwaste',
                    placeholder='Select Option',
                    searchable=True,
                    options=[{'label':'Open Street Style','value':'open-street-map'}, {'label':'Carto Positron Style','value':'carto-positron'}, {'label':'Carto Darkmatter Style','value':'carto-darkmatter'}],
                    className='mb-3 drop'
                )
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ])
]), footer

@callback(
    Output('geo1', 'figure'),
    Input('itemlist', 'value'),
    Input('optionlist', 'value'),
    Input('yearlist', 'value')
)
def getfoodproductionbyCategory(item, option, year):
    year2 = str(year) if year else "2013"
    item2 = item if item else "Wheat"
    option2 = option if option else "open-street-map"
    reg=foodorg[foodorg['Item'] == item2]
    fig = px.scatter_mapbox(reg,
                            lat="latitude", 
                            lon="longitude", 
                            color=year2,
                            hover_name="Country", 
                            size=year2,
                            hover_data=[year2], 
                            size_max=40, 
                            zoom=1,
                            width=900, height=600,
                            title = f'World Map for Food Production for the {item2} of {year2}')
    fig.update_layout(mapbox_style=option2)
    return fig

@callback(
    Output('geowaste', 'figure'),
    Input('wastelist', 'value'),
    Input('optionlistwaste', 'value')
)
def getfoodwastebyLocation(waste, option):
    type=waste if waste else 'Waste'
    options=option if option else 'open-street-map'
    fig = px.scatter_mapbox(waste2,
                            lat="Latitude", 
                            lon="Longitude", 
                            color=type,
                            hover_name="Country Name", 
                            size_max=25, 
                            zoom=1,
                            size=type,
                            width=900, height=500,
                            title = f'World Map for {type}')
    fig.update_layout(mapbox_style=options)
    return fig