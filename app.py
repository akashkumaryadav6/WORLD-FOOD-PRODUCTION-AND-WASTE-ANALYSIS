import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, html, dcc, callback
from Navbar import navbar
from Cardimg import card_img
from Cards import cards
from Footer import footer
from Datasets import dataset
from About import about
from Contact import feedback
from TimeLineAnalysis import time_line
from RegionAnalysis import region
from FoodWasteAnalysis import food_waste
from FoodDataScrapper import scrapper
from FoodCategoryAnalysis import food_category
from India import india_graphs
from Data import datasets

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP, 'https://cdnjs.cloudflare.com/ajax/libs/mdb-ui-kit/4.1.0/mdb.min.css'], suppress_callback_exceptions=True, title="World Food Supply and Waste Analysis")

server = app.server

index = [card_img, cards]

app.layout = html.Div([dcc.Location(id="url", refresh=False),navbar,  
html.Div([], id="page-content", className="pt-5")])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)

def pages(pathname):
    if pathname == '/':
        return index
    elif pathname == '/datasets':
        return dataset
    elif pathname == '/dataset':
        return datasets
    elif pathname == '/about':
        return about
    elif pathname == '/feedback':
        return feedback
    elif pathname == '/timeline':
        return time_line
    elif pathname == '/region':
        return region
    elif pathname == '/scrapper':
        return scrapper
    elif pathname == '/foodwaste':
        return food_waste
    elif pathname == '/foodcategory':
        return food_category
    elif pathname == '/india':
        return india_graphs
    else:
        return index
   

if __name__ == "__main__":
    app.run_server(debug=True, port=8888)