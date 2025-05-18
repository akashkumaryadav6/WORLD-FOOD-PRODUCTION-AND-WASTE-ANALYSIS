from dash import html, Input, Output, State, callback
import dash_bootstrap_components as dbc

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar_component = dbc.Row(
    [
        dbc.Col(dbc.NavLink("Home", href="/",className='nav')),
        dbc.Col(dbc.NavLink("INDIA", href="/india",className='nav')),
        dbc.Col(dbc.NavLink("Dataset", href="/datasets",className='nav')),
        dbc.Col(dbc.NavLink("About", href="/about",className='nav')),
        dbc.Col(dbc.NavLink("Contact", href='/feedback',className='nav')),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                    dbc.Col(
                        dbc.NavbarBrand("Dashboard", className="ms-2")
                    ),
                ],
                align="center",
                className="g-0",
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                navbar_component,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="light",
    dark=False,
    class_name="fixed-top shadow"    
)


@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
