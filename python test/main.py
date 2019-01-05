# Воспользуйтесь этим начальным кодом, чтобы реализовать нужный процедуры

def head(pair):
    if pair is None:
        return None
    return pair[0]

def tail(pair, k=1):
    if pair is None:
        return None
    if len(pair) < 2:
        return None
    if(k != 1):
        return tail(pair[1], k-1)
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
    if(head(pair) is None):
       return None
#hotfix
    if(i == 0):
        return pair[0]
    #if(pair[i] is None):
    #    return None
    #if(head(pair) == i):
    #    return pair[0]
    #i = i-1
    return at(tail(pair), i - 1)

def size(pair):
    if(pair != None):
        return 1 + size(tail(pair))
    else:
        return 0

def eq(pair1, pair2):
    if(size(pair1) != size(pair2)):
        return False
    #
    if(head(pair1) == head(pair2)):
        if((head(pair1) is None) and (head(pair2) is None)):
            return True
        return eq(tail(pair1), tail(pair2))
    else:
        return False

#def concat(pair1, pair2):
#    if pair

def for_each(pair, x):
    if(pair != None):
        x = head(pair)
        return for_each(tail(pair), x)
    else:
        return x
        #return for_each(tail(pair), head(pair))

s = Seq(1,2,3,4,5)
s == (1, (2, (3, (4, (5,)))))
head(s) == 1
tail(s) == (2, (3, (4, (5,))))
#print(at(Seq(1,2,3), 0))
#print(size(Seq(1,2,3,4)))
#print(eq(Seq(1,2), Seq(1,2)))
#print(eq(Seq(1,2,4), Seq(1,2,3)))
#print(eq(Seq(1,2,3), Seq(1,2)))
#print(eq(tail(Seq(1,2,3,4), 2), Seq(3,4)))
#print(len(Seq(1,2,3,4)))
f = lambda x: print(x)
for_each(Seq(1,2,3,4), f)