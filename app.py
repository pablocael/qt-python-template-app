import sys
import logging
import argparse
from decouple import config
from core.logsystem import setup_logging_system
from gui.MainWindow_ui import Ui_MainWindow

from PySide2.QtWidgets import QApplication, QMainWindow

setup_logging_system('logs/main.log')

parser = argparse.ArgumentParser(description='Qt Template Application')

parser.add_argument('--debug_mode', dest='debug_mode', action='store_true', default=False,
                    help='Just a template argument to be modified')
args = parser.parse_args()

# global app parameters
app_debug_mode = args.debug_mode

logger = logging.getLogger(__name__)

logger.info('initializing application')
logger.info(f'args are: {args}')

class MainAppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)
        self.initialize_state()


    def initialize_state(self):
        # read things from settings
        self._debug_mode = config('DEBUG_MODE', False, cast=bool)

    #
    # UI Related methods
    #

    #
    # App Logic Related methods
    #

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainAppWindow = MainAppWindow()
    mainAppWindow.show()
    sys.exit(app.exec_())
