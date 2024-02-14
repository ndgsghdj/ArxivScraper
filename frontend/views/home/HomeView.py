from flet import *
from flet_contrib.vertical_splitter import VerticalSplitter, FixedPane

def HomeView(page: Page):
    # Left pane sign in 
    sign_in_button = ElevatedButton(text="Sign In", on_click=lambda e: print("Sign In"))
    log_in_button = ElevatedButton(text="Log In", on_click=lambda e: print("Log In"))
    left_pane_content = Column([
        ListTile(title=Text("Sign In"), on_click=lambda _: print("Sign In")),
        ListTile(title=Text("Log In"), on_click=lambda _: print("Log In")),
    ])
    left_pane = Container(bgcolor="blue200", content=left_pane_content)

    # Original Arxiv submission 
    arxiv_link_input = TextField(label="ArXiV link", width=500, keyboard_type="url")
    submit_button = ElevatedButton(text="Submit", on_click=lambda e: page.go("/"))
    right_pane_content = Column([
        arxiv_link_input,
        submit_button,
    ])
    right_pane = Container(bgcolor="green200", content=right_pane_content)

    my_point = VerticalSplitter(
        expand=True,
        right_pane=right_pane,
        left_pane=left_pane,
        fixed_pane_min_width=120,
        fixed_pane_width=200,
        fixed_pane_max_width=page.window_width - 25,
        fixed_pane=FixedPane.LEFT
    )

    centered_content = Container(
        content=my_point,
        horizontal_alignment="center",
        vertical_alignment="center"
    )

    page.add(centered_content)

app(main, view=AppView.WEB_BROWSER)

