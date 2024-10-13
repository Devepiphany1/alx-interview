#!/usr/bin/python3

def canUnlockAll(boxes):
    # Total number of boxes
    n = len(boxes)
    
    # A set to track which boxes have been opened
    opened = set([0])  # Start with the first box already opened
    
    # A stack to manage the boxes we are currently exploring
    stack = [0]  # Start with the first box
    
    while stack:
        # Take the top box from the stack
        box = stack.pop()
        
        # Go through all the keys in the current box
        for key in boxes[box]:
            # If the key is a valid box number and that box hasn't been opened yet
            if key < n and key not in opened:
                # Open the box and add it to the opened set
                opened.add(key)
                # Add this box to the stack to explore its keys
                stack.append(key)
    
    # If the number of opened boxes is equal to the total number of boxes, return True
    return len(opened) == n
