from flet import (
    View, AppBar,
    Container, SafeArea, Row, Column, ResponsiveRow, ResponsiveRowBreakpoint,
    Text, TextField, Button,
    Icons, Icon, Image, Colors, BorderRadius,
    MainAxisAlignment, CrossAxisAlignment,
    UrlLauncher, LaunchMode, ControlEvent, ScrollMode, AppBar,
)
from components import IndexContainer

class IndexView(View):
    def __init__(self) -> None:
        super().__init__()
        self.route = "/index"
        self.appbar = AppBar(
            title="DLSearch",
            leading=Image(
                src="icon.png",
            )
        )
        self.controls=[
            Text(
                value="Bienvenido",
            ),
            ResponsiveRow(
                controls=[
                    IndexContainer(
                        title="Buscar Productos en Página",
                        image="images/search.svg",
                        route="/search",
                    ),
                    IndexContainer(
                        title="Buscar Compatibilidades para Laptops",
                        image="images/laptops.svg",
                        route="/laptops",
                    ),
                ],
                scroll=ScrollMode.AUTO,
                expand=True,

            ),
        ]
