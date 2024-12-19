from PySide6.QtWidgets import QApplication
from widget import 메인윈도우
import sys

앱 = QApplication(sys.argv)

윈도우 = 메인윈도우()
윈도우.show()
앱.exec()
