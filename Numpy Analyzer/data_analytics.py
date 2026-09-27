from array_creation import ArrayCreationMixin
from math_operations import MathOperationsMixin
from combine_split import CombineSplitMixin
from search_sort_filter import SearchSortFilterMixin
from aggregates_stats import AggregatesStatsMixin


class DataAnalytics(
    ArrayCreationMixin,
    MathOperationsMixin,
    CombineSplitMixin,
    SearchSortFilterMixin,
    AggregatesStatsMixin,
):
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

    def _has_array(self):
        # checks if an array already exists before any operation
        if self.array is None:
            print("\nNo array found. Please create an array first.")
            return False
        return True

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
