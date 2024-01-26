def main():
  path = "books/frankenstein.txt"
  text = get_book_text(path)
  letters = letter_count(text)
  list_of_counts = list(letters.items())
  list_of_counts.sort(key = lambda x: x[1], reverse=True)

  print(f"{word_count(text)} words found in the document")

  for count in list_of_counts:
    if count[0].isalpha():
      print(f"The '{count[0]}' was found {count[1]} times")

def get_book_text(path):
  with open(path) as f:
    return f.read()

def word_count(text):
  words = text.split()
  return len(words)
  
def letter_count(text):
  letter_count_dict = {}
  text = text.lower() # This assigns the .lower result back to text.
  for char in text:
    if char not in letter_count_dict:
      letter_count_dict[char] = 1 # if the character isnt already in the dict, add it and set its count to 1.
    else:
      letter_count_dict[char] += 1 # if the character is already in the dict, increase its count by 1.
  return letter_count_dict

if __name__ == "__main__":
  main()