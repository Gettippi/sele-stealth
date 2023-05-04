from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def navigator_languages(driver: Driver, languages: [str], **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/navigator.languages.js").read_text(),
        languages,
    )
