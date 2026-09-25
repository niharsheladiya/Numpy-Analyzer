# NumPy Analyzer
# A simple menu-driven tool built using NumPy and OOP concepts.

import numpy as np


class DataAnalytics:
    """Class that handles array creation and all analysis operations."""

    total_arrays_created = 0  # class level attribute, shared by all objects

    def __init__(self):
        self.array = None
        self.second_array = None

    # ---------- utility helpers ----------

    @staticmethod
    def get_numbers(prompt, count):
        """Ask the user for 'count' numbers separated by space."""
        values = input(prompt).split()
        return [float(v) for v in values[:count]]

    @classmethod
    def show_total_arrays(cls):
        print(f"\nTotal arrays created in this session: {cls.total_arrays_created}")

    def __has_array(self):
        # private method, checks if an array already exists before any operation
        if self.array is None:
            print("\nNo array found. Please create an array first.")
            return False
        return True

    # ---------- 1. Array Creation ----------

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

        DataAnalytics.total_arrays_created += 1
        print("\nArray created successfully:")
        print(self.array)

        again = input("\nWould you like to perform indexing or slicing on this array? (y/n): ").lower()
        if again == "y":
            self.index_or_slice()

    def index_or_slice(self):
        if not self.__has_array():
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

    # ---------- 2. Mathematical Operations ----------

    def math_operations(self):
        if not self.__has_array():
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

    # ---------- 3. Combine / Split ----------

    def combine_or_split(self):
        if not self.__has_array():
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

    # ---------- 4. Search, Sort, Filter ----------

    def search_sort_filter(self):
        if not self.__has_array():
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

    # ---------- 5. Aggregates and Statistics ----------

    def aggregate_stats(self):
        if not self.__has_array():
            return
        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Percentile")
        print("7. Correlation with another array")
        choice = input("Enter your choice: ")

        print("\nOriginal Array:")
        print(self.array)

        if choice == "1":
            print("\nSum of Array:", np.sum(self.array))
        elif choice == "2":
            print("\nMean of Array:", np.mean(self.array))
        elif choice == "3":
            print("\nMedian of Array:", np.median(self.array))
        elif choice == "4":
            print("\nStandard Deviation:", np.std(self.array))
        elif choice == "5":
            print("\nVariance:", np.var(self.array))
        elif choice == "6":
            p = float(input("Enter the percentile to calculate (0-100): "))
            print(f"\n{p}th Percentile:", np.percentile(self.array, p))
        elif choice == "7":
            size = self.array.size
            data = self.get_numbers(
                f"Enter elements of the second array ({size} elements separated by space): ", size
            )
            other = np.array(data)
            correlation = np.corrcoef(self.array.flatten(), other)[0, 1]
            print("\nCorrelation Coefficient:", correlation)
        else:
            print("Invalid choice.")

    # ---------- Main Menu ----------

    def run(self):
        print("Welcome to the NumPy Analyzer!")
        print("=" * 40)

        while True:
            print("\nChoose an option:")
            print("1. Create a Numpy Array")
            print("2. Perform Mathematical Operations")
            print("3. Combine or Split Arrays")
            print("4. Search, Sort, or Filter Arrays")
            print("5. Compute Aggregates and Statistics")
            print("6. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.create_array()
            elif choice == "2":
                self.math_operations()
            elif choice == "3":
                self.combine_or_split()
            elif choice == "4":
                self.search_sort_filter()
            elif choice == "5":
                self.aggregate_stats()
            elif choice == "6":
                self.show_total_arrays()
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    analyzer = DataAnalytics()
    analyzer.run()