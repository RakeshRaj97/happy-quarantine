def goto_kitchen(each_person):
    print(each_person + " Cook and eat")
    pass


def goto_washroom(each_person):
    print(each_person + " Make sure you have toilet paper")
    pass


def routine(list_of_roomies, feeling_hungry=False, feeling_to_pee=False):
    for each_person in list_of_roomies:
        if feeling_hungry:
            goto_kitchen(each_person)
        if feeling_to_pee:
            goto_washroom(each_person)
        else:
            print("Stay at room")


roomies = ["me", "suresh"]
routine(roomies, feeling_hungry = True, feeling_to_pee= True)
