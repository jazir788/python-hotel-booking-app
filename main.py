import pandas as pd

df = pd.read_csv("hotels.csv", dtype= {"id":str})
df_cards = pd.read_csv("cards.csv", dtype= str).to_dict(orient="records")
df_cards_security = pd.read_csv("card_security.csv", dtype= str)


class User:
    def view_hotels(self, hotel_id):
        pass


class Hotel:

    def __init__(self,hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()


    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False




class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object
        pass
    def generate(self):
        content = f"""
        
        Thank you for the reservation!
        Here is your booking data
        Name: {self.customer_name}
        Hotel Name: {self.hotel.name}
"""
        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}

        if card_data in df_cards:
            return True
        else:
            return False

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


class SpaHotel(Hotel):
    def book_spa_package(self):
        pass


class SpaReservation:

    def __init__(self, customer_name, hotel_object):
            self.customer_name = customer_name
            self.hotel = hotel_object
    def generate(self):
        content = f"""

            Thank you for your spa reservation!
            Here are your SPA booking details:
            Name: {self.customer_name}
            Hotel Name: {self.hotel.name}
    """
        return content




print(df)
hotel_id = input("Enter the id of the hotel: ")
hotel = SpaHotel(hotel_id)
if hotel.available():
    credit_card_no = input("Enter your credit card number: ")
    credit_card_expiration = input("Enter your credit card expiration date in this format 'mm/yy': ")
    credit_card_holder = input("Enter your credit card holder name: ")
    credit_card_cvc = input("Enter your credit card cvc number: ")
    credit_card_password = input("Enter your credit card password: ")

    credit_card = SecureCreditCard(number = credit_card_no)
    if credit_card.validate(expiration=credit_card_expiration, holder = credit_card_holder, cvc = credit_card_cvc):
        if credit_card.authenticate(given_password= credit_card_password) == True:
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
            spa = input("Do you want to book a spa package: ")
            if spa == "yes":
                hotel.book_spa_package()
                spareservation = SpaReservation(name, hotel)
                print(spareservation.generate())
            else:
                print("Thank you for your booking")
        else:
            print("Credit Card authentication failed")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is not available")

