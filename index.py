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
    def __init__(self, employees, shifts):
        self.employees = employees
        self.shifts = shifts

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

# Sample data
employees = [
    Employee("Alice", ["sewing", "cutting"], ["morning", "afternoon"]),
    Employee("Bob", ["sewing"], ["afternoon", "evening"]),
    Employee("Charlie", ["cutting"], ["morning", "evening"])
]

shifts = [
    Shift("morning", "sewing"),
    Shift("afternoon", "cutting"),
    Shift("evening", "sewing")
]

# Creating the GUI
def schedule_shifts():
    scheduler = ShiftScheduler(employees, shifts)
    scheduler.assign_shifts()
    for shift in shifts:
        if shift.assigned_employee:
            print(f"Shift at {shift.time} assigned to {shift.assigned_employee.name}")
        else:
            print(f"No employee assigned for shift at {shift.time}")

root = tk.Tk()
root.title("Shift Scheduler")

btn_schedule = tk.Button(root, text="Schedule Shifts", command=schedule_shifts)
btn_schedule.pack()

root.mainloop()

