"""
冒泡排序算法的优化实现

这个模块实现了冒泡排序算法，包含性能优化和功能增强。
"""
from typing import List, Union


def bubble_sort(arr: List[Union[int, float]], reverse: bool = False) -> List[Union[int, float]]:
    """
    使用冒泡排序算法对数组进行排序（优化版本）
    
    时间复杂度：
    - 最好情况：O(n) - 当数组已经排序时
    - 平均情况：O(n²)
    - 最坏情况：O(n²)
    
    空间复杂度：O(1) - 原地排序
    
    Args:
        arr (List[Union[int, float]]): 要排序的数字列表
        reverse (bool, optional): 是否降序排列。默认为 False（升序）
        
    Returns:
        List[Union[int, float]]: 排序后的数组
        
    Examples:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]
        
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90], reverse=True)
        [90, 64, 34, 25, 22, 12, 11]
        
        >>> bubble_sort([1])  # 单元素数组
        [1]
        
        >>> bubble_sort([])   # 空数组
        []
    """
    # 处理边界情况
    if len(arr) <= 1:
        return arr
    
    n = len(arr)
    
    # 外层循环控制比较轮数
    for i in range(n):
        # 优化标志：记录这一轮是否有元素交换
        swapped = False
        
        # 内层循环进行相邻元素比较
        # 每轮比较后，最大（或最小）元素会"冒泡"到正确位置
        # 所以每轮比较范围可以减少 i 个元素
        for j in range(0, n - i - 1):
            # 根据排序方向选择比较条件
            if (not reverse and arr[j] > arr[j + 1]) or (reverse and arr[j] < arr[j + 1]):
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果这一轮没有发生任何交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_with_stats(arr: List[Union[int, float]], reverse: bool = False) -> tuple:
    """
    带统计信息的冒泡排序
    
    Args:
        arr (List[Union[int, float]]): 要排序的数字列表
        reverse (bool, optional): 是否降序排列。默认为 False（升序）
        
    Returns:
        tuple: (排序后的数组, 比较次数, 交换次数, 实际轮数)
    """
    if len(arr) <= 1:
        return arr, 0, 0, 0
    
    n = len(arr)
    comparisons = 0
    swaps = 0
    rounds = 0
    
    for i in range(n):
        swapped = False
        rounds += 1
        
        for j in range(0, n - i - 1):
            comparisons += 1
            if (not reverse and arr[j] > arr[j + 1]) or (reverse and arr[j] < arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True
        
        if not swapped:
            break
    
    return arr, comparisons, swaps, rounds


def main():
    """主函数：演示冒泡排序的各种用法"""
    print("=" * 50)
    print("🔸 冒泡排序算法演示")
    print("=" * 50)
    
    # 测试用例1：基本排序
    test_array1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n📊 测试用例1 - 基本排序")
    print(f"原数组: {test_array1}")
    
    sorted_asc = bubble_sort(test_array1.copy())
    print(f"升序排序: {sorted_asc}")
    
    sorted_desc = bubble_sort(test_array1.copy(), reverse=True)
    print(f"降序排序: {sorted_desc}")
    
    # 测试用例2：边界情况
    print(f"\n📊 测试用例2 - 边界情况")
    print(f"空数组: {bubble_sort([])}")
    print(f"单元素: {bubble_sort([42])}")
    print(f"已排序: {bubble_sort([1, 2, 3, 4, 5])}")
    print(f"逆序: {bubble_sort([5, 4, 3, 2, 1])}")
    
    # 测试用例3：性能统计
    test_array3 = [64, 34, 25, 12, 22, 11, 90, 5, 77, 30]
    print(f"\n📊 测试用例3 - 性能统计")
    print(f"原数组: {test_array3}")
    
    result, comparisons, swaps, rounds = bubble_sort_with_stats(test_array3.copy())
    print(f"排序结果: {result}")
    print(f"📈 统计信息:")
    print(f"  - 比较次数: {comparisons}")
    print(f"  - 交换次数: {swaps}")
    print(f"  - 实际轮数: {rounds}")
    print(f"  - 理论最大轮数: {len(test_array3) - 1}")
    
    # 测试用例4：浮点数排序
    test_array4 = [3.14, 2.71, 1.41, 0.57, 1.73]
    print(f"\n📊 测试用例4 - 浮点数排序")
    print(f"原数组: {test_array4}")
    print(f"排序后: {bubble_sort(test_array4.copy())}")
    
    print(f"\n✅ 所有测试完成！")


if __name__ == "__main__":
    main()