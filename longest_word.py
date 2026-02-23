sent=input("Enter a sentence: ")

words=sent.split()
longest_word=""

for word in words:
    if len(word)>len(longest_word):
        longest_word=word
        
print("LOngest word:",longest_word)