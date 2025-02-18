import sys
from PyQt5.QtWidgets import QApplication
from gui import TradingGUI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TradingGUI()
    window.show()
    sys.exit(app.exec_())
