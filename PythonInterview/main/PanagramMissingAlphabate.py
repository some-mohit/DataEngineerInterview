def find_missing_alphabets(sentence):
    alphabet_set = set("abcdefghijklmnopqrstuvwxyz")

    sentence_set = set(sentence.lower())
    print(sentence_set)
    missing_alphabets = alphabet_set - sentence_set

    return sorted(list(missing_alphabets))

# Example usage:
input_sentence = "The quick brown fox jumps over the lazy do"
missing_alphabets = find_missing_alphabets(input_sentence)

print(f"Original Sentence: {input_sentence}")
print(f"Missing Alphabets: {''.join(missing_alphabets)}")
