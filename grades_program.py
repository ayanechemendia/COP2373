import csv

# ============================================
# FUNCTION 1: Write grades to CSV file
# ============================================
def write_grades():
    filename = "grades.csv"

    num_students = int(input("Enter number of students: "))

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow(["First Name", "Last Name", "Exam 1", "Exam 2", "Exam 3"])

        # Input student data
        for i in range(num_students):
            print(f"\nStudent {i + 1}")

            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write row to CSV
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    print("\nData successfully written to grades.csv")


# ============================================
# FUNCTION 2: Read and display CSV file
# ============================================
def read_grades():
    filename = "grades.csv"

    print("\n--- Student Grades ---")

    with open(filename, mode='r') as file:
        reader = csv.reader(file)

        # Print table format
        for row in reader:
            print("{:<15} {:<15} {:<10} {:<10} {:<10}".format(*row))


# ============================================
# MAIN FUNCTION
# ============================================
def main():
    write_grades()
    read_grades()


# Run program
if __name__ == "__main__":
    main()