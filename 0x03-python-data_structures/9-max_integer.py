def max_integer(my_list=[]):
    max_value = None
    void_list = False
    if not my_list:
        void_list = True
    if not void_list:
        for dig in my_list:
            if max_value is None or dig > max_value:
                max_value = dig
        if void_list:
            return None
        else:
            return max_value
