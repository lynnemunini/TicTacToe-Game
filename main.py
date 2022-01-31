import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

choice = input("X or O: ").capitalize()


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe")
        # Create a QGridLayout instance
        layout = QGridLayout()
        game_title = QLabel("TicTacToe")
        game_title.setFont(QFont("Helvetica [Cronyx]", 20, QFont.Bold))
        game_title.setAlignment(Qt.AlignCenter)
        layout.addWidget(game_title, 0, 0, 1, 3)
        # Add widgets to the layout
        layout.setVerticalSpacing(10)   


        # Font
        r_one = QFont("RussoOne-Regular", 10, QFont.Bold) 

        # Buttons
        self.btn1 = QPushButton()
        self.btn2 = QPushButton()
        self.btn3 = QPushButton()
        self.btn4 = QPushButton()
        self.btn5 = QPushButton()
        self.btn6 = QPushButton()
        self.btn7 = QPushButton()
        self.btn8 = QPushButton()
        self.btn9 = QPushButton()        

        buttons = [self.btn1, 
                   self.btn2, 
                   self.btn3, 
                   self.btn4, 
                   self.btn5,
                   self.btn6,
                   self.btn7,
                   self.btn8,
                   self.btn9]

        row = 1
        column = 0 

        # Button Layouts
        for button in buttons: 
            button.setMinimumWidth(100)
            button.setMinimumHeight(100)
            button.setFont(r_one)
            # adding background color to button
            # and background color to pressed button
            button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : black;"
                             "}"
                             )
                
            layout.addWidget(button, row, column)
            # Set action to be performed on clicking                 
            button.clicked.connect(self.on_click(button)) 
            
            column += 1
            
            if column > 2:
                row += 1
                column = 0
             

        status = QPushButton("You Won!")

        status.setStyleSheet("QPushButton"
                             "{"
                             "background-color : white;"
                             "color : black;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             )

        status.setMinimumHeight(40)
        layout.addWidget(status, 4, 0, 1, 3)
        # Restart
        restart = QPushButton("Restart")

        restart.setStyleSheet("QPushButton"
                        "{"
                        "background-color : white;"
                        "color : black;"
                        "}"
                        "QPushButton::hover"
                        "{"
                        "background-color : lightgreen;"
                        "}"
                        )

        restart.setMinimumHeight(40)
        layout.addWidget(restart, 5, 0, 1, 3)
        # Set the layout on the application's window
        self.setLayout(layout)
        

    @pyqtSlot()
    # Explicitly mark method as being a Qt slot
    def on_click(self, button):
        def click(self):
            button.setText(choice)
        return click


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion') 
    # app.setFont(QFont("Times New Roman", 12))
    window = Window()
    window.show()
    sys.exit(app.exec_())