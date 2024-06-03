def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def main():
    strings_list = []

    # Meminta minimal 5 input dari pengguna
    print("Masukkan 5 string:")
    for i in range(5):
        user_input = input(f"String {i + 1}: ")
        strings_list.append(user_input)

    # Mengurutkan list menggunakan bubble sort
    bubble_sort(strings_list)

    # Menampilkan isi list yang telah diurutkan
    print("String di sort ASC menggunakan bubble sort:")
    print("=== TRADE MARK ===")
    for idx, string in enumerate(strings_list):
        print(f"String {idx + 1} is {string}")

if __name__ == "__main__":
    main()
