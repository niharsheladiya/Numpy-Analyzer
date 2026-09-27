# Welcome to Combine Split file 

import numpy as np


class CombineSplitMixin:
    """Handles combining two arrays and splitting one array into parts."""

    def combine_or_split(self):
        if not self._has_array():
            return
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ")

        if choice == "1":
            size = self.array.size
            data = self.get_numbers(
                f"Enter the elements of another array to combine ({size} elements separated by space): ", size
            )
            other = np.array(data).reshape(self.array.shape)

            print("\nOriginal Array:")
            print(self.array)
            print("\nSecond Array:")
            print(other)

            combined = np.vstack((self.array, other))
            print("\nCombined Array (Vertical Stack):")
            print(combined)

        elif choice == "2":
            parts = int(input("Enter the number of parts to split into: "))
            try:
                split_result = np.array_split(self.array, parts)
                print("\nSplit Arrays:")
                for i, part in enumerate(split_result, start=1):
                    print(f"Part {i}:")
                    print(part)
            except ValueError as e:
                print("Could not split array:", e)

        else:
            print("Invalid choice.")
