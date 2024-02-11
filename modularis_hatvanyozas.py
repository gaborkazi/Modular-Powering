def main(): # Programfüggvény
    print("\nFigyelem! Csak pozitív, egész számokat adhat meg!\n\n")
    def data_input_handler(): # A szám, a hatvány és az osztó bekérése
        try:
            number = int(input("Kérem, adja meg a hatványozandó számot: "))
            power = int(input("Kérem, adja meg a hatványozandó szám hatványkitevőjét: "))
            divisor = int(input("Kérem, adja meg a hatványozandó szám osztóját: "))
        except ValueError:
            print("\nCsak pozitív, egész számokat adhat meg!")
            return data_input_handler()
        return number, power, divisor
    
    number, power, divisor = data_input_handler() # szám, hatvány, oszto
    
    def power_decomposition(power): # A bevitt hatvány felbontása a kettő hatványaira
        powers_of_2 = [] # A kettő hatványai a megadott hatványig
        counter = 0
        while (len(powers_of_2) == 0) or (powers_of_2[-1] <= power):
            powers_of_2.append(2**counter)
            counter += 1
        powers_of_2.pop()
        powers_of_2_copy = powers_of_2.copy()
        
        powers = [] # A hatvány felbontása a ketőő hatványainak összegére
        for i in reversed(powers_of_2):
            if power - i < 0:
                continue
            else:
                power -= i
                powers.append(i)
        powers.reverse()
        return powers_of_2_copy, powers
    
    def computer(number, divisor, powers_of_2, powers): # Szám, hatvány, osztó, 2 hatványai, hatvány felbontva 2 hatványaira
        idx_values = [number**i % divisor for i in powers_of_2]
        values = [val2 for val1, val2 in zip(powers_of_2, idx_values) if val1 in powers]
        
        while len(values) > 1:
            values[0] = (values[0] * values[1]) % divisor
            values.pop(1)

        return values[0]
    
    powers_of_2, powers = power_decomposition(power)
    value = computer(number, divisor, powers_of_2, powers)
    
    print(f"\nA {number}^{power} MOD {divisor} értéke: {value}")
    
    handler()
    return value

def handler(): # Kezelőfüggvény
    repeat = input("\n\n\nSzeretné ismét futtatni a programot? (I/N): ").lower()
    if repeat in ("i", "y"):
        main()
    elif repeat == "n":
        exit()
    else:
        print("\n\nHoppá! Valamit elrontott!")
        handler()
main()
