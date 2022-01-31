import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe")
        # Create a QGridLayout instance
        layout = QGridLayout()
        # Add widgets to the layout
        layout.setVerticalSpacing(10)   

        # Button Layouts
        row = 0
        column = 0
        for btn in range(9):
            button = QPushButton()     
            button.setMinimumWidth(100)
            button.setMinimumHeight(100)
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
        layout.addWidget(status, 3, 0, 1, 3)
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
        layout.addWidget(restart, 4, 0, 1, 3)
        # Set the layout on the application's window
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion') 
    window = Window()
    window.show()
    sys.exit(app.exec_())