from flet import (
    Container, Row, Column, Stack,
    Text, Image, Icon, Icons, TextField, Button, OutlineInputBorder,
    UrlLauncher, LaunchMode, ControlEvent,
    Colors, BorderRadius, ResponsiveRowBreakpoint,
    Alignment, MainAxisAlignment, CrossAxisAlignment,
)
from tools import url_launch
from asyncio import create_task

class IndexContainer(Container):
    def __init__(self, title: str, image: str, route: str) -> None:
        super().__init__()
        self.content = Column(
            controls=[
                Text(
                    value=title,
                    expand=True,
                    width=150,
                ),
                Image(
                    src=image,
                    width=130,
                    border_radius=BorderRadius(12,12,12,12)
                ),
            ],
        )
        self.on_click=lambda e: (
            create_task(self.page.push_route(route)),
            e.page.update(),
        )
        self.alignment=Alignment.CENTER
        self.bgcolor=Colors.SURFACE_CONTAINER
        self.border_radius=BorderRadius(10, 10, 10, 10)
        self.height=250
        self.width=250
        self.padding=20
        self.margin=5
        self.expand=True
        self.ink=True
        self.col={
            ResponsiveRowBreakpoint.XXL: 2,
            ResponsiveRowBreakpoint.XL: 2,
            ResponsiveRowBreakpoint.LG: 4,
            ResponsiveRowBreakpoint.MD: 4,
            ResponsiveRowBreakpoint.SM: 4,
            ResponsiveRowBreakpoint.XS: 6,
        }

class SearchStack(Stack):
    def __init__(self, tf_label: str, on_search) -> None:
        super().__init__()
        self.on_search=on_search
        self.search=TextField(
            label=tf_label,
            on_submit=lambda _: self.send_search(),
            on_change=lambda e: (
                setattr(clear, "visible", False) if e.control.value == "" else setattr(clear, "visible", True)
            ),
            expand=True,
            border=OutlineInputBorder(
                border_radius=30,
            ),
            autofocus=True,
        )
        self.controls=[
            Container(
                content=Row(
                    controls=[
                        self.search,
                        clear := Button(
                            content=Icon(Icons.CLOSE),
                            on_click=lambda e: (setattr(self.search, "value", ""), setattr(e.control, "visible", False)),
                            visible=False,
                        ),
                        Button(
                            content=Icon(Icons.SEARCH),
                            on_click=lambda _: self.send_search(),
                        ),
                    ],
                ),
                bgcolor=Colors.SURFACE_CONTAINER,
                padding=12,
                margin=12,
                expand=True,
                border_radius=BorderRadius(30, 30, 30, 30),
                blur=0.5,
            ),
        ]
        self.bottom=0
        self.right=0
        self.left=0

    def send_search(self) -> None:
            if self.on_search:
                self.on_search(self.search.value)

class ResultContainer(Container):
    def __init__(self, search_value: str, urls: dict, where: str) -> None:
        super().__init__()
        self.content = Row(
            controls=[
                Image(
                    src=f"{urls[where]['icon']}",
                    width=20,
                    height=20,
                ),
                Text(
                    value=f"{where}",
                    expand=True,
                ),
                Icon(
                    Icons.SEARCH,
                ),
                Text(
                    value=f"{search_value}",
                ),
            ],
        )
        self.col={
            ResponsiveRowBreakpoint.XXL: 4,
            ResponsiveRowBreakpoint.XL: 6,
            ResponsiveRowBreakpoint.LG: 6,
            ResponsiveRowBreakpoint.MD: 6,
            ResponsiveRowBreakpoint.SM: 12,
            ResponsiveRowBreakpoint.XS: 12,
        }
        self.bgcolor=Colors.SURFACE_CONTAINER
        self.border_radius=BorderRadius(12, 12, 12, 12)
        self.padding=12
        self.margin=4
        self.ink=True
        self.on_click=lambda e, u=urls[where]["url"].format(search=search_value): create_task(self.open_url(e, u))

    async def open_url(self, e: ControlEvent, url: str):
        await url_launch(e, url)

class KingtongCompatibilityContainer(Container):
    def __init__(self) -> None:
        super().__init__()
        self.content=Column(
            controls=[
                Text(
                    value="Buscar Modelo en Kingtong Compatibility",
                ),
                Row(
                    controls=[
                        search := TextField(
                            label="Buscar por Marca, Modelo, etc.",
                            on_submit=lambda e: create_task(self.open_url(e, search.value)),
                            icon=Image(src="icons/Kingston.png"),
                            on_change=lambda e: (
                                setattr(clear, "visible", False) if e.control.value == "" else setattr(clear, "visible", True)
                            ),
                            expand=True,
                        ),
                        clear := Button(
                            content=Icon(Icons.CLOSE),
                            on_click=lambda e: (setattr(search, "value", ""), setattr(e.control, "visible", False)),
                            visible=False,
                        ),
                        Button(
                            content=Icon(Icons.SEARCH),
                            on_click=lambda e: create_task(self.open_url(e, search.value)),
                        ),
                    ],
                ),
            ],
        )
        self.bgcolor=Colors.SURFACE_CONTAINER
        self.border_radius=BorderRadius(30, 30, 30, 30)
        self.padding=12
        self.margin=4
        self.alignment=Alignment.BOTTOM_CENTER

    async def open_url(self, e: ControlEvent, url: str):
        if url == "":
            return
        await url_launch(e, f"https://www.kingston.com/en/memory/search/systemdevices?makeOrModel={url}")

class POWEContainer(Container):
    def __init__(self) -> None:
        super().__init__()
        self.content=Column(
            controls=[
                Text(
                    value="Buscar Bateria o Cargador",
                ),
                Image(
                    src="images/POWE.png",
                    align=Alignment.CENTER
                ),
            ],
        )
        self.bgcolor=Colors.SURFACE_CONTAINER
        self.border_radius=BorderRadius(30, 30, 30, 30)
        self.padding=25
        self.margin=4
        self.ink=True
        self.expand=True
        self.on_click=lambda e: create_task(self.open_url(e))

    async def open_url(self, e: ControlEvent):
        await url_launch(e, f"https://www.powe.mx")

class NoJomoContainer(Container):
    def __init__(self) -> None:
        super().__init__()
        self.content=Column(
            controls=[
                Text(
                    value="Buscar Bateria, Cargador, Displays, etc.",
                ),
                Image(
                    src="images/NoJomo.png",
                    align=Alignment.CENTER
                ),
            ],
            expand=True,
        )
        self.bgcolor=Colors.SURFACE_CONTAINER
        self.border_radius=BorderRadius(30, 30, 30, 30)
        self.padding=25
        self.margin=4
        self.ink=True
        self.expand=True
        self.on_click=lambda e: create_task(self.open_url(e))

    async def open_url(self, e: ControlEvent):
        await url_launch(e, f"https://www.nojomo.com.mx/home.php")
