# Python String Manipulation Exercises

# 1. Concatenate strings to 'Thirty Days Of Python'
result1 = 'Thirty' + ' ' + 'Days' + ' ' + 'Of' + ' ' + 'Python'
print("1.", result1)

# 2. Concatenate strings to 'Coding For All'
result2 = 'Coding' + ' ' + 'For' + ' ' + 'All'
print("2.", result2)

# 3. Declare variable company
company = "Coding For All"

# 4. Print the variable company
print("4.", company)

# 5. Print the length of company string
print("5.", len(company))

# 6. Change to uppercase
print("6.", company.upper())

# 7. Change to lowercase
print("7.", company.lower())

# 8. Use capitalize(), title(), swapcase() methods
print("8a. capitalize():", company.capitalize())
print("8b. title():", company.title())
print("8c. swapcase():", company.swapcase())

# 9. Cut out the first word (slice)
first_word_removed = company[7:]  # Skip "Coding "
print("9.", first_word_removed)

# 10. Check if string contains "Coding" using different methods
print("10a. Using index:", company.index("Coding"))
print("10b. Using find:", company.find("Coding"))
print("10c. Using 'in' operator:", "Coding" in company)

# 11. Replace "Coding" with "Python"
replaced = company.replace("Coding", "Python")
print("11.", replaced)

# 12. Change "Python for Everyone" to "Python for All"
original = "Python for Everyone"
changed = original.replace("Everyone", "All")
print("12.", changed)

# 13. Split 'Coding For All' using space
split_result = company.split()
print("13.", split_result)

# 14. Split at comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = companies.split(", ")
print("14.", split_companies)

# 15. Character at index 0
print("15.", company[0])

# 16. Last index of the string
print("16.", len(company) - 1)

# 17. Character at index 10
print("17.", company[10])

# 18. Acronym for 'Python For Everyone'
pfe = "Python For Everyone"
acronym_pfe = ''.join([word[0] for word in pfe.split()])
print("18.", acronym_pfe)

# 19. Acronym for 'Coding For All'
acronym_cfa = ''.join([word[0] for word in company.split()])
print("19.", acronym_cfa)

# 20. Position of first 'C' in 'Coding For All'
print("20.", company.index('C'))

# 21. Position of first 'F' in 'Coding For All'
print("21.", company.index('F'))

# 22. Position of last 'l' in 'Coding For All People'
sentence_people = "Coding For All People"
print("22.", sentence_people.rfind('l'))

# 23. Position of first 'because' in the sentence
sentence = 'You cannot end a sentence with because because because is a conjunction'
print("23.", sentence.find('because'))

# 24. Position of last 'because' using rindex
print("24.", sentence.rindex('because'))

# 25. Slice out 'because because because'
start_pos = sentence.find('because because because')
end_pos = start_pos + len('because because because')
phrase_removed = sentence[:start_pos] + sentence[end_pos:]
print("25.", phrase_removed)

# 26. Position of first 'because' (same as 23)
print("26.", sentence.find('because'))

# 27. Slice out 'because because because' (same as 25)
start_pos = sentence.find('because because because')
end_pos = start_pos + len('because because because')
phrase_removed2 = sentence[:start_pos] + sentence[end_pos:]
print("27.", phrase_removed2)

# 28. Check if 'Coding For All' starts with 'Coding'
print("28.", company.startswith('Coding'))

# 29. Check if 'Coding For All' ends with 'coding'
print("29.", company.endswith('coding'))

# 30. Remove trailing spaces
spaced_string = '   Coding For All      '
print("30.", spaced_string.strip())

# 31. Check isidentifier()
print("31a. '30DaysOfPython'.isidentifier():", '30DaysOfPython'.isidentifier())
print("31b. 'thirty_days_of_python'.isidentifier():", 'thirty_days_of_python'.isidentifier())

# 32. Join list with hash and space
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_libraries = '# '.join(libraries)
print("32.", joined_libraries)

# 33. Use newline escape sequence
print("33.")
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Use tab escape sequence
print("34.")
print("Name\t\tAge\tCountry\t\tCity")
print("Asabeneh\t250\tFinland\t\tHelsinki")

# 35. String formatting for circle area
radius = 10
area = 3.14 * radius ** 2
print("35.")
print(f"El area del circulo con radio {radius} es {int(area)} metros cuadrados.")

# 36. Mathematical operations formatting
a, b = 8, 6
print("36.")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")