menu = {'apple': 5, 'orange': 6, 'kiwi': 10, 'banana': 3, 'peach': 8, 'dragon fruit': 18}
cart = []
total = 0

while True:
    setted = [(fruit, price) for fruit, price in menu.items()]
    order = input("Enter name of fruit(q to quit): ")
    for sub in setted:
        if order in setted:
            cart.append(order)
            
    if order.lower() == 'q':
        break
        
        