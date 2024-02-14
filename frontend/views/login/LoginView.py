import flet as ft
import flet_material as fm
from flet_route import Params, Basket
from links.login import Authentication
from views.utils import WrongCreds

def LoginView(page: ft.Page, params: Params, basket: Basket):

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

    sign_up = ft.TextButton(text="Don't have an account? Sign up", on_click=lambda e: page.go("/signup"))

    def on_click_login(e):
        login = Authentication(username_input.value, password_input.value).login()
    
        if login.status_code == 200:
            page.session.set("authenticated", True)
            page.go("/")
            page.update()
        else:
            WrongCreds(page, [username_input, password_input], ["Wrong username or password.", "Wrong username or password."]).set_error()

    login = ft.Container(
        ft.ElevatedButton(text="Login", icon=ft.icons.LOGIN, on_click=on_click_login)
    )
    login.padding = ft.padding.only(top=20)

    return ft.View(
        "/login",
        horizontal_alignment="center",
        vertical_alignment="center",
        
        controls=[
            avatar, login_text, cont_username_input, password_input, sign_up, login
        ]
    )