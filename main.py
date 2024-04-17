def count_words(text):
    # Split the text into words using whitespace as the delimiter
    words = text.split()
    # Return the number of words
    return len(words)

def count_characters(text):
    # Convert the text to lowercase to avoid duplicates
    text = text.lower()

    # Initialize an empty dictionary to store character counts
    char_counts = {}

    # Iterate through each character in the text
    for char in text:
        # Increment the count for the current character
        char_counts[char] = char_counts.get(char, 0) + 1

    # Return the dictionary containing character counts
    return char_counts

def print_report(file_contents):
    num_words = count_words(file_contents)
    char_counts = count_characters(file_contents)

    print("Word Count:", num_words)
    print("Character Counts:")
    # Convert char_counts to a list of dictionaries for sorting
    char_counts_list = [{"character": char, "count": count} for char, count in char_counts.items()]
    # Sort the list of dictionaries based on the count in descending order
    char_counts_list.sort(reverse=True, key=lambda x: x["count"])

    for item in char_counts_list:
        print(f"Character '{item['character']}': {item['count']} times")

def main():
    # Define the path to the "frankenstein.txt" file
    path_to_file = "books/frankenstein.txt"

    # Open the file and read its contents
    with open(path_to_file, "r") as f:
        file_contents = f.read()

    # Print the contents of the file to the console
    print(file_contents)
    
    # Count the number of words in the file contents
    num_words = count_words(file_contents)
    print("Number of words in the text:", num_words)
    
    # Print the contents of the file to the report
    print_report(file_contents)
    
    # Count the number of times each character appears in the text
    char_counts = count_characters(file_contents)
    print("Character counts:", char_counts)

# Call the main function to execute the program
if __name__ == "__main__":
    main()