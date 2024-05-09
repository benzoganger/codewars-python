from textwrap import wrap
def solution(s):
    if len(s) %2 == 0:
        x = wrap(s,2)
        return(x)
    elif len(s) %2 != 0:
        x = wrap(s,2)
        x[-1] = x[-1] + '_'
        return(x)
    pass
