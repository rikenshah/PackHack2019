def parse(string):
    return " ".join([x for x in string.split(" ") if len(x) > 2])