def insertion_sort_steps(arr):
    print("Başlangıç:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(f"{i}. adım:", arr)

arr = [22, 27, 16, 2, 18, 6]
insertion_sort_steps(arr.copy())
