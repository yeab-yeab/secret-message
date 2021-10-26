from tkinter import messagebox, simpledialog, Tk
from random import choice


def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []               # make a list variable to store the even letters
    for counter in range(0, len(message)):      # loop through every letters in the message
        if is_even(counter):                # if this is a letter in an even position, python adds it to the end of the list of letters
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'         # add an extra x to any message with an odd number of letters
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):       # loop through the list of odd and even letters
        letter_list.append(odd_letters[counter])        # add the next odd letter to the final message
        letter_list.append(even_letters[counter])       # add the next even letter to the final message 
    new_message = ''.join(letter_list)                  # the join() function turns the list of letters into string
    return new_message

def encrypt(message):
    encrypted_list = []
    fake_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'r', 's', 't', 'u', 'v']
    for counter in range(0, len(message)):
        encrypted_list.append(message[counter])
        encrypted_list.append(choice(fake_letters))
    new_message = ''.join(encrypted_list)
    return new_message

def decrypt(message):
    even_letters = get_even_letters(message)        # Get the original message's letters
    new_message = ''.join(even_letters)             # join the letters in even_letters into a string    
    return new_message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt')
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

root = Tk()
root.withdraw()

while True:
    task = get_task()
    if task == 'encrypt':
        message = get_message()
        encrypted = encrypt(message)
        messagebox.showinfo('Ciphertext of the secret message is:', encrypted)
    elif task == 'decrypt':
        message = get_message()
        decrypted = decrypt(message)
        messagebox.showinfo('Plaintext of the secret message is:', decrypted)
    else:
        break       # stop the loop if the user doesn't input encrypt or decrypt
root.mainloop()     # keep tkinter working
