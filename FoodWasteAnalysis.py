from dash import *
import dash_bootstrap_components as dbc
from buttons import *
from Footer import footer
from datasets_load import *

food_waste = html.Div([
    dbc.Container([
        html.Div([
            html.Div([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(
                            id='waste1',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='wastecountry',
                    placeholder='Select Country',
                    searchable=True,
                    options=waste.Country.unique(),
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='wastetype',
                    placeholder='Select Value Type',
                    searchable=True,
                    options=[{'label':'Loss Percentage', 'value':'Loss Percentage'},{'label':'Loss Quantity', 'value':'Loss Quantity'}],
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='wastedrop',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar','value':'bar'},{'label':'Scatter','value':'scatter'}],
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
                            id='waste2',
                        )
                    ], className='shadow drop2'),
                ],  className='graph drop'),
        ], className="col-md-10 mt-5 drop"),

        html.Div([
            dcc.Dropdown(
                    id='waste2drop',
                    placeholder='Select Basis of Comparison',
                    searchable=True,
                    options=[{'label':'Waste', 'value':'Waste'},{'label':'Organic Waste', 'value':'Organic Waste'}],
                    className='mb-3 drop'
                ),
                dcc.Dropdown(
                    id='waste2type',
                    placeholder='Select Chart Type',
                    searchable=True,
                    options=[{'label':'Bar', 'value':'bar'},{'label':'Scatter', 'value':'scatter'},{'label':'Scatter 3D', 'value':'scatter_3d'}],
                    className='mb-3 drop'
                ),
            ],  className="col-md-2 mt-5"),
        ], className="row"),
    ])
]), footer

@callback(
    Output('waste1','figure'),
    Input('wastecountry', 'value'),
    Input('wastetype', 'value'),
    Input('wastedrop', 'value')
)
def getfoodwastebytype(country, type_waste, drop):
    data=country if country else 'Afghanistan'
    type_waste= type_waste if type_waste else 'Loss Percentage'

    if drop == 'bar':
        return px.bar(waste[waste['Country']==data], y=type_waste, x='Stage', color='Year',
        title=data+' Food Waste by Sectors')
    else:
        return px.scatter(waste[waste['Country']==data], y=type_waste, x='Stage', color='Year',
        title=data+' Food Waste by Sectors')        

@callback(
    Output('waste2','figure'),
    Input('waste2drop', 'value'),
    Input('waste2type','value')
)
def getfoodwastebyLocation(col, value2):
    data=col if col else "Waste"   
    type=value2 if value2 else 'scatter' 
    df=waste2.sort_values(data, ascending=False).head(20)
    if type == 'bar':
        if data == 'Waste':
            return px.bar(df, x='Country Name', y=data,
            title='Top 20 Food Wasting Countries')
        else:
            return px.bar(df, x='Country Name', y=data,
            title='Top 20 Organic Waste Countries')
    elif type=='scatter_3d':
        if data=='Waste':
            return px.scatter_3d(df, x='Country Name', y=data, z='Organic Waste',
            title='Low Organic Waste = Low Food Waste and vice-versa')
        else:
            return px.scatter_3d(df, x='Country Name', y=data, z='Waste',
            title='Low Organic Waste = Low Food Waste and vice-versa')
    else:
        if data == 'Waste':
            return px.scatter(df, x='Country Name', y=data,
            title='Top 20 Food Wasting Countries')
        else:
            return px.scatter(df, x='Country Name', y=data,
            title='Top 20 Organic Waste Countries')
  