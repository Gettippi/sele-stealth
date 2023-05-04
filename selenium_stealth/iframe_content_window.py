from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def iframe_content_window(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/iframe.contentWindow.js").read_text()
    )
