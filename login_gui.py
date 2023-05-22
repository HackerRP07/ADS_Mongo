import tkinter as tk
from pymongo import MongoClient

class MyGUI:
    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        # create a label for the title
        title_label = tk.Label(self.root, text='CRUD Operations', font=('Arial', 16, 'bold'))
        title_label.pack(pady=10)

        # create a frame to hold the input fields and buttons
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        # create input fields for the document data
        name_label = tk.Label(input_frame, text='Name:')
        name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        age_label = tk.Label(input_frame, text='Age:')
        age_label.grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(input_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        city_label = tk.Label(input_frame, text='City:')
        city_label.grid(row=2, column=0, padx=5, pady=5)
        self.city_entry = tk.Entry(input_frame)
        self.city_entry.grid(row=2, column=1, padx=5, pady=5)

        # create buttons for CRUD operations
        create_button = tk.Button(input_frame, text='Create', command=self.create_doc)
        create_button.grid(row=3, column=0, padx=5, pady=5)

        read_button = tk.Button(input_frame, text='Read', command=self.read_doc)
        read_button.grid(row=3, column=1, padx=5, pady=5)

        update_button = tk.Button(input_frame, text='Update', command=self.update_doc)
        update_button.grid(row=3, column=2, padx=5, pady=5)

        delete_button = tk.Button(input_frame, text='Delete', command=self.delete_doc)
        delete_button.grid(row=3, column=3, padx=5, pady=5)

        # create a label to display status messages
        self.status_label = tk.Label(self.root, text='', fg='red')
        self.status_label.pack(pady=10)