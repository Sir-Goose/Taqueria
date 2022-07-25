menudict = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

cost = 0
while True:
    try:
        item = input("Item: ")
        item = item.lower()

        if item in menudict:
            itemcost = menudict[item]
            cost = cost + itemcost

            print("Total: " + "$" + str("{:.2f}".format(cost)))

    except EOFError:
        print("Ctrl + d pressed")
        break
