PLACEHOLDER = '[name]'
with open("invited_names.txt") as names:
    names = names.readlines()

with open("starting_letter.txt") as letter_files:
    letter_contents = letter_files.read()
    for name in names:
        new_name = name.strip()
        letter = letter_contents.replace(PLACEHOLDER, new_name)
        with open(f"letter_for_{new_name}.txt", mode = 'w') as completed_letter:
            completed_letter.write(letter)
