class PrimeFactor:
    def of(self, number) -> []:
        factors = []
        if number > 1:
            factors.append(2)
            factors.append(2)
        else:
            factors.append(number)

        return factors