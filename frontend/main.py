import flet as ft
import flet_material as fm
from links.login import Login
from links.papers import Papers
import utils

fm.Theme.set_theme(theme="blue")

# Your main method with all your components
def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "light"
    page.window_resizable = False
    page.title = "PaperKey"
    page.theme = ft.theme.Theme(color_scheme_seed="blue")
    page.window_height = page.window_height - 100
    page.window_width = page.window_width - 200

    avatar = ft.Container(
        ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON, size=50), width=80, height=80)
    )

    login_text = ft.Text("Login", size=20)

    username_input = ft.TextField(
        label="Username",
        width=300,
        keyboard_type="email",
    )
    cont_username_input = ft.Container(username_input)
    cont_username_input.padding = ft.padding.all(20)

    password_input = ft.TextField(
        label="Password",
        width=300,
        keyboard_type="visiblePassword",
        can_reveal_password=True,
        password=True,
    )

    password_input.padding = ft.padding.only(top=20)

    sign_up = ft.TextButton(text="Don't have an account? Sign up")

    def on_click_login(e):
        login = Login(username_input.value, password_input.value).login()
    
        if login.status_code == 200:
            page.go("/dashboard")
            papers = Papers(token=login.json()["access_token"]).get_papers() # placeholder
            print(papers)
            page.update()
        else:
            utils.wrong_creds(page, username_input, password_input)

    login = ft.Container(
        ft.ElevatedButton(text="Login", icon=ft.icons.LOGIN, on_click=on_click_login)
    )
    login.padding = ft.padding.only(top=20)

    page.add(avatar, login_text, cont_username_input, password_input, sign_up, login)


ft.app(target=main, assets_dir="./assets")