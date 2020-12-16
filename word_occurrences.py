word_count={}
sentence = input("Enter a sentence:")
words=sentences.split()
for word in words:
    word_count[word]=word_count.get(word,0)+1
    for word in words:
        print("{} : {}".format(word, word_count[word]))