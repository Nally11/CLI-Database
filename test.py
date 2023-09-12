import sqlite3

# Function to display all product items from the database
def display_items(cursor):
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    if not products:
        print("No products found in the database.")
    else:
        print("Product ID | Product Name | Price | Quantity")
        print("------------------------------------------")
        for product in products:
            print(f"{product[0]:<11} | {product[1]:<12} | {product[2]:<6} | {product[3]:<8}")

# Main function for user interaction
def main():
    # Establish a connection to the database
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()

        while True:
            # Display menu
            print("\nWarehouse CLI Menu:")
            print("1. Display Items")
            print("2. Exit")
            choice = input("Select an option (1/2): ")

            if choice == "1":
                # Display product items
                display_items(cursor)
            elif choice == "2":
                # Exit the program
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")

    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        # Close the database connection
        if conn:
            conn.close()

if __name__ == "__main__":
    main()
