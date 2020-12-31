"""
Author: chankruze (chankruze@geekofia.in)
Created: Wed Dec 30 2020 21:33:11 GMT+0530 (India Standard Time)

Copyright (c) Geekofia 2020 and beyond
"""
from fbs_runtime.application_context import cached_property

# application context (fbs)
from base import app_context

import sys
# from quote_window import MainWindow
from search import SearchWindow


class App():
    @cached_property
    def home_window(self):
        # return Window(self.db)
        return SearchWindow()

    # @cached_property
    # def db(self):
    #     return Database()

    def run(self):
        # apply styles to app
        stylesheet = app_context.get_resource('styles.qss')
        app_context.app.setStyleSheet(open(stylesheet).read())
        # main home window
        self.home_window.resize(1000, 800)  # width, height
        self.home_window.show()

        return app_context.app.exec_()


if __name__ == '__main__':
    sys.exit(App().run())  # exit_code = ApplicationContext().app.exec_()
