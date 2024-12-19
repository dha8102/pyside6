from PySide6.QtWidgets import QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout
 
class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        레이블 = QLabel("이름:")
        self.라인에디트 = QLineEdit()
        self.라인에디트.returnPressed.connect(self.엔터키눌림)
        # self.라인에디트.textChanged.connect(self.텍스트변경)
        self.레이블2 = QLabel("나의 이름은:")
        
        수평레이아웃 = QHBoxLayout()
        수평레이아웃.addWidget(레이블)
        수평레이아웃.addWidget(self.라인에디트)
        
        수직레이아웃 = QVBoxLayout()
        수직레이아웃.addLayout(수평레이아웃)
        수직레이아웃.addWidget(self.레이블2)
        
        self.setLayout(수직레이아웃)
        
    def 엔터키눌림(self):
        print("이름:",self.라인에디트.text())
        self.레이블2.setText(self.라인에디트.text())
    
    def 텍스트변경(self):
        self.레이블2.setText(self.라인에디트.text())