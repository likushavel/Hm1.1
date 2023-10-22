def get_count_symbols(s):
    temp = "aeiou"
    counter = 0
    for i in temp:
        counter += s.lower().count(i)
    return counter


s = "I like to cook, draw and play video games"
print(get_count_symbols(s))
