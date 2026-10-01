from flet import (
    View, AppBar,
    Container, Row, Column,
    ScrollMode,
)
from asyncio import create_task

class BrandedToolsView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = "/branded_tools"
        self.appbar = AppBar(
            title="",
        )
        self.expand = True
        self.controls = [

        ]

    def did_mount(self) -> None:
        pass

    def will_unmount(self) -> None:
        pass
