from flet import (
    Page,
)

from views import IndexView, SearchView, LaptopsView

class Router:
    def __init__(self, page: Page) -> None:
        def route_change():
            page.views.clear()
            page.views.append(IndexView())
            match page.route.split("/")[1:]:
                case ["index"]:
                    page.views.clear()
                    page.views.append(IndexView())
                case ["search"]:
                    page.views.append(SearchView())
                case ["laptops"]:
                    page.views.append(LaptopsView())
            page.update()

        async def view_pop(e) -> None:
            if e.view is not None:
                page.views.remove(e.view)
                await page.push_route(str(page.views[-1]))

        page.on_route_change = route_change
        page.on_view_pop = view_pop
        route_change()
