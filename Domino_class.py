#Domino
import itertools

class Domino(object):
    """one domino has 2 numbers"""
    def __init__(self, number1, number2):
        self.num1 = number1
        self.num2 = number2

    def get_numbers(self):
        return (self.num1, self.num2)

    def __repr__(self):
        return "%s, %s" % (self.num1,self.num2)

class Domino_Deck(object):
    """This is a domino deck.  A deck has 91 tiles"""
    def __init__(self):
        self.dominos = []
        for dom in itertools.combinations_with_replacement(range(13),2):
            self.dominos.append(Domino(dom[0],dom[1]))
