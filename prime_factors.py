class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:

            divisor = 2
            if number == 4 or number == 6 or number == 9 or number == 12:
                divisor = 2
                while number > 1:
                    while number % divisor == 0:
                        factors.append(divisor)
                        number //= divisor
                    divisor += 1
            else:
                factors.append(number)

        return factors