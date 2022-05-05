
import string

def printer_error(s):
    chars = string.ascii_lowercase
    good = list(chars)[chars.find('a'):chars.find('m')+1]
    count = 0

    for c in s:
        if c not in good:
            count += 1
    return str(count) + "/" + str(len(s))

print(printer_error("aaabbbmmmddd"))
print(printer_error("aaabbzzzzzbmmmyydddx"))


