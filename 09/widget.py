from PySide6.QtWidgets import QWidget, QCheckBox, QGroupBox, QVBoxLayout, QButtonGroup

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        국가 = QGroupBox("국가선택")
        한국 = QCheckBox("한국")
        한국.toggled.connect(self.토글)
        미국 = QCheckBox("미국")
        미국.toggled.connect(self.토글)
        프랑스 = QCheckBox("프랑스")
        프랑스.toggled.connect(self.토글)
        한국.setChecked(True)

        국적레이아웃 = QVBoxLayout()
        국적레이아웃.addWidget(한국)
        국적레이아웃.addWidget(미국)
        국적레이아웃.addWidget(프랑스)
        
        국가.setLayout(국적레이아웃)
        
        도시 = QGroupBox("도시선택")
        서울 = QCheckBox("서울")
        뉴욕 = QCheckBox("뉴욕")
        파리 = QCheckBox("파리")
        서울.setChecked(True)
        
        버튼그룹 = QButtonGroup(self)
        버튼그룹.addButton(서울)
        버튼그룹.addButton(뉴욕)
        버튼그룹.addButton(파리)
        버튼그룹.setExclusive(True)
        
        도시레이아웃 = QVBoxLayout()
        도시레이아웃.addWidget(서울)
        도시레이아웃.addWidget(뉴욕)
        도시레이아웃.addWidget(파리)
        도시.setLayout(도시레이아웃)
        
        
        레이아웃 = QVBoxLayout()
        레이아웃.addWidget(국가)
        레이아웃.addWidget(도시)
        
        self.setLayout(레이아웃)
        
    def 토글(self, chk):
        센더 = self.sender()
        print(chk, 센더.text())