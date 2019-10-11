import pytest
import io
import random
import sys
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation


def test_create_population():
    skynet = Virus('Skynet', 0.8, 0.3)
    sim = Simulation(100, 0.5, skynet, 10)
    sim._create_population()
    assert sim.pop_size == 100
    assert sim.vacc_percentage == 0.5
    assert sim.initial_infected == 10

    test_initial_infected = 0
    test_vaccinated = 0
    test_healthy_unvaccinated = 0
    for person in sim.population:
        if person.is_vaccinated == True:
            test_vaccinated += 1
        elif person.infection != None:
            test_initial_infected += 1
        else:
            test_healthy_unvaccinated += 1
    assert test_vaccinated == 50
    assert test_initial_infected == 10
    assert test_healthy_unvaccinated == 40

    raza_ghul = Virus('Raza Ghul', 0.2, 0.7)
    sim = Simulation(1000, 0.5, raza_ghul, 50)
    sim._create_population()
    assert sim.pop_size == 1000
    assert sim.vacc_percentage == 0.5
    assert sim.initial_infected == 50

    test_initial_infected = 0
    test_vaccinated = 0
    test_healthy_unvaccinated = 0
    for person in sim.population:
        if person.is_vaccinated == True:
            test_vaccinated += 1
        elif person.infection != None:
            test_initial_infected += 1
        else:
            test_healthy_unvaccinated += 1
    assert test_vaccinated == 500
    assert test_initial_infected == 50
    assert test_healthy_unvaccinated == 450


def test_interaction():
    skynet = Virus('Skynet', 0.8, 0.3)
    person = Person(1, False, skynet)
    infected_random_person = Person(1, False, skynet)
    sim = Simulation(100, 0.5, skynet, 10)
    assert sim.Interaction(person, infected_random_person) == False
