def chop(inputList):
    del inputList[0]
    del inputList[-1]
    return None

def middle(inputList):
    outputList = inputList[1:-1]
    return outputList

original_list = [1, 2, 3, 4]
print("my list before call chop function =>", original_list)
chop(original_list)
print("my list after call chop function =>", original_list)

print()

original_list = [1, 2, 3, 4]
print("my list before call middle function =>", original_list)
new_list = middle(original_list)
print("my list after call middle function =>", original_list)
print("new list after call middle function =>", new_list)
