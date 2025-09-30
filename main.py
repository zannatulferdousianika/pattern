import tkinter as tk 
from tkinter import messagebox,ttk

class RestaurantOrderManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")


        self.menu_item={
            "FRIES MEAL":2,
            "COMBO LUNCH": 3,
            "BURGER MEAL": 2,
            "SUBSANDWICH":3,
            "PIZZA MEAL": 4,
            "SPICY NAGA CHICKEN(2 PIECE)": 3,
            "SALAD": 2,
            "DRINKS": 1,
            "SPICY CHOWMIN": 3,
            "ICE CREAM": 2,
            
            "HOT DRINKS":0,
            "COFFEE":1.5,
            "CAPACHINO": 2,
            "LATTE": 2.5,
            "MATCHA TEA": 3,
            "COLD CHOCOLATE COFFEE": 3.5,
            "ICE AMERICANO":3

        }

        self.exchange_rate = 120

        self.setup_background(root)

        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        ttk.abel(frame, text="Restaurant Order Management", font=("Arial",29,"bold")).grid(row=0, columnspan=4,
        padx=10, pady=10)

        self.menu_labels = {}
        self.menu_quantities ={}


        ttk.label(frame, text="Item", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=10)
        ttk.label(frame, text="Price (USD)", font=("Arial", 10, "bold")).grid(row=1, column=1, padx=10)
        ttk.label(frame, text="Price (BDT)", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=10)
        ttk.label(frame, text="Quantity", font=("Arial", 10, "bold")).grid(row=1, column=3, padx=10)


        for i , (item, price) in enumerate(self.mneu_items.items(), start=2):
            #The enumerate() function in Python is a built-in function that 
            # adds a counter to an iterable object (like a list, tuple,
            #  or string) and returns an enumerate object.
            #  This object can then be used in a for loop to access both the index 
            # and the value of each item in the iterable simultaneously.

            bdt_price = price * self.exchange_rate
            ttk.Label(frame, text=f"{item}:", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=5)
            ttk.Label(frame, text=f"${price:.2f}:", font=("Arial", 12)).grid(row=i, column=1, padx=10, pady=5)
            ttk.Label(frame, text=f"৳{bdt_price:.0f}:", font=("Arial", 12)).grid(row=i, column=2, padx=10, pady=5)

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=1, column=3, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry
        
        order_button = ttk.Button(frame, text="Place Order", command=self.place_order)

        order_button.grid(row=len(self.menu_items)+2, column=0, columnspan=2, padx=10, pady=10)


        clear_button = ttk.Button(frame, text="Clear Order", command=self.clear_order)
        clear_button.grid(row=len(self.menu_items)+2, column=2, columnspan=2, padx=10, pady=10)
                

        for entry in self.menu_quantities.values():
            entry.bind("<KeyRelease>", self.update_total)
    def setup_background(self, root):
        bg_width, bg_height = 800,600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

        try:
            original_image = tk.PhotoImage(file="background_png")
            background_image = original_image.subsample(
                max(1, original_image.width() // bg_width),
                max(1, original_image.height() // bg_height))
            canvas.create_image(,,anchor=tk.NW, image+background_image)
            canvas.image = background_image
        except Exception:
            pass
    def place_order(self):
        total_cost=0
        order_summary = "Order Summary: \n"
        symbol = "৳"
        rate = self.exchange_rate
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]*rate
                cost = quantity*price
                total_cost += cost 
                if quantitt > 0:
                    order_summary += f"{item}: {quantity} x {sumbol}{price:.0f} = {sumbol}{cost:.0f}\n"
                    self.clear_order()

                if total_cost >0:
                    order_summary += f"\nTotal Cost: {symbol}{total_cost:.0f}"
                    messagebox.showinfo("Order Placed", order_summary)

                else:
                    messagebox.showerroe("Error", "Please order at least one item.")

    def update_total(self, event=None):
        total_cost = 0
        rate = self.exchange_rate
        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item]*rate
                cost = quantity *price
                total_cost += cost
        self.total_var.set(f"Total: ৳{total_cost:.0f}")

if __name__ =="__main__":
    root = tk.Tk()
    app = R estaurantOrderManagement(root)
    root.geometry("800x600")
    root.mainloop()
