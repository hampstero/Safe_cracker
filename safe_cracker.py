import time
from random import randint, randrange

def fitness(combo, attempt):
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1
    return grade
def random_combination():
    combination = ''
    for i in range(0,randint(9,1000)):
        combination += str(randint(0,9))
    return combination

def saved_results(combination):
    start_time = time.time()
    combo = [int(i) for i in combination]

    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    while best_attempt != combo:
        run_time = time.time()
        next_try = best_attempt[:]

        
        for i in range (0, len(combo)):
            if best_attempt[i] != combo[i]:
                next_try[i] = randint(0,9)
            else:
                next_try[i] = best_attempt[i]

        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        count += 1

    return(run_time - start_time)
def stochastic_results(combination):
    start_time = time.time()
    combo = [int(i) for i in combination]

    best_attempt = [0] * len(combo)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    while best_attempt != combo:
        run_time = time.time()
        next_try = best_attempt[:]

        
        lock_wheel = randrange(0, len(combo))
        next_try[lock_wheel] = randint(0, 9)

        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        count += 1

    return(run_time - start_time)
def main():
    while True:
        user = input("Type 'crack' to generate a safe to crack. Press Enter to exit.\n")
        if user == 'crack':
            combination = random_combination()
            print(f"Combination was {combination}")
            print(f"Length of combination = {len(combination)}")
            stochastic_time = stochastic_results(combination)
            saved_time = saved_results(combination)
            print(f"Time taken by stochastic = {stochastic_time}")
            print(f"Time taken by saved = {saved_time}")
            print(f"Difference was = {stochastic_time - saved_time}")
        else:
            return
if __name__ == '__main__':
    main()