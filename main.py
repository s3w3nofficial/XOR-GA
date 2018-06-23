import random 

gens = []

class Population():

    def __init__(self, size):
        for _ in range(size):
            gens.append(DNA(MUTATION_RATE))

    def evaluate(self):
        max_fit = 0
        for x in range(len(gens)):
            tmp = gens[x].fitness()
            if tmp > max_fit:
                max_fit = tmp
            if tmp == len(data):
                print("best gen is " + str(x) + " with ans " + str(gens[x].ans))

        for x in range(len(gens)):
            if random.randint(0, 100) > 50:
                gens[x].ans[0] = gens[random.randint(0, len(gens)-1)].ans[0]
                gens[x].ans[1] = gens[random.randint(0, len(gens)-1)].ans[1]
            else:
                gens[x].ans[2] = gens[random.randint(0, len(gens)-1)].ans[2]
                gens[x].ans[3] = gens[random.randint(0, len(gens)-1)].ans[3]

        for x in range(len(gens)):
            gens[x].mutation()

class DNA():

    def __init__(self, mutation_rate):
        self.ans = []
        self.mutation_rate = mutation_rate
        for _ in range(len(data)):
            self.ans.append(random.randint(0, 1))

    def fitness(self):
        score = 0
        for x in range(len(self.ans)):
            if self.ans[x] == q[x]:
                score += 1

        return score

    def mutation(self):
        if random.randint(0, 100) / 100 == self.mutation_rate:
            self.ans[random.randint(0, len(self.ans))] = random.randint(0, 1)


data = [[0, 0], [0, 1], [1, 0], [1, 1]]
q = [0, 1, 1, 0]

POP_SIZE = 100
GENERATIONS = 100
MUTATION_RATE = 0.001

def main():
    population = Population(POP_SIZE)

    for x in range(GENERATIONS):
        population.evaluate()

if __name__ == "__main__":
    main()

#vypocet
#evaluace
#krizeni
#mutaci
#nova gen
