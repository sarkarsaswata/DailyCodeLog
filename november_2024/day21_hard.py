from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Precompute sets for rows, columns, and boxes to track used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize sets and identify empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    num = board[i][j]
                    rows[i].add(num)
                    cols[j].add(num)
                    box_index = (i // 3) * 3 + j // 3
                    boxes[box_index].add(num)

        def backtrack(index=0):
            # If all empty cells are filled, we're done
            if index == len(empty_cells):
                return True

            # Get the next empty cell
            row, col = empty_cells[index]
            box_index = (row // 3) * 3 + col // 3

            # Try placing digits 1-9
            for num in '123456789':
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_index]:
                    # Place the number and update sets
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_index].add(num)

                    # Recurse to the next empty cell
                    if backtrack(index + 1):
                        return True

                    # Undo placement and backtrack
                    board[row][col] = '.'
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_index].remove(num)

            # If no number works, backtrack
            return False

        backtrack()