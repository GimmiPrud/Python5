
mylist_1 = "[mario, gino, lucrezia]"
mylist_2 = ["mario","gino","lucrezia"]


def serializza_lista( l_var: list)-> str:
    l_var_1 = str(l_var)
    print(l_var_1)


def deseriallizza_lista(s_var: list)-> list:
    pass


l_prova = serializza_lista(mylist_2)
if l_prova == mylist_1:
    print("procedura avvenuta con successo")

# s_prova = deseriallizza_lista(mylist_1)
# if s_prova == mylist_2:
#     print("procedura avvenuta con successo")
