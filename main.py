print("Hello World")

def add_numbers(a = 0, b = 0, l=None, two=True):
    if two:
        return a + b
    else:
        return sum(l)
