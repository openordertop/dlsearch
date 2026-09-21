from flet import (
    ControlEvent,
    UrlLauncher, LaunchMode,
)

async def url_launch(e: ControlEvent, url: str) -> None:
    if e.page:
        await UrlLauncher().launch_url(url, mode=LaunchMode.EXTERNAL_APPLICATION)
