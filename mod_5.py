import re

#region Ex. 1
print('Ex. 1')
s1 = 'Alex\nKdfe23\t\f\v.\r'
s2 = 'Al\nKdfe23\t\v.\r'

def real_len(text: str) -> int:
    result = re.sub(r"\s", '', text)
    return len(result)

#endregion

#region Ex. 2
print('Ex. 2')
articles_dict = [
    {
        "title": "Endless ocean waters.",
        "author": "Jhon Stark",
        "year": 2019,
    },
    {
        "title": "Oceans of other planets are full of silver",
        "author": "Artur Clark",
        "year": 2020,
    },
    {
        "title": "An ocean that cannot be crossed.",
        "author": "Silver Name",
        "year": 2021,
    },
    {
        "title": "The ocean that you love.",
        "author": "Golden Gun",
        "year": 2021,
    },
]


def find_articles(key, letter_case=False):
    is_in_dict = 0
    new_dict = []
    if letter_case:
        for d in articles_dict:
          for v in d.values():
              val = str(v)
              is_in_dict = val.find(key)
              if is_in_dict != -1:
                  print(val)
                  break
          if is_in_dict != -1:
              new_dict.append(d)
    else:
        for d in articles_dict:
            for v in d.values():
                val = str(v).lower()
                is_in_dict = val.find(key.lower())
                if is_in_dict != -1:
                    break
            if is_in_dict != -1:
              new_dict.append(d)
    return new_dict
# search_text = input("Enter your search: ")
# print(find_articles('The', letter_case=True))
#endregion

#region Ex. 3
print('Ex. 3')
def sanitize_phone_number(phone):
    san_phone = phone.strip()
    san_phone = re.sub(r"[()\-+\s]", "", san_phone)

    return san_phone

# print(sanitize_phone_number("38050 111 22 11   "))
#endregion

#region Ex. 4
print('Ex. 4')
def is_check_name(fullname, first_name) -> bool:
    return fullname.startswith(first_name)
#endregion

#region Ex. 5
print('Ex. 5')
def get_phone_numbers_for_countries(list_phones: list) -> dict:
    sorted_phones = {
                      "UA": [],
                      "JP": [],
                      "TW": [],
                      "SG": []
                    }
    for p in list_phones:
        p = sanitize_phone_number(p)
        if p.startswith("81"):
            sorted_phones["JP"].append(p)
        elif p.startswith("65"):
            sorted_phones["SG"].append(p)
        elif p.startswith("886"):
            sorted_phones["TW"].append(p)
        else:
            sorted_phones["UA"].append(p)
    return sorted_phones

# print(get_phone_numbers_for_countries(phones))
#endregion

#region Ex. 6
print('Ex. 6')

def is_spam_words(text, spam_words, space_around=False) -> bool:
    has_spam = False
    if space_around:
        text = text.split()
        if len(text) == 1:
            has_spam = False
        else:
            for spam in spam_words:
                for word in text:
                    has_spam = True if spam in word else False
    else:
        for s in spam_words:
            has_spam = True if s in text else False
    return has_spam


print(is_spam_words("Молох", ["лох"]))  # True
print(is_spam_words("Молох", ["лох"], True))  # False
print(is_spam_words("Ты лох.", ["лох"]))  # True
print(is_spam_words("Ты лох.", ["лох"], True))  # True
#endregion

#region Ex. 7
print('Ex. 7')
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")

TRANS = {}
    
    
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def translate(name):
    return name.translate(TRANS)

print(translate("Дмитрий Коробов"))  # Dmitrij Korobov
print(translate("Александр Иванович"))  # Aleksandr Ivanovich
#endregion

#region Ex. 8
print('Ex. 8')
grades = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}

def formatted_grades(students):
    result = []
    for s, g in students.items():
        result.append("{:<10}|{:^5}|{:^5}".format(s, g, grades[g]))
    for i in range(0, len(result)):
        result[i] = "{:>4}|".format(i+1) + result[i]
    return result
students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
for el in formatted_grades(students):
    print(el)
#endregion

#region Ex. 9
print('Ex. 9')
def formatted_numbers():
    result = ["|{:^10}|{:^10}|{:^10}|".format("decimal", "hex", "binary")]
    for i in range(16):
        result.append("|{0:<10d}|{0:^10x}|{0:>10b}|".format(i))
    return result

for i in formatted_numbers():
    print(i)

#endregion

#region Ex. 10
print('Ex. 10')
def find_word(text, word) -> dict:
    res_dict = {
        'result': False,
        'first_index': None,
        'last_index': None,
        'search_string': '',
        'string': ''
    }
    search = re.search(word, text)
    if search:
        search_span = search.span()
        res_dict["result"] = True
        res_dict["first_index"] = search_span[0]
        res_dict["last_index"] = search_span[1]
        res_dict["search_string"] = search.group()
        res_dict["string"] = search.string
    else:
        res_dict["search_string"] = word
        res_dict["string"] =  text

    return res_dict

# print(find_word(
#     "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.",
#     "Python"))
# print(find_word(
#     "Guido van Rossum began working on  in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as 0.9.0.",
#     "Python"))
#endregion

#region Ex. 11
print("Ex. 11")
def find_all_words(text, word):
    # result = re.findall(word, text, re.I)
    return re.findall(word, text, re.I)
text = "Ut vel lacinia ipsum, vitae rhoncus nisi. Proin eros mi, ultricies eu convallis ut, egestas vel nisl. Aliquam orci eSt, ullamcorper eget risus eget, dapibus mattis orci. Duis pharetra consectetur auctor. Praesent viverra auctor lacus, ut sagittis nulla lacinia vitae. Curabitur faucibus diam non nisi viverra tincidunt. Quisque facilisis porttitor ante et mollis. Proin rutrum leo eget orci condimentum, ac cursus nibh lobortis. Fusce id nulla ultricies, tempus turpis vel, ornare Est."
# print(find_all_words(text, "est"))
#endregion

#region Ex. 12
print("Ex. 12")
def replace_spam_words(text, spam_words):
    censored_text = text
    for s in spam_words:
        finded_spam = re.finditer(s, censored_text, re.IGNORECASE)
        if finded_spam:
            for f in finded_spam:
                replace = "*"*len(f.group())
                censored_text = re.sub(f.group(), replace, censored_text, re.IGNORECASE)
    return censored_text
text = "Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming PYTHOn language, and first released pYthoN it in 1991 as Python 0.9.0. pythOn"
spam = ['began', 'Python']
# print(replace_spam_words(text, spam))
#endregion

#region Ex. 13
print("Ex. 13")
def find_all_emails(text):
    result = re.findall(r"[A-z.]+\w+@[A-z]+\.[A-z]{2,}", text)
    return result

emails = "Ima.Fool@iana.org Ima.Fool@iana.o 1Fool@iana.org first_last@iana.org first.middle.last@iana.or a@test.com abc111@test.com.net"
# print(find_all_emails(emails))
#endregion

#region Ex. 14
print("Ex. 14")
def find_all_phones(text):
    return re.findall(r"\+380\(\d{2}\)\d{3}\-\d{1}\-\d{3}|\+380\(\d{2}\)\d{3}\-\d{2}\-\d{2}", text)
text = 'Irma +380(67)777-7-771 second +380(67)777-77-77 aloha a@test.com abc111@test.com.net +380(67)111-777-777+380(67)777-77-787'
print(find_all_phones(text))
#endregion

#region Ex. 15
print("Ex. 15")
def find_all_links(text):
    result = []
    iterator = re.finditer(r"http://[www.]?[A-z]+\.\w{2,3}|https://[www.]?([A-z]+\.)+\w{2,3}", text)
    for match in iterator:
        result.append(match.group())
    return result

text = "The main search site in the world is https://www.google.com The main social network for people in the world is https://www.facebook.com But programmers have their own social network http://github.com There they share their code. some url to check https://www..facebook.com www.facebook.com"
print(find_all_links(text))
#endregion