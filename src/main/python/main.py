from fbs_runtime.application_context.PyQt5 import ApplicationContext
from fbs_runtime.application_context import cached_property

import sys
from quote_window import MainWindow


class AppContext(ApplicationContext):
    @cached_property
    def window(self):
        # return Window(self.db)
        return MainWindow()

    @cached_property
    def db(self):
        return Database()

    def run(self):
        # apply styles to app
        stylesheet = self.get_resource('styles.qss')
        self.app.setStyleSheet(open(stylesheet).read())
        # window
        self.window.resize(300, 150)  # width, height
        self.window.show()
        return self.app.exec_()


if __name__ == '__main__':
    appctxt = AppContext()
    sys.exit(appctxt.run())  # exit_code = ApplicationContext().app.exec_()
