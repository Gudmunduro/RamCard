"""
Kristjan O.
Sort_info
Reads file and creates instances of the cards
"""
import Reference
import csv
import Card


class Sort:
    def __init__(self):
        self.card_list = []

    def main(self):
        with open(Reference.FILE_NAME, 'r', encoding=Reference.ENCODING) as data:
            dump = csv.reader(data, delimiter=';')
            for i in dump:
                i[0] = Card.Card(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
                self.card_list.append(i[0])
        print(self.card_list[0])
