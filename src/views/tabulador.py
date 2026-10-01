from flet import (
    View, AppBar,
    Container, Row, Column,
    ScrollMode,
)
from components import TabbuladorFieldContainer
from asyncio import create_task

rango: list[int] = [
    200, 204, 208, 212, 216, 221, 225, 230, 234, 239, 244, 249, 254, 259, 264, 269, 275, 280, 286, 291, 297, 303, 309, 315, 322, 328, 335, 341, 348, 355, 362, 370, 377, 384, 392, 400, 408, 416, 424, 433,
]

class TabuladorView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = "/zenvia"
        self.appbar = AppBar(
            title="Tabulador de Comisiones",
        )
        self.expand = True
        self.controls = [
            TabbuladorFieldContainer(rango=rango),
        ]

    def did_mount(self) -> None:
        pass

    def will_unmount(self) -> None:
        pass
