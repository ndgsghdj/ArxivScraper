import flet as ft
import flet_material as fm

fm.Theme.set_theme(theme="blue")

# Your main method with all your components
def main(page: ft.Page):
    page.title = "PDF reader"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please Enter PDF file needed"
            page.update()
        else:
            PDF = txt_name.value
            page.clean()

    txt_name = ft.TextField(label="PDF Link")

    page.add(txt_name, ft.ElevatedButton("Enter", on_click=btn_click))


ft.app(target=main, view=ft.AppView.WEB_BROWSER)
