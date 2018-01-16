
#returns index/integer position of a letter in the alphabet
def alphposition(letter):
    import string
    #use the property ascii letters to assign the variable 'alphabet' 
    alphabet = string.ascii_uppercase
    return alphabet.index(letter)    

print alphposition("C")

#create a function that rotates characters

#create a function that uses rotate & alphposition functions to move letters a certain amount fwd
