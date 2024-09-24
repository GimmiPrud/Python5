
mylist_1 = "['mario' , 'gino' , 'lucrezia' ]"
mylist_2 = ["mario","gino","lucrezia"]


def serializza_lista( list_var: list)-> str:
    return str(list_var)


def deseriallizza_lista(string_var: list)-> list:
    list_var = eval(string_var)
    return list_var



