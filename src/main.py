#! /usr/bin/env python

from flet import (
    run,
    Page, AppBar, Image,
)
from router import Router

def main(page: Page) -> None:
    page.title = "DLSearch"
    page.route = "/index"
    Router(page)

if __name__ == "__main__":
    run(
        main,
        assets_dir="assets"
    )
