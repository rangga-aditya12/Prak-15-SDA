def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    strings_list = []
    while True:
        # Menampilkan menu
        print("Menu:")
        print("1. Enter Strings")
        print("2. Show Sorted Result")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            # Meminta input string dari pengguna
            num_strings = int(input("Enter the number of strings: "))
            strings_list = []
            for i in range(num_strings):
                user_input = input(f"Enter string {i + 1}: ")
                strings_list.append(user_input)
            print("Strings entered successfully.\n")

        elif choice == '2':
            if not strings_list:
                print("No strings to sort. Please enter strings first.\n")
            else:
                # Mengurutkan dan menampilkan hasil
                bubble_sort(strings_list)
                print("Strings di sort ASC menggunakan bubble sort:")
                for idx, string in enumerate(strings_list):
                    print(f"String {idx + 1} is {string}")
                print()

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
