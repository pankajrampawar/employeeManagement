import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self, name, skills, availability):
        self.name = name
        self.skills = skills
        self.availability = availability

class Shift:
    def __init__(self, time, skill_required):
        self.time = time
        self.skill_required = skill_required
        self.assigned_employee = None

class ShiftScheduler:
    def __init__(self):
        self.employees = []
        self.shifts = []

    def add_employee(self, name, skills, availability):
        self.employees.append(Employee(name, skills, availability))

    def add_shift(self, time, skill_required):
        self.shifts.append(Shift(time, skill_required))

    def assign_shifts(self):
        for shift in self.shifts:
            suitable_employees = [employee for employee in self.employees if shift.skill_required in employee.skills and shift.time in employee.availability]
            if suitable_employees:
                # Assign the shift to the first suitable employee found
                shift.assigned_employee = suitable_employees[0]
                # Update the employee's availability
                shift.assigned_employee.availability.remove(shift.time)
            else:
                messagebox.showwarning("Warning", f"No suitable employee found for shift at {shift.time}.")

class ShiftSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shift Scheduler")

        self.scheduler = ShiftScheduler()

        self.employee_name_label = tk.Label(root, text="Employee Name:")
        self.employee_name_label.grid(row=0, column=0)
        self.employee_name_entry = tk.Entry(root)
        self.employee_name_entry.grid(row=0, column=1)

        self.employee_skills_label = tk.Label(root, text="Employee Skills (comma-separated):")
        self.employee_skills_label.grid(row=1, column=0)
        self.employee_skills_entry = tk.Entry(root)
        self.employee_skills_entry.grid(row=1, column=1)

        self.employee_availability_label = tk.Label(root, text="Employee Availability (comma-separated):")
        self.employee_availability_label.grid(row=2, column=0)
        self.employee_availability_entry = tk.Entry(root)
        self.employee_availability_entry.grid(row=2, column=1)

        self.add_employee_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_employee_button.grid(row=3, column=0, columnspan=2)

        self.shift_time_label = tk.Label(root, text="Shift Time:")
        self.shift_time_label.grid(row=4, column=0)
        self.shift_time_entry = tk.Entry(root)
        self.shift_time_entry.grid(row=4, column=1)

        self.shift_skill_label = tk.Label(root, text="Shift Skill Required:")
        self.shift_skill_label.grid(row=5, column=0)
        self.shift_skill_entry = tk.Entry(root)
        self.shift_skill_entry.grid(row=5, column=1)

        self.add_shift_button = tk.Button(root, text="Add Shift", command=self.add_shift)
        self.add_shift_button.grid(row=6, column=0, columnspan=2)

        self.schedule_button = tk.Button(root, text="Schedule Shifts", command=self.schedule_shifts)
        self.schedule_button.grid(row=7, column=0, columnspan=2)

        self.assigned_shifts_label = tk.Label(root, text="Assigned Shifts:")
        self.assigned_shifts_label.grid(row=8, column=0)
        self.assigned_shifts_text = tk.Text(root, height=5, width=50)
        self.assigned_shifts_text.grid(row=8, column=1)

    def add_employee(self):
        name = self.employee_name_entry.get()
        skills = [s.strip() for s in self.employee_skills_entry.get().split(",")]
        availability = [a.strip() for a in self.employee_availability_entry.get().split(",")]
        self.scheduler.add_employee(name, skills, availability)
        self.update_employee_list()

    def add_shift(self):
        time = self.shift_time_entry.get()
        skill_required = self.shift_skill_entry.get()
        self.scheduler.add_shift(time, skill_required)

    def schedule_shifts(self):
        self.scheduler.assign_shifts()
        assigned_shifts = ""
        for shift in self.scheduler.shifts:
            if shift.assigned_employee:
                assigned_shifts += f"Shift at {shift.time} assigned to {shift.assigned_employee.name} for {shift.skill_required}\n"
            else:
                assigned_shifts += f"No suitable employee found for shift at {shift.time} requiring {shift.skill_required}\n"
        self.assigned_shifts_text.delete(1.0, tk.END)
        self.assigned_shifts_text.insert(tk.END, assigned_shifts)

    def update_employee_list(self):
        self.employee_name_entry.delete(0, tk.END)
        self.employee_skills_entry.delete(0, tk.END)
        self.employee_availability_entry.delete(0, tk.END)

root = tk.Tk()
app = ShiftSchedulerApp(root)
root.mainloop()
