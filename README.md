**ENGLISH**

Here's a summary of what each part of the code does:

*Main Function:*

   `1. Warns the user to only enter positive integers.`
   
   `2. Calls data_input_handler to get the number, power, and divisor from the user.`
   
   `3. Calls power_decomposition to decompose the power into a sum of powers of 2.`
   
   `4. Calls computer to calculate the modular exponentiation.`
   
   `5. Prints the result and calls handler to see if the user wants to run again.`

*Data Input Handler:*

   `1. Prompts the user for the number, power, and divisor.`
   
   `2. Handles ValueError if the user enters non-integers.`
   
   `3. Returns the number, power, and divisor as a tuple.`

*Power Decomposition:*

   `1. Creates lists to store powers of 2 and the final decomposition.`
   
   `2. Iteratively adds increasing powers of 2 until it exceeds the input power.`
   
   `3. Reverses the powers of 2 and removes the highest one.`
   
   `4. Iterates over the powers of 2 from largest to smallest, checking if they fit in the remaining power.`
   
   `5. Adds fitting powers of 2 to the final decomposition and subtracts them from the remaining power.`
   
   `6. Returns the original powers of 2 list and the final decomposition.`

*Computer:*

   `1. Calculates the modular exponentiation of the number for each individual power of 2.`
   
   `2. Filters out unnecessary calculations based on the power decomposition.`
   
   `3. Repeatedly multiplies the remaining values modulo the divisor until there's only one left.`
   
   `4. Returns the final value.`

*Handler:*

    `1. Asks the user if they want to run the program again.`
    
    `2. Restarts the program if the user says yes.`
    
    `3. Exits the program if the user says no.`
    
    `4. Handles invalid input and loops back to ask again.`


=============================================================================================================

**MAGYAR**

Összefoglaló, hogy mit csinálnak a kód egyes részletei:

*Fő függvény:*

   `1. Figyelmezteti a felhasználót, hogy csak pozitív egész számokat írjon be.`
   
   `2. Meghívja a data_input_handler-t, hogy megkapja a számot, a hatványt és az osztót a felhasználótól.`
   
   `3. Meghívja a power_decomposition-t, hogy a hatványt 2 hatványainak összegére bontsa.`
   
   `4. Meghívja a számítógépet a moduláris hatványozás kiszámításához.`
   
   `5. Kinyomtatja az eredményt, és meghívja a kezelőt, hogy megkérdezze, akarja-e a felhasználó újra futtatni.`

*Adatbevitel-kezelő:*

   `1. Megkérdezi a felhasználótól a számot, a hatványt és az osztót.`
   
   `2. Kezeli a ValueError-t, ha a felhasználó nem egész számokat ad meg.`
   
   `3. Visszaadja a számot, a hatványt és az osztót egy tupliként.`

*Hatványfelbontás:*

   `1. Létrehoz listákat a 2-es hatványok és a végső dekompozíció tárolására.`
   
   `2. Iteratív módon addig növeli a 2 növekvő hatványait, amíg az meg nem haladja a bemeneti hatványt.`
   
   `3. Megfordítja a 2-es hatványokat, és eltávolítja a legnagyobbat.`
   
   `4. Iterálja a 2-es hatványokat a legnagyobbtól a legkisebbig, és ellenőrzi, hogy beleférnek-e a fennmaradó teljesítménybe.`
   
   `5. Hozzáadja az illeszkedő 2-es hatványokat a végső bontáshoz, és kivonja őket a maradék hatványból.`
   
   `6. Visszaadja az eredeti 2-es hatványok listáját és a végső dekompozíciót.`
   

*Számológép:*

   `1. Kiszámítja a szám moduláris hatványozását minden egyes 2-es hatványra.`
   
   `2. Kiszűri a felesleges számításokat a hatványbontás alapján.`
   
   `3. Ismételten megszorozza a maradék értékeket modulo az osztóval, amíg csak egy nem marad.`
   
   `4. Visszaadja a végső értéket.`

*Kezelő:*

    `1. Megkérdezi a felhasználót, hogy szeretné-e újra futtatni a programot.`
    
    `2. Újraindítja a programot, ha a felhasználó igent mond.`
    
    `3. Kilép a programból, ha a felhasználó nemet mond.`
    
    `4. Kezeli az érvénytelen bemenetet és visszakérdez a ciklusban.`


