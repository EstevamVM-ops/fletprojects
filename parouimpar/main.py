import flet as ft
def main(page: ft.Page):
    counter = ft.Text("0", size=50,data=0)
    def increment_click(e: ft.Event[ft.FloatingActionButton]):
        counter.data += 1
        counter.data.value = str(counter.data)
    page.floating_actionbutton= ft.FloatingActionButton(
        icon=ft.icons.ADD, key="increment", on_click=increment_click

    )
    page.add(
        ft.SafeArea(
            expand=True,
            content=ft .container(
                content=counter,
                alignment=ft.Alignment.CENTER,

            )
        )
    )