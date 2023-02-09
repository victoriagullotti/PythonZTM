#OOP

class Player():
    
    membership = True

    #Constractor????
    def __init__(self, name='anonymous', age=0):
        if age >= 18:
            # attributes
            self.name = name
            self.age = age
            self._hight # Private variable (_). Do not owerite it!!!

    def shout(self):
        print(f'My name is {self.name}')

    #Using CLASSMETHOD without initiating the class object!!!

    @classmethod
    def add_something(cls, *args): # cls - class
        return sum(args)

    #Using STATICMETHOD. The difference is we dont have an access to Class
    @staticmethod
    def add_something_static(*args):
        return sum(args)

#New object of the class Player
new_player = Player('Tom', 20)

new_player.shout()

#Calling CLASSMETHOD !!!
print(Player.add_something(10, 20, 60))

#Calling STATICMETHOD !!!
print(Player.add_something_static(59, 10, 2))

#My name is Tom
#90
#71