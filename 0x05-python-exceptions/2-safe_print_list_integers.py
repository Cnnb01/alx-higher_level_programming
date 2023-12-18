def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in my_list:
            if count < x:
                print("{}".format(i))
                count = count + 1
            else:
                break
        return count
    except (IndexError, TypeError) as e:
        print(e)
