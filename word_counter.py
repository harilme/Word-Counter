def count_words(text):
    words = text.split()  # Split the text into a list of words
    return len(words)     # Return the count of words

# Get input from the user
input_text = input("Enter a string of text: ")

# Call the function to count words and print the result
word_count = count_words(input_text)
print("The total number of words in the text is:", word_count)
