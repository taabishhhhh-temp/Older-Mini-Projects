'''
This script counts how many times a letter is repeated in a text also gives the average of the letter in the text
'''

with open('HTML_MUST_KNOW_CONCEPTS.txt','r') as f:
    data = f.read()

input_ = input('Enter a Letter: ')[0]
input_lower = input_.lower()
input_upper = input_.upper()
total_count = 0
letter_count = 0
for letter in data:
    total_count += 1
    if letter ==  input_lower or letter == input_upper:
        letter_count += 1

average = total_count / letter_count
print('There are total {} letters in the text and {} is repeated {} times and average of {} in the text is {}'.format(total_count, input_, letter_count, input_, average))