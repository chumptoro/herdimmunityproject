import random
import sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.

    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''

    # <- these are all command lines
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.

        self.logger = Logger('log.txt')
        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.total_vaccinated = 0
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name,
        self.virus.mortality_rate, self.virus.repro_rate)

    def _create_population(self):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # TODO: Finish this method! This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.
<<<<<<< HEAD

        remain_pop = self.pop_size

        # vaccinated population
        vaccinated_pop = self.pop_size * self.vacc_percentage
        for person in range(int(vaccinated_pop)):
            id = self.next_person_id + 1
            person = Person(id, True, False)
            self.population.append(person)

        # infected population
        infected_pop = self.pop_size * self.initial_infected
        for person in range(infected_pop):
            id = self.next_person_id + 1
            person = person.Person(id, False, True)
            self.population.append(person)
        healthy but unvaccinated population
            - infected_pop

        # issue infected population makes everyone infected
        remain_pop = remain_pop - vaccinated_pop
        for person in range(int(remain_pop)):
            id = self.next_person_id + 1
            person = Person(id, False, True)
            self.population.append(person)

        total_to_infect = self.initial_infected
        while total_to_infect != 0:
            person_got = random.choice(self.population)
            if person_got.is_vaccinated == False and person_got.infection == None:
                person_got.infection = self.virus
                total_to_infect -= 1
                self.current_infected += 1
=======
        population = []
        infected_count = 0
        # vaccinated population
        while len(population) != self.pop_size:
            if infected_count != initial_infected:
                population.append(Person(self.next_person_id,
                                         is_vaccinated=False,
                                         infection=self.virus))
                infected_count += 1
            else:
                is_vaccinated = random.random() < self.vacc_percentage
                population.append(Person(self.next_person_id, is_vaccinated))

            self.next_person_id += 1

        return population


        # total_to_infect = self.initial_infected
        # while total_to_infect > 0:
        #     person_got = random.choice(self.population)
        #     if person_got.is_vaccinated == False and person_got.infection == None:
        #         person_got.infection = self.virus
        #         total_to_infect -= 1
        #         self.current_infected += 1

>>>>>>> 7faeee945052fa4a9bec7dafbc0c7d81d90a57fe

        # randomly select a person from population
        # check to see if they are not vaccineated
        # set the amount infected
        # do it as many times as initial infected
        # check if they are not already infected

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

        '''
        return (self.current_infected == 0 and self.pop_size == self.total_dead)


    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continugie() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper
        self._create_population()

        time_step_counter = 0

        while self._simulation_should_continue():
            (newly_infected_people, newly_dead_people) = self.time_step()
            self.logger.log_time_step(time_step_counter,
                                      newly_infected_people, newly_dead_people,
                                      self.total_infected, self.total_dead)
            time_step_counter += 1
            self.current_infected = 0
        print(f'The simulation has ended after {time_step_counter} turns.')
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a random person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
        alive_and_infected = []
        for person in self.population:
            if person.is_alive == True:
                if person.infected == True:
                    alive_and_infected.append(person)

        for _ in range(100):
            self.interaction(person, random_person=random.choice(alive_and_infected))

        newly_dead_people = 0

        for person in alive_and_infected:
            if person.did_survive_infection():
                self.logger.log_infection_survival(person, did_die_from_infection=False)
            else:
                self.logger.log_infection_survival(person, did_die_from_infection=True)
                newly_dead_people += 1

        self.total_dead += newly_dead_people
        newly_infected_people = len(self.newly_infected)


        self._infect_newly_infected()

        return (newly_infected_people, newly_dead_people)


    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed
        # in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.
        if random_person.is_vaccinated:

            self.logger.log_interaction(person, random_person,
                                        did_infect=False, random_person_vacc=True)
        elif (random_person.infection != None or
              random_person._id in self.newly_infected):

            self.logger.log_interaction(person, random_person,
                                        did_infect=False, random_person_sick=True)
        else:
            if random.random() <= person.infection.repro_rate:
                self.newly_infected.append(random_person._id)

                self.logger.log_interaction(person, random_person,
                                            did_infect=True)
            else:
                self.logger.log_interaction(person, random_person,
                                            did_infect=False)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for person in infected_people:
            person.infection = self.virus

        self.current_infected = len(self.newly_infected)
        self.total_infected += self.current_infected
        self.newly_infected.clear()


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_rate = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)

    sim.run()
