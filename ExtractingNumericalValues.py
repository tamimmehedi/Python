text = "I a 30 years old man"
import re
numbers = re.findall('\d+', text)
print(numbers)

\\\\\\\\\\\\\\\\\\\\\\\\

text = "I a 30 years old man"
import re
numbers = re.findall('\d', text)
print(numbers)
