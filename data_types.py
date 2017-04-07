 # -*- coding: utf-8 -*- 

"""
Data types determine whether an object can do something

7 important python data-types:

1) Booleans - True / False
2)  Ints - 1, 2, 3, 4, ...
3) Floats, 1.2, 1.3, 484.44, ... 
4) Str - "Hello World. I am a string. Humans can read me."
5) tuple - ("hello", "I", "am", "a, "tuple", "of", "strings")
6) list - ["hello", "I", "am", "a, "tuple", "of", "strings"]
7) dict - {"bat" : "a flying mammal", 3 : "the integer 3", }
"""

#String
name = "Manu Ginobili"

#Boolean
GOAT = True

#Int
number = 23

#float
career_points_per_36_minutes = 19.1

#tuple, immutable, cannot be changed
draft = ("1999 Draft", "San Antonio Spurs", "2nd round", "28th pick", "57th overall")

#list - immutable, can be changed
awards = ["2x All-Star", "4x NBA Champion", "2x All-NBA", "2002-03 All-Rookie"]

#dict
name_translations = {"Spanish": "Emanuel Ginóbili", "Chinese": "马努·吉诺比利", 
                     "Japanese": "エマニュエル・ジノビリ", "Korean": "마누 지노빌리",
                     "Persian": "مانو جینوبلی آمار"}
text = "\n\nIn Chinese, he is called " + name_translations["Chinese"] + ". "
text += "In Korean, " + name_translations["Korean"] + ", and in "
text += "English, " + name + ". " 
text += "But his mother named him the one and only " + name_translations["Spanish"]
text += ". Wearing the number " + str(number) + ", "
text += name + " was drafted in " + draft[0] + " by the " + draft[1]
text += " as the " + draft[3] + " in the " + draft[2] + ", " + draft[-1]
text += ". Throughout his career " + name + " has averaged "
text += str(career_points_per_36_minutes) + " points per 36 minutes. "

text += "He has been named "
text += ', '.join(awards[0:-1])
text += ", and " + awards[-1]
text += ".\n\n"

if GOAT:
    print(text)
