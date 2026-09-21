from flet import (
    Container, Row, Column, Stack,
    Text, Image, Icon, Icons, TextField, Button, OutlineInputBorder,
    UrlLauncher, LaunchMode, ControlEvent,
    Colors, BorderRadius, ResponsiveRowBreakpoint, Alignment,
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
                Row(
                    controls=[
                        search := TextField(
                            label="Buscar en Kingtong",
                            on_submit=lambda e: create_task(self.open_url(e, search.value)),
                            icon=Image(src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAD1BMVEUAAAAAAACAAAD/AACAgAAXKc/FAAAAAXRSTlMAQObYZgAAALBJREFUeAFt0NERg2AIA2DtBIILSJigZIK2++9UQdTTNm/57hB/hswoW4YOnBlg2fqDW8yjpAEwNStAdQ8ADQDDYcpATcCDCJETJLdETk4JI2RmZ/kPblot/A77r86RkJGpQCmsRMMI2/YioSQBOOFhChEFrGEO6TQ4qynjAkrasIMVQK5gx1YmZIbjyM+zN+gNYo4baH5mukBeuSEPKOQ54yvYDzjteP1nhbcTfOVJv/ycLwXcJ4Q/AAAAAElFTkSuQmCC"),
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
        self.border_radius=BorderRadius(10, 10, 10, 10)
        self.padding=12
        self.margin=4
        self.alignment=Alignment.BOTTOM_CENTER

    async def open_url(self, e: ControlEvent, url: str):
        await url_launch(e, f"https://www.kingston.com/en/memory/search/systemdevices?makeOrModel={url}")

class SearchStack(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.controls=[
            Container(
                content=Row(
                    controls=[
                        search := TextField(
                            label="Buscar en Kingtong",
                            on_submit=lambda e: create_task(self.open_url(e, search.value)),
                            icon=Image(src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAD1BMVEUAAAAAAACAAAD/AACAgAAXKc/FAAAAAXRSTlMAQObYZgAAALBJREFUeAFt0NERg2AIA2DtBIILSJigZIK2++9UQdTTNm/57hB/hswoW4YOnBlg2fqDW8yjpAEwNStAdQ8ADQDDYcpATcCDCJETJLdETk4JI2RmZ/kPblot/A77r86RkJGpQCmsRMMI2/YioSQBOOFhChEFrGEO6TQ4qynjAkrasIMVQK5gx1YmZIbjyM+zN+gNYo4baH5mukBeuSEPKOQ54yvYDzjteP1nhbcTfOVJv/ycLwXcJ4Q/AAAAAElFTkSuQmCC"),
                            on_change=lambda e: (
                                setattr(clear, "visible", False) if e.control.value == "" else setattr(clear, "visible", True)
                            ),
                            expand=True,
                            border=OutlineInputBorder(
                                border_radius=30,
                            ),
                            autofocus=True,
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

    async def open_url(self, e: ControlEvent, url: str):
        await url_launch(e, f"https://www.kingston.com/en/memory/search/systemdevices?makeOrModel={url}")
