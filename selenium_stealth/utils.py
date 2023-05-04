from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver


def with_utils(driver: Driver, **kwargs) -> None:
    print('path: ', Path(__file__))
    print('parent: ', Path(__file__).parent)
    evaluateOnNewDocument(
        driver, Path(__file__).parent.joinpath("js/utils.js").read_text()
    )
