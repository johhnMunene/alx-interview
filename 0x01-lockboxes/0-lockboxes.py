def canUnlockAll(boxes):
    # Set to keep track of opened boxes
    opened = set([0])
    
    # Queue to keep track of boxes to be opened
    queue = [0]
    
    # Perform BFS
    while queue:
        box = queue.pop(0)
        for key in boxes[box]:
            if key not in opened and key < len(boxes):
                opened.add(key)
                queue.append(key)
    
    # Check if all boxes can be opened
    return len(opened) == len(boxes)

# Test cases
if __name__ == "__main__":
    boxes1 = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes1))  # True

    boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes2))  # True

    boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes3))  # False

