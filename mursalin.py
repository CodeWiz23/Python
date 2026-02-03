List = ["1", "2", "3", "4", "5", "6", "7"]

List[0], List[-1] = List[-1], List[0]

print("After swapping:", List)

smallest = min(map(int, List))

print("Smallest number:", smallest)
