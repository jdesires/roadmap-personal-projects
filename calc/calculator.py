class Calculator:
    
    # Each function will be a staticmethod. Meaning they will never change
    @staticmethod
    def add(*args):
        # Set total to 0
        total = 0

        ## Loop through each argument and add x to total
        for x in args:
            total += x
        return total
    
    @staticmethod
    def subtract(*args):
        # Set total to the first argument the user inputs
        total = args[0]

        # Loop through each argument and subtract that number from total
        for x in args[1:]:
            total -= x
        return total

    @staticmethod
    def multiply(*args):
        # Set total to the first argument the user inputs
        total = args[0]

        # Loop through each argument and multiply total by that number
        for x in args[1:]:
            total *= x
        return total

    @staticmethod
    def divide(*args):
        # Set total to the first argument the user inputs
        total = args[0]
        
        # Loop through each argument and divide by that number
        for x in args[1:]:
            total /= x
        return total
    
    @staticmethod
    def exponents(a,b):
        return a ** b
    
    @staticmethod
    def floor_division(*args):
        # Set total to the first argument the user inputs
        total = args[0]

        # Loop through each argument and use floor division on total
        for x in args[1:]:
            total //= x
        return total