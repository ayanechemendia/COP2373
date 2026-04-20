import numpy as np

# ----------------------------------------
# Function to load grades from CSV file
# ----------------------------------------
def load_grades(filename):
    data = np.genfromtxt(
        filename,
        delimiter=',',
        skip_header=1,
        dtype=float,
        filling_values=0
    )

    # Remove first two columns (names), keep only exam scores
    exams = data[:, 2:]

    return exams

    # Extract exam columns
    exams = np.column_stack((data['Exam 1'], data['Exam 2'], data['Exam 3']))

    return exams


# ----------------------------------------
# Function to display exam statistics
# ----------------------------------------
def exam_statistics(data):
    print("\n--- Exam Statistics ---\n")

    means = np.mean(data, axis=0)
    medians = np.median(data, axis=0)
    stds = np.std(data, axis=0)
    mins = np.min(data, axis=0)
    maxs = np.max(data, axis=0)

    for i in range(len(means)):
        print(f"Exam {i+1}:")
        print("Mean:", means[i])
        print("Median:", medians[i])
        print("Standard Deviation:", stds[i])
        print("Minimum:", mins[i])
        print("Maximum:", maxs[i])
        print()


# ----------------------------------------
# Function to display overall statistics
# ----------------------------------------
def overall_statistics(data):
    print("\n--- Overall Statistics ---\n")

    print("Mean:", np.mean(data))
    print("Median:", np.median(data))
    print("Standard Deviation:", np.std(data))
    print("Minimum:", np.min(data))
    print("Maximum:", np.max(data))


# ----------------------------------------
# Function to calculate pass/fail stats
# ----------------------------------------
def pass_fail_statistics(data):
    print("\n--- Pass/Fail Statistics ---\n")

    passed = data >= 60
    failed = data < 60

    total_pass = 0

    for i in range(data.shape[1]):
        print(f"Exam {i+1}:")
        print("Passed:", np.sum(passed[:, i]))
        print("Failed:", np.sum(failed[:, i]))
        print()

        total_pass += np.sum(passed[:, i])

    total_exams = data.size
    pass_percentage = (total_pass / total_exams) * 100

    print(f"Overall Pass Percentage: {pass_percentage:.2f}%")


# ----------------------------------------
# Main function
# ----------------------------------------
def main():
    filename = "grades.csv"

    data = load_grades(filename)

    # Show first few rows
    print("--- First Few Rows ---\n")
    print(data[:5])

    exam_statistics(data)
    overall_statistics(data)
    pass_fail_statistics(data)

data = load_grades("grades.csv")
print(data)
print(data.shape)

# Run program
main()