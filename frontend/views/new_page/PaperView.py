import flet as ft
import flet_material as fm
from flet_route import Params, Basket
from links.papers import Papers
import html2text


def get_llm_response(p: Papers, query: str):
    response = p.query_paper(query=query)
    return response["response"]


def get_paper_text(p: Papers, id: str):
    response = p.get_paper(id)
    return response["paper_html"]


def PaperView(page: ft.Page, params: Params, basket: Basket):
    page.controls.clear()
    page.update()

    p = Papers(token=page.session.get("token"), url=basket.get("url"))

    paper_id = params.get("paper_id")
    if not paper_id:
        return ft.View(
            "/",
            horizontal_alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Text("No paper id")
            ]
        )

    keywords = get_llm_response(p=p, query=get_paper_text(p=p, id=paper_id))

    keyword_text = ft.Row(
        wrap=True,
        controls=[
            ft.ListView(
                controls=[
                    ft.Text(keyword) for keyword in keywords
                ]
            )
        ]
    )

    page.add(keyword_text)

    return ft.View(
        "/paper/:paper_id",
        horizontal_alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        scroll="AUTO",
        controls=[
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=page.controls
            )
        ]
    )
