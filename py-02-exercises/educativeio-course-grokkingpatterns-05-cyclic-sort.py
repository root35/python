import unittest


def find_missing_number(nums):
    if nums is None or len(nums) == 0:
        return -1

    # Sort numbers
    i, length = 0, len(nums)

    while i < length:
        # Correct number at current index, or out of range
        if nums[i] == i or nums[i] < 0 or nums[i] > length:
            i += 1

        # Not correct number: nums[correct_number] != correct_number
        else:
            send_index = nums[i]
            nums[i], nums[send_index] = nums[send_index], nums[i]

    # Find missing number
    for index, number in enumerate(nums):
        if index != number:
            return number

    return -1


class Test(unittest.TestCase):

    def test_find_missing_number(self):
        nums = [4, 0, 3, 1]
        result = find_missing_number(nums)
        self.assertEqual(result, 2)


if __name__ == '__main__':
    unittest.main()
