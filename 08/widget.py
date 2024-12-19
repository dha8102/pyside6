from PySide6.QtWidgets import QWidget, QPushButton, QMessageBox, QVBoxLayout
 
class 위젯(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("위젯 예제")
        크리티컬버튼 = QPushButton("크리티컬")
        크리티컬버튼.clicked.connect(self.크리티컬버튼클릭)
        인포메이션버튼 = QPushButton("인포메이션")
        인포메이션버튼.clicked.connect(self.인포메이션버튼클릭)
        워닝버튼 = QPushButton("워닝")
        워닝버튼.clicked.connect(self.워닝버튼클릭)
        퀘스천버튼 = QPushButton("퀘스천")
        퀘스천버튼.clicked.connect(self.퀘스천버튼클릭)
        어바웃버튼 = QPushButton("어바웃")
        어바웃버튼.clicked.connect(self.어바웃버튼클릭)
        레이아웃 = QVBoxLayout()
        레이아웃.addWidget(크리티컬버튼)
        레이아웃.addWidget(인포메이션버튼)
        레이아웃.addWidget(워닝버튼)
        레이아웃.addWidget(퀘스천버튼)
        레이아웃.addWidget(어바웃버튼)
        self.setLayout(레이아웃)
        
    def 크리티컬버튼클릭(self):
        메세지박스 = QMessageBox()
        메세지박스.setWindowTitle("제목")
        메세지박스.setText("본문")
        메세지박스.setInformativeText('내용')
        메세지박스.setIcon(QMessageBox.Icon.Critical)
        메세지박스.setStandardButtons(QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        결과값 = 메세지박스.exec()
        
        if 결과값 == QMessageBox.StandardButton.Yes:
            print("yes를 클릭했습니다")
        else:
            print("no를 클릭했습니다")
            
    def 인포메이션버튼클릭(self):
        결과값 = QMessageBox.information(self, "제목", "본문", QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        
        if 결과값 == QMessageBox.StandardButton.Yes:
            print("yes를 클릭했습니다")
        else:
            print("no를 클릭했습니다")
        
    def 워닝버튼클릭(self):
        결과값 = QMessageBox.warning(self, "제목", "본문", QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        if 결과값 == QMessageBox.StandardButton.Ok:
            print("yes를 클릭했습니다")
        else:
            print("no를 클릭했습니다")
            
    def 퀘스천버튼클릭(self):
        결과값 = QMessageBox.question(self, "제목", "본문", QMessageBox.StandardButton.Ok|QMessageBox.StandardButton.Cancel)
        if 결과값 == QMessageBox.StandardButton.Ok:
            print("yes를 클릭했습니다")
        else:
            print("no를 클릭했습니다")
            
    def 어바웃버튼클릭(self):
        결과값 = QMessageBox.about(self, "제목", "본문")