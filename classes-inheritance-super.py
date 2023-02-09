class User():

    def __init__(self, email):
        self.email = email

    def sigh_in(self):
        print('User loged in')

class Wizard(User):
    def __init__( self, r5'name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with {self.num_arrows} arrows')

new_wizard = Wizard('Harry Potter', 'Speaking with snakes', 'wizard@gmail.com')
new_wizard.sigh_in()
new_wizard.attack()
