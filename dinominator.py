import tkinter as tk
from tkinter import messagebox
DENOMINATIONS = [1000, 500, 100, 50,20,10]

COLOR_MAP = {
    1000:"#FFD700",
    500:"#FF8C00",
    100:"#FF69B4",
    50: "#ADFF2F",
    20:"#BA55D3",
    10:"#87CEFA"}


def calculate_denominations():
    try:
        amount = int(entry_amount.get())
        if amount < 10:
            raise ValueError("Amount invalid. please give valid ammount")
        remaining = amount
        for widget in frame_result.winfo_children():
            widget.destroy()
        for note in DENOMINATIONS:
            count =remaining//note
            remaining %= note
            if count > 0:
                label = tk.label(frame_result, text=f"{note} Taka x {count} = {note * count} Taka" ,
                                bg= COLOR_MAP[note], fg="black", font=("Arial", 12, "bold"), width=30)
                label.pack(pady=3)
        if remaining > 0:
            tk.Label(frame_result, text=f"Remaining: {remaining} Taka (No matching notes)",
                         fg="red", font=("Arial", 15, "italic")).pack(pady=5)
    except:
        


root = tk.Tk()
root.title("Denomination Calculator")
root.geometry("400x500")
root.config(bg= "#f0f8ff")

tk.label(root, text="Denomination", font=("Arial", 16, "bold"), fg="#2f4f4f", bg="#f0f8ff").pack(pady=15)


tk.label(root, text="Enter amount in Taka", font=("Arial", 12), fg="#f0f8ff").pack()
entry_amount = tk.Entry(root, font=("Arial",12), justify="center")
entry_amount.pack(pady=10)


btn_calculate = tk.Button(root, text="Calculate Notes", font=("Arial",12, "bold"),
                          bg = "#4682b4", fg="white", command=calculate_denominations)

btn_calculate.pack(pady=10)
frame_result = tk.Frame(root, bg="#e6f2ff", bd=2, relief="ridge")
frame_result.pack(pady=10, fill="both", expand=True)
root.mainloop()
    

