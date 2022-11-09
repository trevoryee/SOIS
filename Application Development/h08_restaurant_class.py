#h08_restaurant_class.py

class restaurant:
    def __init__(self, restaurant_name,restaurant_type, restaurant_open):
        self.name= restaurant_name
        self.type= restaurant_type
        self.open= restaurant_open
    def describe_restaurant(self):
        print(self.name + ' is ' + self.type)
    def open_restaurant(self):
        print(self.name + ': ' + self.open)

mcdonald= restaurant('Mcdonalds','Fast Food','Open')
culvers= restaurant('Culvers','Fast Food','Closed')
wendys= restaurant('Wendys','Fast Food','Open')

print(mcdonald.name)
print(mcdonald.type)
mcdonald.describe_restaurant()
mcdonald.open_restaurant()

culvers.describe_restaurant()
culvers.open_restaurant()