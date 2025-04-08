from replacer import replacer_in_text, replacer_in_file, replacer_in_directory
        
def check_user_choice(user_choice):
    match user_choice:
            case '1':
                text = input("Enter your text: ")
                old_word = input("Enter the word to replace: ")
                new_word = input("Enter the new word: ")
                if text == 'q' or old_word == new_word:
                    print("Nothing has changed")
                    return None
                replacer_in_text(text, old_word, new_word)
            case '2':
                path = input("Enter the file path: ")
                old_word = input("Enter the word to replace: ")
                new_word = input("Enter the new word: ")
                if path == 'q' or old_word == new_word:
                    print("Nothing has changed")
                    return
                replacer_in_file(path, old_word, new_word)
            case '3':
                path = input("Enter the directory path: ")
                old_word = input("Enter the word to replace: ")
                new_word = input("Enter the new word: ")
                if path == 'q' or old_word == new_word:
                    print("Nothing has changed")
                    return
                replacer_in_directory(path, old_word, new_word)
    
def main():
    user_choice = ''
    while user_choice.lower() != 'q':
        print("1. Text")
        print("2. File")
        print("3. Directory")
        print("q. exit")
        user_choice = input("Choose!: ")
        check_user_choice(user_choice)

if __name__ == "__main__":
    main()
