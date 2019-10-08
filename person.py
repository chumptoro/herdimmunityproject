import random
random.seed(42)
from virus import Virus


class Person(object):
    ''' Person objects is the basic unit of being that will populate the simulation. '''

    def __init__(self, _id, is_vaccinated, infection=None):
        ''' We start out with is_alive = True, because we don't make vampires or zombies.
        All other values will be set by the simulation when it makes each Person object.

        If person is chosen to be infected when the population is created, the simulation
        should instantiate a Virus object and set it as the value
        self.infection. Otherwise, self.infection should be set to None.
        '''
        self._id = _id  # int
        self.is_alive = True  # boolean
        self.is_vaccinated = is_vaccinated
        self.infection = infection  # Virus object or None

    def did_survive_infection(self):
        ''' Generate a random number and compare to virus's mortality_rate.
        If random number is smaller, person dies from the disease.
        If Person survives, they become vaccinated and they have no infection.
        Return a boolean value indicating whether they survived the infection.
        '''
        # Only called if infection attribute is not None.
        # TODO:  Finish this method. Should return a Boolean
        if random.randint(1, 100) < self.infection.mortality_rate:
            return False
        else:
            self.infection = False
            return True


# class Interaction(object):
#     '''documents the outcome of each interaction
#     between a sick person and 100 healthy people'''

#     def __init__(self, infected_person, population):
#         '''population is a list of healthy people from which 100 are chosen
#         to interact with the infected individual'''
#         self.infected_person = infected_person
#         self.population = population

#     def interact(self):
#         '''the outcome of a sick person interacting with a healthy person:
#         true if infection is spread
#         false if the healthy person is not infected
#         '''
#         if person.is_vaccinated:
#             return False
#         else:
#             prob = random.random()
#             if prob > self.infected_person.infection.repro_rate:
#                 return False
#             else:
#                 return True


''' These are simple tests to ensure that you are instantiating your Person class correctly. '''


def test_vacc_person_instantiation():
    # create some people to test if our init method works as expected
    person = Person(1, True)
    assert person._id == 1
    assert person.is_alive is True
    assert person.is_vaccinated is True
    assert person.infection is None


def test_not_vacc_person_instantiation():
    person = Person(2, False)
    assert person._id == 2
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection is None


def test_sick_person_instantiation():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(3, False, virus)
    assert person._id == 3
    assert person.is_alive is True
    assert person.is_vaccinated is False
    assert person.infection.name == "Dysentery"
    assert person.infection.repro_rate == 0.7
    assert person.infection.mortality_rate == 0.2


def test_did_survive_infection():
    # Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)
    # Create a Person object and give them the virus infection
    person = Person(4, False, virus)
    # Resolve whether the Person survives the infection or not
    survived = person.did_survive_infection()
    # Check if the Person survived or not
    if survived:
        assert person.is_alive is True
    else:
        assert person.is_alive is False
