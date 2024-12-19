from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QTabWidget

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        탭위젯 = QTabWidget()
        
        위젯1 = QWidget()
        레이블 = QLabel("여기는 탭1입니다")
        수평레이아웃 = QHBoxLayout()
        수평레이아웃.addWidget(레이블)
        위젯1.setLayout(수평레이아웃)
        
        위젯2 = QWidget()
        버튼1 = QPushButton("버튼1")
        버튼2 = QPushButton("버튼2")
        버튼3 = QPushButton("버튼3")
        수직레이아웃 = QVBoxLayout()
        수직레이아웃.addWidget(버튼1)
        수직레이아웃.addWidget(버튼2)
        수직레이아웃.addWidget(버튼3)
        위젯2.setLayout(수직레이아웃)
        
        탭위젯.addTab(위젯1, "탭1")
        탭위젯.addTab(위젯2, "탭2")
        
        레이아웃 = QVBoxLayout()
        레이아웃.addWidget(탭위젯)
        self.setLayout(레이아웃)