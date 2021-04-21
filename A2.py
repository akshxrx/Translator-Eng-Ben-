print('''\nHello, welcome to Akshara's version of translator.
Here we translate between bengali and english but only for: 
sports, art, leisure, games and basic socializing.''')

'''Following is the list of improvements I made : ) >>
    1. Changed the domain to mainly sports 
    2. Then expanded domain to other activities (art, leisure, games and socializing)
    3. Changed the language from french to bengali
    4. Increase the vocabulary to 50+
    5. Added comments to help others understand the codes better
    6. Fixed the glitch with double end characters/ period
    7. Wrote codes to take the english to bengali dictionary and generate a bengali to english dictionary 
       (but did not create a function because it messed with other functions and codes written later)
    8. I made the whole translator only translate in present tense
    9. I modified my program to account word that does not exist in Bengali such as am, is or are
    10.I modified my program to fix plural problems
    11.I developed it so it asks the user for specific direction for translating and then ask the use for input
    12.I finally created a loop, where it asks user for input continuously until the user wants to stop
'''

# This is the English to Bengali dictionary
EtoB = {'I': 'Ami', 'playing': 'khelchi', 'friend': 'bondhu', 'a': 'akta',
        'and': 'abong', 'of': 'era', 'chess': 'daba', 'singing': 'gaichi',
        'some': 'koikta', 'You': 'Tumi', 'game': 'khela', 'We': 'Amra', 'with': 'sathe',
        'using': 'baboharkore', 'resting': 'aramkorchi', 'swimming': 'satar', 'song': 'gan',
        'walking': 'hatchi', 'hide': 'lokano', 'seek': 'khuja', 'Hello': 'Nomoskar',
        'Wanna': 'Chow', 'play': 'khelte', 'above': 'opore', 'below': 'niche', 'running': 'duorachi',
        'performing': 'prodorshonkorchi', 'participating': 'ongshograhankorchi', 'need': 'lagbe',
        'My': 'Amar', 'name': 'naam', 'is': 'hoche', 'here': 'akhane', 'drawing': 'akachi',
        'painting': 'aongkonkorchi', 'rival': 'sotru', 'dancing': 'nachkorchi', 'let': 'chere', 'go': 'diachi',
        'creating': 'toirikorchi', 'artist': 'shilpi', 'picture': 'chobi', 'Hi': 'Adab', 'water': 'jol',
        'It': 'Ata', 'help': 'shahajuo', 'color': 'rong', 'red': 'lal', 'blue': 'nil', 'green': 'sobug',
        'yellow': 'holud', 'art': 'silpo', 'What': 'Ki', 'your': 'tomar', 'snakes': 'saap', 'ladders': 'loddo',
        'artwork': 'silpokajjo', 'cityscape': 'sohorerdrisho', 'seascape': 'somodrerdrisho', 'landscape': 'jungolerdrishow',
        'tree': 'gacher', 'games': 'khala', 'Others': 'Aonnora', 'hang': 'addadibe'}

# These few lines converts the English to Bengali
# dictionary to Bengali to English dictionary
BtoE = {}
for key in EtoB:
    BtoE[EtoB[key]] = key

# This assign the proper names to identify the type of dictionary later
dicts = {'English to Bengali': EtoB, 'Bengali to English': BtoE}

# This function goes through each word and finds it in the proper dictinary
# and replaces it accordingly to have a better translation.


def translateWord(word, dictionary):
    verb = ['swimming']
    if word == 'Ami':               # The lines 48 - 55, it fixes the problem with am, are is.
        return f'I am'              # These words does not properly translate in bengali
    elif word == 'Amra':            # So in the translation from bengali to eng, it would not add these words.
        return 'We are'             # This is where I fix the problem and add these necessary words.
    elif word == 'Ata':             # This is so my translation to english is much more coherent.
        return 'It is'              # Plus I have programmed this translator for present tense
    elif word == 'Ki':              # So, I fixed the code corresponding with the tense
        return 'What is'
    elif word in verb:                          # Line 56 - 59, solves the problem with plural
        return f'{dictionary[word]} katchi'     # There was only one instance, in the domain I chose
    elif word == 'friends':                     # So, I decided to fix the problem with this process
        return 'bondhura'
    else:
        if word in dictionary.keys():  # This part actually checks each word in the necessary dictionary
            return dictionary[word]    # Then replaces that word with the word, asked for the translation
        elif word != '':
            return f'"{word}"'         # If the word is not recognized then it returns the word in quotation
        return word


def grammar(word):
    am = ['am', 'are', 'in', 'is']      # Similarly it fixes the problem mentioned before in line 48-55
    if word in am:                      # There's certain words in english that does not exist in bengali
        return ''                       # They are rather replaced certain letter added to the first word
    else:                               # So Through these codes, I attempt to solve this problem by replacing
        return word                     # the word with an empty space

# This function puts together all the translated words
def translate(sentence, dicts, direction):
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters       # Library of all alphabets in both cases
    dictionary = dicts[direction]         # This determines the direction of the translation {Eng to Ben}/{Ben to Eng}
    translation = ''
    word = ''
    for character in sentence:
        if character in letters:          # This 'if' statements check to see each letter in a word then
            word += character             # returns the word in to a previous function, where it translates
        else:                             # the word from the corresponding dictionary
            translation = translation + translateWord(grammar(word), dictionary) + character
            word = ''
    translation = translation + translateWord(grammar(word), dictionary)  # These two similar line are the formation
    return translation                                                    # of the final statements, and returns it.

# The purpose of this function was the main output
# This is where you specify the direction of the translation
# Then input a phrase which can be translated
def choice():
    choice = int(input('\nDo you want? [1]English to Bengali or [2]Bengali to English >>  '))    # The choice making
    if choice == 1:                                                       # Choice 1 > Eng to Ben
        sentence = input('\nEnter sentence here: ')
        translated = translate(sentence, dicts, 'English to Bengali')
        print('--------------------------------------')
        print('Input:', sentence)
        print('Output:', translated)
        print('--------------------------------------')
        return 'Here you go! : )'
    elif choice == 2:                                                     # Choice 2 > Ben to Eng
        sentence = input('\nEnter sentence here: ')
        translated = translate(sentence, dicts, 'Bengali to English')
        print('--------------------------------------')
        print('Input:', sentence)
        print('Output:', translated)
        print('--------------------------------------')
        return 'Here you go! : )'

# This ending part of the code repeats everything until specified to stop
# Then gives out a goodbye message if they choose to stop translating
print(choice())
repeat = int(input('\nDo you want to translate again? [1]Yes or [2]No > '))
if repeat == 1:
    while repeat == 1:
        print(choice())
        repeat = int(input('\nDo you want to translate again? [1]Yes or [2]No > '))
        if repeat == 2:
            print('\nGood bui! See you later, translator! :3')  # Clever pun
            print('Ta Ta Bye Bye! Abar jeno dekha pai! c:')
            exit()
else:
    print('\nGood bui! See you later, translator! :3')
    print('Ta Ta Bye Bye! Abar jeno dekha pai! c:')




