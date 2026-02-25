def get_numbers():
    user_input = input("Enter list of heart rate readings: ")

    if not user_input.startswith("[") or not user_input.endswith("]"):
        raise TypeError("Invalid input format. Enter values inside [].")

    user_input = user_input[1:-1]
    if user_input.strip() == "":
        raise ValueError("Empty list")
    
    elements = user_input.split(",")
    nums = []

    for elememt in elements:
        try:
            nums.append(float(elememt))
        except:
            raise ValueError("Non-numeric value found")
    return nums

def sorting(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):   
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def find_min(nums):
    minimum = nums[0]
    for i in nums:
        if i < minimum:
            minimum = i
    return minimum

def find_max(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
    return maximum

def find_mean(nums):
    total = 0
    for i in nums:
        total += i
    return total / len(nums)

def find_mode(nums):
    frequency = {}
    for n in nums:
        if n in frequency:
            frequency[n] += 1
        else:
            frequency[n] = 1
    
    count = 0
    for i in frequency:
        if frequency[i] > count:
            count = frequency[i]

    modes = []

    for i in frequency:
        if frequency[i] == count:
            modes.append(i)

    return modes

def find_median(nums):
    sorted_nums = sorting(nums)
    n = len(sorted_nums)

    if n%2 == 0:
        median = (sorted_nums[n//2 - 1] + sorted_nums[n//2]) /2

    else:
        median = sorted_nums[n//2]
    return median

def find_range(nums):
    range = find_max(nums) - find_min(nums)
    return range

def find_variance(nums):
    mean = find_mean(nums)
    total = 0
    for n in nums:
        total += (n-mean)**2
    variance = total / (len(nums) - 1)
    return variance

def find_std(nums):
    std = find_variance(nums) ** 0.5
    return std

def find_quartiles(nums):
    sorted_nums = sorting(nums)
    n = len(sorted_nums)

    Q2 = find_median(sorted_nums)

    if n%2 == 0:
        before_Q2 = sorted_nums[:n//2]
        after_Q2 = sorted_nums[n//2:]
    else:
        before_Q2 = sorted_nums[:n//2]
        after_Q2 = sorted_nums[n//2+1:]

    Q1 = find_median(before_Q2)
    Q3 = find_median(after_Q2)

    return Q1, Q2, Q3

def find_IQR(nums):
    Q1, Q2, Q3 = find_quartiles(nums)
    IQR = Q3 - Q1
    return IQR

try:
    nums = get_numbers()

    print("Min:", find_min(nums))
    print("Max:", find_max(nums))
    print("Mean:", round(find_mean(nums), 2))
    print("Mode:", find_mode(nums))
    print("Median:", find_median(nums))
    print("Range:", find_range(nums))
    print("Variance:", round(find_variance(nums), 2))
    print("STD:", round(find_std(nums), 2))
    print("Quartiles:", find_quartiles(nums))
    print("IQR:", find_IQR(nums))

except Exception as e:
    print("Error:", e)
    



    