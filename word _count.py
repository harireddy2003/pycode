def count_words(input_string):
    word_count = 0

    in_word = False

    for char in input_string:

        if char.isspace():

            if in_word:
                word_count += 1
                in_word = False
        else:

            in_word = True


    if in_word:
        word_count += 1

    return word_count


test_string = input("enter a words or sentence : ")
print(f"The number of words in the string is: {count_words(test_string)}")
