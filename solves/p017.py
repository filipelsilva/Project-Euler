import inflect

string = ""

p = inflect.engine()

for i in range(1, 1001):
    string += str(p.number_to_words(i))

string = string.replace(" ", "").replace("-", "")
print(len(string))
