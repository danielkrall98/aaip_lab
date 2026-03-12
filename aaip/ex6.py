import sys

# Count Number of Words in File
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            text = file.read()
            words = text.split()
            print(f"There are {len(words)} Words in this File.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Count Number of Lines in File
def count_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            print(f"There are {len(lines)} Lines in this File.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

# Search for Word in File and Print Lines containing the Word
def search_word(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            found_lines = [line.strip() for line in lines if word.lower() in line.lower()]
            if found_lines:
                print(f"The following lines contain '{word}':")
                for line in found_lines:
                    print(line)
            else:
                print(f"No lines found containing '{word}'.")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python ex6.py <filename> <operation> [<word>]")
        print("Operations: count_words, count_lines, search_word")
        sys.exit(1)

    filename = sys.argv[1]
    operation = sys.argv[2]

    if operation == "count_words":
        count_words(filename)
    elif operation == "count_lines":
        count_lines(filename)
    elif operation == "search_word":
        if len(sys.argv) < 4:
            print("Error: Please provide a word to search for.")
            print("Usage: python ex6.py <filename> search_word <word>")
            sys.exit(1)
        word = sys.argv[3]
        search_word(filename, word)
    else:
        print(f"Error: Unknown operation '{operation}'.")
        print("Operations: count_words, count_lines, search_word")

if __name__ == "__main__":
    main()