from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def media_codecs(driver: Driver, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/media.codecs.js").read_text()
    )
