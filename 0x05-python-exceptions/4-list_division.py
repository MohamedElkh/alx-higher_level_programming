#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    n_list = []
    
    for x in range(list_length):

        try:
               divi = my_list_1[x] / my_list_2[x]
        except TypeError:
               print("wrong type")
               divi = 0
        except ZeroDivisionError:
               print("division by 0")
               divi = 0
        except IndexError:
               print("out of range")
               divi = 0
        finally:
               n_list.append(divi)
    return (n_list)      
