from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def hairline_fix(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/hairline.fix.js").read_text()
    )
