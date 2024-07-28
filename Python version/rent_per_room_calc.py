import tkinter as tk

def calculate_rent_per_room(rent, num_rooms, *room_dimensions, bills=None):
    room_areas = []
    for dimension in room_dimensions:
        area = 1
        for d in dimension:
            area *= d
        room_areas.append(area)
    
    total_area = sum(room_areas)
    rent_per_area = rent / total_area
    rent_per_room = []
    for area in room_areas:
        rent_per_room.append(round(area * rent_per_area, 2))
    if bills is not None:
        total_rent_per_room = []
        for rent_room in rent_per_room:
            total_rent_per_room.append(rent_room + bills/num_rooms)
        return total_rent_per_room
    else:
        return rent_per_room

def calculate_rent():
    rent = float(rent_entry.get())
    num_rooms = int(num_rooms_entry.get())
    room_dimensions = []
    for i in range(num_rooms):
        dimension_str = room_dimension_entries[i].get()
        dimension_list = dimension_str.split(",")
        dimension_list = [float(d.strip()) for d in dimension_list]
        room_dimensions.append(dimension_list)
    bills = float(bills_entry.get()) if bills_entry.get() else None

    rent_per_room = calculate_rent_per_room(rent, num_rooms, *room_dimensions, bills=bills)
    for i in range(num_rooms):
        if bills is not None:
            rent_labels[i].configure(text=f"Room {i+1} should pay {rent_per_room[i]:.2f} in rent and bills.")
        else:
            rent_labels[i].configure(text=f"Room {i+1} should pay {rent_per_room[i]:.2f} in rent.")

# Create the main window
root = tk.Tk()
root.title("Room Rent Calculator")

# Create the input widgets
rent_label = tk.Label(root, text="Rental price:")
rent_label.grid(row=0, column=0)
rent_entry = tk.Entry(root)
rent_entry.grid(row=0, column=1)

num_rooms_label = tk.Label(root, text="Number of rooms:")
num_rooms_label.grid(row=1, column=0)
num_rooms_entry = tk.Entry(root)
num_rooms_entry.grid(row=1, column=1)

room_dimension_labels = []
room_dimension_entries = []
for i in range(5):
    room_dimension_labels.append(tk.Label(root, text=f"Dimensions of room {i+1} (comma separated):"))
    room_dimension_labels[i].grid(row=i+2, column=0)
    room_dimension_entries.append(tk.Entry(root))
    room_dimension_entries[i].grid(row=i+2, column=1)

bills_label = tk.Label(root, text="Bills per month (optional):")
bills_label.grid(row=12, column=0)
bills_entry = tk.Entry(root)
bills_entry.grid(row=12, column=1)

# Create the button to calculate the rent
calculate_button = tk.Button(root, text="Calculate", command=calculate_rent)
calculate_button.grid(row=13, column=0)

# Create the output labels
rent_labels = []
for i in range(5):
    rent_labels.append(tk.Label(root, text=""))
    rent_labels[i].grid(row=i+2, column=2)

# Start the GUI main loop
root.mainloop()
