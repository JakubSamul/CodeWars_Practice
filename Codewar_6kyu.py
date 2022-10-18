# # Title Case

# def title_case(title, minor_words=''):
#     result = ""
#     MinorWords = ""
#     for let in minor_words.split(" "):
#         let = let.lower()
#         MinorWords += let + " "
#     for leter in title.split(" "):
#         leter = leter.lower()
#         if leter in MinorWords:
#             result += leter + " "
#         else:
#             leter = leter.title()
#             result += leter + " "
#     result = result[0:len(result)-1]
#     first = result[0] if result else ""
#     return result.replace(first, first.upper(), 1)



# print(title_case('First a of in', ''))

# Simple Encryption #1 - Alternating Split

def encrypt(encrypted_text, n):
    for i in str(n):
        step1 = []
        step2 = []
        for step in range(1,len(encrypted_text)+1,2):
            step1.append(encrypted_text[step])
        for step in range(0,len(encrypted_text)+1,2):
            step2 += encrypted_text[step]
    print(step1)

print(encrypt("This is a test!", 1))


