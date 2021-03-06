import random
import sys
import time
random.seed(time.process_time())
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

        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.current_pop_size = pop_size

        self.next_person_id = -1  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = initial_infected  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.total_vaccinated = 0

        self.newly_infected = []

        self.vaccinated = []

        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            self.virus.name, self.pop_size, self.vacc_percentage, self.initial_infected)

        self.logger = Logger(self.file_name)

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name,
                                   self.virus.mortality_rate, self.virus.repro_rate)

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
        print("population is " + str(self.pop_size))
        time_step_counter = 0
        stop = 0
        while self._simulation_should_continue() and stop < 5:
            self.time_step()
            time_step_counter += 1
            stop += 1
            print("at step " + str(stop) + " current infected number is " + str(self.current_infected) +
                  " , total_dead is " + str(self.total_dead) + " , total vaccinated is " + str(self.total_vaccinated))

        print(f'The simulation has ended after {time_step_counter} turns.')
        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.

        '''
        if self.current_infected == 0:
            print("no one is current infected")
            return False
        if self.pop_size == self.total_dead:
            print("entire population is dead")
            return False
        if self.total_vaccinated == self.pop_size:
            print("everyone is vaccinated")
            return False
        return True

    def _create_population(self):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        '''
        # This method is called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.

        remain_pop = self.pop_size

        # vaccinated population
        # number is rounded down.  .06 = 0
        vaccinated_pop = int(self.pop_size * self.vacc_percentage)
        for i in range(int(vaccinated_pop)):
            self.next_person_id += 1
            self.vaccinated.append(self.next_person_id)
            person = Person(self.next_person_id, True, None)
            self.population.append(person)
            # print("hi my id is " + str(person._id) + " and i'm vaccinated")
        self.total_vaccinated = len(self.vaccinated)

        for i in range(self.initial_infected):
            self.next_person_id += 1
            person = Person(self.next_person_id, False, self.virus)
            self.population.append(person)
            # print("hi my id is " + str(person._id) + " and i'm infected")

        remain_pop = int(self.pop_size - vaccinated_pop -
                         self.initial_infected)
        for i in range(int(remain_pop)):
            self.next_person_id += 1
            person = Person(self.next_person_id, False, None)
            self.population.append(person)
            # print("hi my id is " + str(person._id) +
            #       " and i'm healthy but not vaccinated ")

        for person in self.population:
            print("hi my id is " + str(person._id) +
                  " and my infection virus is " + str(person.infection))

        # print("initial infected population is " + str(self.initial_infected))
        # print("vaccinated population is " + str(vaccinated_pop))
        # print("heathly unvaccinated population is " + str(remain_pop))

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
        # for testing only
        # self._create_population()

        for person in self.population:
            if person.infection != None and person.is_alive == True:
                print("person with id " + str(person._id) +
                      " and my infection virus is " + str(person.infection))

                interactions = 0
                non_interactions = 0
                while interactions < 1:
                    random_person = random.choice(self.population)
                    if random_person.is_alive == False or random_person._id == person._id:
                        # edge case:
                        # no one is alive except person, who is infected....
                        # we need to ensure that he/she does not interact with
                        # himself, which means he might self-innoculate by
                        # exposure himself to himself
                        non_interactions += 1
                        print("non-interaction number " +
                              str(non_interactions) + " with person of id " + str(random_person._id))

                        if self.current_pop_size == 1:
                            break

                        continue

                    else:
                        print("this is interaction number " + str(interactions))
                        interaction_infects = self.interaction(
                            person, random_person)
                        if interaction_infects == True:
                            random_person.infection = person.infection
                            self.newly_infected.append(random_person._id)
                            print("person with id " + str(person._id) +
                                  " infects person with id " + str(random_person._id))
                        else:
                            random_person.infection = None
                            print("person with id " + str(person._id) +
                                  " did NOT infect person with id " + str(random_person._id))
                        #print("end of interaction")
                        interactions += 1

                # update whether the person who's doing the infecting lives and
                # dies.  If alive, they become vaccinated
                person_alive = person.did_survive_infection()
                if person_alive == True:
                    self.total_vaccinated += 1
                    self.current_infected -= 1
                    self.logger.log_infection_survival(person, False)
                else:
                    self.total_dead += 1
                    self.current_pop_size -= 1
                    self.current_infected -= 1
                    self.logger.log_infection_survival(person, True)
            else:
                print("person with id " + str(person._id) +
                      " and my infection virus is " + str(person.infection))
        # update list of people who are infected
        self._infect_newly_infected()

    def interaction(self, person, random_person, prob=None):
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
        random_person_sick = None
        random_person_vacc = None
        did_infect = False
        case = 3

        print(" in this interaction, person infecting has id " + str(person._id))
        print(" in this interaction, random person has id " +
              str(random_person._id))

        if random_person.infection != None:
            random_person_sick = True
            random_person_vacc = False
            print("case 1")
            case = 1

        if random_person.is_vaccinated == True:
            random_person_vacc = True
            random_person_sick = False
            print("case 2")
            case = 2

        if case == 3:
            print("case 3")
            random_person_vacc = False
            random_person_sick = False
            if prob == None:
                real_prob = random.random()
                print("rate is" + str(real_prob))
            else:
                real_prob = prob
            # print(" real prob rate is " + str(real_prob) +
            #       " rep rate is " + str(person.infection.repro_rate))
            if real_prob > person.infection.repro_rate:
                did_infect = False
                random_person.is_vaccinated = True
                self.total_vaccinated += 1
                # print("random healthy person does not infected due to good luck")
            else:
                # self.newly_infected.append(random_person._id)
                did_infect = True

         # Call slogger method during this method.
        self.logger.log_interaction(
            person, random_person, random_person_sick, random_person_vacc,
            did_infect)

        return did_infect

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        for _id in self.newly_infected:
            self.population[_id].infection = self.virus
            self.current_infected += 1
        self.newly_infected = []


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
