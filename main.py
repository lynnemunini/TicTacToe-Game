import sys
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import random
from test import Test

test = Test()
players = ["X", "O"]
choice = random.choice(players)

dec_buttons_list = []
buttons_dict = {
    'button0': '',
    'button1': '',
    'button2': '',
    'button3': '',
    'button4': '',
    'button5': '',
    'button6': '',
    'button7': '',
    'button8': ''
}

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TicTacToe")
        # Create a QGridLayout instance
        layout = QGridLayout()

        game_title = QLabel(f"You are {choice}!")
        game_title.setFont(QFont("Helvetica [Cronyx]", 20, QFont.Bold))
        game_title.setAlignment(Qt.AlignCenter)

        layout.addWidget(game_title, 0, 0, 1, 3)
        # Add widgets to the layout
        layout.setVerticalSpacing(10)  
        
        # Font
        font = QFont("RussoOne-Regular", 20, QFont.Bold) 

        # Buttons
        self.btn1 = QPushButton("")
        self.btn2 = QPushButton("")
        self.btn3 = QPushButton("")
        self.btn4 = QPushButton("")
        self.btn5 = QPushButton("")
        self.btn6 = QPushButton("")
        self.btn7 = QPushButton("")
        self.btn8 = QPushButton("")
        self.btn9 = QPushButton("")        

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

        # Status Button
        status = QPushButton("")
        status.setFont(QFont("Helvetica [Cronyx]", 12, QFont.Bold))

        status.setStyleSheet(
                             "QPushButton"
                             "{"
                             "background-color : lightgreen;"
                             "color : black;"
                             "}"
                             "QPushButton::hover"
                             "{"
                             "background-color : white;"
                             "color : lightgreen;"
                             "}"
                             )

        status.setMinimumHeight(40)
        layout.addWidget(status, 4, 0, 1, 3)

        # Button Layouts
        for iteration, button in enumerate(buttons):    
            # print(iteration)
            button.setMinimumWidth(100)
            button.setMinimumHeight(100)
            button.setFont(font)
            # adding background color to button
            # and background color to pressed button
            button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : lightgreen;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : white;"
                             "}"
                             )


            layout.addWidget(button, row, column)
            dec_buttons_list.append(button)

            # Set action to be performed on clicking                 
            button.clicked.connect(self.on_click(button, iteration, buttons, status)) 

            column += 1
            
            if column > 2:
                row += 1
                column = 0        
            
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
        restart.clicked.connect(self.reset_game) 
        layout.addWidget(restart, 5, 0, 1, 3)
        # Set the layout on the application's window
        self.setLayout(layout)


    # Explicitly mark method as being a Qt slot
    @pyqtSlot()
    def on_click(self, button, iteration, buttons, status):
        def click(self):
                # choice = self.choice
                button.setStyleSheet("QPushButton"
                                "{"
                                "background-color : white;"
                                "}")


                button.setText(choice)
                buttons_dict[f"button{iteration}"] = choice


                # Disabling buttons after clicking
                button.setEnabled(False)
                

                if len(dec_buttons_list) != 0:
                    dec_buttons_list.remove(button)

                try:
                    if test.horizontal_compare(buttons_dict, str(iteration), dec_buttons_list, status) != True and \
                    test.vertical_compare(buttons_dict, str(iteration), dec_buttons_list, status) != True and \
                    test.diagonal1_compare(buttons_dict, str(iteration), dec_buttons_list, status) != True and \
                    test.diagonal2_compare(buttons_dict, str(iteration), dec_buttons_list, status) != True:
                        computer = random.choice(dec_buttons_list)
                        # Get the index of the random button in original buttons list
                        position = buttons.index(computer)
                        
                        if choice == "X":
                            computer.setText("O")
                            buttons_dict[f"button{position}"] = "O"
                        elif choice == "O":
                            computer_choice = computer.setText("X")
                            buttons_dict[f"button{position}"] = "X"
                        
                        test.horizontal_compare(buttons_dict, str(position), dec_buttons_list, status)
                        test.vertical_compare(buttons_dict, str(position), dec_buttons_list, status)
                        test.diagonal1_compare(buttons_dict, str(position), dec_buttons_list, status)
                        test.diagonal2_compare(buttons_dict, str(position), dec_buttons_list, status)
                        
                        computer.setEnabled(False)
                        dec_buttons_list.remove(computer)

                except:
                    status.setText("DRAW!!...GAME OVER!!")          

        return click

    def reset_game(self):
        # Restart the QApplication
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)
        # print(status)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion') 
    window = Window()
    window.show()
    sys.exit(app.exec_())