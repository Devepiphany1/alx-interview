#!/usr/bin/python3
def can_unlock_all(boxes):
        """Determines if all boxes can be unlocked."""
            n = len(boxes)
                opened = {0}  # Start with the first box already opened
                    stack = [0]  # Stack to manage the boxes to be explored

                        while stack:
                                    box = stack.pop()

                                            for key in boxes[box]:
                                                            if key < n and key not in opened:
                                                                                opened.add(key)
                                                                                                stack.append(key)

                                                                                                    return len(opened) == n
                                                                                            
