__author__ = 'QingxiaoDong'

def findCrossDuplicate(string_input):
    for c in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
        first_occurrence = string_input.find(c)
        second_occurrence = string_input.find(c, first_occurrence + 1)
        if second_occurrence != -1:
            check_duplicate = {}
            for e in string_input[first_occurrence + 1:second_occurrence]:
                check_duplicate[e] = 1
            cache_list = []
            for n in string_input[second_occurrence + 1:]:
                if n == c:
                    for m in cache_list:
                        check_duplicate[m] = 1
                        cache_list = []
                else:
                    if n in check_duplicate:
                        return True
                    else:
                        cache_list.append(n)
    return False

#test case:
print findCrossDuplicate('')
print findCrossDuplicate('adddddfsgklhbzxcvnmmaqwerewererttayuioooppoib')
print findCrossDuplicate('asdfgawzxxvcmnkayuip')
s_input = input("Enter a string of characters (from 'a' to 'z'): ")
print findCrossDuplicate(s_input)