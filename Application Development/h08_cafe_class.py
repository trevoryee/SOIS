#h08_cafe_class.py

class restaurant():
    def __init__(self, restaurant_name,restaurant_type, restaurant_open):
        self.name= restaurant_name
        self.type= restaurant_type
        self.open= restaurant_open
    def describe_restaurant(self):
        print(self.name + ' is ' + self.type)
    def open_restaurant(self):
        print(self.name + ': ' + self.open)

class cafe(restaurant):
    def __init__(self, restaurant_name,restaurant_type,restaurant_open):
        super().__init__(restaurant_name,restaurant_type,restaurant_open)
        self.menu= []
    def menuprint(self):
        print('The menu at ' + self.name + ' is: ')
        for self.menu in self.menu:
            print("- " + self.menu.title())

mcdonald= restaurant('Mcdonalds','Fast Food','Open')
culvers= restaurant('Culvers','Fast Food','Closed')
wendys= restaurant('Wendys','Fast Food','Open')

cafebustelo= cafe('Cafe Bustelo','Cafe','Open')
cafebustelo.menu =['Coffee','Sandwich','Soda']

cafelucy= cafe('Cafe Lucy','Cafe','Open')
cafelucy.menu =['Croissant','Tea','Biscuit']


cafebustelo.describe_restaurant()
cafebustelo.menuprint()
cafelucy.describe_restaurant()
cafelucy.menuprint()