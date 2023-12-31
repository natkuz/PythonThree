# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

text = "С точки зрения научной систематики, домашняя кошка - млекопитающее семейства кошачьих отряда хищных. " \
       "Одни исследователи рассматривают домашнюю кошку как подвид дикой кошки, другие - как отдельный биологический вид." \
       "Являясь одиночным охотником на грызунов и других мелких животных, кошка - социальное животное, " \
       "использующее для общения широкий диапазон звуковых сигналов, а также феромоны и движения тела. " \
       "В настоящее время в мире насчитывается около шестиста млн домашних кошек, выведено около двухсот пород, " \
       "от длинношёрстных (персидская кошка) до лишённых шерсти (сфинксы), признанных и зарегистрированных " \
       "различными фелинологическими организациями. На протяжении десяти тысяч лет кошки ценятся человеком, " \
       "в том числе за способность охотиться на грызунов и других домашних вредителей, " \
       "а также за умение забавлять и утешать детей"

text = text.replace("-", "").replace(",", "").replace(".", "").replace("(", "").replace(")", "").replace("  ", " ").lower().split()

words = {}
for i in text:
    words[i] = text.count(i)

sorted_words = dict(sorted(words.items(), key=lambda item: item[1]))
rev_sorted_words = dict(reversed(sorted_words.items()))

COUNT = 10
for key, value in list(rev_sorted_words.items())[:COUNT]:
    print(f'Слово "{key}" встречается {value} раз(a)')
