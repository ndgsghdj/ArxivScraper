import flet as ft
import flet_material as fm
from flet_route import Params, Basket
from links.papers import Papers
from uuid import uuid4
import html2text


def get_html(p: Papers):
    response = p.scrape_paper()
    return response["html"]

def NewPageView(page: ft.Page, params: Params, basket: Basket):
    if page.controls:
        page.controls.clear()
        page.update()

    link_textfield = ft.TextField(
        label="ArXiV link",
        width=500,
        keyboard_type="url"
    )

    name_textfield = ft.TextField(
        label="Name",
        width=500,
        keyboard_type="text"
    )

    h = html2text.HTML2Text()
    h.ignore_links = True

    def handle_submit(e):
        if link_textfield.value and name_textfield.value:
            data = {
                "paper_id": str(uuid4()),
                "paper_url": {"url": link_textfield.value},
                "paper_name": name_textfield.value,
                "paper_keywords": ""
            }
            p = Papers(token=page.session.get("token"), url=link_textfield.value)
            data["paper_html"] = str(h.handle(get_html(p=p)))
            p.post_paper(data=data)
            page.go(f"/paper/{data['paper_id']}")
            basket.url = link_textfield.value
        else:
            print("No data")

    submit_button = ft.ElevatedButton(
        text="Submit",
        on_click=handle_submit
    )

    page.add(link_textfield, name_textfield, submit_button)
    page.update()

    return ft.View(
        "/paper",
        horizontal_alignment="center",
        vertical_alignment="center",
        controls=page.controls
    )
