import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic  # Qt Designer에서 제작한 UI를 호출하는 Class

form_class = uic.loadUiType("ui/uiTest.ui")[0]  # Qt Desinger에서 제작한 ui 파일을 불러온다. 뒤에 index번호 꼭 붙여야한다

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()  # 부모클래스 생성자 호출
        self.setupUi(self)  # 위에서 불러온 uiTest.ui 를 연결
        self.setWindowTitle("연습 프로그램")
        self.Button1.clicked.connect(self.button1Click)
        self.Button2.clicked.connect(self.button2Click)
        #(self.button2Click) 부분에서 button2Click 이 함수이므로 자동완성으로 뒤에 () 붙는데 ()는 빼줘야한다

    def button1Click(self):
        self.LabelTxt.setText("Hello World!!!")
    def button2Click(self):
        self.LabelTxt.setText("안녕하세요!!!!!!!!")

if __name__ == "__main__":
    app = QApplication(sys.argv) # 모든 응용프로그램이 작동하려면 QApplication 객체 필요.
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())   # 창을 닫아주는 명령어