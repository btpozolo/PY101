#1 Error - yes index
numbers = [1, 2, 3]
numbers[6] = 5

#2
def ends_in_question(string):
    return string.endswith('!')
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

ends_in_question(str1)
ends_in_question(str2)

#3
famous_words = "seven years ago..."

new_string = 'Four score and ' + famous_words
new_string = f'Four score and {famous_words}'

#4
munsters_description = "the Munsters are CREEPY and Spooky."
print(munsters_description.lower().capitalize())
# => 'The munsters are creepy and spooky.'

#5
munsters_description = "The Munsters are creepy and spooky."
print(munsters_description.swapcase())

#6
str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

str1.find('Dino') >= 0
str2.find('Dino') >= 0

'Dino' in str2

#7
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append('Dino')
flintstones

#8
flintstones.extend(['Dino', 'Hoppy'])
flintstones

#9
advice = "Few things in life are as important as house training your pet dinosaur."
advice.partition('house')[0]

# Expected output:
# Few things in life are as important as

#10
advice = "Few things in life are as important as house training your pet dinosaur."
print(advice.replace('important', 'urgent'))
