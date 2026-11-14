"""Task 3: Secure Random Password Generator."""
import secrets
import string

def yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"): return True
        if answer in ("n", "no"): return False
        print("Please enter y or n.")

def main():
    print("\n=== Random Password Generator ===")
    while True:
        try:
            length = int(input("Password length (minimum 8): ").strip())
            if length < 8:
                print("Length must be at least 8.")
                continue
            break
        except ValueError:
            print("Enter a whole number.")

    groups = []
    if yes_no("Include uppercase letters? (y/n): "): groups.append(string.ascii_uppercase)
    if yes_no("Include lowercase letters? (y/n): "): groups.append(string.ascii_lowercase)
    if yes_no("Include numbers? (y/n): "): groups.append(string.digits)
    if yes_no("Include symbols? (y/n): "): groups.append("!@#$%^&*()-_=+[]{};:,.?/")

    if len(groups) < 2:
        print("Select at least TWO character types. Run the program again.")
        return

    if yes_no("Exclude ambiguous characters (0, O, l, 1)? (y/n): "):
        groups = ["".join(c for c in group if c not in "0O1l") for group in groups]
    if any(not group for group in groups):
        print("A selected character group is empty after filtering. Run again.")
        return

    def generate():
        chars = [secrets.choice(group) for group in groups]
        pool = "".join(groups)
        chars.extend(secrets.choice(pool) for _ in range(length - len(chars)))
        secrets.SystemRandom().shuffle(chars)
        return "".join(chars)

    print("\nGenerated password:", generate())
    while yes_no("Generate another with same settings? (y/n): "):
        print("Generated password:", generate())
    print("Keep your password private.")

if __name__ == "__main__":
    main()
