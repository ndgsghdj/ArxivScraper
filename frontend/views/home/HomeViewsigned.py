from flet import *
from flet_contrib.vertical_splitter import VerticalSplitter, FixedPane
from flet_route import Basket, Params

def HomeViewsigned(page: Page, params: Params, basket: Basket):
    con_left = Container(
        content=Column([
            ListTile(
                title=Text("PDFs"),
                leading=Icon(name="PDF"),
            ),
            Divider(),
            ListTile(
                title=Text("Upload new paper"),
                leading=Icon(name="add"),
            ),
        ])
    )

    exp_panel_list = ExpansionPanelList(
        expand_icon_color="red_400",
        controls=[
            ExpansionPanel(
                header=ListTile(title=Text("Your Account"), leading=Icon(name="Account")),
                content=Column([
                    ListTile(
                        title=Text("Information"),
                        leading=Icon(name="PDF"),
                    ),
                    ListTile(
                        title=Text("Log Out"),
                        leading=Icon(name="xx"),
                        on_click=lambda _: print("Log Out")
                    ),
                ])
            )
        ]
    )

    my_point = VerticalSplitter(
        expand=True,
        right_pane=Container(
            bgcolor="green200",
            content=exp_panel_list
        ),
        left_pane=con_left,
        fixed_pane_min_width=120,
        fixed_pane_width=200,
        fixed_pane_max_width=page.window_width - 25,
        fixed_pane=FixedPane.LEFT
    )

    return View(
        "/",
        controls=[
            my_point
        ]
    
    )
