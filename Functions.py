"""
Guðmundur
fundtions
26/4/2017
"""

def intinput(text="Sláðu inn tölu", limit_from = 0, limit_to = 1000):
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