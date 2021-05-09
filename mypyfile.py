book1 = set(open("book1.txt","r",encoding='utf-8').read().split())

book2 = set(open("book2.txt","r",encoding='utf-8').read().split())

punctuation = '''!()-[]{};:'"\, <>./?@#$%^&*_~'''

for word in book1:
    for char in word:
        if char in punctuation:
            word = word.replace(char, "")
            
for word in book2:
    for char in word:
        if char in punctuation:
            word = word.replace(char, "")          

Result = book1.intersection(book2)

print(Result)