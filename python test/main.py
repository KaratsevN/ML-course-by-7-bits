# Воспользуйтесь этим начальным кодом, чтобы реализовать нужный процедуры

def head(pair):
    if pair is None:
        return None
    return pair[0]

def tail(pair):
    if pair is None:
        return None
    if len(pair) < 2:
        return None
    return pair[1]

def Seq(*elements):
    def first(x):
        return x[0]
    def other(x):
        return x[1:]

    if len(elements) == 0:
        return None

    if len(elements) == 1:
        return first(elements), None

    if len(elements) == 2:
        return first(elements), other(elements)

    return first(elements), Seq(*other(elements))


def at(pair , i):
    #if(head(pair) is None):
    #   return "Not find"
    #hotfix
    if(i == 0):
        return pair[0]
    #if(pair[i] is None):
    #    return None
    #if(head(pair) == i):
    #    return pair[0]
    #i = i-1
    return at(tail(pair), i - 1)

j = 0
def size(pair):
    if(pair is not None):
        j = j + 1
        return size(tail(pair))
    else return j

s = Seq(1,2,3,4,5)
s == (1, (2, (3, (4, (5,)))))
head(s) == 1
tail(s) == (2, (3, (4, (5,))))
print(at(Seq(1,2,3), 1))