"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 19:52:50 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic

# application context (fbs)
from base import app_context


class SearchWindow(QMainWindow):
    def __init__(self):
        super(SearchWindow, self).__init__()
        uic.loadUi(app_context.get_resource("search.ui"), self)
        print(self.__dict__)
