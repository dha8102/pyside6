from PySide6.QtWidgets import QWidget, QPushButton, QSizePolicy, QLineEdit, QHBoxLayout, QVBoxLayout

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        라인에디트 = QLineEdit()
        라인에디트.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        수평레이아웃1 = QHBoxLayout()
        수평레이아웃1.addWidget(라인에디트)
        
        버튼1 = QPushButton("버튼1")
        버튼2 = QPushButton("버튼2")
        버튼3 = QPushButton("버튼3")
        
        수평레이아웃2 = QHBoxLayout()
        수평레이아웃2.addWidget(버튼1, 2)
        수평레이아웃2.addWidget(버튼2, 1)
        수평레이아웃2.addWidget(버튼3, 3)
        
        수직레이아웃 = QVBoxLayout()
        수직레이아웃.addLayout(수평레이아웃1)
        수직레이아웃.addLayout(수평레이아웃2)
        self.setLayout(수직레이아웃)
        