class Test:
    # Class responsible for testing if there's a winner
    def horizontal_compare(self, dictionary, position, dec_buttons_list, status):
        if position == "0" or position == "3" or position == "6":
            btn1 = position
            btn2 = str(int(position) + 1)
            btn3 = str(int(position) + 2)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)

                return game_over

        elif position == "1" or position == "4" or position == "7":
            btn1 = position
            btn2 = str(int(position) - 1)
            btn3 = str(int(position) + 1)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "2" or position == "5" or position == "8":
            btn1 = position
            btn2 = str(int(position) - 1)
            btn3 = str(int(position) - 2)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over


    def vertical_compare(self, dictionary, position, dec_buttons_list, status):
        if position == "0" or position == "1" or position == "2":
            btn1 = position
            btn2 = str(int(position) + 3)
            btn3 = str(int(position) + 6)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "3" or position == "4" or position == "5":
            btn1 = position
            btn2 = str(int(position) - 3)
            btn3 = str(int(position) + 3)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "6" or position == "7" or position == "8":
            btn1 = position
            btn2 = str(int(position) - 3)
            btn3 = str(int(position) - 6)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

    def diagonal1_compare(self, dictionary, position, dec_buttons_list, status):
        if position == "0":
            btn1 = position
            btn2 = str(int(position) + 4)
            btn3 = str(int(position) + 8)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "4":
            btn1 = position
            btn2 = str(int(position) - 4)
            btn3 = str(int(position) + 4)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "8":
            btn1 = position
            btn2 = str(int(position) - 4)
            btn3 = str(int(position) - 8)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

    def diagonal2_compare(self, dictionary, position, dec_buttons_list, status):
        if position == "2":
            btn1 = position
            btn2 = str(int(position) + 2)
            btn3 = str(int(position) + 4)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "4":
            btn1 = position
            btn2 = str(int(position) - 2)
            btn3 = str(int(position) + 2)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over

        elif position == "6":
            btn1 = position
            btn2 = str(int(position) - 2)
            btn3 = str(int(position) - 4)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                status.setText(f"{dictionary['button' + btn1]} Won!")
                game_over = True
                for button in dec_buttons_list:
                    button.setEnabled(False)
                return game_over