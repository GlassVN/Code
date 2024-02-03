'''[bài 5 cách 3]'''
while False:
    input_string = "3-5-8-9-4-6-5-8-7-3-1"
    numbers = input_string.split('-')
    int_numbers = []
    for num in numbers:
        int_numbers.append(int(num))
    total = sum(int_numbers)
    max_value = max(int_numbers)
    print("Tổng các phần tử là:", total)
    print("Giá trị lớn nhất là:", max_value)
