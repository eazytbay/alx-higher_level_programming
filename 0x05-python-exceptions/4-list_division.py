#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    comp_rslt = [0] * list_length
    for x in range(list_length):
        try:
            rslt = my_list_1[x] / my_list_2[x]
            comp_rslt[x] = rslt
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            pass
    return comp_rslt
