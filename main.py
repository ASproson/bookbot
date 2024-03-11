def main ():
  file_contents = get_book_text('books/frankenstein.txt')
  word_count = count_num_of_words(file_contents)
  char_count = count_letters(file_contents)



  print("--- Begin report of books/frankenstein.txt ---")
  print(f"{word_count} words found in the document")
  for char_info in char_count:
    char = char_info["char"]
    count = char_info["count"]
    print(f"The '{char}' character was found {count} times")
  print("--- End report ---")


def get_book_text(path):
  with open(path) as f:
    return f.read()

def count_num_of_words(book):
  word_count = len(book.split())
  return word_count

def count_letters(text):
    char_count = {}
    characters = text.lower()
    for char in characters:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    
    char_list = []
    for char, count in char_count.items():
        char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=lambda x: x["count"])
    
    return char_list


main()