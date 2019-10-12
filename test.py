import pytest
import io
import random
import sys
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation


# def test_create_population():
#     skynet = Virus('Skynet', 0.8, 0.3)
#     sim = Simulation(100, 0.5, skynet, 10)
#     sim._create_population()
#     assert sim.pop_size == 100
#     assert sim.vacc_percentage == 0.5
#     assert sim.initial_infected == 10

#     test_initial_infected = 0
#     test_vaccinated = 0
#     test_healthy_unvaccinated = 0
#     for person in sim.population:
#         if person.is_vaccinated == True:
#             test_vaccinated += 1
#         elif person.infection != None:
#             test_initial_infected += 1
#         else:
#             test_healthy_unvaccinated += 1
#     assert test_vaccinated == 50
#     assert test_initial_infected == 10
#     assert test_healthy_unvaccinated == 40

#     raza_ghul = Virus('Raza Ghul', 0.2, 0.7)
#     sim = Simulation(1000, 0.5, raza_ghul, 50)
#     sim._create_population()
#     assert sim.pop_size == 1000
#     assert sim.vacc_percentage == 0.5
#     assert sim.initial_infected == 50

#     test_initial_infected = 0
#     test_vaccinated = 0
#     test_healthy_unvaccinated = 0
#     for person in sim.population:
#         if person.is_vaccinated == True:
#             test_vaccinated += 1
#         elif person.infection != None:
#             test_initial_infected += 1
#         else:
#             test_healthy_unvaccinated += 1
#     assert test_vaccinated == 500
#     assert test_initial_infected == 50
#     assert test_healthy_unvaccinated == 450


# def test_interaction():
#     skynet = Virus('Skynet', 0.8, 0.3)
#     person = Person(1, False, skynet)
#     sim = Simulation(100, 0.5, skynet, 10)

#     # random person is sick
#     infected_random_person = Person(1, False, skynet)
#     assert sim.interaction(person, infected_random_person) == False

#     # random person is vaccinated
#     vacced_random_person = Person(2, True, skynet)
#     assert sim.interaction(person, vacced_random_person) == False

#     # healthy random person does not get infected
#     healthy_random_person = Person(3, False)
#     assert sim.interaction(person, healthy_random_person, .81) == False

#     # healthy random person does get infected
#     healthy_random_person = Person(4, False)
#     assert sim.interaction(person, healthy_random_person, .79) == True

# # test_interaction()


# def test_simulation_should_continue():
#     skynet = Virus('Skynet', 0.8, 0.3)
#     sim = Simulation(100, 0.5, skynet, 10)
#     sim.current_infected = 0
#     assert sim._simulation_should_continue() == False

#     sim1 = Simulation(100, 0.5, skynet, 10)
#     sim1.pop_size = 0
#     sim1.total_dead = 0
#     assert sim1._simulation_should_continue() == False

#     sim2 = Simulation(100, 0.5, skynet, 10)
#     sim2.pop_size = 100
#     sim2.total_dead = 1
#     assert sim2._simulation_should_continue() == True


def test_time_step():
    skynet = Virus('Skynet', 0.8, 0.8)
    sim = Simulation(10, 0.2, skynet, 2)
    sim.time_step()

test_time_step()


# def test_run():
#     skynet = Virus('Skynet', 0.8, 0.8)
#     sim = Simulation(10, 0.2, skynet, 2)
#     # pop size = 10, vacc_percentage = .2, initial_infected = 2
#     sim.run()

# test_run()


# test_simulation_should_continue()

# def test_infect_newly_infected():
