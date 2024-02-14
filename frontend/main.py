import flet as ft
import flet_material as fm
from routing.ExtendedRouting import ExtendedRouting, ExtendedPath
from views.login.LoginView import LoginView
from views.sign_up.SignUpView import SignUpView
from views.home.HomeView import HomeView

fm.Theme.set_theme(theme="blue")

# Your main method with all your components
def main(page: ft.Page):
    page.theme_mode = "light"
    app_routes = [
        ExtendedPath(
            url="/login",
            clear=True,
            view=LoginView,
            protected=False
        ),
        ExtendedPath(
            url="/signup",
            clear=True,
            view=SignUpView().view,
            protected=False
        ),
        ExtendedPath(
            url="/",
            clear=True,
            view=HomeView,
            protected=True
        )
    ]
    ExtendedRouting(
        page=page,
        app_routes=app_routes
    )
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="./assets")