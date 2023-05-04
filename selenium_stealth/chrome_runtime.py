from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from .patch import path


def chrome_runtime(driver: Driver, run_on_insecure_origins: bool = False, **kwargs) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/chrome.runtime.js").read_text(),
        run_on_insecure_origins,
    )
