import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")


dictionary = {row.letter:row.code for row in df.itertuples(index=False)}
print(dictionary)
user_input = input("Enter a word: ").upper()
word_list = [dictionary.get(words) for words in user_input]
print(word_list)
