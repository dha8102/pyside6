from PySide6.QtWidgets import QApplication
from widget import 위젯
import sys

앱 = QApplication(sys.argv)
윈도우 = 위젯()
윈도우.show()
앱.exec()
 