from flet import (
    View, Page, AppBar,
    Container, SafeArea, Row, Column, ResponsiveRow, ResponsiveRowBreakpoint,
    Text, TextField, Button,
    Icons, Icon, Image, Colors, BorderRadius,
    MainAxisAlignment, CrossAxisAlignment,
    UrlLauncher, LaunchMode, ControlEvent, ScrollMode, ScrollType
)
from components import ResultContainer, KingtongCompatibilityContainer, SearchStack
from asyncio import create_task

urls: dict = {
    "Kingtong Technology": {
        "url": "https://www.kingston.com/en/memory/search/systemdevices?makeOrModel={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgBAMAAACBVGfHAAAAD1BMVEUAAAAAAACAAAD/AACAgAAXKc/FAAAAAXRSTlMAQObYZgAAALBJREFUeAFt0NERg2AIA2DtBIILSJigZIK2++9UQdTTNm/57hB/hswoW4YOnBlg2fqDW8yjpAEwNStAdQ8ADQDDYcpATcCDCJETJLdETk4JI2RmZ/kPblot/A77r86RkJGpQCmsRMMI2/YioSQBOOFhChEFrGEO6TQ4qynjAkrasIMVQK5gx1YmZIbjyM+zN+gNYo4baH5mukBeuSEPKOQ54yvYDzjteP1nhbcTfOVJv/ycLwXcJ4Q/AAAAAElFTkSuQmCC",
    },
}

class LaptopsView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = "/laptops"
        self.test = SearchStack()
        self.appbar = AppBar(
            title="Buscar Cargadores, Baterias, etc.",
        )
        self.expand = True
        self.pages = ResponsiveRow(
            controls=[
                Icon(Icons.SEARCH),
            ],
            expand=True,
            scroll=ScrollMode.AUTO,
            spacing=4,
            run_spacing=4,
            on_scroll=lambda e: (setattr(self.test, "visible", False) if e.pixels >= 54 else setattr(self.test, "visible", True), print(e)),
        )
        self.controls = [
            Column(
                controls=[
                ],
                expand=True,
            ),
        ]

    async def open_url(self, e, url: str):
        if self.page:
            await UrlLauncher().launch_url(url, mode=LaunchMode.EXTERNAL_APPLICATION)

    def did_mount(self) -> None:
        self.page.overlay.append(self.test)
        self.page.update()

    def will_unmount(self) -> None:
        self.page.overlay.clear()
        self.page.update()
