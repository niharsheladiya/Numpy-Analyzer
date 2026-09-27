import numpy as np


class ArrayCreationMixin:
    """Handles array creation, indexing, and slicing."""

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter the number of elements: "))
            data = self.get_numbers(f"Enter {n} elements for the array separated by space: ", n)
            self.array = np.array(data)

        elif choice == "2":
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            data = self.get_numbers(f"Enter {rows * cols} elements for the array separated by space: ", rows * cols)
            self.array = np.array(data).reshape(rows, cols)

        elif choice == "3":
            depth = int(input("Enter the depth: "))
            rows = int(input("Enter the number of rows: "))
            cols = int(input("Enter the number of columns: "))
            total = depth * rows * cols
            data = self.get_numbers(f"Enter {total} elements for the array separated by space: ", total)
            self.array = np.array(data).reshape(depth, rows, cols)

        else:
            print("Invalid choice.")
            return

        type(self).total_arrays_created += 1
        print("\nArray created successfully:")
        print(self.array)

        again = input("\nWould you like to perform indexing or slicing on this array? (y/n): ").lower()
        if again == "y":
            self.index_or_slice()

    def index_or_slice(self):
        if not self._has_array():
            return
        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")
        choice = input("Enter your choice: ")

        if choice == "1":
            idx = input("Enter the index (use commas for multiple dimensions): ")
            index = tuple(int(i) for i in idx.split(","))
            print("\nValue at index:", self.array[index])

        elif choice == "2":
            row_range = input("Enter the row range (start:end): ")
            col_range = input("Enter the column range (start:end): ")
            r1, r2 = (int(x) for x in row_range.split(":"))
            c1, c2 = (int(x) for x in col_range.split(":"))
            print("\nSliced Array:")
            print(self.array[r1:r2, c1:c2])

        elif choice == "3":
            return
        else:
            print("Invalid choice.")
