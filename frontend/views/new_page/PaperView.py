import flet as ft
import flet_material as fm
from flet_route import Params, Basket
from links.papers import Papers
import html2text

def get_html(url: str):
    p = Papers(token="", url=url)
    response = p.get_paper()
    return response["html"]

def PaperView(page: ft.Page, params: Params, basket: Basket):

    h = html2text.HTML2Text()
    h.ignore_links = True
    paper = ft.Text(h.handle(get_html("https://arxiv.org/html/2402.05137v1")))
    return ft.View(
        "/paper",
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="AUTO",
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.Text(h.handle(get_html("https://arxiv.org/html/2402.05137v1")))
                ]
            )
        ]
    )