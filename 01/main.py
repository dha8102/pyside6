from PySide6.QtWidgets import QApplication, QWidget
# QApplication: GUI 제어, 기본 설정 관리
# QWidget: 프로그램의 기본이 되는 창
import sys
 
앱 = QApplication(sys.argv)
print(sys.argv)
윈도우 = QWidget()
윈도우.show()

앱.exec()