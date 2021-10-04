#########################################################################
##                                                                      #
#                    Code Maker - By James Lu                           #
#                     last revised: 9/24/21                             #
#                                                                       #
#   A cybertext program that uses a randomly generated OTP              #
#   (one-time-pad) to code and decode messages. alpha characters        #
#   are the only inputs allowed, all others will produce no result      #
#   User is asked prompted to enter a word message to code or decode.   #
#   Messages are broken up into individual letters and comapred to the  #
#   OTP's values. To code the message, letters are replaced with the    #
#   OTP code value based on the letter's ascii position. To decode,     #
#   letters are replaced with the OTP code value based on the letter's  #
#   ascii position. Every OTP is random, so if the program is ran again #                                                                     
#   and the same letters are inputed, the coded message would be        #
#   different                                                           #
#                                                                       #
#########################################################################

import random
import string
alphabet_string0 = string.ascii_uppercase
alphabet_string1 = string.ascii_lowercase
alphabet_list_up = list(alphabet_string0)
alphabet_list_low = list(alphabet_string1)
random.shuffle(alphabet_list_up)
random.shuffle(alphabet_list_low)
print("Welcome to CodeMaker!")
choice = 0
while choice != 3:
    choice = int(input("\n\nPlease enter 1 to code, 2 to decode, or 3 to quit coding \n"))
    
    if choice == 1:
        toocoded = input("\nEnter the message to be coded here:  ")
        waytoocoded = ""
        
        for letter in toocoded:
            if (ord(letter)-97) in range(list(alphabet_string1).index('a'),(list(alphabet_string1).index('z')+1)):
                waytoocoded += alphabet_list_low[alphabet_list_low.index(letter)-alphabet_list_low.index('z')]
            elif (ord(letter)-65) in range(list(alphabet_string0).index('A'),(list(alphabet_string0).index('Z')+1)):
                waytoocoded += alphabet_list_up[alphabet_list_up.index(letter)-alphabet_list_up.index('Z')]
            elif letter == ' ': waytoocoded += ' '
            else: waytoocoded += '?'
        print (waytoocoded, "\n\n")

    elif choice == 2:
        toocoded = input("\nEnter the message to be decoded here:  ")
        waytoocoded = ""
        
        for letter in toocoded:
            if (ord(letter)-97) in range(list(alphabet_string1).index('a'),(list(alphabet_string1).index('z')+1)):
                waytoocoded += alphabet_list_low[alphabet_list_low.index(letter)+(alphabet_list_low.index('z')-26)]
            elif (ord(letter)-65) in range(list(alphabet_string0).index('A'),(list(alphabet_string0).index('Z')+1)):
                waytoocoded += alphabet_list_up[alphabet_list_up.index(letter)+(alphabet_list_up.index('Z')-26)]
            elif letter == ' ': waytoocoded += ' '
            else: waytoocoded += '?'
        print (waytoocoded, "\n\n")

print ("\n***** Thank you, please come again *****\n\n")