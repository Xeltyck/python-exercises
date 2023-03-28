subjet = ["I","You"]
verb = ["Play","love"]
object = ["Hockey","Football"]

for number in range(0,8):

    combinations = bin(number) # Number of combinations than can be reached given the 3 bits.
    binary = combinations[2:] # Removes the "0b" from "0b111"
    while len(binary) < 3: # Converts any binary to a 3 digits binary number. 
        binary = "0" + binary
    print(f'{subjet[int(binary[0])]} {verb[int(binary[1])]} {object[int(binary[2])]}')

