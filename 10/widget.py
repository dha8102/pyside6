from PySide6.QtWidgets import QWidget, QPushButton, QGroupBox, QHBoxLayout, QRadioButton, QMessageBox

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        사람 = QGroupBox("사람선택")
        self.홍길동 = QRadioButton("홍길동")
        self.홍길동.toggled.connect(self.토글)
        self.뽀로로 = QRadioButton("뽀로로")
        self.뽀로로.toggled.connect(self.토글)
        self.타요 = QRadioButton("타요")
        self.타요.toggled.connect(self.토글)
        self.타요.setChecked(True)
        사람레이아웃 = QHBoxLayout()
        사람레이아웃.addWidget(self.홍길동)
        사람레이아웃.addWidget(self.뽀로로)
        사람레이아웃.addWidget(self.타요)
        
        사람.setLayout(사람레이아웃)
        
        선택버튼 = QPushButton("선택")
        선택버튼.clicked.connect(self.선택버튼클릭)
        레이아웃 = QHBoxLayout()
        레이아웃.addWidget(사람)
        레이아웃.addWidget(선택버튼)
        
        self.setLayout(레이아웃)
        
    def 토글(self, chk):
        센더 = self.sender()
        print(chk, 센더.text())
        
    def 선택버튼클릭(self):
        if self.홍길동.isChecked():
            QMessageBox.about(self,"제목", self.홍길동.text())
        elif self.뽀로로.isChecked():
            QMessageBox.about(self,"제목", self.뽀로로.text())
        elif self.타요.isChecked():
            QMessageBox.about(self,"제목", self.타요.text())