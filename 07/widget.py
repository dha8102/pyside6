from PySide6.QtWidgets import QMainWindow, QPushButton, QTextEdit, QToolBar 
class 메인윈도우(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("메인윈도우 예제")
        self.텍스트에디트 = QTextEdit()
        복사버튼 = QPushButton("복사")
        복사버튼.clicked.connect(self.텍스트에디트.copy)
        
        잘라내기버튼 = QPushButton('잘라내기')
        잘라내기버튼.clicked.connect(self.텍스트에디트.cut)
        
        붙여넣기버튼 = QPushButton("붙여넣기")
        붙여넣기버튼.clicked.connect(self.텍스트에디트.paste)
        
        실행취소버튼 = QPushButton("실행취소")
        실행취소버튼.clicked.connect(self.텍스트에디트.undo)
        
        재실행버튼 = QPushButton("재실행")
        재실행버튼.clicked.connect(self.텍스트에디트.redo)
        
        클리어버튼 = QPushButton("클리어")
        클리어버튼.clicked.connect(self.텍스트에디트.clear)
        
        플레인텍스트버튼 = QPushButton("플레인 텍스트")
        플레인텍스트버튼.clicked.connect(self.플레인텍스트버튼클릭)
        
        html버튼 = QPushButton("HTML")
        html버튼.clicked.connect(self.html버튼클릭)
        
        툴바 = QToolBar()
        self.addToolBar(툴바)
        툴바.addWidget(복사버튼)
        툴바.addWidget(잘라내기버튼)
        툴바.addWidget(붙여넣기버튼)
        툴바.addWidget(실행취소버튼)
        툴바.addWidget(재실행버튼)
        툴바.addWidget(클리어버튼)
        툴바.addWidget(플레인텍스트버튼)
        툴바.addWidget(html버튼)
        
        self.setCentralWidget(self.텍스트에디트)
    
    def 플레인텍스트버튼클릭(self):
        self.텍스트에디트.setPlainText("ABCDEFG")
    def html버튼클릭(self):
        self.텍스트에디트.setHtml("<h1>abcd</H1><BR>efggg")