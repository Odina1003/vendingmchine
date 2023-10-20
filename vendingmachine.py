from beverage import Beverage
from qator import Qator
from card import Card

class VendingMachine:
    def __init__(self) -> None:
        self.card_list: list[Card] = []
        self.qator_list = [Qator(i) for i in range(1, 7)]

    def available_cans(self, name):
        count = 0
        for qator in self.qator_list:
            ichimlik = qator.ichimlik
            if ichimlik == None:
                continue
            elif ichimlik.name == name:
                count += qator._number_beverage
        return count

    def add_beverage(self, qator, beverage: Beverage, number_beverage):
        qator = self.qator_list[qator-1]
        return qator.add_beverage(beverage, number_beverage)

    def info(self, qator: Qator):
        qator = self.qator_list[qator-1]
        return qator.getinfo()

    def get_price(self, name):
        for qator in self.qator_list:
            check = qator.get_price(name)
            if  check != None:
                return check
        return -1.0

    def get_credit(self, id):
        for card in self.card_list:
            if card._id == id:
                return card.kretid
        return -1.0

    def recharge_card(self, id, debit):
        for card in self.card_list:
            if card._id == id:
                card.add_summa(debit)
                print(f'{id} ga {debit} som qo\'shildi, {card.kretid}')
                return
        card = Card(id, debit)
        self.card_list.append(card)
        print('karta qo\'shildi')

    def sell(self, card_id, ichimlik_nomi):
        if self.get_price(ichimlik_nomi) != -1.0:
            for i in self.qator_list:
                if i.ichimlik == None:
                    continue
                if i.ichimlik.name == ichimlik_nomi:
                    i._number_beverage -= 1
                    if self.get_credit(card_id) != -1.0:
                        for j in self.card_list:
                            if j._id == card_id:
                                narx = self.get_price(ichimlik_nomi)
                                return j.spend_money(narx)
        else:
            return -1.0