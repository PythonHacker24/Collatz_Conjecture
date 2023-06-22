import random

set = ["heads", "tails"]



heads = 1
tails = 1

while True:
    selection = random.choice(set)
    if selection == "heads":
        heads += 1
    if selection == "tails":
        tails += 1
    
    total_outcomes = heads + tails
    prob_heads = heads / total_outcomes

    print(prob_heads)
