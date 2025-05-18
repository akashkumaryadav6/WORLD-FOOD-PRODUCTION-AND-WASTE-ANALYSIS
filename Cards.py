import dash_bootstrap_components as dbc
from dash import html

# Reusable function for card creation
def create_card(title, subtitle, image_path, link):
    return html.Div(
        html.A(
            dbc.Card(
                [
                    dbc.CardImg(src=image_path, top=True, style={"opacity": 0.4}),
                    dbc.CardImgOverlay(
                        dbc.CardBody([html.H4(title, className="card-title"),
                                      html.P(subtitle, className="card-text",
                                            )])
                    ),
                ],
                className="shadow"
            ),
            href=link,
            className='nav'
        ),
        className="col-4 mb-4",
    )

cards = html.Div(
    [
        html.Div(
            [
                create_card("Food Category Analysis", "Food on the basis of categories", "/static/Images/b-g-1.png", "/foodcategory"),
                create_card("Timeline Analysis", "Travel through various years of food production", "/static/Images/b-g-2.png", "/timeline"),
                create_card("Regional Analysis", "Various Countries and their particular representation", "/static/Images/b-g-8.png", "/region"),
                create_card("Food Waste Analysis", "Do you waste food? How much?", "/static/Images/bg4.png", "/foodwaste"),
                create_card("The Scrapper", "Live news source and extraction", "/static/Images/b-g-7.png", "/scrapper"),
                create_card("Datasets", "Get the dataset and start your discovering", "/static/Images/b-g-9.png", "/dataset"),
            ],
            className="row",
        ),
        html.Br(),
        html.Div([''], className="row"),
    ],
    className="container",
    style={"margin-top": "5rem"},
)