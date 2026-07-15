def missing_number(nums):
    """
    Находит пропущенное число в последовательности натуральных чисел.

    Временная сложность: O(N)
    Пространственная сложность: O(1)
    """
    n = len(nums) + 1
    exp_sum = (n * (n+1)) // 2
    act_sum = sum(nums)
    return exp_sum - act_sum