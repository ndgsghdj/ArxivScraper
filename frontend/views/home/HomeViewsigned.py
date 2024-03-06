from flet import *
from flet_contrib.vertical_splitter import VerticalSplitter, FixedPane
from flet_route import Basket, Params
from links.papers import Papers
import asyncio


def HomeViewsigned(page: Page, params: Params, basket: Basket):
    page.controls.clear()
    page.update()

    def fetch_papers():
        p = Papers(token=page.session.get("token"), url=basket.get("url"))
        papers = p.get_papers()
        return papers

    con_left_contents = [
        ListTile(
            title=Text("Upload new paper"),
            leading=Icon(name="add"),
            on_click=lambda _: page.go("/paper")
        ),
        Divider(),
    ]
    papers = fetch_papers()
    for paper in papers:
        con_left_contents.append(
            ListTile(
                title=Text(paper["paper_name"]),
                leading=Icon(name="insert_drive_file"),
                on_click=lambda _: page.go(f"/paper/{paper['paper_id']}")
            ))

    con_left = Container(
        content=Column(con_left_contents)
    )

    exp_panel_list = ExpansionPanelList(
        expand_icon_color="red_400",
        controls=[
            ExpansionPanel(
                header=ListTile(title=Text("Your Account"),
                                leading=Icon(name="Account")),
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

    page.controls.append(my_point)

    return View(
        "/",
        controls=page.controls

    )
