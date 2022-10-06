# Title Case

def title_case(title, minor_words=''):
    result = ""
    MinorWords = ""
    for let in minor_words.split(" "):
        let = let.lower()
        MinorWords += let + " "
    for leter in title.split(" "):
        leter = leter.lower()
        if leter in MinorWords:
            result += leter + " "
        else:
            leter = leter.title()
            result += leter + " "
    result = result[0:len(result)-1]
    first = result[0]
    return result.replace(first, first.upper(), 1)



print(title_case('THE WIND IN THE WILLOWS', 'The In'))
