from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QMessageBox, QVBoxLayout

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        self.콤보박스  = QComboBox()
        self.콤보박스.addItem('A')
        self.콤보박스.addItem('B')
        self.콤보박스.addItem('C')
        self.콤보박스.currentIndexChanged.connect(self.변경)
        
        버튼1 = QPushButton("버튼1")
        버튼1.clicked.connect(self.버튼1클릭)
        버튼2 = QPushButton("버튼2")
        버튼2.clicked.connect(self.버튼2클릭)
        self.레이블 = QLabel()
        레이아웃 = QVBoxLayout()
        레이아웃.addWidget(self.콤보박스)
        레이아웃.addWidget(버튼1)
        레이아웃.addWidget(버튼2)
        레이아웃.addWidget(self.레이블)
        
        self.setLayout(레이아웃)
        
    def 변경(self):
        self.레이블.setText(str(self.콤보박스.currentIndex()))
    
    def 버튼1클릭(self):
        QMessageBox.about(self,"",self.콤보박스.currentText())
        
    def 버튼2클릭(self):
        self.콤보박스.setCurrentIndex(1)