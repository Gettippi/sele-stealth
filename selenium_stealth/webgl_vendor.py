from pathlib import Path
from .wrapper import evaluateOnNewDocument
from selenium.webdriver import Chrome as Driver
from patch import path


def webgl_vendor_override(
    driver: Driver,
    webgl_vendor: str,
    renderer: str,
    **kwargs
) -> None:
    evaluateOnNewDocument(
        driver, path.joinpath("js/webgl.vendor.js").read_text(),
        webgl_vendor,
        renderer,
    )
