#https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

Morse_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']

def encode(word):                                          #translates the given word into morse code
    morse_string = ""
    for ch in word:
        index = Alphabet_list.index(ch)
        morse_string += Morse_list[index]
    print('{0} = {1}'.format(word, morse_string))
        
####################################################################################################################################
#main
word_list = ["sos", "daily", "programmer", "bits", "three"]
for word in word_list:
    encode(word)
