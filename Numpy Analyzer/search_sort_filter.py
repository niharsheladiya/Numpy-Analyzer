# Welcome to Search , Sort , Filter file 

import numpy as np


class SearchSortFilterMixin:
    """Handles searching, sorting, and filtering array values."""

    def search_sort_filter(self):
        if not self._has_array():
            return
        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = input("Enter your choice: ")

        if choice == "1":
            value = float(input("Enter the value to search: "))
            positions = np.where(self.array == value)
            if len(positions[0]) == 0:
                print(f"\n{value} not found in the array.")
            else:
                print(f"\n{value} found at position(s):", positions)

        elif choice == "2":
            order = input("Sort in ascending or descending order? (a/d): ").lower()
            print("\nOriginal Array:")
            print(self.array)
            sorted_array = np.sort(self.array, axis=-1)
            if order == "d":
                sorted_array = np.flip(sorted_array, axis=-1)
            print("\nSorted Array:")
            print(sorted_array)
            print("(Sorting applied row-wise.)")

        elif choice == "3":
            op = input("Enter a comparison operator (>, <, >=, <=, ==): ")
            value = float(input("Enter the value to compare with: "))

            if op == ">":
                result = self.array[self.array > value]
            elif op == "<":
                result = self.array[self.array < value]
            elif op == ">=":
                result = self.array[self.array >= value]
            elif op == "<=":
                result = self.array[self.array <= value]
            elif op == "==":
                result = self.array[self.array == value]
            else:
                print("Invalid operator.")
                return
            print("\nFiltered Values:")
            print(result)

        else:
            print("Invalid choice.")
