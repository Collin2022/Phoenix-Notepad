# 导入基础库文件
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json


# 导入基础数据文件
with open("./asset/settings.json", "r", encoding="utf-8") as fp:
    settings = json.load(fp)

about_message = settings["about-message"]
enable_autosave = settings["enable-autosave"]
enable_codehighlight = settings["enable-codehighlight"]
enable_autocomplete = settings["enable-autocomplete"]
font = settings["font"]
font_size = settings["font-size"]
version = settings["version"]
encoding = settings["encoding"]
