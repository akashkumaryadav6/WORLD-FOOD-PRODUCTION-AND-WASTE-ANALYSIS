from tkinter import Scrollbar
from dash import *
import dash_bootstrap_components as dbc 
from Footer import footer

top_card = dbc.Card([
        dbc.CardImg(src="/static/Images/apple3.png", top=True, style={'height':'20rem','width':'20rem'}),
        dbc.CardBody([
            dbc.Input(id="name", placeholder="Name...", type="text", valid=True),
            dbc.Input(id="email", placeholder="E-mail", type="email", valid=True),
            dbc.Textarea(id='suggest',placeholder="Suggestion...", valid=True),
            dbc.Button("SUBMIT", className="me-1 shadow btn-dark"),
        ]),
    ], className='text-center mx-auto', style={'margin-top': '4rem', 'width': '23rem', 'margin-bottom': '3rem'})

cards = dbc.Row([
    dbc.Col(top_card, className='text-center mx-auto')
])

feedback = html.Div([cards, footer])