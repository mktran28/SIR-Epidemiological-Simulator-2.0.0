# Import the necessary modules
import random
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def initPopulation(numPeople):
    '''
    Creates an intial population

    Parameters:
    - numPeople (int): number of people in a population

    Returns:
    - population (list): a list of people in a population
    '''
    # Create a population with 5 intial infectious people
    population = ['infectious'] * 5 + ['susceptible'] * (numPeople - 5)
    return population

def recover(population, recoverProb):
    '''
    Modifies the population after some people recover

    Parameters:
    - population (list): a list of people in a population
    - recoverProb (float): probability of recovery in a time step

    Returns:
    - newpopulation (list): a list of people in a population after some recover
    '''
    # Assign to newpopulation an empty list
    newpopulation = []
    # Add to the newpopulation list a recovered person if the person is infectious and recovers; otherwise, add a person with the current status
    for person in population:
        if person == 'infectious' and random.random() < recoverProb:
            newpopulation.append('recovered')
        else:
            newpopulation.append(person)
    return newpopulation

def infect(population, contactRate):
    '''
    Modifies the population after some people get infected

    Parameters:
    - population (list): a list of people in a population
    - contactRate (float): rate of contact between a susceptible and an infectious person in each time step

    Returns:
    - newpopulation (list): a list of people in a population after some get infected
    '''
    # Assign to newpopulation an empty list
    newpopulation = []
    # Count the number of infectious people
    numInfectious = population.count('infectious')
    # Append to the newpopulation list an infectious person if the person is susceptible and get infected; otherwise, add a person with the current status
    for person in population:
        if person == 'susceptible' and random.random() < contactRate * numInfectious / len(population):
            newpopulation.append('infectious')
        else:
            newpopulation.append(person)
    return newpopulation

def oneSimulation(numDay, numPeople, recoverProb, contactRate):
    '''
    Simulates the change in the population over a period once

    Parameters:
    - numDay (int): number of days over which the simulation takes place
    - numPeople (int): number of people in a population
    - recoverProb (float): probability of recovery in a time step
    - contactRate (float): rate of contact between a susceptible and an infectious person in each time step

    Returns:
    - newpopulation (list): a list of people in a population with updated statuses after the simulation
    '''
    # Make a list of initial population
    population = initPopulation(numPeople)
    stats = []
    # Loop through the number of days to change the statuses of people in the population if applicable; if the number of susceptible or infectious people reaches 0, simulation ends early
    for day in range(numDay):
        population = recover(population, recoverProb)
        population = infect(population, contactRate)
        stats.append([population.count('susceptible'), population.count('infectious'), population.count('recovered')])
        if population.count('susceptible') == 0:
            break
        elif population.count('infectious') == 0:
            break
    # If simulation ends early, repeat the last statistics for the remaining days
    while len(stats) < numDay:
        stats.append(stats[-1])
    return stats

def multipleSimulations(numDay, numPeople, recoverProb, contactRate):
    '''
    Simulates the change in the population over a period multiple times

    Parameters:
    - numDay (int): number of days over which the simulation takes place
    - numPeople (int): number of people in a population
    - recoverProb (float): probability of recovery in a time step
    - contactRate (float): rate of contact between a susceptible and an infectious person in each time step

    Returns:
    - newpopulation (list): a list of people in a population with updated statuses after the simulations
    '''
    # Assign to simulation and averageDailyStats empty lists
    simulations = []
    averageDailyStats = []
    # Assign to the daily count of each population composition a list of zero for every day
    totalDailyNumSusceptible = [0] * numDay
    totalDailyNumInfectious = [0] * numDay
    totalDailyNumRecovered = [0] * numDay
    # Loop through the number of simulations to add the results of every simulation to the simulation list
    for num in range(5):
        stats = oneSimulation(numDay, numPeople, recoverProb, contactRate)
        simulations.append(stats)
    # Compute the total daily count for each population composition for each day
    for simulation in simulations:
        for day in range(numDay):
            totalDailyNumSusceptible[day] = totalDailyNumSusceptible[day] + simulation[day][0]
            totalDailyNumInfectious[day] = totalDailyNumInfectious[day] + simulation[day][1]
            totalDailyNumRecovered[day] = totalDailyNumRecovered[day] + simulation[day][2]
    # Loop through the number of days of simulation, compute the average daily count of each population composition and the average percentage of infectious people, and add them to the averageDailyStats list
    for day in range(numDay):
        averageDailyStats.append([totalDailyNumSusceptible[day] / 5, totalDailyNumInfectious[day] / 5, totalDailyNumRecovered[day] / 5, (totalDailyNumInfectious[day] / 5) / numPeople])
    return averageDailyStats

def createGraph(old_stats, new_stats = False, filename = "graph.png"):
    '''
    Creates two graphs to show the changes in the population composition
    
    Parameters:
    - old_stats (list): a list of average daily count of each population composition and percentage of infectious people based on original statistics
    - new_stats (list): a list of average daily count of each population composition and percentage of infectious people based on new statistics
    - filename (string): name of downloaded png file of the graphs

    Returns:
    - a downloaded file with two graphs demonstrating the changes in the population composition
    '''
    # Assign to numSusceptible, numInfectious, numRecovered, percentInfectious each an empty list
    numSusceptible = []
    numInfectious = []
    numRecovered = []
    percentInfectious = []

    # Loop through the old_stats list to add the average daily count of each population composition to the corresponding list
    for item in old_stats:
        numSusceptible.append(item[0])
        numInfectious.append(item[1])
        numRecovered.append(item[2])
        percentInfectious.append(item[3])
    
    # If the value of a factor changes
    if new_stats:

        # Assign new_numSusceptible, new_numInfectious, new_numRecovered, new_percentInfectious each an empty list
        new_numSusceptible = []
        new_numInfectious = []
        new_numRecovered = []
        new_percentInfectious = []

        # Loop through the new_stats list to add the average daily count of each population composition to the corresponding list
        for item in new_stats:
            new_numSusceptible.append(item[0])
            new_numInfectious.append(item[1])
            new_numRecovered.append(item[2])
            new_percentInfectious.append(item[3])
    
    # Make a list of the number of days of simulations
    numDayList = list(range(1, len(old_stats) + 1))

    # Create two graphs
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (14, 6))

    # Create the first graph with the average daily count of each population composition
    ax1.plot(numDayList, numSusceptible, label = "Susceptible (Before)")
    ax1.plot(numDayList, numInfectious, label = "Infectious (Before)")
    ax1.plot(numDayList, numRecovered, label = "Recovered (Before)")

    # If the value of a factor changes, plot the new average daily count of each population composition on the same graph
    if new_stats:
        ax1.plot(numDayList, new_numSusceptible, label = "Susceptible (After)")
        ax1.plot(numDayList, new_numInfectious, label = "Infectious (After)")
        ax1.plot(numDayList, new_numRecovered, label = "Recovered (After)")
    ax1.set_xlabel("Time (in Days)")
    ax1.set_ylabel("Count")
    ax1.legend()
    ax1.set_title("SIR Model Dynamics")

    # Add the second y-axis demonstrating the percentage
    ax1b = ax1.twinx()
    ax1b.set_ylabel("Fraction of Population")

    # Create the second graph with the average daily percentage of infectious people
    ax2.plot(numDayList, percentInfectious, label = "Infectious (Before)")

    # If the value of a factor changes, plot the new average daily percentage of infectious people on the same graph
    if new_stats:
        ax2.plot(numDayList, new_percentInfectious, label = "Infectious (After)")
    ax2.set_xlabel("Time (in Days)")
    ax2.set_ylabel("Percent Infectious")
    ax2.set_title("Percent Infectious")
    ax2.legend()
    plt.tight_layout()

    # Save the graphs for later display
    plt.savefig("simulations/static/" + filename)

def normalGraph(numDay, numPeople, recoverProb, contactRate):
    '''
    Creates two graphs demonstrating the changes in the population composition based on original statistics

    Parameters:
    - numDay (int): number of days over which the simulation takes place
    - numPeople (int): number of people in a population
    - recoverProb (float): probability of recovery in a time step
    - contactRate (float): rate of contact between a susceptible and an infectious person in each time step

    Returns:
    - a downloaded file with two graphs demonstrating the changes in the population composition based on original statistics
    '''
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on original statistics
    old_stats = multipleSimulations(numDay, numPeople, recoverProb, contactRate)
    # Create a downloaded file with two graphs demonstrating the changes in the population composition based on original statistics
    createGraph(old_stats, filename = "normal_graph.png")

def strategy1Graph(numDay, numPeople, recoverProb, contactRate, new_contactRate):
    '''
    Creates two graphs demonstrating the changes in the population composition after the contact rate changes

    Parameters:
    - numDay (int): number of days over which the simulation takes place
    - numPeople (int): number of people in a population
    - recoverProb (float): probability of recovery in a time step
    - contactRate (float): original rate of contact between a susceptible and an infectious person in each time step
    - new_contactRate (float): new rate of contact between a susceptible and an infectious person in each time step

    Returns:
    - a downloaded file with two graphs demonstrating the changes in the population composition after the contact rate changes
    '''
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on original statistics
    old_stats = multipleSimulations(numDay, numPeople, recoverProb, contactRate)
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on new statistics
    new_stats = multipleSimulations(numDay, numPeople, recoverProb, new_contactRate)
    # Create a downloaded file with two graphs demonstrating the changes in the population composition based on original and new statistics
    createGraph(old_stats, new_stats, filename = "strategy1_graph.png")

def strategy2Graph(numDay, numPeople, recoverProb, contactRate, new_recoverProb):
    '''
    Creates two graphs demonstrating the changes in the population composition after the recovery probability changes

    Parameters:
    - numDay (int): number of days over which the simulation takes place
    - numPeople (int): number of people in a population
    - recoverProb (float): original probability of recovery in a time step
    - contactRate (float): rate of contact between a susceptible and an infectious person in each time step
    - new_recoverProb (float): new probability of recovery in a time step

    Returns:
    - a downloaded file with two graphs demonstrating the changes in the population composition after the recovery probability changes
    '''
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on original statistics
    old_stats = multipleSimulations(numDay, numPeople, recoverProb, contactRate)
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on new statistics
    new_stats = multipleSimulations(numDay, numPeople, new_recoverProb, contactRate)
    # Create a downloaded file with two graphs demonstrating the changes in the population composition based on original and new statistics
    createGraph(old_stats, new_stats, filename = "strategy2_graph.png")

def strategy3Graph(numDay, numPeople, recoverProb, contactRate, new_numPeople):
    '''
    Creates two graphs demonstrating the changes in the population composition after the number of susceptible people changes

    Parameters:
    - numDay (int): number of days over which the simulation takes place
    - numPeople (int): original number of people in a population
    - recoverProb (float): original probability of recovery in a time step
    - contactRate (float): rate of contact between a susceptible and an infectious person in each time step
    - new_numPeople (int): new number of people in a population

    Returns:
    - a downloaded file with two graphs demonstrating the changes in the population composition after the number of susceptible people changes
    '''
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on original statistics
    old_stats = multipleSimulations(numDay, numPeople, recoverProb, contactRate)
    # Make a list with average daily count of each population composition and the average percentage of infectious people based on new statistics
    new_stats = multipleSimulations(numDay, new_numPeople, recoverProb, contactRate)
    # Create a downloaded file with two graphs demonstrating the changes in the population composition based on original and new statistics
    createGraph(old_stats, new_stats, filename = "strategy3_graph.png")