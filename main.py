print("****WELCOME TO BOOKYOURMOVIE.COM*****")
rows = int(input("\n Enter number of rows:"))
columns = int(input("\n Enter the number of seats in each row:"))

seat_rows = []
for i in range(rows):
    seats = []
    for j in range(columns):
        seats.append('S')
    seat_rows.append(seats)



class Booking:
    def __init__(self, Name, Gender, Age, Phone, Price):
        self.Name = Name
        self.Gender = Gender
        self.Age = Age
        self.Phone = Phone
        self.Price = Price


def calculate_price(rows):
    if rows * columns <= 60:
        return 10
    else:
        if rows <= (rows // 2):
            return 10
        else:
            return 8


booking_dict = {}
number_of_tickets = 0
current_income = 0
total_income = 0


def book_ticket():
    rows = int(input("\nEnter row: "))
    columns = int(input("\nEnter column: "))
    price = calculate_price(rows)
    answer = input("\nPrice of your ticket is " + str(price) + ". Please press Yes and enter if you want to book.")
    if answer == 'Yes':
        name = str(input("\nName:"))
        gender = str(input("\nGender: "))
        age = str(input("\nAge: "))
        phone = int(input("\nphone number: "))
        booking = Booking(name, gender, age, phone, price)
        booking_dict[(rows, columns)] = booking
        seat_rows[rows - 1][columns - 1] = 'B'
        return price
    elif seat_rows[rows - 1][columns - 1] == 'B':

        print("Seat already booked, please enter another seat no.")
        book_ticket()
    else:
        return


def print_seat_map():
    for i in range(rows + 1):
        for j in range(columns + 1):
            if i == 0:
                print(j, " ", end="")
            else:
                if j == 0:
                    print(i, " ", end="")
                else:
                    print(seat_rows[i - 1][j - 1], " ", end="")
        print("\n")


def income():
    if price == 10:
        print((rows * columns) * 10)
    elif price == 8:
        print((rows * columns) * 8)


def info(rows, columns):
    class_val = booking_dict[(rows, columns)]
    print("\nName:" + class_val.Name)
    print("Gender:" + class_val.Gender)
    print("Age:" + class_val.Age)
    print("Ticket price:" + str(class_val.Price))
    print("Phone no:" + str(class_val.Phone))


n = 0
while n != 5:
    print("\n1. Show the seats\n2. Buy a ticket\n3. Statistics\n4. Show booked tickets user info\n5. Exit")
    n = int(input())
    if n == 1:

        print_seat_map()
    elif n == 2:
        price = book_ticket()
        current_income = price
        number_of_tickets += 1
        total_income += price

        print("Your Ticket is booked!! Enjoy the movie")

    elif n == 3:
        print("\nNumber of purchased tickets:" + str(number_of_tickets))
        print("\nPercentage:" + str(((number_of_tickets) / (rows * columns)) * 100) + "%")
        print("\nCurrent Income: $" + str(current_income))
        print("\nTotal Income: $" + str((rows * columns) * 10))
    elif n == 4:
        rows = int(input("Enter row:"))
        columns = int(input("Enter column:"))
        info(rows, columns)