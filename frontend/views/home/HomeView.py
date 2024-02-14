import flet as ft
import flet_material as fm
from flet_route import Params, Basket

# Home page with upload ArXiV link text input and submit button

def HomeView(page: ft.Page, params: Params, basket: Basket):
    # ArXiV link text input
    arxiv_link_input = ft.TextField(
        label="ArXiV link",
        width=500,
        keyboard_type="url",
    )
    arxiv_link_input.padding = ft.padding.all(20)

    # Submit button
    submit = ft.ElevatedButton(text="Submit", on_click=lambda e: page.go("/"))

    return ft.View(
        "/",
        horizontal_alignment="center",
        vertical_alignment="center",
        
        controls=[
            arxiv_link_input, submit
        ]
    )