'''
Extra 
(): better functionality for yes no to restart the loop
'''

import random
scale_dct = {'Major': {'C':['C','D','E','F','G','A','B'], 'C#':['C#','D#','F','F#','G#','A#','C'], 'Db':['Db','Eb','F','Gb','Ab','Bb','C'], 'D':['D','E','F#','G','A','B','C#'], 'D':['D','E','Gb','G','A','B','Db'], 'D#':['D#','F','G','G#','A#','C','D'], 'Eb':['Eb','F','G','Ab','Bb','C','D'], 'E':['E','F#','G#','A','B','C#','D#'], 'E':['E','Gb','Ab','A','B','Db','Eb'], 'F':['F','G','A','A#','C','D','E'], 'F':['F','G','A','Bb','C','D','E'], 'F#':['F#','G#','A#','B','C#','D#','F'], 'Gb':['Gb','Ab','Bb','B','Db','Eb','F'], 'G':['G','A','B','C','D','E','F#'], 'G':['G','A','B','C','D','E','Gb'], 'G#':['G#','A#','C','C#','D#','F','G'], 'Ab':['Ab','Bb','C','Db','Eb','F','G'], 'A':['A','B','C#','D','E','F#','G#'], 'A':['A','B','Db','D','E','Gb','Ab'], 'A#':['A#','C','D','D#','F','G','A'], 'Bb':['Bb','C','D','Eb','F','G','A'], 'B':['B','C#','D#','E','F#','G#','A#'], 'B':['B','Db','Eb','E','Gb','Ab','Bb']},'Minor': {'C':['C','D','D#','F','G','G#','A#'], 'C':['C','D','Eb','F','G','Ab','Bb'], 'C#':['C#','D#','E','F#','G#','A','B'], 'Db':['Db','Eb','E','Gb','Ab','A','B'], 'D':['D','E','F','G','A','A#','C'], 'D':['D','E','F','G','A','Bb','C'], 'D#':['D#','F','F#','G#','A#','B','C#'], 'Eb':['Eb','F','Gb','Ab','Bb','B','Db'], 'E':['E','F#','G','A','B','C','D'], 'E':['E','Gb','G','A','B','C','D'], 'F':['F','G','G#','A#','C','C#','D#'], 'F':['F','G','Ab','Bb','C','Db','Eb'], 'F#':['F#','G#','A','B','C#','D','E'], 'Gb':['Gb','Ab','A','B','Db','D','E'], 'G':['G','A','A#','C','D','D#','F'], 'G':['G','A','Bb','C','D','Eb','F'], 'G#':['G#','A#','B','C#','D#','E','F#'], 'Ab':['Ab','Bb','B','Db','Eb','E','Gb'], 'A':['A','B','C','D','E','F','G'], 'A#':['A#','C','C#','D#','F','F#','G#'], 'Bb':['Bb','C','Db','Eb','F','Gb','Ab'], 'B':['B','C#','D','E','F#','G','A'], 'B':['B','Db','D','E','Gb','G','A']}}

letter_map = {'A':'A', 'B':'B', 'C':'C', 'D':'D', 'E':'E', 'F':'F', 'G':'G', 'H':'A', 'I':'B', 'J':'C', 'K':'D', 'L':'E', 'M':'F', 'N':'G', 'O':'A', 'P':'B', 'Q':'C', 'R':'D', 'S':'E', 'T':'F', 'U':'G', 'V':'A', 'W':'B', 'X':'C', 'Y':'D', 'Z':'E'}

def find_partial_match(token, token_list):
    for full_string in token_list:
        if token in full_string:
            return token,full_string

print("Do you have a key in mind? \n Type y for YES \n Type n for no, I want a random key")
print('\n')
answer = input()
if answer.upper() == 'Y':
    print('Major or Minor? \n Type j for MAJOR \n Type n for MINOR')
    # key = input():
    # if key.upper() == 'J':
        # t = 
    # elif key.upper() == 'N':
    # scale_dct['Major']
    # scale_dct['Minor']

elif answer.upper() == 'N':
    minor_major = random.choice(list(scale_dct.keys()))
    key = random.choice(list(scale_dct[minor_major].keys()))
    scale = scale_dct[minor_major][key]
    print(f"Your key is {key} {minor_major}: {' '.join(scale_dct[minor_major][key])}")

print('\n')
print('Type the word you want to map to a scale')
word = input()
new_ls = [letter_map[x.upper()] for x in word if x.upper() in letter_map]
for i in new_ls:
    try:
        a,b = find_partial_match(i,scale)    
        idx = new_ls.index(a)
        new_ls[idx] = b
    except TypeError:
        new_ls = new_ls
a = new_ls
print('\n')
print(f"Your progression is: {' '.join(a)}")
# print(f"Your progression is:  {' '.join([letter_map[x.upper()] for x in word if x.upper() in letter_map])}")