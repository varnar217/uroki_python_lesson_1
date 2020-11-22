def get_summ(one, two, delimiter='&'):
    one_1=str(one)
    two_1=str(two)
    return (one_1+delimiter+two_1).upper()
print(get_summ('Learn','python'))
