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