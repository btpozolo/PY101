def greetings(lst, dct):
    name = " ".join(lst)
    title = dct['title']
    occupation = dct['occupation']

    return f"Hello, {name}! Nice to have a {title} {occupation} around."

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)