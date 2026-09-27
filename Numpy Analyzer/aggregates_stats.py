import numpy as np


class AggregatesStatsMixin:
    """Handles sum, mean, median, standard deviation, variance, percentile, and correlation."""

    def aggregate_stats(self):
        if not self._has_array():
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
