from PySide6.QtWidgets import QWidget, QPushButton, QListWidget, QAbstractItemView, QMessageBox, QVBoxLayout

class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        self.리스트위젯 = QListWidget()
        self.리스트위젯.setSelectionMode(QAbstractItemView.MultiSelection)
        self.리스트위젯.addItem("홍길동")
        self.리스트위젯.addItem("임꺽정")
        self.리스트위젯.addItems(['타요', '뽀로로'])
        self.리스트위젯.itemClicked.connect(self.아이템선택)
        
        버튼추가 = QPushButton('아이템 추가')
        버튼추가.clicked.connect(self.아이템추가)
        버튼삭제 = QPushButton('아이템 삭제')
        버튼삭제.clicked.connect(self.아이템삭제)
        버튼카운트 = QPushButton('아이템 갯수')
        버튼카운트.clicked.connect(self.아이템갯수)
        버튼선택 = QPushButton('선택된 아이템')
        버튼선택.clicked.connect(self.선택된아이템)            
        
        레이아웃 = QVBoxLayout()
        레이아웃.addWidget(self.리스트위젯)
        레이아웃.addWidget(버튼추가)
        레이아웃.addWidget(버튼삭제)
        레이아웃.addWidget(버튼카운트)
        레이아웃.addWidget(버튼선택)
        
        self.setLayout(레이아웃)
        
    def 아이템선택(self):
        print("선택한 아이템:", self.리스트위젯.currentItem().text())
    def 아이템갯수(self):
        QMessageBox.about(self,'',str(self.리스트위젯.count()))
    def 아이템삭제(self):
        self.리스트위젯.takeItem(self.리스트위젯.currentRow())
    def 아이템추가(self):
        self.리스트위젯.addItem('카봇')
    def 선택된아이템(self):
        lst = self.리스트위젯.selectedItems()
        for i in lst:
            print(i.text())
        