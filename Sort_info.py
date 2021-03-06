"""
Kristjan O.
Sort_info
Reads file and creates instances of the cards
"""
import Reference
import csv
import Card

unaccounted = lambda x: 'Eiginleiki ekki mældur' if (x == 'x') else int(x)
# unaccounted finds if a attribute dose not have a value

class Sort:
    """ Class witch reads in info from file """
    def __init__(self):
        self.card_list = []

    def main(self):
        """ reads the info from file and appends to self.card_list """
        with open(Reference.FILE_NAME, 'r', encoding=Reference.ENCODING) as data:
            dump = csv.reader(data, delimiter=';')
            for i in dump:
                i[0] = Card.Card(i[0], float(i[1]), int(i[2]), float(i[3]), int(i[4]), float(i[5]), int(i[6]),
                                 unaccounted(i[7]), float(i[8]))
                self.card_list.append(i[0])
