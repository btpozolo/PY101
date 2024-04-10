def penultimate(sentence):
    word_list = sentence.split()
    return (word_list[-2])

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

def middle(sentence):
    word_list = sentence.split()
    index = (len(word_list) // 2) + 1
    return (word_list[-index])

middle("Launch School is great!") 
middle("Launch School a is great!") 
middle("Launch School a is great! time") 
middle("Launch") 