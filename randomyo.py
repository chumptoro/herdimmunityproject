import random
import sys
import time

random.seed(time.process_time())


class Simulation(object):

    def __init__(self, name):
        self.name = name

    def printstuff(self):
        for i in range(1):
            prob = random.random()
            print(prob)


sim = Simulation('random')
sim.printstuff()
