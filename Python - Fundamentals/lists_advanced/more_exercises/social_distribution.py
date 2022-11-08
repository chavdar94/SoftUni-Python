population = list(map(int, input().split(", ")))
minimum_wealth = int(input())

if sum(population) < len(population) * minimum_wealth:
    print("No equal distribution possible")
else:
    poorest = min(population)

    while poorest < minimum_wealth:
        poorest_index = population.index(poorest)
        richest = max(population)
        richest_index = population.index(richest)

        needed = minimum_wealth - poorest
        can_take = richest - minimum_wealth
        redistributed_wealth = min(needed, can_take)
        population[poorest_index] += redistributed_wealth
        population[richest_index] -= redistributed_wealth

        poorest = min(population)

    print(population)