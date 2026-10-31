medicines = [
    {
        "id": "M101",
        "name": "Paracetamol 500 mg",
        "category": "Tablet",
        "quantity": 120,
        "price": 15.00,
        "expiry": "2027-06-30"
    },
    {
        "id": "M102",
        "name": "Cetirizine 10 mg",
        "category": "Tablet",
        "quantity": 18,
        "price": 22.00,
        "expiry": "2027-02-28"
    },
    {
        "id": "M103",
        "name": "ORS Sachet",
        "category": "Rehydration",
        "quantity": 45,
        "price": 20.00,
        "expiry": "2027-12-31"
    }
]


# Display the details of one medicine
def show_medicine(m):
    print("\nMedicine ID:", m["id"])
    print("Name:", m["name"])
    print("Category:", m["category"])
    print("Quantity:", m["quantity"])
    print("Unit Price: Rs.", format(m["price"], ".2f"))
    print("Expiry Date:", m["expiry"])


# Algorithm 1: Linear Search
def linear_search(key):
    key = key.strip().lower()

    for medicine in medicines:
        if (medicine["id"].lower() == key or
                medicine["name"].lower() == key):
            return medicine

    return None


# Algorithm 2: Binary Search by medicine ID
def binary_search_by_id(target):
    ordered = sorted(medicines, key=lambda m: m["id"])

    target = target.strip().upper()
    low = 0
    high = len(ordered) - 1

    while low <= high:
        mid = (low + high) // 2
        current = ordered[mid]["id"]

        if current == target:
            return ordered[mid]
        elif current < target:
            low = mid + 1
        else:
            high = mid - 1

    return None


# Display all medicines
def show_all():
    for medicine in medicines:
        show_medicine(medicine)


# Display medicines with low stock
def show_low_stock(threshold=20):
    print("\nMedicines at or below", threshold, "units:")
    found = False

    for medicine in medicines:
        if medicine["quantity"] <= threshold:
            print(
                medicine["id"], "-",
                medicine["name"],
                "(", medicine["quantity"], "units )"
            )
            found = True

    if not found:
        print("No low-stock medicines.")


# Main menu
def main():
    while True:
        print("\nPHARMACY MEDICINE INVENTORY SEARCH SYSTEM")
        print("1. Display all medicines")
        print("2. Search by ID or exact name (Linear Search)")
        print("3. Search by ID (Binary Search)")
        print("4. Show low-stock medicines")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            show_all()

        elif choice == "2":
            key = input("Enter medicine ID or exact name: ")

            if not key.strip():
                print("Search key cannot be empty.")
                continue

            result = linear_search(key)

            if result:
                show_medicine(result)
            else:
                print("Medicine not found.")

        elif choice == "3":
            key = input("Enter medicine ID: ")
            result = binary_search_by_id(key)

            if result:
                print("Medicine found.")
                show_medicine(result)
            else:
                print("Medicine not found.")

        elif choice == "4":
            show_low_stock()

        elif choice == "5":
            print("Exiting inventory system.")
            break

        else:
            print("Invalid choice. Enter 1 to 5.")


if __name__ == "__main__":
    main()