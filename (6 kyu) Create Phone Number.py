def create_phone_number(n):
    n = str(n)
    x = '(' + n[1] + n[4] + n[7] + ')' + ' ' + n[10] + n[13] + n[16] + '-' + n[19] + n[22] + n[25] + n[28]
    return x
