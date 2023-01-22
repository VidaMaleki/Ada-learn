











from string import punctuation


def reverse_word(word):
    puctuation = [",", "!", "?"]
    punc = ""
    reverse = []
    for letter in range(len(word), -1, -1):
        if letter in puctuation:
            punc = letter
            word.replace(letter, "")
        reverse.append(letter)
    word = "".join(reverse) + punc
    return word

def reverse_sentence(sentence):
    splited_s = sentence.split()
    new_list = []
    for word in splited_s:
        word = reverse_word(word)
        new_list.append(word)
    return " ".join(new_list)

sentence = "I have a question, could you answer?"
print(reverse_sentence(sentence))