from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
 
class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        버튼1 = QPushButton("버튼1")
        버튼1.clicked.connect(self.버튼클릭)
        버튼2 = QPushButton("버튼2")
        버튼2.pressed.connect(self.버튼눌림)
        버튼3 = QPushButton("버튼3")
        버튼3.released.connect(self.버튼눌림해제)
        
        레이아웃 = QHBoxLayout()
        레이아웃.addWidget(버튼1)
        레이아웃.addWidget(버튼2)
        레이아웃.addWidget(버튼3)
        
        self.setLayout(레이아웃)
        
    def 버튼클릭(self):
        print("버튼클릭")
    def 버튼눌림(self):
        print("버튼눌림")
    def 버튼눌림해제(self):
        print("버튼눌림해제")
        