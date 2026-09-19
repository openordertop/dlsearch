#! /usr/bin/env python

from flet import (
    run,
    Page, AppBar,
    Container, SafeArea, Row, Column, ResponsiveRow, ResponsiveRowBreakpoint,
    Text, TextField, Button,
    Icons, Icon, Image, Colors, BorderRadius,
    MainAxisAlignment, CrossAxisAlignment,
    UrlLauncher, LaunchMode, ControlEvent, ScrollMode,
)
from asyncio import create_task

urls: dict = {
    "Digitalife": {
        "url": "https://www.digitalife.com.mx/buscar?search_text={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAcCAYAAACQ0cTtAAAAs0lEQVR4AWJwL/ChGx6Glo1adodXFMBbHZAAEMIAFK1xIZbDEJfABIZYEDPYwwLrYABvwAQYwwPcBD4HB/i4U7VwaJQ58MY6N3/CG5gOrmHSc4IhV1Vtg9EJ1jjiujxBLR4LTF6/UQbagtUfkwyMIjHSYCTWb2JT1aMWSDIwjMKagYEX9nKPBAbUIo6rwg31bnifjUO+jqy9dYrRGmzdbQaeXW9qmR+Uypq7b6NtkFHLqIYBPqOYO0lr+sUAAAAASUVORK5CYII=",
    },
    "CyberPuerta": {
        "url": "https://cyberpuerta.mx/search?q={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAATlBMVEUAZrsAY7oAYroAX7kAWrcAV7Yjcb9xmtClvuDS3+9AfsQvdsH5+v3///8db76ZttwAYLmHqNUAXbhKg8Zdj8t3n9IATbPv9Pre6PQXbL4cwpMaAAAAaElEQVR4AcXStQHAMAwAwXDMjPsPGmYq42+vsSVlqcuLsqryJyirumkBhOiuBQaQ0DFSlRfLGd3K+EWF3FFRnL8j0b+isR/oyg/0ZMekXynMjiJc11JxsmF2q6xZO62Ul29HUrOosqT14goNhLVzfgEAAAAASUVORK5CYII=",
    },
    "Abasteo": {
        "url": "https://www.abasteo.mx/?cl=search&searchparam={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAEQklEQVR4Ab2VY5BkSxSEszHmw9jPtm3btm3btm2ubdu7Y7Oxtvn9GNyouM1FRnyN6oqTeepWdSkqfVYVq88rnEL6oupaeEhIX9ek6+vqL+FcbS9hnq7PKh/T55UZ7QHOhJOE9E1NFubv836IkL6rvUrf176kH2qTttK0IlafVsQL6fOqOALsRYAY2em7OlYG/VTvxvwb+Ek/1m1dAMxPheMUoTBO1Q91ifq53g3X6pf6e/RrQ3w0AZIgTla9V+bWu6XJkAYpeq+UFbEX5oVQTYDxBNg5XNMCyJFFGKXqnTlnwmvQDcbAZBgLveAtOEsEklW/1sdhfqp+adgvgq4rCwmQKaH32fHvzjmN4oNgBWwOwgroT4gjZOrPJpf+aDwHbuFzcphByh0UvAH8sDkCxhEiSxZhvC+06s/GhQQ4ROGIzk+mmMfGYCUsgMWw3ub3VXC2LMI4A97XX01PQXIY5mUpFOlnFF4NP8AZeqf0ADicz/dAqzFvA1wrQxg7FK5YwvNFp0bh79nxibKKPcL4nzKDvssKmPq3JUn/NN+tf5uf1n8tGaECXEahP+C3dr6D/Wzm5TI+yQjgYXX2kSHML8Z8NUFWEOB8BRNn3akPKhyGWSzFd6Z4CR0ezedbYDBsMAKMF8fWZgUOwXgo/KL/W/PCeAyzHRjlUexyir4HfWAGNMES09jC9/q4xiE7/deaALHh7IGdKfQklMO6IEduk83YQ7JTt9ZkOEbd20oUTCxxDkX+te2QMVgMFfAjTLQ5oqfLVI82N+bvwQp1bx2hnp7sQJ3HUeArG+Na+BSuY86RPJos3tP5PsqY10ADxTJE18kYj4TNhJlJgPxA3Z8hnq9RdAxm++s9c1PO2Z/fvMbcYcxNlI0wPgU+UM+2UxVIFPjCPNNwcYC5j9vsgU8VqYwbb4J5pmEvm7mHM14NxoYsvV2merVl0PWz6uV5TL09qTJl/KnUGkWXUfQyfcCxer/KyZwMlv5axmfDZnMunCBTPT33EmIzAZYT4JRgATIoUGpT2AP/wz8wA1YHOIINUCRDGJ+PcQuMUB9vYbB/P1f7ZbM5BGugJ9Qb47NFEzLVx+fGfE/MsxRS3HIUmhLkT6cK7sWomPfpneMAy+ByIfXyJmB6JVysvr7YSDfj7hR6FUbA7HajXoR7VPxmuRfOg5vhxnb4TAMI4zNhBV3PVV/vgYpYH5Q7eCSJGGXAzhBRFxgfC42YD4cchaXfG3P1R+N+ika9/Q42217q7d2PJXeor9/F+16AeZjC/GZ4KboAngKYDmV0XKyo9EdTKqQL6e/mffRP8y36pyW+6zy3OSxnOx6Ooetd25e8BEphvLHkUQpz6K1/W1Par9Lz4S0ulZT2ABcQaCkBnhRSP78T433Uz1ekbaJ/W1Ih23KXf8BNNpEAGUIYnwyjWfLztSOEcQE3GR2y2RCby8Vyp6mPx6kotQUOTMfL6OdlNgAAAABJRU5ErkJggg==",
    },
    "DDTech": {
        "url": "https://ddtech.mx/buscar/{search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAh1BMVEVHcEwQY8oAVrgAVbkAVLkAVrgFVrgQZMEgdMggdcgec8kAVLhPh9AfdMcgdMdPh9BMhM5MhM4nbMtTitFMhM5Ohs8gdMdMhM4gdMdMhM4gdMcAVrgAVrhMhM6OygAAVrgAVriJxQCBvgCBvgCSzwCAvQCAvQAAVbiBvgCAvQCAvQGAvQGAvQFkoiztAAAALXRSTlMAIYCGPv8wZ4aRS3cj1P9K/4wMO+hj9854tu1PorMG9NpJxp8i9v/GZuEzDkXA0rGfAAAA3UlEQVR4AdXPRRbDQAwE0TYzhZnNvv/5IskO8zK1/W9GEq5TVFXVdDxPNyjtHar/jqZlO66g5/u35AYh5ZiCUZz0rswOJbvFfhwPhmezwnskjiD1RkJX30pj//LpRFF63bZJ3MaPZRn3+pTeVHAA9GZks7s7+2PWDgPBOaMH9BYehoN4Kd8GVm/FuGCcw1sbxkZHwhu5Cra7PQDP4BT5XH6gDvs0yw6a0ZbL5/ySKsqMKrHu0GRcW8AFC70zC4QLnKuIkQut5wBME1cV2R5avskXVg8P1VmD1xUr/N4Rq3AS9l+OLMsAAAAASUVORK5CYII=",
    },
    "Zegucom": {
        "url": "https://www.zegucom.com.mx/#271f/classic/m=and&q={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAq1BMVEVHcEwFQYYFQYYFQYYFQYYFQYYFQYYFQYYFQYYFQYYFQYYFQYYFQYYFQYYEQYbaAAwAM4AAPIQALX7bARcAOIJTdKP7///3vr749/n909Lj7/e0xNjV4+7dKTaCmbusvdPsnKBzi7HlX2bbESS5ydyTqMXiS1PyqavriIsAHXjsfIDztbf6ysoxWZPsgITtlJf829uhs8yks8v/6OfP2+fmdnvdMz700tVEZ5seWm1BAAAADnRSTlMADRnqsVDHNHxp2I2Mm5TiENEAAAFhSURBVCiRZZLXloIwFEVBababQDAwKFIVsOFY5/+/bFIABfcb7HWTk+QoSoc+0wxDm+nKFyMNOrRR382hx/zTTWHA9O3GQwcwbp0BLm6wsYP5hw2GdBNwk5XkCtE92uR5frJhIiQAjrz9+VyWpe/HaX07729LG4A7i8tjXcchyaiHUFwi9MOlJdO4yfU39xGJ6YGElDaSZVJ5NhdXq5ggf+uRMPAbCaqiy+iYZlm6TnpSZ1nF6ObIfiWbnpzwPAwnSLOQVn1pSWn/sThF5AylWNbJa4LoCQ+XNcWWlGSPdTWYNPkF8TgEXaIkidg5g/ac/Io0EYdkHsM/IPLyCBFSY9Lkcp+mO8aFPp67F5GTpnwxvFpL7hGllO15WbZvxi4QO5IqKOL4iRAVlycwu/d3gkNRFJ5/xXJRUcpW2smWsTlh+ChoN2u7HPs9J1h8tmsxbLVqNf2cWup353ntTbNX9n+VbjBXit0UqQAAAABJRU5ErkJggg==",
    },
    "MiPC": {
        "url": "https://mipc.com.mx/buscar/{search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAclBMVEVHcEwVFRUAAAAAAAALCwsFBQULCwofHx8JCg0AAAAMDAwAAAA8PDwAAACGORZ9NBLyZSIAAAH8aSP2ZiI2NjYmJycfISEuLy89PT2dQxgrKyvVWR+4Th1CQkITHB1WKBMLExXpYSGDOBY4FwhtMBQ+Jx3H+2qlAAAAEHRSTlMAXGzBMhSTIEcHsd3k8YXV5hakNAAAAYdJREFUOI11k4FywiAQRCFCQqK2HMTWFAwQ7f//Yo8jtFrjOuOZ7LvlGIGxe/Wy+6f+zhXt4fIk8Wvzw/lyOT9JrXZ3GMczfv6rAvzJGcfPcfLTWAD+uaFRG2s8AeprQydvtbYuA91pS7PLACUMH1uaF2OMOyEgPmZS/A4hlzmE7zjjy7Dc5lmxfoiT1joFZ41Jt+h17kTcJlRUTMaYx9GWvpIzWLTxsJg8IwI8Qh6nqv6ME80IirUREjnJFoCKibnLLAgMcM2pNlCQdRDoETJvAgI7eoNhkEcxN4g5IkHBCKDVJqAEcy28o9hUgLUTaHEo40/LGotD1s4rddaVaqxgTdnE2unrSq7E7jsmaudU9kX8ussrDJJ178bi/46duQYEbK4eDwNugvdMvk0oNJZcAWdIzvsQ8GGBvehZL/bwUo3E4yCbl/5O5GvRd8ML/6gkHVkpdtsAr/dqmzg2f/dOivbJ3/P7eykFfww5turh3uKkohmOv92tEvLBRwIRxZsW1SjR/dk/ya1CdNaLw/wAAAAASUVORK5CYII=",
    },
    "RekonTech": {
        "url": "https://rekontech.com.mx/products?search={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAnFBMVEVHcEwAAAAAAAABAAUAAAAAAACenp+Eg4R8fH2Li4ugoKE7Oj7/+v/j4uX29fni4eRhYGNSUVNjY2YoJysfHiNpaWsAAAD///+ysrLo6OhmZmaQkJBcXFzFxcXU1NTZ2dnLy8usrKx3d3e5ubmlpaUPDw+Xl5cuLi5JSUnf399UVFSioqJBQUE5OTkkJCTBwcFxcXH4+PgZGRnv7++5yOO/AAAAFnRSTlMAMmeXfk3+/f7956EZ2riRnrq2urSl0lfrnQAAAhBJREFUOI1lUwmSozAMJCcms7uzZ8vGxtw3BJL8/29rG5LMZFRFoZJkt9Rqe97DDr+PUWwsqn5tva+278WUnWGsZpE4vr+kN1L4JhfKvpfKOEQ4fDquU4Dl6TyW5cDSPKwVuh/fHvmdCKGmEA9j04gY3x/nxYBjhU+W+n0idiu+7hhXeLGsgp8vfci0S3VXvNzQMB9JuAAASaBv0cd8LCLwEQ6ksPPhlhJ/5hPKW2BC4Rv+hAtd6paye76iSJlw0KHdev/yJjcxgZyoXPIjUX/VxuHQf7xTGFFo/YhobaMlSlG4gsr3omvYG1/h0hONNq+Ijrd6MJ4cO+7FkLUN+ynCpc+EGkSO1nAuE1NQOGjba0DWs4h1bL0hQGwKelswaDeL2XfXunobbAJoC2GRl10cDeOMWY/7d4jorOz8SeD6a4DZtVTYdqpapd6JwWgBE7Xm+iuWbxCU3sf8OSF37Dg6VjlQ7sTHEf+1VM8Lxw11S34mh6KMjGKz8KPEyuD54n7lZd3YnBbMbHMr0KxiCC0wpmGt7yH2VhB+Drku0nZzfa5dq0VySYZiqRjN9JUjNqAZFd8soty2CtLdbiYuF7jk0mR6/5B1m2GYLHdlYVcLOZ0h9e75cLbRZFrMedDVtZKcm3k133sfbMOEXUbDpGR2iEKEm5fXua3aJGgcYVK3/t77aoe3U67jWPPg7cPD/Q8HnFUVYIAyrQAAAABJRU5ErkJggg==",
    },
    "DimerCom": {
        "url": "https://dimercom.mx/?s={search}&post_type=produc",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAACg0lEQVR4Ac2XA4xdQRiFa7dBbdsIasZpw9pWbLtujDJmbRtr27atp7P/Seaud+/M+iTfy2Tmn3/Ou/eOBgx49UeXMcJB4b7gK+QJtQqWfVXbQcZq59UIWiA8EioFaFKp+izoioERwk2hTkAnYd9bzGVqYL4QIqCbYK4FugbWCbkdJRwoTPvkgxU/AgnLrLMzkcvcdgboMr+jRPO/+iOyvAotxTq22Zhg7gXtGRgphHaUYOibv4ivqEZ7YhtjbEyEqbFaGbgloCM2/QmBpdfZhVjzMwiEZSXGMNaOWy0NzBccdh1PBsWCcno8WP49AOVOFwjLrKMYo2HAISxoMKDmLOw4HxIPqsThxPZ/obDEclGdE9QFiWGsBo8tA2N1F5m9PpGwdCwwBueC40DW/QqCSz2BfRKjvVhxbLV0QocJH7wbHjV//xSW4m5CBvgElspreJqZj0kfvRmry0EaeGhV6L4Gtwet5F1UhhmffRmjD8dWmwhM2Po3FJ9yi/jeW60Fahrq4ksDBbodDgVE42FKNg74RzfUjXv3H9fj0mFpz/9wfQMc22Sz4QdHhZZWNqsf8vov8msdoK6GJRhtVt1igCRV1ljT0NhAQXcYYB3FGNNX4NuHBnzVNOwjA2oaHuxDAwcbluI+MFBlLcXkcR8YaNiMyALBobMQUVk1dRj0urGeZdZRjNHcjhcaH0g2/AqGpZvx6eACRFhWYoyOgdvtHcnCOuo4WAaL4nlQqczpAlFiG2N0jmSjOn0onfPFD2FllWgp1rFN51Dar4/lFgtsXocpYSqn8dXslt3ssMGhdTWzYaE6tFYZDFyt5vlCu/ym1/NDwgPBT31QDgXLfqrtkMn1vB6ttJ1mzjYmWwAAAABJRU5ErkJggg==",
    },
    "Libra": {
        "url": "https://tienda.libra.com.mx/productos?b={search}&post_type=product",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAw1BMVEX////x8fKVmJx9gYanq67s7e6FiY8dKTRWXGNKUVkxOkTU1df7+/tFTFTm5+i0trl0eX7Aw8Xe3+AoMj08QlBqbnieoaVxdnwVIzI6RURzkixYbzNPVGPLzM4jKz2VvhyUvB2Suh9kfTBCUjqChosnLUSJsCRTckeEqCWGsS4sNEFOXz+Ltih6pTlJYElgZW4uNEdieDdumEQ/T0gwOERljkdbfklpl0tMZUhxnUBgh0lSbUktN0F8nSuAqjNsm0tVaT1E0/bOAAABWklEQVR4Aa3SBZaDMBQFUDzFBoc6Wjeoe7v/VQ0/FBnXdyRyc+LEf4WkaIb9CDlU4wVOlN4ztiY/sQqPVK3aq4u4EA1VgoITBIbMjZJNS0m7FWQ/prB55zE3WW80W0abIVWjU2yNVwgcpdtyPT8ITUEot0qrWRn1mp7vu/2BIBNFHPqxR2GYoj8ajKPCJCvDzngyTc2bzcdKiYtsIBUnHuBytRZLrHG45GNY0ptu1qatSznyGEUhxrOOtuv1WLAoPUOTgoIZr1w/zWy32+5X4zGSqQ5LSAag5MQJxsMuzeZ4agjozHMRYuAqhPXFA+xfD7vNbnfb1zTnXEf4PjS0GmLER50ddvMFHI8Bw+gCQDzPn04AcfC0k8vQLdwFLKIIY6ERBpe+jwe4YYkwv3NG47i3ugcwQYFFdCZarLtxLNybF8F55+PpSiSb4+4aDvhudIWybIn4MEDfyTMJDCjzi8jo7wAAAABJRU5ErkJggg==",
    },
    "GlobalOffice": {
        "url": "https://globaloffice.com.mx/app/shopping/productos?buscar={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAclBMVEX////7/P3c4eQ9WGsAKkkAM08gRVy5wshsfosTQFgAN1Kkr7fEy9AAL0zM1NkAAB1hd4VzhJFVbX0AHkELO1Xl6+2zvsWMmaPt8PLi4+Q2VGgoTGKCkp2str2apa7U2t73+fpRZ3gAADKNn6lHYHLz8/S2HSQnAAAAv0lEQVR4AdXQRWLEMBAAwR4tmllrjGXQ/58YJtM9qYtYA/xlwhF1Ol+ut/vZcT3W/EBBGMVAkrKSCZAXdxGINQv6AagUyqqiqFl43Lhfc6dpWiohYKF7QiRM8RPpKRsWzBngbIawhNZjqasN9GMMTDVrvnuaXW++zucWtmwJmPKwecKWp3UlGuiw1li7+M9X06Qnr5s6LNYuL/id8vVNh16IsYiIMcKXkh5DQWnElAU9ioIvBYry41DM+4SSf+cFQzAM7IeOoo0AAAAASUVORK5CYII=",
    },
    "AlterCo": {
        "url": "https://www.altercomx.com/search?options%5Bprefix%5D=last&filter.p.product_type=&q={search}",
        "icon": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABwAAAAcCAMAAABF0y+mAAAAh1BMVEX////x8fHi4uPLzMzm5uba29vs7e309PTp6enV1dW8vb3Dw8TNzc63uLixs9Dz8/d6frNyrIbG283d3urKy9+fosf5+fwtNpHr6/Omqcr9+/+81sNtcavr7PO5u9Xi4u2JjLnQ0uKPk709RZfBw9lYXaF+grOSlbuHi7OfoJ6ur7CcnZyTlJUQvQfuAAAAsElEQVR4Ae3KhYEDIRBA0R93WHf3Bfpv79y1gOQho9w8WixZsV6y2bLasWez5rB4jAC7LcfHzmrDac+Zw0PcsOGy4H8CpMUj2wFXeH7AKxlGYBFDkoLMwM2RPCvKCqwoywshsjgrAPy6gUdN3YL1EAr3YU0IoOvIAoAuoBNYVG7Fw5U95F7DABCMAbUf+UxSDEFcEo2dS9GVPJrVPM/6dJr1PBt9NHqlD1rNmq8CrtE9GcENTsHeJaAAAAAASUVORK5CYII=",
    },
}

class Index(Container):
    def __init__(self):
        super().__init__()
        self.expand = True
        self.search_tf = TextField(
            label="Buscar Producto por Nombre, SKU, etc.",
            expand=True,
            autofocus=True,
            on_submit=lambda e: self.search_pages(e),
        )
        self.pages = ResponsiveRow(
            controls=[
                Icon(Icons.SEARCH),
            ],
            scroll=ScrollMode.AUTO,
            spacing=4,
            run_spacing=4,
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

    def search_pages(self, e: ControlEvent) -> None:
        self.pages.controls.clear()
        search_value = self.search_tf.value or ""

        for where in urls:
            self.pages.controls.append(
                Container(
                    Row(
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
                    ),
                    col={
                        ResponsiveRowBreakpoint.XXL: 4,
                        ResponsiveRowBreakpoint.XL: 6,
                        ResponsiveRowBreakpoint.LG: 6,
                        ResponsiveRowBreakpoint.MD: 6,
                        ResponsiveRowBreakpoint.SM: 12,
                        ResponsiveRowBreakpoint.XS: 12,
                    },
                    bgcolor=Colors.SURFACE_CONTAINER,
                    border_radius=BorderRadius(12, 12, 12, 12),
                    padding=12,
                    margin=4,
                    ink=True,
                    on_click=lambda e, u=urls[where]["url"].format(search=search_value): create_task(self.open_url(e, u)),
                ),
            )
        self.update()

def main(page: Page) -> None:
    page.title = "DLSearch"
    page.appbar = AppBar(
        title="DLSearch",
        leading=Image(
            src="icon.png",
        )
    )
    page.add(Index())

if __name__ == "__main__":
    run(
        main,
        assets_dir="assets"
    )
