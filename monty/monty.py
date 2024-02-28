# Script to run simulations to compute the probabilty of the Monty Hall problem
# https://en.wikipedia.org/wiki/Monty_Hall_problem
#
# Suppose you're on a game show, and you're given the choice of three doors: 
# Behind one door is a car; behind the others, goats. You pick a door, say No. 1,
# and the host, who knows what's behind the doors, opens another door, say No. 3,
# which has a goat. He then says to you, "Do you want to pick door No. 2?" 
# Is it to your advantage to switch your choice?
#
# (C) 2024 - Juan Caballero

import logging
import argparse
from random import choice, shuffle

parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
parser.add_argument("-n", "--numsim", type=int, default=100, help="number of simulations, default=100")
parser.add_argument("-s", "--switch", action="store_true", help="switch doors")
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug("Verbose mode on")

num_sim = args.numsim
switch  = args.switch
doors   = [1, 2, 3]
prizes  = ['A', 'B', 'C'] # C is Car, A/B is a goat
wins    = 0

def get_host_sel(cprizes, our):
    '''
    function to open a door which is not the selected and has no prize
    returns the other door
    '''
    sel = None
    for door in doors:
        if door == our or cprizes[door - 1] == 'C':
            continue
        sel = door
    return sel

def get_new_door(our, host):
    '''
    function to switch door which is not the previouly selected or the host selection
    returns the other door
    '''
    sel = None
    for door in doors:
        if door == our or door == host:
            continue
        sel = door
    return sel

# Main simulation part
print(f"Welcome to the show, we're running {num_sim} simulations")
rep = int(num_sim / 10) # report every 10%

for sim in range(num_sim):
    shuffle(prizes)
    our_door  = choice(doors)
    host_door = get_host_sel(cprizes=prizes, our=our_door)

    if switch:
        our_door = get_new_door(our=our_door, host=host_door)

    win = 'no'
    if prizes[our_door - 1] == 'C':
        wins += 1
        win = 'yes'

    logging.debug(f"Simulation {sim} => prizes: {prizes}, our: {our_door}, host: {host_door}, switch: {switch}, win: {win}")

    if sim % rep == 0 and sim > 0:
        print("  {}%".format(int(10 * sim / rep)))

print(" 100%")
res = int(100 * wins / num_sim)
if switch:
    mode = "with switch"
else:
    mode = "without switch"
print(f"Results {mode}: {wins}/{num_sim} = {res}%")
