from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def window_outerdimensions(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/window.outerdimensions.js").read_text()
    )
