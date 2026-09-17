#! /usr/bin/env python

from flet import (
    run,
    Page, AppBar,
    Container, Row, Column,
    Text, TextField, Button,
    Icons, Icon,
    MainAxisAlignment, CrossAxisAlignment,
    UrlLauncher, LaunchMode,
)
from asyncio import create_task
# import json

# urls: dict = {}

# with open("data/urls.json", "r") as f:
#     urls = json.load(f)

class Index(Container):
    def __init__(self):
        super().__init__()
        self.search_tf = TextField(
            label="Buscar Producto por Nombre, SKU, etc.",
            expand=True,
            autofocus=True,
            on_submit=lambda e: self.search_pages(e),
        )
        self.pages = Column(
            controls=[],
        )
        self.content = Column(
            controls=[
                Row(
                    controls=[
                        self.search_tf,
                        Button(
                            content="Buscar",
                            icon=Icons.SEARCH,
                            on_click=lambda e: self.search_pages(e),
                        ),
                    ],
                ),
                self.pages,
            ],
        )

    async def open_url(self, e, url: str):
        if self.page:
            await UrlLauncher().launch_url(url, mode=LaunchMode.EXTERNAL_APPLICATION)

    def search_pages(self, e) -> None:
        self.pages.controls.clear()

        urls: dict = {
          "CyberPuerta": "https://cyberpuerta.mx/search?q={search}",
          "Abasteo": "https://www.abasteo.mx/?cl=search&searchparam={search}",
          "DDTech": "https://ddtech.mx/buscar/{search}",
          "Zegucom": "https://www.zegucom.com.mx/#271f/classic/m=and&q={search}",
          "MiPC": "https://mipc.com.mx/buscar/{search}",
          "RekonTech": "https://rekontech.com.mx/products?search={search}",
          "DimerCom": "https://dimercom.mx/?s={search}&post_type=produc",
          "Libra": "https://tienda.libra.com.mx/productos?b={search}&post_type=product",
          "GlobalOffice": "https://globaloffice.com.mx/app/shopping/productos?buscar={search}",
          "AlterCo": "https://www.altercomx.com/search?options%5Bprefix%5D=last&filter.p.product_type=&q={search}"
        }

        search_value = self.search_tf.value or ""

        for base_url in urls:
            try:
                formatted_url = urls[base_url].format(search=search_value)
                btn = Button(
                    content=Container(content=Icon(Icons.OPEN_IN_BROWSER)),
                    on_click=lambda e, u=formatted_url: create_task(self.open_url(e, u))
                )
                self.pages.controls.append(
                    Row(
                        controls=[
                            Text(
                                value=f"{base_url}",
                                expand=True,
                            ),
                            Text(
                                value=f"[{search_value}]",
                            ),
                            btn,
                        ],
                    )
                )
            except Exception as err:
                print(err)

        self.update()

def main(page: Page) -> None:
    page.title = "Search"
    page.appbar = AppBar()
    page.add(Index())

if __name__ == "__main__":
    run(main)
