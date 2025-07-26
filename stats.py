def count_words(text):
    words = text.split(" ")
    return len(words)

def count_letters(text):
    letters = {}
    for char in text:
        if char in '\n':
            if '\\n' in letters:
                letters['\\n'] += 1
            else:
                letters['\\n'] = 1
        elif char in letters:
            letters[char] += 1
        else:
           letters[char] = 1
    return letters