"""
Guðmundur
functions
26/4/2017
"""
import Reference


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


def question(text):
    """Function for yes or no questions"""
    ans = ""
    while True:
        ans = input(text + ": ")
        if ans.lower() in ["j", "já", "ja", "y", "n", "nei"]:
            break
        else:
            print("Þetta er ekki gilt svar")
    return ans.lower() in ["j", "já", "ja"]


def get_attr(num, attri, cardsDictio):
    if attri == Reference.CATEGORY.WEIGHT:
        return cardsDictio[num].weight
    elif attri == Reference.CATEGORY.MILK:
        return cardsDictio[num].milk
    elif attri == Reference.CATEGORY.WOOL:
        return cardsDictio[num].wool
    elif attri == Reference.CATEGORY.CHILDS:
        return cardsDictio[num].childs
    elif attri == Reference.CATEGORY.HIND_LEGS:
        return cardsDictio[num].hind_legs
    elif attri == Reference.CATEGORY.FERTILITY:
        return cardsDictio[num].fertility
    elif attri == Reference.CATEGORY.MEAT:
        return cardsDictio[num].meat
    elif attri == Reference.CATEGORY.ASS:
        return cardsDictio[num].ass


def debug(text):
    """prints only when Refrence.DEBUG is true"""
    if Reference.DEBUG:
        print(text)
