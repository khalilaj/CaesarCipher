import sys

# Global Variable of the 26 letter alphabet
alphabet = ["a", "b", "c", "d","e","f","g","h", "i", "j", 
            "k", "l", "m", "n","o","p", "q", "r","s", "t",
             "u", "v", "w", "x", "y", "z"]

# A classe that performs the cipher logic
class CeaserCipher:
    def __init__(self,N = 13):
        # N : Number of steps to rotate the alphabet by
        # Default value given is 13 because if you apply N=13 shift 2 you get back the original message --SO COOL--

        self.cipher_alphabet = alphabet[N:]
        self.cipher_alphabet.extend(alphabet[0:N])

    def encrypt(self, message):
        encrypted = ""
        message = message.lower()

        for letter in message:
            if alphabet.count(letter) > 0:
                letter_index = alphabet.index(letter)
                encrypted += self.cipher_alphabet[letter_index]
            else:
                encrypted += letter
        return encrypted

    def decrypt(self, message):
        decrypted = ""
        message = message.lower()

        for letter in message:
            if alphabet.count(letter) > 0:
                letter_index = self.cipher_alphabet.index(letter)
                decrypted += alphabet[letter_index]
            else:
                decrypted += letter
        return decrypted

# Check to see if the system reads the file
if __name__ == "__main__":

    # Verify if the two inputs are entered
    if len(sys.argv)< 3:
        print("Please provide action (e/d) and message and CLI options")

    # Program takes in two inputs the option of encrypting or decrypting
    #  and the phrase that the user wants to be worked on
    action = sys.argv[1]
    phrase = sys.argv[2]

    rotation_distance = 3
    cipher = CeaserCipher(rotation_distance)

    # Ckeck which action was selected and perform the required action
    if action == "e":
        phrase = cipher.encrypt(phrase)
        print("Encrypting: {}".format(phrase))
    elif action == "d":
        phrase = cipher.decrypt(phrase)
        print("Decrypting: {}".format(phrase))
    else:
        print("Invalid action, Please provide e or d for encrypting and decrypting")

    # print(sys.argv)

 