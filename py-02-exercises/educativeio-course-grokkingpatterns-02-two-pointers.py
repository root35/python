import unittest


def search_triplets_with_sum(arr, target_sum):
    triplets = list()
    arr.sort()

    for j in range(len(arr)):
        pairs = search_pairs_with_sum(arr[j+1:], target_sum - arr[j])
        triplets.extend([[arr[j]] + pair for pair in pairs])

    return triplets


def search_pairs_with_sum(arr, target_sum):
    left, right = 0, len(arr) - 1
    pairs = set()

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            pairs.add((arr[left], arr[right]))
            left += 1
            right -= 1

        elif current_sum > target_sum:
            right -= 1

        elif current_sum < target_sum:
            left += 1

    return (list(pair) for pair in pairs)



class Test(unittest.TestCase):

    def test_triplets_with_sum(self):
        arr = [-3, 0, 1, 2, -1, 1, -2]
        target_sum = 0
        result = search_triplets_with_sum(arr, target_sum)
        expected_result = [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]


if __name__ == '__main__':
    unittest.main()
