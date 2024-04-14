import tkinter as tk
from tkinter import messagebox, simpledialog

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Colorful Contact Manager")
        self.contacts = {}

        # Color and font styles
        self.bg_color = "#7627B7"
        self.text_color = "#000000"
        self.button_color = "#000000"
        self.entry_bg_color = "#555555"
        self.text_area_bg_color = "#C0BDBF"
        self.button_text_color = "#FFFFFF"

        self.root.configure(bg=self.bg_color)

        # Frame for List / Search
        list_frame = tk.Frame(self.root, bg=self.bg_color)
        list_frame.pack(pady=20)

        tk.Label(list_frame, text="Search or View Contacts:", fg=self.text_color, bg=self.bg_color).pack(side=tk.TOP, pady=5)
        self.search_entry = tk.Entry(list_frame, width=50, bg=self.entry_bg_color, fg=self.text_color)
        self.search_entry.pack(side=tk.LEFT, padx=10)
        search_button = tk.Button(list_frame, text="Search", command=self.search_contact, bg=self.button_color, fg=self.button_text_color)
        search_button.pack(side=tk.LEFT)
        view_all_button = tk.Button(list_frame, text="View All", command=self.view_contacts, bg=self.button_color, fg=self.button_text_color)
        view_all_button.pack(side=tk.LEFT, padx=10)

        # Frame for Contact Info Display
        self.text = tk.Text(self.root, height=15, width=80, bg=self.text_area_bg_color, fg=self.text_color)
        self.text.pack(pady=20)

        # Frame for Buttons
        button_frame = tk.Frame(self.root, bg=self.bg_color)
        button_frame.pack(pady=20)

        add_button = tk.Button(button_frame, text="Add Contact", command=self.add_contact, bg=self.button_color, fg=self.button_text_color)
        add_button.grid(row=0, column=0, padx=10)
        
        update_button = tk.Button(button_frame, text="Update Contact", command=self.update_contact, bg=self.button_color, fg=self.button_text_color)
        update_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Delete Contact", command=self.delete_contact, bg=self.button_color, fg=self.button_text_color)
        delete_button.grid(row=0, column=2, padx=10)

    def add_contact(self):
        name = simpledialog.askstring("Contact Name", "Enter the store name:", parent=self.root)
        if name in self.contacts:
            messagebox.showerror("Error", "Contact already exists!")
            return
        phone = simpledialog.askstring("Phone Number", "Enter the phone number:", parent=self.root)
        email = simpledialog.askstring("Email", "Enter the email address:", parent=self.root)
        address = simpledialog.askstring("Address", "Enter the address:", parent=self.root)
        self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
        messagebox.showinfo("Added", "Contact added successfully!")

    def view_contacts(self):
        self.text.delete(1.0, tk.END)
        for name, info in self.contacts.items():
            self.text.insert(tk.END, f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n")

    def search_contact(self):
        search_query = self.search_entry.get()
        self.text.delete(1.0, tk.END)
        for name, info in self.contacts.items():
            if search_query.lower() in name.lower() or search_query in info['phone']:
                self.text.insert(tk.END, f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\nAddress: {info['address']}\n\n")

    def update_contact(self):
        name = simpledialog.askstring("Update Contact", "Enter the name of the contact to update:", parent=self.root)
        if name in self.contacts:
            phone = simpledialog.askstring("Phone Number", "Enter the new phone number:", parent=self.root)
            email = simpledialog.askstring("Email", "Enter the new email address:", parent=self.root)
            address = simpledialog.askstring("Address", "Enter the new address:", parent=self.root)
            self.contacts[name] = {'phone': phone, 'email': email, 'address': address}
            messagebox.showinfo("Updated", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")

    def delete_contact(self):
        name = simpledialog.askstring("Delete Contact", "Enter the name of the contact to delete:", parent=self.root)
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Deleted", "Contact deleted successfully!")
            self.view_contacts()
        else:
            messagebox.showerror("Error", "Contact not found!")

if __name__ == "__main__":
    root = tk.Tk()
    cm = ContactManager(root)
    root.mainloop()
