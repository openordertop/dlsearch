from flet import (
    AlertDialog,
    Text,
    Icon, Icons, Colors, Clipboard,
)
from asyncio import create_task

class ZenviaMessageAD(AlertDialog):
    def __init__(self, value: str) -> None:
        super().__init__()
        # self.actions = [
        #     Text(
        #         value=value,
        #     ),
        # ]
