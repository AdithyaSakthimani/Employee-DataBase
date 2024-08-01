import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class EmployeeData:
    def __init__(self, master):  
        self.master = master
        self.master.title("Employee Data Management")
        self.master.config(bg="azure")
        self.employee_data = {}
        self.create_widgets()
    def create_widgets(self):
        # Buttons
        disclaimer = tk.Label(self.master, text="WELCOME TO EMPLOYEE DATABASE !!!", font=('algerian', 25, "bold"), bg="azure", fg="darkslategray")
        disclaimer.pack(pady=20)

        self.add_button = tk.Button(self.master, text="Add Employee", command=self.add_employee, bg="indianred", fg="white", font=("Comic Sans MS", 14))
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self.master, text="Delete Employee", command=self.delete_employee, bg="indianred", fg="white", font=("Comic Sans MS", 14))
        self.delete_button.pack(pady=10)

        self.search_button = tk.Button(self.master, text="Search Employee", command=self.search_employee, bg="indianred", fg="white", font=("Comic Sans MS", 14))
        self.search_button.pack(pady=10)

        self.display_button = tk.Button(self.master, text="Display All Employees", command=self.display_employees, bg="indianred", fg="white", font=("Comic Sans MS", 14))
        self.display_button.pack(pady=10)

        # Text widget for display
        self.display_text = tk.Text(self.master, height=50, width=80, bg="paleturquoise", font=("times", 18))
        self.display_text.pack(pady=10)

    def add_employee(self):
        add_window = tk.Toplevel(self.master) 
        add_window.title("Add Employee")
        add_window.config(bg="honeydew")
        add_window.geometry("500x500")

        id_label = tk.Label(add_window, text="Enter Employee ID:", font=("Comic Sans MS", 14), bg="honeydew")
        id_label.pack(pady=10)
        id_entry = tk.Entry(add_window, font=14)
        id_entry.pack(pady=10)

        name_label = tk.Label(add_window, text="Enter Employee Name:", font=("Comic Sans MS", 14), bg="honeydew")
        name_label.pack(pady=10)``
        name_entry = tk.Entry(add_window, font=14)
        name_entry.pack(pady=10)

        dob_label = tk.Label(add_window, text="Enter Date of Birth DOB (YYYY-MM-DD):", font=("Comic Sans MS", 14), bg="honeydew")
        dob_label.pack(pady=10)
        dob_entry = tk.Entry(add_window, font=14)
        dob_entry.pack(pady=10)

        post_label = tk.Label(add_window, text="Enter Employee Position (Post):", font=("Comic Sans MS", 14), bg="honeydew")
        post_label.pack(pady=5)
        post_entry = tk.Entry(add_window, font=14)
        post_entry.pack(pady=5)

        confirm_button = tk.Button(add_window, text="Add", bg="yellowgreen", font=("Comic Sans MS", 14), command=lambda: self.confirm_add_employee(id_entry.get(), name_entry.get(), dob_entry.get(), post_entry.get(), add_window))
        confirm_button.pack(pady=10)

    def confirm_add_employee(self, emp_id, name, dob, post, add_window):
        if emp_id and name and dob and post:
            employee_info = f"      Name: {name}      DOB: {dob}        Position: {post}"
            self.employee_data[emp_id] = employee_info
            add_window.destroy()

    def delete_employee(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Employee")
        delete_window.config(bg="honeydew")
        delete_window.geometry("300x200")

        id_label = tk.Label(delete_window, text="Enter Employee ID to Delete:", bg="honeydew", font=("Comic Sans MS", 14))
        id_label.pack(pady=5)
        id_entry = tk.Entry(delete_window, font=14)
        id_entry.pack(pady=5)

        confirm_button = tk.Button(delete_window, text="Delete", bg="indianred", font=("Comic Sans MS", 14), fg="white", command=lambda: self.confirm_delete_employee(id_entry.get(), delete_window))
        confirm_button.pack(pady=10)

    def confirm_delete_employee(self, emp_id, delete_window):
        if emp_id in self.employee_data:
            del self.employee_data[emp_id]
            self.display_text.delete(1.0, tk.END)  # Clear previous display
            self.display_text.insert(tk.END, f"Employee ID {emp_id} deleted.\n")
        else:
            self.display_text.delete(1.0, tk.END)
            self.display_text.insert(tk.END, f"Employee ID {emp_id} not found.\n")
        delete_window.destroy()

    def search_employee(self):
        search_window = tk.Toplevel(self.master)
        search_window.title("Search Employee")
        search_window.config(bg="honeydew")
        search_window.geometry("300x200")

        id_label = tk.Label(search_window, text="Enter Employee ID to Search:", bg="honeydew", font=("Comic Sans", 14))
        id_label.pack(pady=5)
        id_entry = tk.Entry(search_window, font=14)
        id_entry.pack(pady=5)

        confirm_button = tk.Button(search_window, text="Search", bg="yellowgreen", font=("Comic Sans MS", 14), command=lambda: self.confirm_search_employee(id_entry.get(), search_window))
        confirm_button.pack(pady=10)

    def confirm_search_employee(self, emp_id, search_window):
        search_window.destroy()
        if emp_id in self.employee_data:
            self.display_text.delete(1.0, tk.END)
            self.display_text.insert(tk.END, f"Employee ID {emp_id}: {self.employee_data[emp_id]}\n")
        else:
            self.display_text.delete(1.0, tk.END)
            self.display_text.insert(tk.END, f"Employee ID {emp_id} not found.\n")

    def display_employees(self):
        self.display_text.delete(1.0, tk.END)  # Clear previous display
        if self.employee_data:
            for emp_id, details in self.employee_data.items():
                self.display_text.insert(tk.END, f"Employee ID: {emp_id}, {details}\n")
        else:
            messagebox.showinfo("No employee found", "Employee data is not found")

if __name__ == "__main__":  
    root = tk.Tk()
    app = EmployeeData(root)
    root.mainloop()
