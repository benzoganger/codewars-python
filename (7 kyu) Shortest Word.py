def find_short(s):
    words = []
    lenghts = []
    words = s.split()
    for word in words:
        y = len(word)
        lenghts.append(y)
    lenghts.sort()
    l = (lenghts[0])
    return l
