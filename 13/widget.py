from PySide6.QtWidgets import QWidget, QPushButton, QGridLayout, QSizePolicy    

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        버튼1 = QPushButton("버튼1")
        버튼2 = QPushButton("버튼2")
        버튼2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        버튼3 = QPushButton("버튼3")
        버튼4 = QPushButton("버튼4")
        버튼5 = QPushButton("버튼5")
        버튼6 = QPushButton("버튼6")
        버튼7 = QPushButton("버튼7")
        버튼8 = QPushButton("버튼8")
        버튼9 = QPushButton("버튼9")
        
        그리드 = QGridLayout()
        그리드.addWidget(버튼1,0,0)
        그리드.addWidget(버튼2,0,1,2,2)
        # 그리드.addWidget(버튼3,0,2)
         
        그리드.addWidget(버튼4,1,0)
        # 그리드.addWidget(버튼5,1,1)
        # 그리드.addWidget(버튼6,1,2)
        
        그리드.addWidget(버튼7,2,0)
        그리드.addWidget(버튼8,2,1)
        그리드.addWidget(버튼9,2,2)
        
        self.setLayout(그리드)