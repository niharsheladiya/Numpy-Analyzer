# Welcome to Math Operations file

import numpy as np


class MathOperationsMixin:
    """Handles element-wise math operations and matrix multiplication."""

    def math_operations(self):
        if not self._has_array():
            return
        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product / Matrix Multiplication (2D only)")
        choice = input("Enter your choice: ")

        if choice in ("1", "2", "3", "4"):
            size = self.array.size
            data = self.get_numbers(
                f"Enter the same-size array elements ({size} elements separated by space): ", size
            )
            self.second_array = np.array(data).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)
            print("\nSecond Array:")
            print(self.second_array)

            if choice == "1":
                result = self.array + self.second_array
                print("\nResult of Addition:")
            elif choice == "2":
                result = self.array - self.second_array
                print("\nResult of Subtraction:")
            elif choice == "3":
                result = self.array * self.second_array
                print("\nResult of Multiplication:")
            else:
                result = self.array / self.second_array
                print("\nResult of Division:")
            print(result)

        elif choice == "5":
            if self.array.ndim != 2:
                print("This operation needs a 2D array.")
                return
            rows, cols = self.array.shape
            data = self.get_numbers(
                f"Enter elements for a {cols}x{rows} array separated by space: ", cols * rows
            )
            self.second_array = np.array(data).reshape(cols, rows)
            print("\nDot Product:")
            print(np.dot(self.array, self.second_array))

        else:
            print("Invalid choice.")
