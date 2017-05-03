"""
Guðmundur
functions
26/4/2017
"""
from Reference import CATEGORY


def intinput(text="Sláðu inn tölu", limit_from=0, limit_to=1000):
    """Input for numbers"""
    while True:
        value = 0
        try:
            value = int(input(text + ": "))
        except ValueError:
            print("Þetta er ekki tala")
        finally:
            if limit_from <= value <= limit_to:
                return value
            else:
                print("Talan þarf að vera á milli {} og {}".format(str(limit_from), str(limit_to)))


def get_attr(num, attri, cardsDictio):
    if attri == CATEGORY.WEIGHT:
        return cardsDictio[num].weight
    elif attri == CATEGORY.MILK:
        return cardsDictio[num].milk
    elif attri == CATEGORY.WOOL:
        return cardsDictio[num].wool
    elif attri == CATEGORY.CHILDS:
        return cardsDictio[num].childs
    elif attri == CATEGORY.HIND_LEGS:
        return cardsDictio[num].hind_legs
    elif attri == CATEGORY.FERTILITY:
        return cardsDictio[num].fertility
    elif attri == CATEGORY.MEAT:
        return cardsDictio[num].meat
    elif attri == CATEGORY.ASS:
        return cardsDictio[num].ass