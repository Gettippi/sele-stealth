import os
from pathlib import Path

user = os.getlogin()

path = Path(fr"C:\Users\{user}\AppData\Local\Programs\Python\Python310\lib\site-packages\selenium_stealth")
if not os.path.exists(path):
    path = Path(fr"C:\Users\{user}\AppData\Local\Programs\Python\Python311\lib\site-packages\selenium_stealth")