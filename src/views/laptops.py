from flet import (
    View, AppBar,
    Container, Row, Column,
    ScrollMode,
)
from components import KingtongCompatibilityContainer, POWEContainer, NoJomoContainer
from asyncio import create_task

class LaptopsView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = "/laptops"
        self.appbar = AppBar(
            title="Buscar Cargadores, Baterias, etc.",
        )
        self.expand = True
        self.controls = [
            Column(
                controls=[
                    KingtongCompatibilityContainer(),
                    Row(
                        controls=[
                            POWEContainer(),
                            NoJomoContainer(),
                        ],
                        expand=True,
                    ),
                ],
                expand=True,
                scroll=ScrollMode.AUTO,
            ),
        ]

    def did_mount(self) -> None:
        self.page.overlay.clear()
        self.page.update()

    def will_unmount(self) -> None:
        self.page.overlay.clear()
        self.page.update()
