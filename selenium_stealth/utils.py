from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path

def with_utils(driver: Driver, **kwargs) -> None:

    evaluateOnNewDocument(
        driver, path.joinpath("js/utils.js").read_text()
    )
