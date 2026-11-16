def comma_code(items):
    if len(items) == 0:
        return ''
    if len(items) == 1:
        return str(items[0])
    return ', '.join(str(item) for item in items[:-1]) + ', and ' + str(items[-1])


spam = ['apples', 'bananas', 'tofu', 'cats']
print(comma_code(spam))        # apples, bananas, tofu, and cats
print(comma_code(['one']))     # one
print(comma_code(['a', 'b']))  # a, and b
print(repr(comma_code([])))    # ''
