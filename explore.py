def rot13(txt):
  alpha = "abcdefghijklmnopqrstuvwxyz"
  other = "nopqrstuvwxyzabcdefghijklm"

  result = ""
  for letter in txt:
    is_upper = letter.isupper()
    letter = letter.lower()
    if letter in alpha:
      index = alpha.index(letter)
      new_letter = other[index]
      if is_upper:
        new_letter = new_letter.upper()
      result += new_letter
  return result

word_exists = {}
rot_words = []

words = open("twl3.txt").readlines()
for word in words:
  word = word.strip()
  word_exists[word] = True

for word in words:
  word = word.strip()
  rotted = rot13(word)
  if rotted in word_exists:
    rot_words.append(word + "," + rotted)

for word in rot_words:
  print(word)

