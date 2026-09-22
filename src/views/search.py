from re import search
from flet import (
    View, Page, AppBar,
    Container, SafeArea, Row, Column, ResponsiveRow, ResponsiveRowBreakpoint,
    Text, TextField, Button,
    Icons, Icon, Image, Colors, BorderRadius,
    MainAxisAlignment, CrossAxisAlignment,
    UrlLauncher, LaunchMode, ControlEvent, ScrollMode,
)
from components import ResultContainer, SearchStack
from asyncio import create_task

urls: dict = {
    "Digitalife": {
        "url": "https://www.digitalife.com.mx/buscar?search_text={search}",
        "icon": "icons/Digitalife.png",
    },
    "CyberPuerta": {
        "url": "https://cyberpuerta.mx/search?q={search}",
        "icon": "icons/CyberPuerta.png",
    },
    "Abasteo": {
        "url": "https://www.abasteo.mx/?cl=search&searchparam={search}",
        "icon": "icons/Abasteo.png",
    },
    "DDTech": {
        "url": "https://ddtech.mx/buscar/{search}",
        "icon": "icons/DDTech.png",
    },
    "Zegucom": {
        "url": "https://www.zegucom.com.mx/#271f/classic/m=and&q={search}",
        "icon": "icons/Zegucom.png",
    },
    "MiPC": {
        "url": "https://mipc.com.mx/buscar/{search}",
        "icon": "icons/MiPC.png",
    },
    "RekonTech": {
        "url": "https://rekontech.com.mx/products?search={search}",
        "icon": "icons/RekonTech.png",
    },
    "DimerCom": {
        "url": "https://dimercom.mx/?s={search}&post_type=produc",
        "icon": "icons/DimerCom.png",
    },
    "Libra": {
        "url": "https://tienda.libra.com.mx/productos?b={search}&post_type=product",
        "icon": "icons/Libra.png",
    },
    "GlobalOffice": {
        "url": "https://globaloffice.com.mx/app/shopping/productos?buscar={search}",
        "icon": "icons/GlobalOffice.png",
    },
    "AlterCo": {
        "url": "https://www.altercomx.com/search?options%5Bprefix%5D=last&filter.p.product_type=&q={search}",
        "icon": "icons/AlterCo.png",
    },
}

class SearchView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = "/search"
        self.expand = True
        self.appbar = AppBar(
            title="Buscar en Página",
        )
        self.search=SearchStack(
            tf_label="Buscar Prodcuto por Nombre, SKU, etc.",
            on_search=lambda e: self.send_search(e),
        )
        self.pages = ResponsiveRow(
            controls=[
                Icon(Icons.SEARCH),
            ],
            expand=True,
            scroll=ScrollMode.AUTO,
            spacing=4,
            run_spacing=4,
        )
        self.controls = [
            Column(
                controls=[
                    self.pages,
                ],
                expand=True,
            )
        ]

    async def open_url(self, e, url: str):
        if self.page:
            await UrlLauncher().launch_url(url, mode=LaunchMode.EXTERNAL_APPLICATION)

    def send_search(self, search: str) -> None:
        if search == "":
            return
        self.pages.controls.clear()

        for where in urls:
            self.pages.controls.append(
                ResultContainer(
                    search_value=search,
                    urls=urls,
                    where=where,
                ),
            )
        self.pages.controls.append(Container(margin=40))
        self.update()

    def did_mount(self) -> None:
        self.page.overlay.clear()
        self.page.overlay.append(self.search)
        self.page.update()

    def will_unmount(self) -> None:
        self.page.overlay.clear()
        self.page.update()
