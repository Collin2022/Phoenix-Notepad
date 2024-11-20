# 导入基础库文件
import tkinter
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json


# 导入基础数据文件
with open("./asset/settings.json", "r", encoding="utf-8") as fp:
    settings = json.load(fp)
enable_autosave = settings["enable-autosave"]
enable_codehighlight = settings["enable-codehighlight"]
enable_autocomplete = settings["enable-autocomplete"]
font = settings["font"]
font_size = settings["font-size"]
version = settings["version"]
encoding = settings["encoding"]
lang = settings["lang"]

# 导入语言文件
with open("./asset/lang/{}.json".format(lang), "r", encoding="utf-8") as fp:
    lang_data = json.load(fp)
lang_title = lang_data["title"]
lang_about_message = lang_data["about_data"]
lang_file = lang_data["menu"][0]
lang_edit = lang_data["menu"][1]
lang_view = lang_data["menu"][2]
lang_command = lang_data["menu"][3]
lang_run = lang_data["menu"][4]
lang_terminal = lang_data["menu"][5]
lang_about = lang_data["menu"][6]


