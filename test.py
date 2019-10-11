import pytest
import io
import random
import sys
from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation


def test_create_population():
	skynet = virus('Skynet', 0.8, 0.3)
    sim = Simulation(10, 0.5, skynet, 1)
    sim._create_population()
    assert sim.pop_size == 10
    assert sim.vacc_percentage == 0.5


