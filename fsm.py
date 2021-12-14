from transitions import Machine
class PizzaOrder(object):

    def __init__(self, id):
        self.machine = Machine(model=self, states=States.pizzaSizes, initial='Большую', model_attribute='pizzaSize')
        self.machine = Machine(model=self, states=States.payTypes, initial='Наличкой', model_attribute='payType')

class States():
    start = ['start', '/start']
    pizzaSizes = ['Большую', 'Маленькую']
    payTypes = ['Наличкой', 'Картой']
    orderStates = ['Да', 'Нет']
    orderStateYes = ['Да']
    orderStateNo = ['Нет']
    newOrder = ['Новый заказ']


