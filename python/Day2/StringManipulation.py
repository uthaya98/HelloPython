single_quote = 'Hello, World!'
double_quote = "Hello, World!"
triple_quote = """Multi-line 
String"""

text = "Python Programming"
#print(text[0: 5])
#print(text[:6])
#print(text[6:]) 
print("==============================")
print(text[-6: -1][::-1])
print(text[-1: -6])
print(text[-6: -1])
print(text[-1: -6: -2])
print(text[0])

name = " bob the builder "

print(name.strip())
print(name.lower())
print(name.upper())
print(name.replace("b", "B"))
print(name.split(" "))
print(name.replace(" ", "").upper())

sentence = "Python is powerful programming language. It's easy to learn and versatile."

wordArr = sentence.replace(".", "").split(" ")

CharacterCheck = sentence.replace(".", "").replace(" ", "")

sentenceArr = sentence.split(".")

charactercount = len(CharacterCheck)

wordcount = len(wordArr)
print("Word Count:", wordcount)
print("Character Count:", charactercount)
print("Sentences count:", sentenceArr)

