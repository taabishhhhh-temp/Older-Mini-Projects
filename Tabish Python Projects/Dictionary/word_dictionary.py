import json
# import pyttsx3
# from difflib import get_close_matches

# speaker = pyttsx3.init()

# def speak(sentence):
#     speaker.say(sentence)
#     speaker.runAndWait()

data = json.load(open('data.json'))

def meaning(word):
    if word in data.keys():
        output = data[word]
        if len(output) > 1:
            print()
            # speak('Here are the Results')
            print('Here are the Results--->')
            print()
            i = 1
            for word in output:
                print(i , ': ', word)
                i+=1
            print()
        else:
            print()
            # speak('Here is the Result')
            print('Here is the Result--->')
            print()
            print(output)
            print()
    else:
        print()
        # speak('Sorry Sir Meaning of this word is not Available in the Dictionary.')
        print('Sorry Sir Meaning of this word is not Available in the Dictionary.')
        # speak('Thank you for Using')
        print('Thank you for Using')
        print()

while True:
    # speak('Enter the word')
    word = input('Enter the word: ').lower()
    meaning(word)