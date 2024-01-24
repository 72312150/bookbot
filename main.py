def main():
  path = "books/frankenstein.txt"
  text = get_book_text(path)
  letters = letter_count(text)
  print(f"{letters}")

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