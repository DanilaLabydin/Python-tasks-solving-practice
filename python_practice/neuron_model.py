import random


class Neuroimpulse:
    def generate_impulse(self):
        power_impulse = random.randint(-1, 1)
        return power_impulse


class Neuron:
    def __init__(self, nb_impulses):
        self.nb_impulses = nb_impulses

    def generate_all_impulse(self):
        self.impulses_quantity = []
        for i in range(self.nb_impulses):
            a = Neuroimpulse()
            self.impulses_quantity.append(a.generate_impulse())
        return self.impulses_quantity

    def sum_impulses(self, impulses_quantity):
        sm = sum(impulses_quantity)
        return sm

    def activation_function(self, sm):
        if sm > self.nb_impulses / 5:
            return True
        return False




def main():
    # create am instance of Neuron class
    simple_neuron = Neuron(20)

    # make a few iteration to demonstrate a neuron
    for i in range(10):
        list_of_impulses = simple_neuron.generate_all_impulse()
        print(list_of_impulses)
        summatr = simple_neuron.sum_impulses(list_of_impulses)
        print(summatr)
        print(simple_neuron.activation_function(summatr))



if __name__ == '__main__':
    main()
