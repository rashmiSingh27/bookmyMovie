# book my movie ticket project without using DB.

class BookMyMovie:
    user_details = {}
    current_income = 0

    def __init__(self):
        print("** Welcome to BookMyMovie **")
        self.rows = int(input("Enter the number of rows:"))
        self.colms = int(input("Enter number of seats in each row:"))
        self.total_seats = self.rows * self.colms
        self.price_of_a_seat = 0
        self.price_of_back_half = 0
        self.price_of_front_half = 0
        self.row = 0
        self.column = 0
        self.no_of_booked_ticket = 0
        self.percentage = 0
        self.total_income = 0
        self.currently_income = 0
        self.d1 = {}
        self.booked = False
        self.t = []
        self.dummy = []
        self.x = [" "]
        self.show_seats1()

    def show_seats1(self):
        self.q = [str(i) for i in range(1, self.rows+1)]  # keys for dict
        for i in range(self.rows):
            self.t.append(["S" for i in range(1, self.colms+1)])  # keys for dict
        if self.booked:
            self.update_cinema()
        self.d1 = dict.fromkeys(self.q)
        for i in range(1, len(self.t)+1):
            self.d1[str(i)] = self.t[i-1]
        [self.x.append(i) for i in range(1, self.colms+1)]

    def update_cinema(self):
        self.t[self.row-1][self.column-1] = "B"

    def show_seats(self):
        for i in self.x:
            print(i, end=" ")
        print("\n")
        for k in self.d1:
            print(k, end=" ")
            print(' '.join(self.d1[k]))

    def buy_ticket1(self):

        if self.total_seats == 1 and self.t[0][0] == "B":
            return "full_cinema"
        else:
            for i in self.t:
                for j in i:
                    self.dummy.append(j)
            if "S" in self.dummy:
                return "avail"
            else:
                return "full_cinema"

    def buy_ticket2(self):
        self.row = int(input("enter row no to be booked:"))
        self.column = int(input("enter column no to be booked:"))
        if self.row > self.rows or self.column > self.colms:
            return "seat_not_present"
        else:

            if self.t[self.row-1][self.column-1] == "B":
                print("this seat is already booked.View in option 1 ")
                return "seat_not_available"
            else:
                return "available"

    def book_ticket(self):
        if self.total_seats < 60:
            print("***This is a small cinema,so prices of all seats are equal***")
            self.price_of_a_seat = 10
            print("price of your ticket is $ ", self.price_of_a_seat)
        if self.total_seats >= 60:
            print("***this is a bigger cinema hall so prices of front seats are high***")
            self.price_of_front_half = 10
            self.price_of_back_half = 8
            if self.row <= self.rows // 2:
                print("Price of your ticket is $ ", self.price_of_front_half)
                self.price_of_a_seat = self.price_of_front_half
            else:
                print("Price of your ticket is $ ", self.price_of_back_half)
                self.price_of_a_seat = self.price_of_back_half

        confirmation = str(input("Confirm booking by Y or N:"))
        if confirmation == "Y":
            name = input("enter you name:")
            BookMyMovie.user_details["name"] = name
            gender = input("enter you gender(M/F):")
            while gender not in ["m", "M", "f", "F"]:
                print("gender not in correct format")
                gender = input("enter you gender(M/F):")
            BookMyMovie.user_details["gender"] = gender

            age = int(input("enter you age:"))
            BookMyMovie.user_details["age"] = age
            phone_num = input('Please enter your 10 digit number:')
            while len(phone_num) != 10 or (not phone_num.isdigit()):
                print('Not a 10 digit number')
                phone_num = input('Please enter your 10 digit number:')
            phone_num = int(phone_num)
            BookMyMovie.user_details["phone_no"] = phone_num
            BookMyMovie.current_income += self.price_of_a_seat
            self.booked = True
            self.update_cinema()
            return "Booked"

        else:
            self.booked = False
            return "not booked"

    def buy_ticket(self):
        a = self.book_ticket()
        if a == "Booked":
            return a
        else:
            return "not booked"

    def statistics(self, no_of_booked_ticket):
        print("---STATISTICS---")
        if self.booked:

            self.no_of_booked_ticket = no_of_booked_ticket
            self.percentage = (self.no_of_booked_ticket / self.total_seats) * 100
            self.total_income = BookMyMovie.current_income
            self.currently_income = self.price_of_a_seat
            print("No_of_booked_ticket: ", self.no_of_booked_ticket)
            print("Percentage: ", self.percentage, "%")
            print("Total_income:", "$", self.total_income)
            print("Current_income: ", "$", self.currently_income)
            print("\n")
        else:
            print("No Statistics available.Try after booking a Tikcet")

    def booked_user_info(self):
        print("---LAST USER INFO---")
        if not self.booked:
            print("No user information available for now .Book a ticket")
            print("*****************************************************")
        else:

            print("Name:", BookMyMovie.user_details["name"])
            print("Gender:", BookMyMovie.user_details["gender"])
            print("Age:", BookMyMovie.user_details["age"])
            print("Ticket price:", self.price_of_a_seat)
            print("phone_number:", BookMyMovie.user_details["phone_no"])
            print("seat booked:", self.row, "X", self.column)
            print("\n")


def main():
    user = BookMyMovie()
    no_of_booked_ticket = 0

    while 1:
        print("---MENU---")
        print("1.Show the seats")

        print("2.Buy a Ticket")

        print("3.Statistics")

        print("4.Show booked ticket user info")

        print("5.EXIT")

        b = int(input("\nEnter your choice:"))
        if b == 1:
            user.show_seats()

        if b == 2:
            full = user.buy_ticket1()
            if full == "avail":
                full2 = user.buy_ticket2()
                while full2 == "seat_not_available":
                    full2 = user.buy_ticket2()
                if full2 == "available":
                    booked = user.buy_ticket()
                    if booked == "Booked":
                        print("Your ticket is BOOKED successfully !!!")
                        no_of_booked_ticket += 1
                        print("*********************************************")
                    if booked == "not booked":
                        print("Booking is CANCELED !!!")
                        print("**********************************************")
                if full2 == "seat_not_present":
                    print("SORRY!! This seat is  not present in cinema.Check option 1 .")
                    print("************************************************************")
            if full == "full_cinema":
                print("SORRY!!! Cinema is full.")
                print("********************************************************")

        if b == 3:
            user.statistics(no_of_booked_ticket)

        if b == 4:
            user.booked_user_info()

        if b == 5:
            quit()


main()
