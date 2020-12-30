"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 14:06:29 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

import sys

Form, Window = uic.loadUiType("search.ui")

app = QApplication(sys.argv)
app.setApplicationDisplayName("MovieBoat")
# init window & form
window = Window()
form = Form()
form.setupUi(window)
window.setWindowTitle("Home")
window.show()
sys.exit(app.exec_())
