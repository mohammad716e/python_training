# بازی وار در پاسور را با پایتون بنویسید
from random import shuffle

SUITS = 'H D S C'.split(' ')

RANK = '2 3 4 5 6 7 8 9 10 J Q K A'.split(' ')

class deck():
    def __init__(self):
        print('creating new order of deck')
        self.allcards = [(s,r) for s in SUITS for r in RANK]

    def shuffle(self):
        print('shuffling the cards')
        shuffle(self.allcards)

    def split_in_half(self):
        return (self.allcards[:26],self.allcards[26:])

class hand():
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return f'contains {len(self.cards)} cards'

    def add_card(self , new_cards):
        self.cards.extend(new_cards)

    def remove_card(self):
        if len(self.cards) !=0:
            return self.cards.pop()



class player():

    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def paly_card(self):
        drawn_card = self.hand.remove_card()
        print(f'palyer {self.name} has drown card {drawn_card} \n')
        return drawn_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) >3:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards
        else:
            self.hand.cards = []
    
    def still_has_cards(self):
        return len(self.hand.cards) !=0 #:
        #     return True
        # else:
        #     return False

# game logic
print(' welcome to war lets play man')
d =deck()
d.shuffle()
half1,half2 = d.split_in_half()

comp = player('computer', hand(half1))
name = input('enter your name ')
user = player( name , hand(half2))
total_rounds = 0 
total_wars = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds +=1
    print('time for new round ')
    print ( ' here are current standings')
    print(user.name + ' has the count: '+str(len(user.hand.cards)))
    print(comp.name + ' has the count: '+str(len(comp.hand.cards)))
    print('play a card')
    print()

    table_cards = []
    #  ایا اینا اکسپرشن هستند یا نه ؟
    c_card = comp.paly_card()
    p_card = user.paly_card()

    table_cards.append(p_card)
    table_cards.append(c_card)

    if c_card[1] == p_card[1]: #and  : #(len(comp.hand.cards)!=1 or len(user.hand.cards)) !=1
        total_wars +=1

        print('war')
        #  put tree cars out
        try :
            table_cards.extend(comp.remove_war_cards())
            table_cards.extend(user.remove_war_cards())
        except:
            
            # print(' game ended ')
            break
        
        c_card = comp.paly_card()
        p_card = user.paly_card()

        table_cards.append(p_card)
        table_cards.append(c_card)

        print('hi hi hi')
        print(table_cards)
        
        if RANK.index(p_card[1]) < RANK.index(c_card[1]):
            comp.hand.add_card(table_cards)
        else:
            user.hand.add_card(table_cards)
    else:
        if RANK.index(p_card[1]) <RANK.index(c_card[1]):
            comp.hand.add_card(table_cards)
        else:
            user.hand.add_card(table_cards)

    print(f' game over rounds count were {total_rounds}')
    print(f'     wars count were {total_wars}')

print(' ------------------------------------------------------- ')

# هوررررراااااااااااااااااااا
# کار میکنه

