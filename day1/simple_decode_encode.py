import string
alphabet  = list(string.ascii_lowercase)

print('''
             .'`'.'`'.
         .''.`.  :  .`.''.
         '.    '. .'    .'
         .```  .' '.  ```.
         '..',`  :  `,'..'
              `-'`'-`))
                     ((    ldb
                      \|
                      
      ''')
def encrypt_string(user_input, amount_shift):
    encrypted_string = ""
    for i in str(user_input):
        if i in alphabet:
            index = alphabet.index(i) + amount_shift
            while index > 25:
                index -=26
            encrypted_string += alphabet[index]
        else:
            encrypted_string += i
    print(f"Here's encoded message: {encrypted_string}")

def decrypt_string(user_input, amount_shift):
    decrypted_string = ""
    for i in user_input:
        if i in alphabet:
            index = alphabet.index(i) - amount_shift
            while index < 0:
                index +=26
            decrypted_string += alphabet[index]
        else:
            decrypted_string += i
    print(f"The decoded message is : {decrypted_string}")


user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
user_input = input("Type your message here : \n").lower()
amount_shift = int(input("Type the shift number: \n"))
if user_choice == "encode":
    encrypt_string(user_input, amount_shift)
elif user_choice == "decode":
    decrypt_string(user_input, amount_shift)
else: 
    print("invalid choice. Exitting the program...")


