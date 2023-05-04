from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from patch import path


def navigator_vendor(driver: Driver, vendor: str, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/navigator.vendor.js").read_text(), vendor
    )
