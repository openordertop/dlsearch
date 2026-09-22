from flet import (
    View, Page, AppBar,
    Container, Row, Column, ResponsiveRow, ResponsiveRowBreakpoint,
    Text, TextField, Button,
    Icons, Icon, Image, Colors, BorderRadius,
    MainAxisAlignment, CrossAxisAlignment,
    UrlLauncher, LaunchMode, ControlEvent, ScrollMode, ScrollType
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
            ),
        ]

    async def open_url(self, e, url: str):
        if self.page:
            await UrlLauncher().launch_url(url, mode=LaunchMode.EXTERNAL_APPLICATION)

    def did_mount(self) -> None:
        self.page.overlay.clear()
        self.page.update()

    def will_unmount(self) -> None:
        self.page.overlay.clear()
        self.page.update()
