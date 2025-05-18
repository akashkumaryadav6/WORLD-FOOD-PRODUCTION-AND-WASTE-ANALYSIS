from dash import html
import dash_bootstrap_components as dbc

def cardimg(title, subtitle, img_path):
    return dbc.Container([
    dbc.Card([
        dbc.CardImg(src=img_path, top=True, style={"opacity": 0.2},),
        dbc.CardImgOverlay(
            dbc.CardBody([html.H6(title, className="title"),
                          html.P([subtitle], className="card-text1"),
            ])
        )
    ], className='shadow')
], className="pt-5")


card_img = html.Div(
    [
        html.Div(
            [
                cardimg("World Food Supply & Waste Analysis", "A Collective dashboard for food production & waste over the years", "/static/Images/ooter.jpg"),
            ],
            className="row",
        ),
        html.Br(),
        html.Div([''], className="row"),
    ],
    className="container",
    style={"margin-top": "5rem"},
)