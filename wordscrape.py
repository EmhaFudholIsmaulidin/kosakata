import requests

response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt")
words = response.text.splitlines()

five_letter_words = [word for word in words if len(word) == 5]

with open("fw.js", "w") as file:
    file.write("const fiveLetterWords = [\n")
    file.write(",\n".join(f'"{word}"' for word in five_letter_words))
    file.write("\n];")