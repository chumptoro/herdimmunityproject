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
