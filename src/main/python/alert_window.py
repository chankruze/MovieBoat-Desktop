"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 14:17:32 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""


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
