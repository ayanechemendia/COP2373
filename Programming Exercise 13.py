import sqlite3
import random
import matplotlib.pyplot as plt


# --------------------------------------------------
# FUNCTION 1: Create database and insert 2025 data
# --------------------------------------------------
def create_database():
    conn = sqlite3.connect("population_AEC.db")
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    """)

    # Clear old data (prevents duplicates if re-run)
    cursor.execute("DELETE FROM population")

    # Florida cities with estimated 2025 populations
    cities = {
        "Miami": 460000,
        "Orlando": 320000,
        "Tampa": 410000,
        "Jacksonville": 1000000,
        "Tallahassee": 200000,
        "St. Petersburg": 260000,
        "Hialeah": 220000,
        "Fort Lauderdale": 185000,
        "Cape Coral": 210000,
        "Sarasota": 58000
    }

    # Insert initial data (2025)
    for city, pop in cities.items():
        cursor.execute(
            "INSERT INTO population VALUES (?, ?, ?)",
            (city, 2025, pop)
        )

    conn.commit()
    conn.close()


# --------------------------------------------------
# FUNCTION 2: Simulate 20 years of population change
# --------------------------------------------------
def simulate_growth():
    conn = sqlite3.connect("population_AEC.db")
    cursor = conn.cursor()

    # Get 2025 data
    cursor.execute("SELECT city, population FROM population WHERE year = 2025")
    rows = cursor.fetchall()

    for city, pop in rows:
        current_pop = pop

        for year in range(2026, 2046):  # 20 years
            # Growth/decline between -2% and +5%
            rate = random.uniform(-0.02, 0.05)
            current_pop = int(current_pop * (1 + rate))

            cursor.execute(
                "INSERT INTO population VALUES (?, ?, ?)",
                (city, year, current_pop)
            )

    conn.commit()
    conn.close()


# --------------------------------------------------
# FUNCTION 3: Display population graph
# --------------------------------------------------
def plot_population():
    conn = sqlite3.connect("population_AEC.db")
    cursor = conn.cursor()

    # Get city list
    cursor.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cursor.fetchall()]

    print("\n========== CITY OPTIONS ==========")
    for i, city in enumerate(cities, 1):
        print(f"{i}. {city}")

    # User selects city
    choice = int(input("\nEnter a number (1-10): "))
    selected_city = cities[choice - 1]

    print(f"\nYou selected: {selected_city}")

    # Get data
    cursor.execute("""
        SELECT year, population
        FROM population
        WHERE city = ?
        ORDER BY year
    """, (selected_city,))

    data = cursor.fetchall()

    years = [row[0] for row in data]
    populations = [row[1] for row in data]

    # Plot graph
    plt.figure()
    plt.plot(years, populations)
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid()

    plt.show()

    conn.close()


# --------------------------------------------------
# MAIN FUNCTION
# --------------------------------------------------
def main():
    create_database()
    simulate_growth()
    plot_population()


# Run program
main()