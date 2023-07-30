def find_min_max(numbers):

    min_val = numbers[0]  # 초기값으로 첫 번째 원소를 설정
    max_val = numbers[0]

    for num in numbers:
        if num < min_val:  # 현재 숫자가 최소값보다 작으면 최소값을 업데이트
            min_val = num
        elif num > max_val:  # 현재 숫자가 최대값보다 크면 최대값을 업데이트
            max_val = num

    return min_val, max_val


if __name__ == '__main__':
    numbers = [3, 1, 5, 2, 4]
    min_value, max_value = find_min_max(numbers)
    print("최소값:", min_value)  # 출력: 최소값: 1
    print("최대값:", max_value)  # 출력: 최대값: 5

####################################################

def custom_sum(lst):
    total = 0
    for num in lst:
        total += num
    return total

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    result = custom_sum(numbers)
    print("리스트의 합:", result)  # 출력: 리스트의 합: 15

#####################################################

def custom_len(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    length = custom_len(numbers)
    print("리스트의 길이:", length)  # 출력: 리스트의 길이: 5    
