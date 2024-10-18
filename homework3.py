#1 Oski stole your power
def exponent(x,y):
    if y < 0:
        x =1/x
        y = -y

    result = 1
    for _ in range(y):
        result*= x 
    return result
print(exponent(2,3))

#2 What Should I Wear?
def min_max_temperatures(temps):
    if not temps:
        return None 
    return (min(temps), max(temps))
temperatures = [15, 14, 17, 20, 23, 28, 20]
result = min_max_temperatures(temperatures)
print(result)

#3 Check if its the Weekend
def is_weekend(day):
    return day == 6 or day == 7

print(is_weekend(5))
print(is_weekend(6))
print(is_weekend(7))

#4 Fuel Efficiency Calculator
def fuel_efficiency(distance,fuel):
    if fuel <= 0:
        return None
    return distance / fuel
distance = 70 #miles
fuel = 21.5 #gallons
fuel_efficiency(distance,fuel)
print(fuel_efficiency)

#5 Secret Code 
def decode_numbers(n):
    if n < 10:
        return n  
    
    last_digit = n % 10  
    remaining_number = n // 10  
    
    num_digits = 0
    temp = remaining_number
    while temp > 0:
        temp //= 10
        num_digits += 1

    
    new_number = last_digit * (10 ** num_digits) + remaining_number
    
    return new_number


n = 12345
result = decode_numbers(n)
print(result)
    
#6 Min and Max but with Loops!
def find_min_with_for_loop(nums):
    if not nums:
        return None  
    
    min_value = nums[0]  
    for num in nums:
        if num < min_value:
            min_value = num  
    return min_value

def find_max_with_for_loop(nums):
    if not nums:
        return None  
    
    max_value = nums[0]  
    for num in nums:
        if num > max_value:
            max_value = num  
    return max_value


nums = [2024, 98, 131, 2, 3, 72]
print(find_min_with_for_loop(nums))  
print(find_max_with_for_loop(nums))  

#7 Counting Vowels
def vowel_and_consonant_count(text):
    vowels = "aeiouAEIOU"  
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():  
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return (vowel_count, consonant_count)

text = "UC Berkeley, founded in 1868!"
result = vowel_and_consonant_count(text)
print(result)  

#8 Calculate Digital Root
def digital_root(num):
    
    num = abs(num)
    total_sum = 0
    
    while num > 0:
        total_sum += num % 10  
        num //= 10  
    
    return total_sum


num = 2468
result = digital_root(num)
print(result)
