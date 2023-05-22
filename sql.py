import mysql.connector
from tkinter import *

# Establish connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ritesh@123",
    database="sqls"
)

# Create a cursor
cursor = connection.cursor()


def create_record():
    # Get input from the user
    name = entry_name.get()
    age = entry_age.get()

    # SQL query to insert data
    query = "INSERT INTO data (name, age) VALUES (%s, %s)"
    values = (name, age)

    # Execute the query
    cursor.execute(query, values)
    connection.commit()

    # Clear input fields
    entry_name.delete(0, END)
    entry_age.delete(0, END)


def read_records():
    # Clear the output field
    output.delete("1.0", END)

    # SQL query to retrieve data
    query = "SELECT * FROM data"
    cursor.execute(query)

    # Fetch all rows
    rows = cursor.fetchall()

    # Display the records
    for row in rows:
        output.insert(END, f"Name: {row[0]}, Age: {row[1]}\n")


def update_record():
    # Get input from the user
    name = entry_name.get()
    age = entry_age.get()

    # SQL query to update data
    query = "UPDATE data SET age = %s WHERE name = %s"
    values = (age, name)

    # Execute the query
    cursor.execute(query, values)
    connection.commit()

    # Clear input fields
    entry_name.delete(0, END)
    entry_age.delete(0, END)


def delete_record():
    # Get input from the user
    name = entry_name.get()

    # SQL query to delete data
    query = "DELETE FROM data WHERE name = %s"
    values = (name,)

    # Execute the query
    cursor.execute(query, values)
    connection.commit()

    # Clear input fields
    entry_name.delete(0, END)
    entry_age.delete(0, END)


# Create the GUI
root = Tk()
root.title("CRUD Operations")

# Labels
label_name = Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=5, pady=5)

label_age = Label(root, text="Age:")
label_age.grid(row=1, column=0, padx=5, pady=5)

# Entry fields
entry_name = Entry(root)
entry_name.grid(row=0, column=1, padx=5, pady=5)

entry_age = Entry(root)
entry_age.grid(row=1, column=1, padx=5, pady=5)

# Buttons
button_create = Button(root, text="Create", command=create_record)
button_create.grid(row=2, column=0, padx=5, pady=5)

button_read = Button(root, text="Read", command=read_records)
button_read.grid(row=2, column=1, padx=5, pady=5)

button_update = Button(root, text="Update", command=update_record)
button_update.grid(row=3, column=0, padx=5, pady=5)

button_delete = Button(root, text="Delete", command=delete_record)
button_delete.grid(row=3, column=1, padx=5, pady=5)

# Output field
output = Text(root, width=30, height=10)
output.grid(row=4, columnspan=2, padx=5, pady=5)


# Functions for CRUD operations

# ...


# Output field scrollbar
scrollbar = Scrollbar(root)
scrollbar.grid(row=4, column=2, sticky=N+S)

# Configure the output field to use the scrollbar
output.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output.yview)


# Start the GUI
root.mainloop()