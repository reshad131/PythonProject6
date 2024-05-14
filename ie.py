import random
import math

def randomMath():
    numbers = [random.randint(20, 50) for _ in range(5)]
    print("List:", numbers)
    kvadrat_eded = [math.pow(num, 2) if num % 2 == 0 else num for num in numbers]
    return kvadrat_eded


kvadrat_eded = randomMath()
print("List:", kvadrat_eded)
