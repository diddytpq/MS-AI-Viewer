from PySide6.QtWidgets import QApplication, QMainWindow, QSlider
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Qt App")
        self.setGeometry(100, 100, 600, 400)

        # 윈도우 아이콘 설정
        self.setWindowIcon(QIcon('./ui/images/icon2.ico'))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # QApplication 아이콘 설정 (작업 표시줄에 표시됨)
    app.setWindowIcon(QIcon('./ui/images/icon2.ico'))

    main_window = MainWindow()
    main_window.show()

    sys.exit(app.exec_())