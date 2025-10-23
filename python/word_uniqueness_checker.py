#doesn't return the correct number of word. If we wanted to do so we would have to import libraries or use a for loop.

with open("words.txt","r") as w:
    words = w.read().split()
    print(len(words))
