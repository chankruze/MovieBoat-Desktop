"""
Author: chankruze (chankruze@geekofia.in)
Created: Tue Dec 29 2020 19:55:38 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

import requests


def _get_quote():
    return requests.get('https://build-system.fman.io/quote').text


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        text = QLabel()
        text.setWordWrap(True)
        button = QPushButton('Next quote >')
        button.clicked.connect(lambda: text.setText(_get_quote()))
        layout = QVBoxLayout()
        layout.addWidget(text)
        layout.addWidget(button)
        layout.setAlignment(text, Qt.AlignHCenter)
        layout.setAlignment(button, Qt.AlignHCenter)
        self.setLayout(layout)
