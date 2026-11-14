"""Task 2: BMI Calculator."""
def positive_number(prompt):
    while True:
        try:
            n = float(input(prompt).strip())
            if n <= 0:
                print("Please enter a value greater than zero.")
            else:
                return n
        except ValueError:
            print("Invalid input. Enter a number, e.g. 65 or 1.70.")

def main():
    print("\n=== BMI Calculator ===")
    while True:
        weight = positive_number("Weight in kg: ")
        height = positive_number("Height in metres (e.g. 1.70): ")
        bmi = weight / (height ** 2)
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        print(f"Your BMI: {bmi:.2f}")
        print(f"Category: {category}")
        if input("Calculate again? (y/n): ").strip().lower() not in ("y", "yes"):
            print("Thank you!")
            break

if __name__ == "__main__":
    main()
