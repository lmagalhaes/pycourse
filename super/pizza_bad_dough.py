class BadDough(object):

    def get_dough(self):
        return "a dough that tastes bad"

class Pizza(BadDough):

    def order_pizza(self, *toppings):
        print("Getting dough...")
        dough = super().get_dough()
        print("Making pizza with {}".format(dough))

        for t in toppings:
            print("Adding topping: {}".format(t))
