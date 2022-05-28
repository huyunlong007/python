def make_pizza(size, *toppings):
    print("\nmaking a "+str(size)+"-inch pizza with the following toopings: ")
    for topping in toppings:
        print("- "+topping)
make_pizza(11, 'pepperoni')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')