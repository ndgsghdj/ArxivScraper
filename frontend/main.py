import flet as ft
import flet_material as fm

fm.Theme.set_theme(theme="blue")

# Your main method with all your components
def main(page: ft.Page):
    page.bgcolor = fm.Theme.bgcolor

    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    def show_notification(e):
        badge.notification += 1
        badge.add_notification(badge.notification)

    btn = ft.ElevatedButton(on_click=lambda e: show_notification(e))

    badge = fm.NotificationBadge(title="Hello!", size="md", notification=0)

    page.add(badge)
    page.add(btn)

    page.update()


if __name__ == "__main__":
   ft.app(target=main)