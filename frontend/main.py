import flet as ft
import flet_material as fm
from routing.ExtendedRouting import ExtendedRouting, ExtendedPath
from views.login.LoginView import LoginView
from views.sign_up.SignUpView import SignUpView
from views.home.HomeViewsigned import HomeViewsigned
from views.new_page.NewPageView import NewPageView
from views.new_page.PaperView import PaperView

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
            view=HomeViewsigned,
            protected=True
        ),
        ExtendedPath(
            url="/paper",
            clear=True,
            view=NewPageView,
            protected=False
        ),
        ExtendedPath(
            url="/paper/:paper_id",
            clear=True,
            view=PaperView,
            protected=False
        )
    ]
    ExtendedRouting(
        page=page,
        app_routes=app_routes
    )
    page.go(page.route)

if __name__ == "__main__":
    ft.app(target=main, assets_dir="./assets")