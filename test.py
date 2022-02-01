class Test:
    # Class responsible for testing if there's a winner
    def horizontal_compare(self, dictionary, position, dec_buttons_list):
        if position == "0" or position == "3" or position == "6":
            btn1 = position
            btn2 = str(int(position) + 1)
            btn3 = str(int(position) + 2)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                print(f"{dictionary['button' + btn1]} Won!")

        elif position == "1" or position == "4" or position == "7":
            btn1 = position
            btn2 = str(int(position) - 1)
            btn3 = str(int(position) + 1)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                print(f"{dictionary['button' + btn1]} Won!")

        elif position == "2" or position == "5" or position == "8":
            btn1 = position
            btn2 = str(int(position) - 1)
            btn3 = str(int(position) - 2)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                print(f"{dictionary['button' + btn1]} Won!")


    def vertical_compare(self, dictionary, position, dec_buttons_list):
        if position == "0" or position == "1" or position == "2":
            btn1 = position
            btn2 = str(int(position) + 3)
            btn3 = str(int(position) + 6)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                print(f"{dictionary['button' + btn1]} Won!")

        elif position == "3" or position == "4" or position == "5":
            btn1 = position
            btn2 = str(int(position) - 3)
            btn3 = str(int(position) + 3)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                print(f"{dictionary['button' + btn1]} Won!")

        elif position == "6" or position == "7" or position == "8":
            btn1 = position
            btn2 = str(int(position) - 3)
            btn3 = str(int(position) - 6)
            if dictionary["button" + btn1] == dictionary["button" + btn2] == dictionary["button" + btn3]:
                print(f"{dictionary['button' + btn1]} Won!")