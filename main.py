import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def main():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    if rows <= 0 or cols <= 0:
        print("Invalid input. The rows and columns must be positive numbers.")
        return 1

    clear_screen()

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print("{:>4}".format(i * j), end='')
        print()

    print("\nPress enter to continue...")
    input()

    return 0

if __name__ == "__main__":
    main()
