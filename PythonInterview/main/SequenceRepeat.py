"""
Hermione is preparing a cheat-sheet for her final exam in Potions class.
To create a potion, one must combine ingredients in a specific order, any of which may
be repeated.
As an example, consider the following potion which uses 4 distinct ingredients
(A,B,C,D) in 11 steps: A, B, A, B, C, A, B, A, B, C, D.
Hermione realizes she can save tremendous space on her cheat-sheet by introducing a
special instruction, &#39;*&#39;, which means &quot;repeat from the beginning&quot;.
Using these optimizations, Hermione is able to encode the potion above using only 6
characters: A,B,*,C,*,D
"""

def compress_potion_sequence(sequence):
    compressed_sequence = []
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == sequence[i - 1]:
            count += 1
        else:
            if count > 1:
                compressed_sequence.append('*')
            compressed_sequence.append(sequence[i - 1])
            count = 1

    if count > 1:
        compressed_sequence.append('*')

    compressed_sequence.append(sequence[-1])

    return compressed_sequence

def potion_sequence_to_string(sequence):
    compressed_sequence = compress_potion_sequence(sequence)
    compressed_string = ''.join(map(str, compressed_sequence))
    return compressed_string

# Example usage:
original_sequence = ['A', 'B', 'A', 'B', 'C', 'A', 'B', 'A', 'B', 'C', 'D']
compressed_string = potion_sequence_to_string(original_sequence)

print("Original Sequence:", ''.join(original_sequence))
print("Compressed Sequence:", compressed_string)
