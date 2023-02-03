import pandas as pd

df = pd.read_csv('hotels.csv', dtype={"id": str})
class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = df.loc[df['id'] == self.hotel_id, 'name'].squeeze()

    def available_room(self):
        #hotelid = int(self.hotel_id)
        avail = df.loc[df['id'] == self.hotel_id, 'available'].squeeze()
        if avail == 'yes':
            return True
        else:
            return False


    def bookRoom(self):
        df.loc[df['id'] == self.hotel_id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)
class Booking:
    def __init__(self, name, hotel):
        self.name = name
        self.hotel = hotel

    def generateTicket(self):
        return f'Hello  {self.name}, your booking for {self.hotel.hotel_name} is confirmed'

print(df)

hotel_id = input('Enter the id of the hotel to book')
hotel = Hotel(hotel_id)
if hotel.available_room():
    hotel.bookRoom()
    name = input('Enter your name')
    book = Booking(name, hotel)
    print(book.generateTicket())
else:
    print("Selected hotel not available to book")