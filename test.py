def compare():
    if self.btn1.text() == self.btn2.text() == self.btn3.text():
        print(f"{self.btn1.text()} Won!")
        game_over = True

    elif self.btn4.text() == self.btn5.text() == self.btn6.text():
        print(f"{self.btn4.text()} Won!")
        game_over = True

    elif self.btn7.text() == self.btn8.text() == self.btn9.text():
        print(f"{self.btn4.text()} Won!")
        game_over = True

    elif self.btn3.text() == self.btn5.text() == self.btn7.text():
        print(f"{self.btn3.text()} Won!")
        game_over = True

    elif self.btn1.text() == self.btn5.text() == self.btn9.text():
        print(f"{self.btn1.text()} Won!")
        game_over = True

    else:
        if len(dec_buttons_list) == 0:
            print("Draw!!")
            game_over = True

    return game_over
