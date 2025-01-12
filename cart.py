menu = {'apple': 5, 'orange': 6, 'kiwi': 10, 'banana': 3, 'peach': 8, 'dragon fruit': 18}
cart = []
total = 0
setted = [(fruit, price) for fruit, price in menu.items()]

while True:    
    order = input("Enter name of fruit(q to quit): ")
    for item, cash in setted:        
        if order == item:
            cart.append((item, cash))
            
    if order.lower() == 'q':
        break

        
        