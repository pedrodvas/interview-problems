import random

def merge_sort(numbers: list[int]):
    return_list = []
    if len(numbers) <= 1:
        return numbers
    
    left_part = merge_sort(numbers[:len(numbers)//2])
    right_part = merge_sort(numbers[len(numbers)//2:])
    print(f"first part:\n{left_part}")
    print(f"second part:\n{right_part}")

    iterator_left = 0
    iterator_right = 0
    while iterator_left + iterator_right < len(numbers):
        if iterator_left == len(left_part):
            #takes from the right
            return_list.append(right_part[iterator_right])
            iterator_right += 1
        elif iterator_right == len(right_part):
            #takes from the left
            return_list.append(left_part[iterator_left])
            iterator_left += 1
        else:
            if left_part[iterator_left]>right_part[iterator_right]:
                #takes from right
                return_list.append(right_part[iterator_right])
                iterator_right += 1
            else:
                #takes from left
                return_list.append(left_part[iterator_left])
                iterator_left += 1
    
    return return_list



if __name__ == "__main__":
    print(merge_sort([5, 4, 3, 2, 1]))
    print("=========================")
    print(merge_sort([2, 1]))
    n = 234
    list = [random.randint(1, 465) for _ in range(n)]
    list = merge_sort(list)
    print(list)
    for i in range(1, len(list)):
        if list[i] < list[i-1]:
            print("errou")
    print("verifique se acertou!")