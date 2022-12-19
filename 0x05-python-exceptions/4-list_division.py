#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            res = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("{:s}".format("wrong type"))
            res = 0
        except ZeroDivisionError:
            print("{:s}".format("division by 0"))
            res = 0
        except IndexError:
            print("{:s}".format("out of range"))
            res = 0
        except Exception:
            res = 0
        finally:
            new_list.append(res)
    return new_list
