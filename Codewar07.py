# def z(n):
# return [x for x in range(2, n + 1) if len([i for i in range(2, x) if x % i == 0]) == 0]


# print(z(300))


# def qsort(l):
# return l if len(l) <= 1 else qsort([x for x in l[1:] if x < l[0]]) + [l[0]] + qsort([x for x in l[1:] if x >= l[0]])


# print(qsort([1, 2, 5, 7, 8, 2, 6, 8]))

# def count_by(x, n):
#    return lambda x, n: x * range(0,n)

# print(count_by(1,10))

# def draw_stairs(n):
#     i = "I"
#     a = 1
#     while a <= n:
#         print(i)
#         i += " "
#         a += 1


# print(draw_stairs(3))


# result = []
# for i in range(10):
#     result.append(" " * i + "I")
# print(result)
# wynik = "\n".join(result)
# print(wynik)

# import itertools

# lista = [10, 2, 1]

# lista.sort(reverse=True)

# result = []
# for a, b in itertools.zip_longest(lista, lista[1:]):
#     if b is not None:
#         result.append(a-b)
# print(sum(result))

# def like_or_dislike(lst):
#     if len(lst) == 0:
#         return "Nothing"
#     if len(lst) == 1:
#         return lst[0]
#     if len(lst) == 2:
#         return "Nothing" if lst[-1] == lst[-2] else lst[-1]
#     if len(lst) == 3:
#         if lst[-1] == "Like" and lst[-2] == "Like":
#             return "Like"
#         elif lst[-1] == "Dislike" and lst[-2] == "Dislike":
#             return "Nothing"
#         elif lst[-1] == "Dislike":
#             return "Dislike"
#     if len(lst) > 3:
#         if lst[-1] == lst[-2]:
#             return "Nothing"
#         if lst[-1] == "Dislike":
#             return "Dislike"
#         elif lst[-1] == "Like":
#             return "Like"

# def words_to_marks(s):

# def high_and_low(numbers):
#     if numbers:
#         numbers = numbers.split(" ")
#         h = numbers[0]
#         l = numbers[0]
#         for num in numbers:
#             if int(num) > int(h):
#                 h = num
#             if int(num) < int(l):
#                 l = num
#         return h + " " + l


# print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
# def is_triangle(a, b, c):
#     t = [a, b, c]
#     l = len(t)
#     for i in range(l):
#         for j in range(0, l-i-1):
#             if t[j] > t[j+1]:
#                 t[j], t[j+1] = t[j+1], t[j]
#     if t[2] >= t[1] + t[0]:
#         return True
#     else:
#         return False


# print(is_triangle(5, 9, 1))


# a = "hello case"
# b = a.split()
# text = []
# for i in b:
#     c = i.capitalize()
#     text.extend(c)

# result = "".join(text)
# print(result)

# print(divmod(10, 2))
# print(divmod(10, 3))


# def solution(A):
#     if len(A) == 1:
#         return A[0]
#     A.sort()
#     for i in range(len(A)):
#         if i == 0:
#             if A[i] != A[i+1]:
#                 return A[i]
#         if i == len(A)-1:
#             if A[i] != A[i-1]:
#                 return A[i]
#         if i != 0 and i < (len(A)-1):
#             if A[i] != A[i-1] and A[i] != A[i+1]:
#                 return A[i]


# print(solution([3, 0.9, 3, 3]))

# def add_binary(a, b):
#     return "{0:b}".format(a + b)


# print(add_binary(1, 4))

# def is_pangram(s):
#     alpha1 = list(map(lambda x: x.lower(), list(map(chr, range(97, 123)))))
#     alpha2 = list(map(lambda x: x.upper(), list(map(chr, range(97, 123)))))
#     alphabet = alpha1 + alpha2
#     for i in s:
#         if alphabet is i:
#     return True


# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))

# def array_diff(a, b):
#     for i in a:
#         if i in b:
#             a.remove(i)
#     return a


# print(array_diff([1, 2, 2], [2]))

# def delete_nth(order, max_e):
#     size_numbers = {}
#     result = []
#     for numbers in order:
#         if numbers not in size_numbers:
#             size_numbers[numbers] = 0
#         else:
#             size_numbers[numbers] += 1
#         if size_numbers[numbers] < max_e:
#             result.append(numbers)
#     return result


# print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3))

# def nb_year(p0, percent, aug, p):
#     i = 0
#     while True:
#         po = p0 + (p0 * percent / 100) + aug
#         p0 = po
#         i += 1
#         if po >= p:
#             return i


# def number(lines):
#     my_lines = []
#     number = 1
#     for i in lines:
#         my_lines = my_lines + [str(number)+": "+str(i)]
#         number += 1
#     return my_lines


# print(number(["a", "b", "c"]))

# def digitize(n):
#     for s in str(n)[::-1]:
#         return int(s)


# print(digitize(35231))


# def duplicate_count(text):
#     new_text = text.lower()

#     count = 0
#     dictionary = {}

#     for i in range(0, len(new_text)):
#         dictionary[new_text[i]] = 0

#     for key in dictionary:
#         for i in range(0, len(new_text)):
#             if(key == new_text[i]):
#                 dictionary[key] = dictionary[key] + 1

#     for key in dictionary:
#         if(dictionary[key] > 1):
#             count = count + 1

#     print(dictionary)
#     return count


# print(duplicate_count("abcbaddea"))

def two_sum(numbers, target):
    result = []
    for i, x in enumerate(numbers):
        for j, y in enumerate(numbers):
            summ = x + y
            if summ == target and i != j:
                result += i, j
                return result


print(two_sum([1, 5, 3], 4))
