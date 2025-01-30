student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet_df = pandas.DataFrame(nato_alphabet_data)

#Create NATO dictionary out of Dataframe.
nato_alphabet_dict = {row.letter:row.code for (index, row) in nato_alphabet_df.iterrows()}
print(nato_alphabet_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# user_word = input("What word would you like to convert to NATO alphabet?: ").upper()

#converted_list = [code for (letter, code) in nato_alphabet_dict.items() if letter in user_word]

# converted_list = [nato_alphabet_dict[letter] for letter in user_word]
# print(converted_list)

#Using try/catch error handling
def generate_phonetic():
    user_word = input("What word would you like to convert to NATO alphabet?: ").upper()
    try:
        converted_list = [nato_alphabet_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters in the dictionary please.")
        generate_phonetic()
    else:
        print(converted_list)

generate_phonetic()