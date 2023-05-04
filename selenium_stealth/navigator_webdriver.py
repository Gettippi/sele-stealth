from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def navigator_webdriver(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/navigator.webdriver.js").read_text()
    )
