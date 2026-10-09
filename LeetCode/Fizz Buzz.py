def FizzBuzz(Num: int) -> list[str]:

    Array = []

    for Index in range(Num):

        if (Index + 1) % 3 == 0 and (Index + 1) % 5 == 0:
            Array.append("FizzBuzz")

        elif (Index + 1) % 5 == 0:
            Array.append("Buzz")

        elif (Index + 1) % 3 == 0:
            Array.append("Fizz")

        else:
            Array.append(str(Index + 1))

    return Array


