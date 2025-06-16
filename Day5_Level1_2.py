# Python List Manipulation Exercises

# 1. Declare an empty list
empty_list = []
print("1. Empty list:", empty_list)

# 2. Declare a list with more than 5 items
fruits = ['apple', 'banana', 'orange', 'grape', 'mango', 'pineapple', 'strawberry']
print("2. List with more than 5 items:", fruits)

# 3. Find the length of your list
print("3. Length of fruits list:", len(fruits))

# 4. Get first, middle, and last item
first_item = fruits[0]
middle_item = fruits[len(fruits)//2]
last_item = fruits[-1]
print("4a. First item:", first_item)
print("4b. Middle item:", middle_item)
print("4c. Last item:", last_item)

# 5. Declare mixed_data_types list
mixed_data_types = ['John Doe', 25, 5.9, 'Single', '123 Main St']
print("5. Mixed data types:", mixed_data_types)

# 6. Declare it_companies list
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("6. IT companies:", it_companies)

# 7. Print the list
print("7. IT companies list:", it_companies)

# 8. Print number of companies
print("8. Number of companies:", len(it_companies))

# 9. Print first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[len(it_companies)//2]
last_company = it_companies[-1]
print("9a. First company:", first_company)
print("9b. Middle company:", middle_company)
print("9c. Last company:", last_company)

# 10. Modify one company and print
it_companies[0] = 'Meta'  # Changed Facebook to Meta
print("10. After modifying first company:", it_companies)

# Reset for next exercises
it_companies[0] = 'Facebook'

# 11. Add an IT company
it_companies.append('Tesla')
print("11. After adding Tesla:", it_companies)

# 12. Insert company in the middle
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Netflix')
print("12. After inserting Netflix in middle:", it_companies)

# 13. Change one company to uppercase (excluding IBM)
it_companies[0] = it_companies[0].upper()  # Facebook to FACEBOOK
print("13. After changing Facebook to uppercase:", it_companies)

# 14. Join companies with '#; '
joined_companies = '#; '.join(it_companies)
print("14. Joined companies:", joined_companies)

# 15. Check if certain company exists
company_to_check = 'Google'
exists = company_to_check in it_companies
print(f"15. Does {company_to_check} exist in the list? {exists}")

# 16. Sort the list
it_companies_copy = it_companies.copy()  # Make a copy to preserve original
it_companies_copy.sort()
print("16. Sorted list:", it_companies_copy)

# 17. Reverse the list in descending order
it_companies_copy.reverse()
print("17. Reversed (descending) list:", it_companies_copy)

# Reset to original for remaining exercises
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 18. Slice out first 3 companies
first_three = it_companies[:3]
print("18. First 3 companies:", first_three)

# 19. Slice out last 3 companies
last_three = it_companies[-3:]
print("19. Last 3 companies:", last_three)

# 20. Slice out middle company/companies
total_companies = len(it_companies)
if total_companies % 2 == 1:
    # Odd number - get single middle element
    middle_companies = [it_companies[total_companies // 2]]
else:
    # Even number - get two middle elements
    mid = total_companies // 2
    middle_companies = it_companies[mid-1:mid+1]
print("20. Middle company/companies:", middle_companies)

# 21. Remove first IT company
it_companies_temp = it_companies.copy()
it_companies_temp.pop(0)
print("21. After removing first company:", it_companies_temp)

# 22. Remove middle company/companies
it_companies_temp = it_companies.copy()
total = len(it_companies_temp)
if total % 2 == 1:
    # Remove single middle element
    it_companies_temp.pop(total // 2)
else:
    # Remove two middle elements
    mid = total // 2
    it_companies_temp.pop(mid)  # Remove second middle element first
    it_companies_temp.pop(mid-1)  # Then remove first middle element
print("22. After removing middle company/companies:", it_companies_temp)

# 23. Remove last IT company
it_companies_temp = it_companies.copy()
it_companies_temp.pop()
print("23. After removing last company:", it_companies_temp)

# 24. Remove all IT companies
it_companies_temp = it_companies.copy()
it_companies_temp.clear()
print("24. After removing all companies:", it_companies_temp)

# 25. Destroy the IT companies list
del it_companies_temp
print("25. IT companies list destroyed (deleted)")

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack_technologies = front_end + back_end
print("26. Joined lists:", full_stack_technologies)

# 27. Copy joined list and insert Python and SQL after Redux
full_stack = full_stack_technologies.copy()
redux_index = full_stack.index('Redux')
full_stack.insert(redux_index + 1, 'Python')
full_stack.insert(redux_index + 2, 'SQL')
print("27. Full stack with Python and SQL added:", full_stack)

# Additional demonstrations of list methods
print("\n--- Additional List Method Demonstrations ---")

# Different ways to add elements
demo_list = [1, 2, 3]
print("Original demo list:", demo_list)

# append() vs extend() vs insert()
demo_list.append(4)
print("After append(4):", demo_list)

demo_list.extend([5, 6])
print("After extend([5, 6]):", demo_list)

demo_list.insert(0, 0)
print("After insert(0, 0):", demo_list)

# Different ways to remove elements
print("\nRemoval methods:")
demo_list2 = ['a', 'b', 'c', 'd', 'e']
print("Original:", demo_list2)

removed_item = demo_list2.pop(2)  # Remove and return item at index 2
print(f"After pop(2), removed '{removed_item}':", demo_list2)

demo_list2.remove('b')  # Remove first occurrence of 'b'
print("After remove('b'):", demo_list2)

del demo_list2[0]  # Delete item at index 0
print("After del demo_list2[0]:", demo_list2)

# List comprehension example
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print(f"\nList comprehension - squares of {numbers}:", squared)

#LEVEL 2

# 1. Student ages analysis
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print("Original ages:", ages)

# Sort the list and find min and max age
ages_sorted = sorted(ages)  # Create sorted copy
print("Sorted ages:", ages_sorted)
min_age = min(ages)
max_age = max(ages)
print(f"Min age: {min_age}")
print(f"Max age: {max_age}")

# Add min and max age again to the list
ages.append(min_age)
ages.append(max_age)
print("Ages after adding min and max again:", ages)

# Find the median age
ages_for_median = sorted(ages)
n = len(ages_for_median)
if n % 2 == 0:
    # Even number of elements - average of two middle elements
    median = (ages_for_median[n//2 - 1] + ages_for_median[n//2]) / 2
else:
    # Odd number of elements - middle element
    median = ages_for_median[n//2]
print(f"Median age: {median}")

# Find the average age
average_age = sum(ages) / len(ages)
print(f"Average age: {average_age:.2f}")

# Find the range of ages
age_range = max_age - min_age
print(f"Range of ages: {age_range}")

# Compare (min - average) and (max - average) using abs()
min_avg_diff = abs(min_age - average_age)
max_avg_diff = abs(max_age - average_age)
print(f"Absolute difference (min - average): {min_avg_diff:.2f}")
print(f"Absolute difference (max - average): {max_avg_diff:.2f}")

if min_avg_diff > max_avg_diff:
    print("Min age is further from average than max age")
elif max_avg_diff > min_avg_diff:
    print("Max age is further from average than min age")
else:
    print("Min and max ages are equally distant from average")

print("\n" + "="*50 + "\n")

# 2. Countries list operations
countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana',
'Brazil','Brunei','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad',
'Chile','China','Colombia','Comoros','Congo (Brazzaville)','Congo','Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark',
'Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia',
'Ethiopia','Fiji','Finland','France','Gabon','Gambia, The','Georgia','Germany','Ghana','Greece','Grenada','Guatemala','Guinea','Guinea-Bissau',
'Guyana','Haiti','Honduras','Hungary','Iceland','India','Indonesia','Iran','Iraq''Ireland','Israel','Italy','Jamaica','Japan','Jordan',
'Kazakhstan','Kenya','Kiribati','Korea, North','Korea, South','Kuwait','Kyrgyzstan','Laos','Latvia','Lebanon','Lesotho','Liberia','Libya',
'Liechtenstein','Lithuania','Luxembourg','Macedonia','Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Mauritania',
'Mauritius','Mexico','Micronesia','Moldova','Monaco','Mongolia','Morocco','Mozambique','Myanmar','Namibia','Nauru','Nepal','Netherlands',
'New Zealand','Nicaragua','Niger','Nigeria','Norway','Oman','Pakistan','Palau','Panama','Papua New Guinea','Paraguay','Peru','Philippines',
'Poland',
'Portugal',
'Qatar',
'Romania',
'Russia',
'Rwanda',
'Saint Kitts and Nevis',
'Saint Lucia',
'Saint Vincent',
'Samoa',
'San Marino',
'Sao Tome and Principe',
'Saudi Arabia',
'Senegal',
'Serbia and Montenegro',
'Seychelles',
'Sierra Leone',
'Singapore',
'Slovakia',
'Slovenia',
'Solomon Islands',
'Somalia',
'South Africa','Spain',
'Sri Lanka',
'Sudan',
'Suriname',
'Swaziland',
'Sweden',
'Switzerland',
'Syria',
'Taiwan',
'Tajikistan',
'Tanzania',
'Thailand',
'Togo',
'Tonga',
'Trinidad and Tobago',
'Tunisia','Turkey',
'Turkmenistan',
'Tuvalu',
'Uganda',
'Ukraine',
'United Arab Emirates',
'United Kingdom',
'United States',
'Uruguay',
'Uzbekistan',
'Vanuatu',
'Vatican City',
'Venezuela',
'Vietnam',
'Yemen',
'Zambia',
'Zimbabwe',
];

print("Countries list:", countries)
print(f"Number of countries: {len(countries)}")

# Find the middle country(ies)
n_countries = len(countries)
if n_countries % 2 == 0:
    # Even number - two middle countries
    mid1 = n_countries // 2 - 1
    mid2 = n_countries // 2
    middle_countries = [countries[mid1], countries[mid2]]
    print(f"Middle countries (even list): {middle_countries}")
else:
    # Odd number - one middle country
    mid = n_countries // 2
    middle_countries = [countries[mid]]
    print(f"Middle country (odd list): {middle_countries}")

# 3. Divide countries into two equal lists
if n_countries % 2 == 0:
    # Even number - divide equally
    mid_point = n_countries // 2
    first_half = countries[:mid_point]
    second_half = countries[mid_point:]
    print(f"First half ({len(first_half)} countries): {first_half}")
    print(f"Second half ({len(second_half)} countries): {second_half}")
else:
    # Odd number - first half gets one more
    mid_point = n_countries // 2 + 1
    first_half = countries[:mid_point]
    second_half = countries[mid_point:]
    print(f"First half ({len(first_half)} countries): {first_half}")
    print(f"Second half ({len(second_half)} countries): {second_half}")

print("\n" + "="*50 + "\n")

# 4. Unpack specific countries
country_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("Original country list:", country_list)

# Unpack first three and rest as scandic countries
first, second, third, *scandic_countries = country_list
print(f"First country: {first}")
print(f"Second country: {second}")
print(f"Third country: {third}")
print(f"Scandic countries: {scandic_countries}")