def count_occurrences(word, text):
    count = 0
    words = text.split()
    for w in words:
        if w.strip(".,!?") == word:
            count += 1
    return count

def replace_word(word, replacement, text):
    words = text.split()
    replaced_words = []
    count = 0
    for w in words:
        if w.strip(".,!?") == word:
            count += 1
            if count % 2 == 0:
                replaced_words.append(replacement)
            else:
                replaced_words.append(word)
        else:
            replaced_words.append(w)
    return ' '.join(replaced_words)

# Read the file
with open('file_to_read.txt', 'r') as file:
    text = file.read()

# Calculate the total occurrences of "terrible"
word_to_count = "terrible"
occurrences = count_occurrences(word_to_count, text)
print(f'Total occurrences of "{word_to_count}": {occurrences}')

# Replace the word based on its occurrence
replacement_even = "pathetic"
replacement_odd = "marvellous"
replaced_text = replace_word(word_to_count, replacement_even, text)

# Write the modified text to a new file
with open('result.txt', 'w') as file:
    file.write(replaced_text)

print('Replacement completed. The modified text has been written to "result.txt".')
