from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtGui import QPixmap
 
class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        레이블 = QLabel("텍스트표시")
        이미지레이블 = QLabel()
        이미지레이블.setPixmap(QPixmap("05/이미지/로봇.png"))
        이미지레이블.mousePressEvent = self.이미지클릭
        레이아웃 = QVBoxLayout()
        레이아웃.addWidget(레이블)
        레이아웃.addWidget(이미지레이블)
        
        self.setLayout(레이아웃)
        
    def 이미지클릭(self, ev):
        print("이미지클릭")
        
        