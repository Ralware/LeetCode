def fib(self, Num: int) -> int:

        Pre,Next = 0,1

        for _ in range(Num):
            Pre,Next = Next,(Pre+Next)

        return Pre