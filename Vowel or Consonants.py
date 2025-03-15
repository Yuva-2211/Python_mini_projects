#Check  if the following Alphabet is a vowel or not


alphabet = str(input("Enter your Alphabet:"))
vowels={'a','e','i','o','u','A','E','I','O','U'}

if len(alphabet) != 1 or not alphabet.isalpha():
    print("Error: Please enter a single alphabet character.")
elif(alphabet in vowels):
    print(alphabet,",Yes its an vowel")

else:
    print(alphabet,",Its a Consonant")

