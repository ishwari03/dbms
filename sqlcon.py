import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pass@123",
    database="mydatabase"
)
cursor = db.cursor()
def add_customer(name, city, mobile):
    sql = "INSERT INTO customers (name, city, mobile) VALUES (%s, %s, %s)"
    values = (name, city, mobile)
    cursor.execute(sql, values)
    db.commit()
    print(f"Customer added with ID: {cursor.lastrowid}")
def list_customers():
    sql = "SELECT * FROM customers"
    cursor.execute(sql)
    result = cursor.fetchall()
    for row in result:
        print(row)
def update_customer(customer_id, name=None, city=None, mobile=None):
    update_data = []
    sql = "UPDATE customers SET "
    if name:
        sql += "name = %s, "
        update_data.append(name)
    if city:
        sql += "city = %s, "
        update_data.append(city)
    if mobile:
        sql += "mobile = %s, "
        update_data.append(mobile)
    sql = sql.rstrip(", ")  
    sql += " WHERE id = %s"
    update_data.append(customer_id)
    
    cursor.execute(sql, tuple(update_data))
    db.commit()
    if cursor.rowcount > 0:
        print("Customer updated successfully.")
    else:
        print("Customer not found.")
def delete_customer(customer_id): 
    sql = "DELETE FROM customers WHERE id = %s"
    cursor.execute(sql, (customer_id,))
    db.commit()
    if cursor.rowcount > 0:
        print("Customer deleted successfully.")
    else:
        print("Customer not found.")
def find_customer_by_id(customer_id):
    sql = "SELECT * FROM customers WHERE id = %s"
    cursor.execute(sql, (customer_id,))
    customer = cursor.fetchone()
    if customer:
        print(customer)
    else:
        print("Customer not found.")

add_customer("Alice", "New York", "1234567890")
add_customer("Bob", "Los Angeles", "0987654321")
print("\nAll Customers:")
list_customers()
sample_id = int(input("\nEnter customer ID to update: "))
update_customer(sample_id, name="Alice Smith", mobile="1112223333")
sample_id = int(input("\nEnter customer ID to find: "))
find_customer_by_id(sample_id)
sample_id = int(input("\nEnter customer ID to delete: "))
delete_customer(sample_id)
print("\nAll Customers after deletion:")
list_customers()
cursor.close()
db.close()