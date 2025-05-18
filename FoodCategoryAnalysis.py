from dash import *
import dash_bootstrap_components as dbc
from datasets_load import *
from Footer import footer

food_category = html.Div([
    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='itemtotal',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='itemtotaldrop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
            dcc.Dropdown(
                id='count2',
                placeholder='Select Count',
                searchable=True,
                options=[{'label':'Top 5 Countries', 'value':5},{'label':'Top 10 Countries', 'value':10},{'label':'Top 20 Countries', 'value':20}],
                className='mb-3 drop'
            )
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
                            id='itemmax',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='itemmaxdrop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
            dcc.Dropdown(
                id='count3',
                placeholder='Select Count',
                searchable=True,
                options=[{'label':'Top 5 Countries', 'value':5},{'label':'Top 10 Countries', 'value':10},{'label':'Top 20 Countries', 'value':20}],
                className='mb-3 drop'
                )
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
                            id='itemavg',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='itemavgdrop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
            dcc.Dropdown(
                id='count4',
                placeholder='Select Count',
                searchable=True,
                options=[{'label':'Top 5 Countries', 'value':5},{'label':'Top 10 Countries', 'value':10},{'label':'Top 20 Countries', 'value':20}],
                className='mb-3 drop'
            )
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
                            id='topby_year',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                id='topby_itemdrop',
                placeholder='Select Item',
                searchable=True,
                options=item_listfoodorg,
                className='mb-3 drop'
            ),
            dcc.Dropdown(
                id='topby_yeardrop',
                placeholder='Select Year',
                searchable=True,
                options=years,
                className='mb-3 drop'
            ),
            dcc.Dropdown(
                id='count',
                placeholder='Select Count',
                searchable=True,
                options=[{'label':'Top 5 Countries', 'value':5},{'label':'Top 10 Countries', 'value':10},{'label':'Top 20 Countries', 'value':20}],
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
                            id='cropworld',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='cropworlddrop',
                    placeholder='Select Item',
                    searchable=True,
                    options=item_listfoodorg,
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='cropyeardrop',
                    placeholder='Select Year',
                    searchable=True,
                    options=list(range(1961,2014)),
                    className='mb-3 drop'
                ),
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ])
]), footer

@callback(
    Output('itemtotal','figure'),
    Input('itemtotaldrop', 'value'),
    Input('count2', 'value')
)
def getUniqueCategorytotal(value,value2):
    count=value2 if value2 else 20
    crop = value if value else "Wheat"
    yearly_total_df = foodorg[[str(i) for i in range(1961,2014)]].sum(axis=1)
    copy = foodorg.copy(deep=True)
    copy["Total"] = yearly_total_df
    req_cols = copy[["Country","Item","Total"]]
    crop_df = req_cols[req_cols['Item'] == crop]

    top_20_df = crop_df.sort_values('Total',ascending=False)[:count]
    
    fig = px.bar(
        top_20_df,
        title=f"Top {count} {crop} producing countries [Total]",
        labels={"Total": "Quantity"},
        x='Country',
        y="Total",
        color='Total'
    )
    return fig

@callback(
    Output('itemmax','figure'),
    Input('itemmaxdrop', 'value'),
    Input('count3', 'value')
)
def getUniqueCategorymax(value,value2):
    count=value2 if value2 else 20
    crop = value if value else "Wheat"
    yearly_max_df = foodorg[[str(i) for i in range(1961,2014)]].max(axis=1)
    copy = foodorg.copy(deep=True)
    copy["Max"] = yearly_max_df
    req_cols = copy[["Country","Item","Max"]]
    crop_df = req_cols[req_cols['Item'] == crop]

    top_20_df = crop_df.sort_values('Max',ascending=False)[:count]
    
    fig = px.bar(
        top_20_df,
        title=f"Top {count} {crop} producing countries [Max]",
        labels={"Max": "Quantity"},
        x='Country',
        y="Max",
        color='Max'
    )
    return fig

@callback(
    Output('itemavg','figure'),
    Input('itemavgdrop', 'value'),
    Input('count4', 'value')
)
def getUniqueCategorymean(value,value2):
    count=value2 if value2 else 20
    crop = value if value else "Wheat"
    yearly_mean_df = foodorg[[str(i) for i in range(1961,2014)]].mean(axis=1)
    copy = foodorg.copy(deep=True)
    copy["Mean"] = yearly_mean_df
    req_cols = copy[["Country","Item","Mean"]]
    crop_df = req_cols[req_cols['Item'] == crop]

    top_20_df = crop_df.sort_values('Mean',ascending=False)[:count]
    
    fig = px.bar(
        top_20_df,
        title=f"Top {count} {crop} producing countries [Average]",
        labels={"Mean": "Quantity"},
        x='Country',
        y="Mean",
        color='Mean'
    )
    return fig

@callback(
    Output('cropworld','figure'),
    Input('cropworlddrop','value'),
    Input('cropyeardrop','value')
)
def getUniqueCategory(crop, year):
    data=crop if crop else "Wheat"
    years=str(year) if year else "2013"
    return px.bar(foodorg[foodorg['Item'] == data],
            x='Country',
            y=years,
            title=(data+' Production'),
            labels={'variable':'Year', 'index':'Country', 'value':'Quantity Measure (Tonnes)'})

@callback(
    Output('topby_year', 'figure'),
    Input('topby_yeardrop', 'value'),
    Input('topby_itemdrop', 'value'),
    Input('count', 'value')
)
def topby_year(value,value2,value3):
    year=str(value) if value else '1961'
    item=value2 if value2 else 'Wheat'
    count=value3 if value3 else 20 
    return px.bar(foodorg[foodorg['Item']==item].sort_values(year, ascending=False).head(count), 
        x='Country', 
        y=year, 
        color=year,
        title=f'Top {count} {item} producing countries for the year {year}',
        labels={year:'Quantity'})