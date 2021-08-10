# O(n^2)
def count_sums(array, sums):
    count = 0
    seen = {}

    for i in range(0,len(array)):
        for j in range(i+1, len(array)):
            if str(array[i]) + str(array[j]) in seen.keys() or str(array[j]) + str(array[i]) in seen.keys():
                    continue
            if array[i] + array[j] == sums:
                seen[str(array[i]) + str(array[j])] = 1
                count+=1

    return count

# O(n)
def count_sums_better(array, sums):
    count = 0
    seen = []
    for i in array:
        if sums - i in array:
            if i in seen:
                continue
            else:
                count += 1
                seen.append(sums - i)
    return count


array = [1,5,7,-1, 5]
sums = 6
print(count_sums(array,sums))
print(count_sums_better(array,sums))