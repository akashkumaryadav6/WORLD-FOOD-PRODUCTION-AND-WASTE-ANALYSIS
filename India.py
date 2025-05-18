from dash import *
import dash_bootstrap_components as dbc
from datasets_load import *
from Footer import footer

def plotindia2():
    fig = px.line(data_frame=foodindia.drop(columns=['Commodity']).sum(),
    labels={'value':'Quantity Measure (Tonnes)', 'index':'Years', 'variable':'India'},
    title = 'India Food Production over the years [2013 - 2019][Total]',
    color_discrete_sequence=['brown'])
    return fig

def plotindia3():
    fig = px.line(data_frame=foodindia.drop(columns=['Commodity']).max(),
    labels={'value':'Quantity Measure (Tonnes)', 'index':'Years', 'variable':'India'},
    title = 'India Food Production over the years [2013 - 2019][Maximum]',
    color_discrete_sequence=['brown'])
    return fig

def plotindia4():
    fig = px.line(data_frame=foodindia.drop(columns=['Commodity']).mean(),
    labels={'value':'Quantity Measure (Tonnes)', 'index':'Years', 'variable':'India'},
    title = 'India Food Production over the years [2013 - 2019][Average]',
    color_discrete_sequence=['brown'])
    return fig
    
india_graphs = html.Div([
    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='india',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='indiadrop',
                    placeholder='Select Year',
                    searchable=True,
                    options=list((range(2013,2020))),
                    className='mb-3 shadow'
                ),
                html.Hr(),
                html.Button([
                        'Download Dataset', 
                ], id='indiadownload', className="btn large btn-info"),
                dcc.Download(id='indiadown')
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
                            id='item'
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='itemdrop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodindia,
                    className='mb-3 shadow'
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
                            id='year2',
                            figure=plotindia2()
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
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
                            id='year3',
                            figure=plotindia3()
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
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
                            id='year4',
                            figure=plotindia4()
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
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
                            id='cerealwise',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='cerealwisedrop',
                    placeholder='Select Cereal',
                    searchable=True,
                    options=item_listcereals,
                    className='mb-3 shadow'
                ),
                dcc.Dropdown(
                    id='cerealdrop',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar','value':'bar'},{'label':'Line','value':'line'},{'label':'Scatter','value':'scatter'}],
                    className='mb-3 shadow'
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
                            id='fruitwise',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='fruitwisedrop',
                    placeholder='Select Fruit',
                    searchable=True,
                    options=item_listfruits,
                    className='mb-3 shadow'
                ),
                dcc.Dropdown(
                    id='fruitdrop',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar','value':'bar'},{'label':'Line','value':'line'},{'label':'Scatter','value':'scatter'}],
                    className='mb-3 shadow'
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
                            id='vegwise',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='vegwisedrop',
                    placeholder='Select Vegetable',
                    searchable=True,
                    options=item_listveg,
                    className='mb-3 shadow'
                ),
                dcc.Dropdown(
                    id='vegdrop',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar','value':'bar'},{'label':'Line','value':'line'},{'label':'Scatter','value':'scatter'}],
                    className='mb-3 shadow'
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
                            id='oilwise',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='oilwisedrop',
                    placeholder='Select Seed',
                    searchable=True,
                    options=item_listoilseeds,
                    className='mb-3 shadow'
                ),
                dcc.Dropdown(
                    id='oildrop',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar','value':'bar'},{'label':'Line','value':'line'},{'label':'Scatter','value':'scatter'}],
                    className='mb-3 shadow'
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
                            id='cropswise',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='cropswisedrop',
                    placeholder='Select Crop',
                    searchable=True,
                    options=item_listcrops,
                    className='mb-3 shadow'
                ),
                dcc.Dropdown(
                    id='cropsdrop',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar','value':'bar'},{'label':'Line','value':'line'},{'label':'Scatter','value':'scatter'}],
                    className='mb-3 shadow'
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
                            id='importpie',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='importpiedrop',
                    placeholder='Select Year',
                    searchable=True,
                    options=list(range(2012,2021)),
                    className='mb-3 shadow'
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
                            id='EXportpie',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='EXportpiedrop',
                    placeholder='Select Year',
                    searchable=True,
                    options=list(range(2012,2021)),
                    className='mb-3 shadow'
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
                            id='comparepie',
                        )
                    ], className='shadow'),
                ],  className='graph drop'),
            ], className="col-md-10 mt-5 drop"),
                
        html.Div([
            html.Div([], className='row'),
                dcc.Dropdown(
                    id='IMpiedrop',
                    placeholder='Select Year of Import',
                    searchable=True,
                    options=[str(x)+ ' Import' for x in range(2012,2021)],
                    className='mb-3 shadow'
                ),
                dcc.Dropdown(
                    id='EXpiedrop',
                    placeholder='Select Year of Export',
                    searchable=True,
                    options=[str(x)+ ' Export' for x in range(2012,2021)],
                    className='mb-3 shadow'
                ),
                # html.Button([
                #     'Download as Image'
                # ], id='downloadcompare'),
                # dcc.Download(id='down-compare')
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ])
]), footer

@callback(
    Output('india', 'figure'),
    Input('indiadrop', 'value')
)
def plotindia(value):
    data = value if value else '2013'
    fig = px.bar(foodindia, x=str(data),
        labels={'value':'Quantity Measure (Tonnes)', 'Index':'Commodity','variable':str(data), 'color':'Category'},
        title="India Food Production in year "+str(data),
        color=item_listfoodindia)
    return fig

@callback(
    Output('item', 'figure'),
    Input('itemdrop', 'value')
)
def plotindia(value):
    data = value if value else 'Pulses'
    fig = px.bar(foodindia[foodindia['Commodity'] == data][['2013','2014','2015','2016','2017','2018','2019']].T,
        labels={'value':'Quantity Measure (Tonnes)', 'Index':'Crop', 'index':'Years', 'color':'Legend'},
        title=data+" Production over the years",
        color=['2013','2014','2015','2016','2017','2018','2019'])
    return fig

@callback(
    Output('cerealwise', 'figure'),
    Input('cerealwisedrop','value'),
    Input('cerealdrop','value')
)
def cerealwise(crop, type):
    data=crop if crop else "Jowar"
    if type=='bar':
        return px.bar(cereals[cereals['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Cereals production in India [2013-2019]['+data+']',
        color_discrete_sequence=['orange'])
    elif type=='scatter':
        return px.scatter(cereals[cereals['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Cereals production in India [2013-2019]['+data+']',
        color_discrete_sequence=['orange'])
    else:
        return px.line(cereals[cereals['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Cereals production in India [2013-2019]['+data+']',
        color_discrete_sequence=['orange'])

@callback(
    Output('fruitwise', 'figure'),
    Input('fruitwisedrop','value'),
    Input('fruitdrop','value')
)
def fruitwise(crop, type):
    data=crop if crop else "Apple"
    if type=='bar':
        return px.bar(fruits[fruits['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Fruits production in India [2013-2019]['+data+']',
        color_discrete_sequence=['red'])
    elif type=='scatter':
        return px.scatter(fruits[fruits['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Fruits production in India [2013-2019]['+data+']',
        color_discrete_sequence=['red'])
    else:
        return px.line(fruits[fruits['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Fruits production in India [2013-2019]['+data+']',
        color_discrete_sequence=['red'])

@callback(
    Output('vegwise', 'figure'),
    Input('vegwisedrop','value'),
    Input('vegdrop','value')
)
def vegwise(crop, type):
    data=crop if crop else "Okra"
    if type=='bar':
        return px.bar(veg[veg['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Vegetables production in India [2013-2019]['+data+']',
        color_discrete_sequence=['green'])
    elif type=='scatter':
        return px.scatter(veg[veg['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Vegetables production in India [2013-2019]['+data+']',
        color_discrete_sequence=['green'])
    else:
        return px.line(veg[veg['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Vegetables production in India [2013-2019]['+data+']',
        color_discrete_sequence=['green'])

@callback(
    Output('oilwise', 'figure'),
    Input('oilwisedrop','value'),
    Input('oildrop','value')
)
def oilseedswise(crop, type):
    data=crop if crop else "Sunflower"
    if type=='bar':
        return px.bar(oilseeds[oilseeds['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Oilseeds production in India [2013-2019]['+data+']',
        color_discrete_sequence=['black'])
    elif type=='scatter':
        return px.scatter(oilseeds[oilseeds['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Oilseeds production in India [2013-2019]['+data+']',
        color_discrete_sequence=['black'])
    else:
        return px.line(oilseeds[oilseeds['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Oilseeds production in India [2013-2019]['+data+']',
        color_discrete_sequence=['black'])

@callback(
    Output('cropswise', 'figure'),
    Input('cropswisedrop','value'),
    Input('cropsdrop','value')
)
def cropswise(crop, type):
    data=crop if crop else "Cocoa"
    if type=='bar':
        return px.bar(crops[crops['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Plantation Crops production in India [2013-2019]['+data+']')
    elif type=='scatter':
        return px.scatter(crops[crops['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Plantation Crops production in India [2013-2019]['+data+']')
    else:
        return px.line(crops[crops['Commodity'] == data][['2013', '2014', '2015', '2016', '2017', '2018', '2019']].T,
        labels={'index':'Years', 'value':'Quantity Measure (Million Tonnes)'},
        title='Plantation Crops production in India [2013-2019]['+data+']')


@callback(
    Output('importpie', 'figure'),
    Input('importpiedrop', 'value')
)
def pie(value):
    data=str(value) if value else '2012'
    return px.pie(importx.sort_values(data, ascending=False), values=data,                
        color_discrete_sequence=['violet'],
        height=550, width=690, hole=0.6, 
        hover_name=item_listimportx,
        title=f'India Food Import for the year {data}')

@callback(
    Output('EXportpie', 'figure'),
    Input('EXportpiedrop', 'value')
)
def pie(value):
    data=str(value) if value else '2012'
    return px.pie(exportx.sort_values(data, ascending=False), values=data,                
        color_discrete_sequence=['red'],
        height=550, width=690, hole=0.6, 
        hover_name=item_listexportx,
        title=f'India Food Export for the year {data}')

@callback(
    Output('comparepie', 'figure'),
    # Output('down-compare', 'data'),
    Input('EXpiedrop', 'value'),
    Input('IMpiedrop', 'value')
    # Input('downloadcompare', 'n_clicks')
)
def compare(value1,value2):
    imp=value2 if value2 else '2012 Import'
    exp=value1 if value1 else '2012 Export'
    fig=px.scatter_3d(data_frame=exchange, 
        x='Commodity', 
        y=imp, 
        z=exp, 
        color='Commodity', 
        title=f'Comparison of {exp} and {imp}')
    return fig
# def down(n_clicks):
#     compare()
#     if not os.path.exists('C:/Users/user/Downloads/PLOTLY'):
#         os.mkdir('C:/Users/user/Downloads/PLOTLY')
#     return pio.write_image(fig, 'C:/Users/user/Downloads/PLOTLY/compare.png')
    

