for i in range (1, 11):
    print (i) 


def getindex(skyscaper, c):
    for c in enumerate ('skyscraper'):
        print('skyscraper'.index('c'))
        return

getindex('skyscraper', 'c') 


def shout_words(words):
    print (words.upper()) 


words = 'Everybody likes bananas'
shout_words('Everybody likes bananas')


#I have an issue here
def extract_longer(length, sentence):
    words = sentence.split()
    word_length = {len (w) for w in words}
    for w in words with word_length >= length:
        print (words)
    else:
        print ('false')

 
extract_longer(5, 'Try not to interrupt the speaker') 