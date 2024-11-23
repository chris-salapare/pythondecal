#2.1
pickleball = list(range(20))
#Didn't encounter an error, but i indexed wrong
#It should've been pickleball = list(range(20)) to get a list of 0-20
print(pickleball)

#2.2

def squareList(input_list):
    return [x ** 2 for x in input_list]

basketball = squareList(pickleball)

print(basketball)

#2.3

def first_fifteen_elements(input_list):
    return input_list[:15]

basketball = squareList(pickleball)

first15 = first_fifteen_elements(basketball)

print(first15)

#2.4


def every_fifth_element(input_list):
    
    return input_list[::5]
#Syntax error on line 32
#Fixed it by changing from parentheses to []
#Example input_list[::5]

anotherNameYouWant = squareList(pickleball)

fifth_elements = every_fifth_element(basketball)

print(fifth_elements)

#2.5
def fancy_function(input_list):
   
    return input_list[-30:][::-3]

basketball = squareList(pickleball)

result = fancy_function(basketball)
    
print(result)

#3

def create_2d_list():
    matrixthing = []  
    num = 1  
    
    for i in range(5):
        row = []  
        for j in range(5):
            row.append(num)  
            num += 1  
        matrixthing.append(row) 
    
    return matrixthing

matrixthing = create_2d_list()

print(matrixthing)

#3.2

def modified_2d_list(matrixthing):
    for i in range(len(matrixthing)):  
        for j in range(len(matrixthing[i])):  
            if matrixthing[i][j] % 3 == 0:  
                matrixthing[i][j] = "?"  
    return matrixthing

matrixthing = create_2d_list()

modified_matrixthing = modified_2d_list(matrixthing)

print(modified_matrixthing)

#3.3
def sum_non_question_elements(matrixthing):
    total_sum = 0  
    for row in matrixthing:  
        for element in row:
            if element != "?":  
                total_sum += element  
    return total_sum

matrixthing = create_2d_list()

new_matrixthing = modified_2d_list(matrixthing)

result = sum_non_question_elements(new_matrixthing)

print(result)