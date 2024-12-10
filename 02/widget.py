from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
 
class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        레이블 = QLabel("레이블")
        버튼 = QPushButton("클릭")
        레이아웃 = QHBoxLayout()
        레이아웃.addWidget(레이블)
        레이아웃.addWidget(버튼)
        self.setLayout(레이아웃)
        