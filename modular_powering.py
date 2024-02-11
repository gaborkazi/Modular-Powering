def main(): # Programfüggvény
    print("\nWarning! You can only enter positive integers!\n\n")
    def data_input_handler(): # Get the number, the power and the divisor
        try:
            number = int(input("Please enter the number to be exponentiated: "))
            power = int(input("Please enter the exponent of the number to be exponentiated: "))
            divisor = int(input("Please enter the divisor of the number to be power: "))
        except ValueError:
            print("\nYou can only enter positive integers!")
            return data_input_handler()
        return number, power, divisor
    
    number, power, divisor = data_input_handler()
    
    def power_decomposition(power): # Decomposition of the input power into powers of two
        powers_of_2 = [] # The powers of two to the given power
        counter = 0
        while (len(powers_of_2) == 0) or (powers_of_2[-1] <= power):
            powers_of_2.append(2**counter)
            counter += 1
        powers_of_2.pop()
        powers_of_2_copy = powers_of_2.copy()
        
        powers = [] # Decomposition of the power into the sum of the powers of two
        for i in reversed(powers_of_2):
            if power - i < 0:
                continue
            else:
                power -= i
                powers.append(i)
        powers.reverse()
        return powers_of_2_copy, powers
    
    def computer(number, divisor, powers_of_2, powers): # Power divided into powers of 2
        idx_values = [number**i % divisor for i in powers_of_2]
        values = [val2 for val1, val2 in zip(powers_of_2, idx_values) if val1 in powers]
        
        while len(values) > 1:
            values[0] = (values[0] * values[1]) % divisor
            values.pop(1)

        return values[0]
    
    powers_of_2, powers = power_decomposition(power)
    value = computer(number, divisor, powers_of_2, powers)
    
    print(f"\nThe value of {number}^{power} MOD {divisor}: {value}")
    
    handler()
    return value

def handler(): # Handling function
    repeat = input("\n\n\nWant to run the program again? (Y/N): ").lower()
    if repeat in ("yes", "y"):
        main()
    elif repeat == "n" or "no:
        exit()
    else:
        print("\n\nOops! You've done something wrong!")
        handler()
main()
