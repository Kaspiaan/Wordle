def get_answers():
    with open('answers.txt') as f:
        lines = f.readlines()
        return [x[0:5] for x in lines]


def get_guesses():
    with open('guesses.txt') as f:
        lines = f.readlines()
        return [x[0:5] for x in lines]


def analyse_letter_used():
    letter_dict = {}
    all_words = get_guesses() + get_answers()
    for word in all_words:
        letters = list(word)
        for letter in letters:
            if letter in letter_dict:
                letter_dict[letter] = letter_dict[letter] + 1
            else:
                letter_dict[letter] = 1
    sorted_letters = {k: v for k, v in sorted(letter_dict.items(), key=lambda item: item[1])}
    return sorted_letters, list(sorted_letters.keys())


def analyse_letter_location():
    letter_dict = {}
    all_words = get_guesses() + get_answers()
    for word in all_words:
        letters = list(word)
        for i, letter in enumerate(letters):
            if letter in letter_dict:
                letter_dict[letter] = [x + y for x, y in
                                       zip(letter_dict[letter], [1 if x == i else 0 for x in range(len(word))])]
            else:
                letter_dict[letter] = [1 if x == i else 0 for x in range(len(word))]
    return letter_dict


def give_word_value_relative():
    letter_dict_score = {}
    answers = get_answers()
    sorted_letters, letter_keys = analyse_letter_used()
    for i in answers:
        score_sum = 0
        for letter in list(set(i)):
            score_sum += sorted_letters[letter]
        letter_dict_score[i] = score_sum
    return {k: v for k, v in sorted(letter_dict_score.items(), key=lambda item: item[1], reverse=True)}


def give_word_value_index():
    letter_dict_score = {}
    answers = get_answers()
    sorted_letters, letter_keys = analyse_letter_used()
    for i in answers:
        score_sum = 0
        for letter in list(set(i)):
            score_sum += letter_keys.index(letter)
        letter_dict_score[i] = score_sum
    return {k: v for k, v in sorted(letter_dict_score.items(), key=lambda item: item[1], reverse=True)}


def give_letter_value_relative():
    letter_dict_score = {}
    answers = get_answers()
    letter_values = analyse_letter_location()
    for i in answers:
        score_sum = 0
        for loc, letter in enumerate(list(set(i))):
            score_sum += letter_values[letter][loc]
        letter_dict_score[i] = score_sum
    return {k: v for k, v in sorted(letter_dict_score.items(), key=lambda item: item[1], reverse=True)}


print(give_letter_value_relative())
