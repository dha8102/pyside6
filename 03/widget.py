from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout
from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton
from PySide6.QtGui import QAction

class 메인윈도우(QMainWindow):
    def __init__(self, 앱):
        self.앱 = 앱
        super().__init__() 
        self.setWindowTitle("메인윈도우 예제")
        메뉴바 = self.menuBar()
        파일메뉴 = 메뉴바.addMenu("&File")
        종료액션 = 파일메뉴.addAction("종료")
        종료액션.triggered.connect(self.종료액션클릭)
        
        에디트메뉴 = 메뉴바.addMenu('수정')
        에디트메뉴.addAction("복사")
        에디트메뉴.addAction("잘라내기")
        에디트메뉴.addAction("붙여넣기")
        
        툴바 = QToolBar()
        self.addToolBar(툴바)
        툴바.addAction(종료액션)
        
    def 종료액션클릭(self):
        self.앱.quit()
        