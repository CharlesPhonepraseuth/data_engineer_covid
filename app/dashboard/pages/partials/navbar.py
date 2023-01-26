import dash_bootstrap_components as dbc


def create_navbar():

    navbar = dbc.NavbarSimple(
        children = [
            dbc.DropdownMenu(
                nav = True,
                in_navbar = True,
                label = "Menu",
                children = [
                    dbc.DropdownMenuItem("Accueil", href = '/'),
                    dbc.DropdownMenuItem(divider = True),
                    dbc.DropdownMenuItem("Covid", href = '/covid')
                ],
            ),
        ],
        brand = "Dashboard",
        brand_href = "/",
        sticky = "top",
        color = "dark",
        dark = True
    )

    return navbar
