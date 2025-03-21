import tkinter as tk
from Connect import tec_controller 

def start_ramp():
    #grab temps from the input boxes
    temp1123 = temp_input1.get()
    temp1090 = temp_input2.get()
    
    #query which device is connected to which port
    device1 = connection.get_device_type(1)
    device2 = connection.get_device_type(2)
    
    if device1== 1123:
        connection.set_temp(temp1123, 1)
        #connection.set_temp(temp1090, 2) #uncomment this line to enable the 1090 
    else:
        connection.set_temp(temp1090, 1)
        #connection.set_temp(temp1123, 2)
    
    connection.set_enable(1, True)
    #connection.set_enable(2, True) #uncomment this line to enable the 1090

    

def end_ramp():
    print(connection.set_enable(1, False))
    print(connection.set_enable(2, False))
    print("Ending ramp.")

# Create the main window
connection = tec_controller() 

# gui setup
root = tk.Tk()
root.title("Temperature Ramp")

# Create and place the first input box for temperature input
tk.Label(root, text="Temperature 1123 (°C):").grid(row=0, column=0, padx=10, pady=5)
temp_input1 = tk.Entry(root)
temp_input1.grid(row=0, column=1, padx=10, pady=5)

# Create and place the second input box for temperature input
tk.Label(root, text="Temperature 1090 (°C):").grid(row=1, column=0, padx=10, pady=5)
temp_input2 = tk.Entry(root)
temp_input2.grid(row=1, column=1, padx=10, pady=5)

# Create and place the Start Ramp button
start_button = tk.Button(root, text="Start Ramp", command=start_ramp)
start_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the End Ramp button
end_button = tk.Button(root, text="End Ramp", command=end_ramp)
end_button.grid(row=3, column=0, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
