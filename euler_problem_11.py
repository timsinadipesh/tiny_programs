st = """08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

"""
finding the greatest product of 4 adjacent numbers in any of the following direction:
horizontal, vertical, diagonal
"""

neg_inf = float('-inf')

# find the maximum product of 4 numbers in a given list
def max_prod_tu(arr):
    max_prod = neg_inf
    max_tu = ()

    for i in range(len(arr) - 3):
        nums = (arr[i], arr[i+1], arr[i+2], arr[i+3])
        prod = 1
        for each in nums:
            prod *= each
        if prod > max_prod:
            max_prod = prod
            max_tu = nums  
    
    return max_tu, max_prod


# make a list of list out of the string of numbers
def break2lists(st):
    st = st.split("\n")
    li = []
    for each in st:
        li.append([int(x) for x in each.split(" ")])
    return li


# search for the max product in the vertical axis
def left_right(li):
    max_prod = neg_inf
    maxtu = ()
    for each in li:
        new_tu, new_max = max_prod_tu(each)
        if new_max > max_prod:
            max_prod = new_max
            maxtu = new_tu 
    return maxtu, max_prod


# search for the max product in the vertical axis
def up_down(li):
    max_prod = neg_inf
    maxtu = ()
    for i in range(len(li)):
        newli = []
        for j in range(len(li) - 3):
            newli.append(li[j][i])
        new_tu, new_max = max_prod_tu(newli)
        if new_max > max_prod:
            max_prod = new_max
            maxtu = new_tu 
    return maxtu, max_prod


# search for the max product in the direction of the main diagonal
def main_diag(li):
    max_prod = neg_inf
    max_tu = ()
    # check for the products in both sides of the main diagonal
    for i in range(len(li) - 3):                                            
        li_left = []                                                        
        li_right = []                                                       
        # in each iteration of i: 0->17
        # make a list of left and right diagonals
        for j in range(len(li) - i):
            li_left.append(li[i+j][j])
            li_right.append(li[j][i+j])
        # find the max product of both lists
        left_tu = max_prod_tu(li_left)
        right_tu = max_prod_tu(li_right)
        # compare and find the max product among two lists
        if left_tu[1] > max_prod:
            max_tu = left_tu[0]
            max_prod = left_tu[1]
        elif right_tu[1] > max_prod:
            max_tu = right_tu[0]
            max_prod = right_tu[1]
    return max_tu, max_prod   
        

# search for the max product in the direction of the secondary diagonal
def second_diag(li):
    max_prod = neg_inf
    maxtu = ()
    len_li = len(li)
    # check for the products in both sides of the secondary diagonal
    for i in range(len_li - 3):                                            
        li_left = []                                                        
        li_right = []                                                       
        # in each iteration of i: 0->17
        # make a list of left and right diagonals
        for j in range(len_li - i):
            li_left.append(li[j][len_li - i - j - 1])
            li_right.append(li[i+j][len_li - j - 1])
        # find the max product of both lists
        left_tu = max_prod_tu(li_left)
        right_tu = max_prod_tu(li_right)
        # compare and find the max product among two lists
        if left_tu[1] > max_prod:
            max_tu = left_tu[0]
            max_prod = left_tu[1]
        elif right_tu[1] > max_prod:
            max_tu = right_tu[0]
            max_prod = right_tu[1]
    return max_tu, max_prod   


li = break2lists(st)
di = {}
di['leftright'] = left_right(li)
di['updown'] = up_down(li)
di['maindiag'] = main_diag(li)
di['seconddiag'] = second_diag(li)

val = neg_inf
for value in di.values():
    if value[1] > val:
        val = value[1]

print(val)
