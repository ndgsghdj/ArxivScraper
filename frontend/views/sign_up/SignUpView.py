import flet as ft
from links.login import Authentication
from views.utils import WrongCreds
from flet_route import Params, Basket

class SignUpView:
    def __init__(self):
        pass
    def view(self, page: ft.Page, params: Params, basket: Basket):
        avatar = ft.Container(
            ft.CircleAvatar(content=ft.Icon(ft.icons.PERSON, size=50), width=80, height=80)
        )

        login_text = ft.Text("Sign Up", size=20)

        username_input = ft.TextField(
            label="Username",
            width=300,
            keyboard_type="email",
        )
        cont_username_input = ft.Container(username_input)
        cont_username_input.padding = ft.padding.all(20)

        email_input = ft.TextField(
            label="Email",
            width=300,
            keyboard_type="visiblePassword",
            can_reveal_password=True,
            password=True,
        )

        cont_email_input = ft.Container(email_input)
        cont_email_input.padding = ft.padding.only(bottom=20)

        password_input = ft.TextField(
            label="Password",
            width=300,
            keyboard_type="visiblePassword",
            can_reveal_password=True,
            password=True,
        )

        cont_password_input = ft.Container(password_input)
        cont_password_input.padding = ft.padding.only(bottom=20)

        password_confirm_input = ft.TextField(
            label="Confirm Password",
            width=300,
            keyboard_type="visiblePassword",
            can_reveal_password=True,
            password=True,
        )

        password_confirm_input.padding = ft.padding.only(bottom=20)

        sign_up = ft.TextButton(text="Already have an account? Login", on_click=lambda e: page.go("/login"))

        def on_click_signup(e):
            while True:
                if password_input.value != password_confirm_input.value:
                    WrongCreds(page, [password_input, password_confirm_input], ["", "Passwords do not match.", "Passwords do not match."]).set_error()
                    break
                if len(password_input.value) < 8:
                    WrongCreds(page, [password_input, password_confirm_input], ["", "Password must be at least 8 characters long.", "Password must be at least 8 characters long."]).set_error()
                    break
                if username_input.value == "":
                    WrongCreds(page, [username_input, password_input, password_confirm_input], ["Username is required.", "", ""]).set_error()
                    break
                if password_input.value == "":
                    WrongCreds(page, [username_input, password_input, password_confirm_input], ["", "Password is required.", ""]).set_error()
                    break
                if password_confirm_input.value == "":
                    WrongCreds(page, [username_input, password_input, password_confirm_input], ["", "", "Password confirmation is required."]).set_error()
                    break
                else:
                    break

            sign_up_response = Authentication(username_input.value, password_input.value, email=email_input.value).signup()
        
            if sign_up_response.status_code == 200:
                page.go("/login")
                page.update()
            
            elif sign_up_response.status_code == 400:
                WrongCreds(page, [username_input, password_input, password_confirm_input], ["Username is taken.", "", ""]).set_error()

            else:
                WrongCreds(page, [username_input, password_input, password_confirm_input], ["Try again later.", "", ""]).set_error()
        
        signup = ft.Container(
            ft.ElevatedButton(text="Sign Up", icon=ft.icons.PERSON_ADD, on_click=on_click_signup)
        )
        signup.padding = ft.padding.only(top=20)

        view = ft.View(
            "/signup",
            horizontal_alignment="center",
            vertical_alignment="center",
            controls=[
                avatar, login_text, cont_username_input, cont_email_input, cont_password_input, password_confirm_input, sign_up, signup
            ]
        )

        return view
