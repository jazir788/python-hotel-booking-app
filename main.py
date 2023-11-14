import pandas as pd

df = pd.read_csv("hotels.csv")

class User:
    def view_hotels(self, id):
        self.id = id
        pass


class Hotel:
    def book(self):
        pass
    def available(self):
        pass


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        pass
    def generate(self):
        pass


print(df)
id = input("Enter the id of the hotel: ")
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is not available")