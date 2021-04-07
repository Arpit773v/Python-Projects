# pip install translate

from translate import Translator
lang = Translator(from_lang="English", to_lang="Hindi")

words = input("Write your text here, to convert it to Hindi: ")

result = lang.translate(words)
print(result)