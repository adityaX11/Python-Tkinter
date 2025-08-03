# UPDATE-> 0.0.1

# import tkinter as tk
# from tkinter import messagebox, filedialog, ttk
# from datetime import datetime
# import os

# HISTORY_FILE = "history.txt"

# SHOP_ITEMS = ["Pizza", "Burger", "Fries", "Coke", "Salad", "Pasta", "Ice Cream", "Coffee"]

# def load_history_from_file():
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#             return f.read()
#     return ""

# def save_invoice_to_file(invoice_text: str):
#     with open(HISTORY_FILE, "a", encoding="utf-8") as f:
#         f.write(invoice_text + "\n" + "-" * 50 + "\n\n")

# def clear_history():
#     if not os.path.exists(HISTORY_FILE) or os.stat(HISTORY_FILE).st_size == 0:
#         messagebox.showinfo("Already Empty", "No history to clear.")
#         return

#     confirm = messagebox.askyesno("Confirm Delete", "Do you want to back up history before deleting?")
#     if confirm:
#         save_history_backup()

#     try:
#         with open(HISTORY_FILE, "w", encoding="utf-8"):
#             pass
#         update_history_display()
#         messagebox.showinfo("Success", "History cleared successfully.")
#     except Exception as e:
#         messagebox.showerror("Error", f"Failed to clear history.\n{e}")

# def save_history_backup():
#     backup_path = filedialog.asksaveasfilename(
#         defaultextension=".txt",
#         filetypes=[("Text Files", "*.txt")],
#         title="Save History Backup As"
#     )
#     if backup_path:
#         with open(HISTORY_FILE, "r", encoding="utf-8") as original, open(backup_path, "w", encoding="utf-8") as backup:
#             backup.write(original.read())
#         messagebox.showinfo("Backup Saved", f"History saved to:\n{backup_path}")

# def generate_invoice_gui():
#     customer_name = name_entry.get().strip() or "Guest"
#     items_text = item_entry.get().strip()
#     all_items = [item.strip() for item in items_text.split(",") if item.strip()]

#     try:
#         tax = float(tax_entry.get() or 0)
#         delivery = float(delivery_entry.get() or 0)
#         service = float(service_entry.get() or 0)
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Charges must be numbers.")
#         return

#     charges = {"Tax": tax, "Delivery": delivery, "Service": service}
#     total = sum(charges.values())
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     lines = [f"Invoice for {customer_name}:\n"]
#     lines.append(f"Date: {timestamp}")

#     if all_items:
#         lines.append("Items:")
#         for item in all_items:
#             lines.append(f"- {item}")

#     if any(val > 0 for val in charges.values()):
#         lines.append("Charges:")
#         for key, value in charges.items():
#             if value > 0:
#                 lines.append(f"{key}: ₹{value:.1f}")

#     lines.append(f"Total Amount Due: ₹{total:.1f}")

#     invoice_text = "\n".join(lines)
#     save_invoice_to_file(invoice_text)
#     update_history_display()

# def update_history_display():
#     content = load_history_from_file()
#     history_output.config(state="normal")
#     history_output.delete("1.0", tk.END)
#     history_output.insert(tk.END, content)
#     history_output.config(state="disabled")

# def add_item_from_dropdown():
#     selected_item = item_combobox.get()
#     current_text = item_entry.get().strip()
#     updated_text = f"{current_text}, {selected_item}" if current_text else selected_item
#     item_entry.delete(0, tk.END)
#     item_entry.insert(0, updated_text)

# # ---------- GUI Setup ----------
# root = tk.Tk()
# root.title(" ---------------------------------------------------------------Invoice Generator with Item Dropdown--------------------------------------------------------------")
# root.geometry("700x850")
# root.config(bg="#f9f9f9")

# tk.Label(root, text="Customer Name:", bg="#f9f9f9").pack(pady=(10, 0))
# name_entry = tk.Entry(root, width=50)
# name_entry.pack(pady=5)

# # Item Section
# tk.Label(root, text="Select Item from Shop:", bg="#f9f9f9").pack()
# item_frame = tk.Frame(root, bg="#f9f9f9")
# item_frame.pack(pady=5)

# item_combobox = ttk.Combobox(item_frame, values=SHOP_ITEMS, state="readonly", width=30)
# item_combobox.set("Select Item")
# item_combobox.grid(row=0, column=0, padx=5)

# tk.Button(item_frame, text="➕ Add Item", command=add_item_from_dropdown, bg="#2196F3", fg="white").grid(row=0, column=1)

# tk.Label(root, text="Manual Items (comma-separated):", bg="#f9f9f9").pack(pady=(10, 0))
# item_entry = tk.Entry(root, width=50)
# item_entry.pack(pady=5)

# # Charges Section
# tk.Label(root, text="Charges (leave blank if none):", bg="#f9f9f9", font=("Arial", 10, "bold")).pack(pady=(20, 5))
# charges_frame = tk.Frame(root, bg="#f9f9f9")
# charges_frame.pack()

# tk.Label(charges_frame, text="Tax ₹", bg="#f9f9f9").grid(row=0, column=0, padx=5, pady=5)
# tax_entry = tk.Entry(charges_frame, width=10)
# tax_entry.grid(row=0, column=1)

# tk.Label(charges_frame, text="Delivery ₹", bg="#f9f9f9").grid(row=0, column=2, padx=5)
# delivery_entry = tk.Entry(charges_frame, width=10)
# delivery_entry.grid(row=0, column=3)

# tk.Label(charges_frame, text="Service ₹", bg="#f9f9f9").grid(row=0, column=4, padx=5)
# service_entry = tk.Entry(charges_frame, width=10)
# service_entry.grid(row=0, column=5)

# # Buttons
# button_frame = tk.Frame(root, bg="#f9f9f9")
# button_frame.pack(pady=15)

# tk.Button(button_frame, text="🧾 Generate Invoice", command=generate_invoice_gui, bg="#4CAF50", fg="white", width=20).grid(row=0, column=0, padx=10)
# tk.Button(button_frame, text="🗑️ Clear History", command=clear_history, bg="red", fg="white", width=20).grid(row=0, column=1, padx=10)

# # History Area
# tk.Label(root, text="Invoice History", bg="#f9f9f9", font=("Arial", 12, "bold")).pack()

# history_output = tk.Text(root, height=25, width=85, font=("Courier", 10), wrap="word")
# history_output.pack(pady=10)
# history_output.config(state="disabled")

# scrollbar = tk.Scrollbar(root, command=history_output.yview)
# scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# history_output.config(yscrollcommand=scrollbar.set)

# update_history_display()
# root.mainloop()

# UPDATE-> 0.0.2

# import tkinter as tk
# from tkinter import messagebox, ttk
# from datetime import datetime
# import os

# # ---------- File Setup ----------
# HISTORY_FILE = "invoice_history.txt"

# # ---------- Utility Functions ----------

# def save_invoice_to_file(invoice_text):
#     with open(HISTORY_FILE, "a", encoding="utf-8") as f:
#         f.write(invoice_text + "\n" + "-" * 50 + "\n")

# def load_history():
#     if not os.path.exists(HISTORY_FILE):
#         return ""
#     with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#         return f.read()

# def update_history_display():
#     history_text.delete(1.0, tk.END)
#     history = load_history()
#     history_text.insert(tk.END, history)
#     refresh_date_list()

# def refresh_date_list():
#     dates = set()
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#             for line in f:
#                 if line.startswith("Date:"):
#                     date_only = line.split("Date:")[1].strip().split(" ")[0]
#                     dates.add(date_only)
#     date_combo['values'] = sorted(list(dates))
#     if dates:
#         date_combo.current(0)
#     else:
#         date_combo.set("No Dates")

# def clear_all_history():
#     if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete ALL history?"):
#         open(HISTORY_FILE, "w", encoding="utf-8").close()
#         update_history_display()
#         messagebox.showinfo("Deleted", "All history cleared.")

# def delete_history_by_date():
#     selected_date = date_combo.get()
#     if selected_date in ("Select Date", "No Dates", ""):
#         messagebox.showwarning("Select Date", "Please select a valid date to delete.")
#         return

#     if not os.path.exists(HISTORY_FILE):
#         return

#     with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#         lines = f.readlines()

#     keep_lines = []
#     skip_block = False
#     for line in lines:
#         if line.startswith("Date:"):
#             current_date = line.split("Date:")[1].strip().split(" ")[0]
#             skip_block = (current_date == selected_date)
#         if not skip_block:
#             keep_lines.append(line)

#     with open(HISTORY_FILE, "w", encoding="utf-8") as f:
#         f.writelines(keep_lines)

#     update_history_display()
#     messagebox.showinfo("Deleted", f"History for {selected_date} deleted.")

# def generate_invoice_gui():
#     customer_name = name_entry.get() or "Guest"
#     selected_item = item_var.get()
#     custom_item = manual_item_entry.get()
#     items = []

#     if selected_item and selected_item != "Choose Item":
#         items.append(selected_item)
#     if custom_item:
#         items.extend(i.strip() for i in custom_item.split(",") if i.strip())

#     try:
#         tax = float(tax_entry.get() or 0)
#         delivery = float(delivery_entry.get() or 0)
#         service = float(service_entry.get() or 0)
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Charges must be numbers.")
#         return

#     charges = {"Tax": tax, "Delivery": delivery, "Service": service}
#     total = sum(charges.values())
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#     lines = [f"Invoice for {customer_name}:"]
#     lines.append(f"Date: {timestamp}")
#     if items:
#         lines.append("Items:")
#         for item in items:
#             lines.append(f"- {item}")
#     if any(val > 0 for val in charges.values()):
#         lines.append("Charges:")
#         for key, value in charges.items():
#             if value > 0:
#                 lines.append(f"{key}: ₹{value:.1f}")
#     lines.append(f"Total Amount Due: ₹{total:.1f}")

#     invoice_text = "\n".join(lines)
#     save_invoice_to_file(invoice_text)
#     update_history_display()
#     messagebox.showinfo("Invoice Generated", "Invoice has been saved and added to history.")

# # ---------- GUI Setup ----------
# root = tk.Tk()
# root.title("🧾 INVOICE GENERATOR ")
# root.geometry("880x880")
# root.configure(bg="light blue")

# title = tk.Label(root, text="🧾 Shop Invoice Generator", font=("Arial", 20, "bold"), bg="#f5f5f5", fg="#333")
# title.pack(pady=10)

# form_frame = tk.Frame(root, bg="#f5f5f5")
# form_frame.pack(pady=10)

# # Customer name
# tk.Label(form_frame, text="Customer Name:", bg="#f5f5f5").grid(row=0, column=0, sticky="e", padx=5, pady=5)
# name_entry = tk.Entry(form_frame, width=30)
# name_entry.grid(row=0, column=1, padx=5, pady=5)

# # Item dropdown
# tk.Label(form_frame, text="Select Item:", bg="#f5f5f5").grid(row=1, column=0, sticky="e", padx=5, pady=5)
# item_var = tk.StringVar()
# item_options = ["Burger", "Pizza", "Pasta", "Coke", "Fries", "Sandwich", "Salad"]
# item_menu = ttk.Combobox(form_frame, textvariable=item_var, values=item_options, state="readonly", width=28)
# item_menu.set("Choose Item")
# item_menu.grid(row=1, column=1, padx=5, pady=5)

# # Manual item entry
# tk.Label(form_frame, text="Add Items (comma-separated):", bg="#f5f5f5").grid(row=2, column=0, sticky="e", padx=5, pady=5)
# manual_item_entry = tk.Entry(form_frame, width=30)
# manual_item_entry.grid(row=2, column=1, padx=5, pady=5)

# # Charges
# tk.Label(form_frame, text="Tax:", bg="#f5f5f5").grid(row=3, column=0, sticky="e", padx=5, pady=5)
# tax_entry = tk.Entry(form_frame, width=30)
# tax_entry.grid(row=3, column=1, padx=5, pady=5)

# tk.Label(form_frame, text="Delivery:", bg="#f5f5f5").grid(row=4, column=0, sticky="e", padx=5, pady=5)
# delivery_entry = tk.Entry(form_frame, width=30)
# delivery_entry.grid(row=4, column=1, padx=5, pady=5)

# tk.Label(form_frame, text="Service:", bg="#f5f5f5").grid(row=5, column=0, sticky="e", padx=5, pady=5)
# service_entry = tk.Entry(form_frame, width=30)
# service_entry.grid(row=5, column=1, padx=5, pady=5)

# generate_btn = tk.Button(root, text="Generate Invoice", command=generate_invoice_gui, bg="#4caf50", fg="white", width=30)
# generate_btn.pack(pady=10)

# # ---------- History Area ----------
# tk.Label(root, text="Invoice History", font=("Arial", 14, "bold"), bg="#f5f5f5").pack(pady=5)
# history_text = tk.Text(root, height=20, width=100, wrap="word", font=("Courier", 10))
# history_text.pack(pady=5)

# # ---------- Delete Section ----------
# delete_frame = tk.Frame(root, bg="#f5f5f5")
# delete_frame.pack(pady=5)

# tk.Label(delete_frame, text="Select Date to Delete:", bg="#f5f5f5").grid(row=0, column=0, padx=5)
# date_combo = ttk.Combobox(delete_frame, state="readonly", width=20)
# date_combo.grid(row=0, column=1, padx=5)

# delete_btn = tk.Button(delete_frame, text="🗑️ Delete Selected Date", command=delete_history_by_date, bg="tomato", fg="white")
# delete_btn.grid(row=0, column=2, padx=10)

# clear_all_btn = tk.Button(delete_frame, text="🧹 Clear All History", command=clear_all_history, bg="red", fg="white")
# clear_all_btn.grid(row=0, column=3, padx=10)

# # Initial display
# update_history_display()
# root.mainloop()


# UPDATE -> 0.0.3

# import tkinter as tk
# from tkinter import messagebox, ttk
# from datetime import datetime
# import os
# import re

# # ---------- File and Data Setup ----------
# HISTORY_FILE = "invoice_history.txt"

# # Prices for predefined items
# ITEM_PRICES = {
#     "Burger": 150.00, "Pizza": 450.00, "Pasta": 250.00, "Coke": 40.00,
#     "Fries": 90.00, "Sandwich": 120.00, "Salad": 180.00, "Coffee": 100.00,
#     "Ice Cream": 80.00
# }


# # ---------- Utility Functions ----------

# def save_invoice_to_file(invoice_text):
#     """Appends a new invoice to the history file."""
#     with open(HISTORY_FILE, "a", encoding="utf-8") as f:
#         f.write(invoice_text + "\n" + "-" * 50 + "\n")

# def load_history():
#     """Loads all invoice history from the file."""
#     if not os.path.exists(HISTORY_FILE):
#         return ""
#     with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#         return f.read()

# def update_history_display():
#     """Refreshes the history text area and the date dropdown."""
#     history_text.delete(1.0, tk.END)
#     history = load_history()
#     history_text.insert(tk.END, history)
#     refresh_date_list()

# def refresh_date_list():
#     """Updates the dropdown list with dates from the history file."""
#     dates = set()
#     if os.path.exists(HISTORY_FILE):
#         with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#             for line in f:
#                 if line.startswith("Date:"):
#                     # **FIX**: Logic updated for the new date-only format.
#                     date_only = line.split("Date:")[1].strip()
#                     dates.add(date_only)
    
#     sorted_dates = sorted(list(dates), reverse=True)
#     date_combo['values'] = sorted_dates
#     if dates:
#         date_combo.set("Select Date")
#     else:
#         date_combo.set("No Dates")

# def clear_all_history():
#     """Deletes the entire invoice history file after confirmation."""
#     if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete ALL history? This cannot be undone."):
#         if os.path.exists(HISTORY_FILE):
#             os.remove(HISTORY_FILE)
#         update_history_display()
#         messagebox.showinfo("Deleted", "All history has been cleared.")

# def delete_history_by_date():
#     """Deletes invoices matching the selected date."""
#     selected_date = date_combo.get()
#     if selected_date in ("Select Date", "No Dates", ""):
#         messagebox.showwarning("Select Date", "Please select a valid date to delete.")
#         return
#     if not os.path.exists(HISTORY_FILE):
#         return
#     with open(HISTORY_FILE, "r", encoding="utf-8") as f:
#         lines = f.readlines()
#     keep_lines = []
#     skip_block = False
#     for line in lines:
#         if line.startswith("Date:"):
#             # **FIX**: Logic updated for the new date-only format.
#             current_date = line.split("Date:")[1].strip()
#             skip_block = (current_date == selected_date)
#         elif line.strip() == "-" * 50:
#             if not skip_block:
#                 keep_lines.append(line)
#             skip_block = False
#             continue
#         if not skip_block:
#             keep_lines.append(line)
#     with open(HISTORY_FILE, "w", encoding="utf-8") as f:
#         f.writelines(keep_lines)
#     update_history_display()
#     messagebox.showinfo("Deleted", f"History for {selected_date} has been deleted.")

# # --- Item handling functions ---

# def add_items():
#     """Moves selected predefined items to the 'Selected' list."""
#     selected_indices = available_listbox.curselection()
#     for i in reversed(selected_indices):
#         item_name = available_listbox.get(i)
#         price = ITEM_PRICES.get(item_name, 0.0)
#         formatted_item = f"{item_name} (₹{price:.2f})"
#         selected_listbox.insert(tk.END, formatted_item)
#         available_listbox.delete(i)

# def remove_items():
#     """Moves items from 'Selected' back to 'Available'."""
#     selected_indices = selected_listbox.curselection()
#     for i in reversed(selected_indices):
#         item_with_price = selected_listbox.get(i)
#         item_name = item_with_price.split(" (₹")[0]
#         if item_name in ITEM_PRICES:
#             available_listbox.insert(tk.END, item_name)
#         selected_listbox.delete(i)
#     sorted_list = sorted(available_listbox.get(0, tk.END))
#     available_listbox.delete(0, tk.END)
#     for item in sorted_list:
#         available_listbox.insert(tk.END, item)

# def add_custom_item():
#     """Adds a manually entered item to the 'Selected' list."""
#     name = custom_name_entry.get().strip()
#     price_str = custom_price_entry.get().strip()
#     if not name or not price_str:
#         messagebox.showwarning("Input Missing", "Please enter both a name and a price.")
#         return
#     try:
#         price = float(price_str)
#         formatted_item = f"{name} (₹{price:.2f})"
#         selected_listbox.insert(tk.END, formatted_item)
#         custom_name_entry.delete(0, tk.END)
#         custom_price_entry.delete(0, tk.END)
#     except ValueError:
#         messagebox.showerror("Invalid Price", "Please enter a valid number for the price.")

# def reset_all_inputs():
#     """Clears all input fields."""
#     name_entry.delete(0, tk.END)
#     custom_name_entry.delete(0, tk.END)
#     custom_price_entry.delete(0, tk.END)
#     tax_entry.delete(0, tk.END)
#     delivery_entry.delete(0, tk.END)
#     service_entry.delete(0, tk.END)
    
#     items_to_move = selected_listbox.get(0, tk.END)
#     for item_with_price in items_to_move:
#         item_name = item_with_price.split(" (₹")[0]
#         if item_name in ITEM_PRICES:
#             available_listbox.insert(tk.END, item_name)
#     selected_listbox.delete(0, tk.END)
#     sorted_list = sorted(available_listbox.get(0, tk.END))
#     available_listbox.delete(0, tk.END)
#     for item in sorted_list:
#         available_listbox.insert(tk.END, item)
#     # Switch back to the first tab
#     notebook.select(tab1)


# # --- Invoice Generation Logic ---
# def generate_invoice_gui():
#     """Generates the invoice from all inputs."""
#     customer_name = name_entry.get() or "Guest"
#     items_with_prices = selected_listbox.get(0, tk.END)

#     if not items_with_prices:
#          messagebox.showwarning("Empty Invoice", "Please add at least one item to the invoice.")
#          notebook.select(tab1) # Switch to item tab
#          return

#     try:
#         subtotal = 0.0
#         for item in items_with_prices:
#             match = re.search(r'₹([\d.]+)', item)
#             if match:
#                 subtotal += float(match.group(1))

#         tax = float(tax_entry.get() or 0)
#         delivery = float(delivery_entry.get() or 0)
#         service = float(service_entry.get() or 0)
#         grand_total = subtotal + tax + delivery + service
        
#     except ValueError:
#         messagebox.showerror("Invalid Input", "Charges must be valid numbers.")
#         return

#     # **FIX**: Timestamp now stores date only in a cleaner format.
#     timestamp = datetime.now().strftime("%d-%b-%Y") 

#     lines = [f"Invoice for: {customer_name}", f"Date: {timestamp}", "-" * 40, "Items:"]
#     lines.extend([f"- {item}" for item in items_with_prices])
#     lines.extend(["-" * 40, f"Subtotal: ₹{subtotal:.2f}"])
    
#     if tax > 0: lines.append(f"Tax: ₹{tax:.2f}")
#     if delivery > 0: lines.append(f"Delivery: ₹{delivery:.2f}")
#     if service > 0: lines.append(f"Service Charge: ₹{service:.2f}")

#     lines.extend(["=" * 40, f"GRAND TOTAL: ₹{grand_total:.2f}"])

#     invoice_text = "\n".join(lines)
#     save_invoice_to_file(invoice_text)
#     update_history_display()
#     messagebox.showinfo("Invoice Generated", "Invoice has been saved and added to history.")
#     reset_all_inputs()


# # ---------- GUI Setup ----------
# root = tk.Tk()
# root.title("🧾 Invoice Pro")
# root.geometry("1000x750")
# # Set a theme for a modern look
# style = ttk.Style(root)
# style.theme_use('clam') # Other options: 'alt', 'default', 'classic'

# # Main layout frames
# main_frame = ttk.Frame(root, padding="10")
# main_frame.pack(fill="both", expand=True)

# left_frame = ttk.Frame(main_frame)
# left_frame.pack(side="left", fill="y", padx=(0, 10), anchor="n")

# right_frame = ttk.Frame(main_frame)
# right_frame.pack(side="right", fill="both", expand=True)

# # --- LEFT FRAME: Tabbed Interface for Invoice Creation ---
# notebook = ttk.Notebook(left_frame)
# notebook.pack(fill="y", expand=True)

# tab1 = ttk.Frame(notebook, padding="10")
# tab2 = ttk.Frame(notebook, padding="10")

# notebook.add(tab1, text=' 1. Add Items ')
# notebook.add(tab2, text=' 2. Charges & Generate ')

# # --- TAB 1: Item Management ---
# ttk.Label(tab1, text="Customer Name:", font=("", 10, "bold")).pack(anchor="w")
# name_entry = ttk.Entry(tab1, width=40, font=("", 10))
# name_entry.pack(anchor="w", pady=(2, 10), fill="x")

# ttk.Label(tab1, text="Available Items", font=("", 10, "bold")).pack(anchor="w", pady=(5, 2))
# available_listbox = tk.Listbox(tab1, selectmode=tk.EXTENDED, height=8, exportselection=False, font=("", 10))
# for item in sorted(ITEM_PRICES.keys()):
#     available_listbox.insert(tk.END, item)
# available_listbox.pack(fill="x", expand=True)

# button_frame = ttk.Frame(tab1)
# button_frame.pack(pady=5)
# add_button = ttk.Button(button_frame, text="Add Selected ↓", command=add_items)
# add_button.pack(side="left", padx=5)
# remove_button = ttk.Button(button_frame, text="↑ Remove Selected", command=remove_items)
# remove_button.pack(side="left", padx=5)

# ttk.Label(tab1, text="Selected Items", font=("", 10, "bold")).pack(anchor="w", pady=(5, 2))
# selected_listbox = tk.Listbox(tab1, selectmode=tk.EXTENDED, height=8, exportselection=False, font=("", 10))
# selected_listbox.pack(fill="x", expand=True)

# custom_item_frame = ttk.LabelFrame(tab1, text="Add Custom Item", padding="10")
# custom_item_frame.pack(pady=15, fill="x")
# ttk.Label(custom_item_frame, text="Item Name:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
# custom_name_entry = ttk.Entry(custom_item_frame, width=20)
# custom_name_entry.grid(row=0, column=1, padx=5, pady=2)
# ttk.Label(custom_item_frame, text="Price (₹):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
# custom_price_entry = ttk.Entry(custom_item_frame, width=10)
# custom_price_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
# add_custom_btn = ttk.Button(custom_item_frame, text="Add", command=add_custom_item)
# add_custom_btn.grid(row=0, column=2, rowspan=2, padx=10, sticky="ns")

# # --- TAB 2: Charges and Finalization ---
# charges_frame = ttk.LabelFrame(tab2, text="Additional Charges", padding="10")
# charges_frame.pack(pady=10, fill="x")
# ttk.Label(charges_frame, text="Tax (₹):").grid(row=0, column=0, sticky="w", pady=2)
# tax_entry = ttk.Entry(charges_frame, width=12)
# tax_entry.grid(row=0, column=1, padx=5, pady=2)
# ttk.Label(charges_frame, text="Delivery (₹):").grid(row=1, column=0, sticky="w", pady=2)
# delivery_entry = ttk.Entry(charges_frame, width=12)
# delivery_entry.grid(row=1, column=1, padx=5, pady=2)
# ttk.Label(charges_frame, text="Service (₹):").grid(row=2, column=0, sticky="w", pady=2)
# service_entry = ttk.Entry(charges_frame, width=12)
# service_entry.grid(row=2, column=1, padx=5, pady=2)

# ttk.Separator(tab2, orient='horizontal').pack(fill='x', pady=20)

# style.configure('Success.TButton', font=('Helvetica', 12, 'bold'), background='#4CAF50')
# generate_btn = ttk.Button(tab2, text="✅ Generate Invoice", command=generate_invoice_gui, style='Success.TButton')
# generate_btn.pack(pady=15, ipady=8, fill='x')

# # --- RIGHT FRAME: History and Deletion ---
# ttk.Label(right_frame, text="🧾 Invoice History", font=("", 16, "bold")).pack(pady=(0, 10))
# history_text_frame = ttk.Frame(right_frame)
# history_text_frame.pack(fill="both", expand=True)
# history_scrollbar = ttk.Scrollbar(history_text_frame)
# history_scrollbar.pack(side="right", fill="y")
# history_text = tk.Text(history_text_frame, wrap="word", font=("Courier New", 10), yscrollcommand=history_scrollbar.set, relief="solid", borderwidth=1)
# history_text.pack(side="left", fill="both", expand=True)
# history_scrollbar.config(command=history_text.yview)

# delete_frame = ttk.Frame(right_frame, padding=(0, 10))
# delete_frame.pack(fill="x")
# ttk.Label(delete_frame, text="Delete by Date:").grid(row=0, column=0, padx=5)
# date_combo = ttk.Combobox(delete_frame, state="readonly", width=15)
# date_combo.grid(row=0, column=1, padx=5)
# delete_btn = ttk.Button(delete_frame, text="🗑️ Delete", command=delete_history_by_date)
# delete_btn.grid(row=0, column=2, padx=10)
# clear_all_btn = ttk.Button(delete_frame, text="🧹 Clear All", command=clear_all_history)
# clear_all_btn.grid(row=0, column=3, padx=10)

# # --- Initial Display ---
# update_history_display()
# root.mainloop()

# UPDATE-> 0.0.4

import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from datetime import datetime
import os
import re

# ---------- File and Data Setup ----------
HISTORY_FILE = "invoice_history.txt"

# Prices for predefined items
ITEM_PRICES = {
    "Burger": 150.00, "Pizza": 450.00, "Pasta": 250.00, "Coke": 40.00,
    "Fries": 90.00, "Sandwich": 120.00, "Salad": 180.00, "Coffee": 100.00,
    "Ice Cream": 80.00
}


# ---------- Utility Functions ----------

def save_invoice_to_file(invoice_text):
    """Appends a new invoice to the history file."""
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(invoice_text + "\n" + "-" * 50 + "\n")

def load_history():
    """Loads all invoice history from the file."""
    if not os.path.exists(HISTORY_FILE):
        return ""
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        return f.read()

def update_history_display():
    """Refreshes the history text area and the date dropdown."""
    history_text.delete(1.0, tk.END)
    history = load_history()
    history_text.insert(tk.END, history)
    refresh_date_list()

def refresh_date_list():
    """Updates the dropdown list with dates from the history file."""
    dates = set()
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith("Date:"):
                    # **FIX**: Reverted to split the time off to get the date.
                    date_only = line.split("Date:")[1].strip().split(" ")[0]
                    dates.add(date_only)
    
    sorted_dates = sorted(list(dates), reverse=True)
    date_combo['values'] = sorted_dates
    if dates:
        date_combo.set("Select Date")
    else:
        date_combo.set("No Dates")

def clear_all_history():
    """Deletes the entire invoice history file after confirmation."""
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete ALL history? This cannot be undone."):
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
        update_history_display()
        messagebox.showinfo("Deleted", "All history has been cleared.")

def delete_history_by_date():
    """Deletes invoices matching the selected date."""
    selected_date = date_combo.get()
    if selected_date in ("Select Date", "No Dates", ""):
        messagebox.showwarning("Select Date", "Please select a valid date to delete.")
        return
    if not os.path.exists(HISTORY_FILE):
        return
    with open(HISTORY_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    keep_lines = []
    skip_block = False
    for line in lines:
        if line.startswith("Date:"):
            # **FIX**: Reverted to split the time off to get the date for comparison.
            current_date = line.split("Date:")[1].strip().split(" ")[0]
            skip_block = (current_date == selected_date)
        elif line.strip() == "-" * 50:
            if not skip_block:
                keep_lines.append(line)
            skip_block = False
            continue
        if not skip_block:
            keep_lines.append(line)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        f.writelines(keep_lines)
    update_history_display()
    messagebox.showinfo("Deleted", f"History for {selected_date} has been deleted.")

# --- Item handling functions ---

def add_items():
    """Moves selected predefined items to the 'Selected' list."""
    selected_indices = available_listbox.curselection()
    for i in reversed(selected_indices):
        item_name = available_listbox.get(i)
        price = ITEM_PRICES.get(item_name, 0.0)
        formatted_item = f"{item_name} (₹{price:.2f})"
        selected_listbox.insert(tk.END, formatted_item)
        available_listbox.delete(i)

def remove_items():
    """Moves items from 'Selected' back to 'Available'."""
    selected_indices = selected_listbox.curselection()
    for i in reversed(selected_indices):
        item_with_price = selected_listbox.get(i)
        item_name = item_with_price.split(" (₹")[0]
        if item_name in ITEM_PRICES:
            available_listbox.insert(tk.END, item_name)
        selected_listbox.delete(i)
    sorted_list = sorted(available_listbox.get(0, tk.END))
    available_listbox.delete(0, tk.END)
    for item in sorted_list:
        available_listbox.insert(tk.END, item)

def add_custom_item():
    """Adds a manually entered item to the 'Selected' list."""
    name = custom_name_entry.get().strip()
    price_str = custom_price_entry.get().strip()
    if not name or not price_str:
        messagebox.showwarning("Input Missing", "Please enter both a name and a price.")
        return
    try:
        price = float(price_str)
        formatted_item = f"{name} (₹{price:.2f})"
        selected_listbox.insert(tk.END, formatted_item)
        custom_name_entry.delete(0, tk.END)
        custom_price_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Invalid Price", "Please enter a valid number for the price.")

def edit_selected_item_price(event):
    """Opens a dialog to edit the price of a double-clicked item."""
    if not selected_listbox.curselection():
        return
        
    selected_index = selected_listbox.curselection()[0]
    item_string = selected_listbox.get(selected_index)
    
    match = re.match(r'^(.*?) \(₹([\d.]+)\)$', item_string)
    if not match:
        messagebox.showerror("Error", "Could not parse the selected item's price.")
        return
        
    item_name, current_price_str = match.groups()
    current_price = float(current_price_str)
    
    new_price = simpledialog.askfloat(
        "Edit Price",
        f"Enter new price for:\n{item_name}",
        initialvalue=current_price,
        minvalue=0.0,
        parent=root
    )
    
    if new_price is not None:
        new_item_string = f"{item_name} (₹{new_price:.2f})"
        selected_listbox.delete(selected_index)
        selected_listbox.insert(selected_index, new_item_string)
        selected_listbox.select_set(selected_index)


def reset_all_inputs():
    """Clears all input fields."""
    name_entry.delete(0, tk.END)
    custom_name_entry.delete(0, tk.END)
    custom_price_entry.delete(0, tk.END)
    tax_entry.delete(0, tk.END)
    delivery_entry.delete(0, tk.END)
    service_entry.delete(0, tk.END)
    
    items_to_move = selected_listbox.get(0, tk.END)
    for item_with_price in items_to_move:
        item_name = item_with_price.split(" (₹")[0]
        if item_name in ITEM_PRICES:
            available_listbox.insert(tk.END, item_name)
    selected_listbox.delete(0, tk.END)
    sorted_list = sorted(available_listbox.get(0, tk.END))
    available_listbox.delete(0, tk.END)
    for item in sorted_list:
        available_listbox.insert(tk.END, item)
    notebook.select(tab1)


# --- Invoice Generation Logic ---
def generate_invoice_gui():
    """Generates the invoice from all inputs."""
    customer_name = name_entry.get() or "Guest"
    items_with_prices = selected_listbox.get(0, tk.END)

    if not items_with_prices:
         messagebox.showwarning("Empty Invoice", "Please add at least one item to the invoice.")
         notebook.select(tab1)
         return

    try:
        subtotal = 0.0
        for item in items_with_prices:
            match = re.search(r'₹([\d.]+)', item)
            if match:
                subtotal += float(match.group(1))

        tax = float(tax_entry.get() or 0)
        delivery = float(delivery_entry.get() or 0)
        service = float(service_entry.get() or 0)
        grand_total = subtotal + tax + delivery + service
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Charges must be valid numbers.")
        return

    # **FIX**: Timestamp now includes the time again.
    timestamp = datetime.now().strftime("%d-%b-%Y %H:%M:%S") 

    lines = [f"Invoice for: {customer_name}", f"Date: {timestamp}", "-" * 40, "Items:"]
    lines.extend([f"- {item}" for item in items_with_prices])
    lines.extend(["-" * 40, f"Subtotal: ₹{subtotal:.2f}"])
    
    if tax > 0: lines.append(f"Tax: ₹{tax:.2f}")
    if delivery > 0: lines.append(f"Delivery: ₹{delivery:.2f}")
    if service > 0: lines.append(f"Service Charge: ₹{service:.2f}")

    lines.extend(["=" * 40, f"GRAND TOTAL: ₹{grand_total:.2f}"])

    invoice_text = "\n".join(lines)
    save_invoice_to_file(invoice_text)
    update_history_display()
    messagebox.showinfo("Invoice Generated", "Invoice has been saved and added to history.")
    reset_all_inputs()


# ---------- GUI Setup ----------
root = tk.Tk()
root.title("🧾 Invoice Pro")
root.geometry("1000x750")
style = ttk.Style(root)
style.theme_use('clam')

# Main layout frames
main_frame = ttk.Frame(root, padding="10")
main_frame.pack(fill="both", expand=True)

left_frame = ttk.Frame(main_frame)
left_frame.pack(side="left", fill="y", padx=(0, 10), anchor="n")

right_frame = ttk.Frame(main_frame)
right_frame.pack(side="right", fill="both", expand=True)

# --- LEFT FRAME: Tabbed Interface for Invoice Creation ---
notebook = ttk.Notebook(left_frame)
notebook.pack(fill="y", expand=True)

tab1 = ttk.Frame(notebook, padding="10")
tab2 = ttk.Frame(notebook, padding="10")

notebook.add(tab1, text=' 1. Add Items ')
notebook.add(tab2, text=' 2. Charges & Generate ')

# --- TAB 1: Item Management ---
ttk.Label(tab1, text="Customer Name:", font=("", 10, "bold")).pack(anchor="w")
name_entry = ttk.Entry(tab1, width=40, font=("", 10))
name_entry.pack(anchor="w", pady=(2, 10), fill="x")

ttk.Label(tab1, text="Available Items", font=("", 10, "bold")).pack(anchor="w", pady=(5, 2))
available_listbox = tk.Listbox(tab1, selectmode=tk.EXTENDED, height=8, exportselection=False, font=("", 10))
for item in sorted(ITEM_PRICES.keys()):
    available_listbox.insert(tk.END, item)
available_listbox.pack(fill="x", expand=True)

button_frame = ttk.Frame(tab1)
button_frame.pack(pady=5)
add_button = ttk.Button(button_frame, text="Add Selected ↓", command=add_items)
add_button.pack(side="left", padx=5)
remove_button = ttk.Button(button_frame, text="↑ Remove Selected", command=remove_items)
remove_button.pack(side="left", padx=5)

ttk.Label(tab1, text="Selected Items (Double-click to edit price)", font=("", 10, "bold")).pack(anchor="w", pady=(5, 2))
selected_listbox = tk.Listbox(tab1, selectmode=tk.SINGLE, height=8, exportselection=False, font=("", 10))
selected_listbox.pack(fill="x", expand=True)
selected_listbox.bind('<Double-1>', edit_selected_item_price)

custom_item_frame = ttk.LabelFrame(tab1, text="Add Custom Item", padding="10")
custom_item_frame.pack(pady=15, fill="x")
ttk.Label(custom_item_frame, text="Item Name:").grid(row=0, column=0, sticky="w", padx=5, pady=2)
custom_name_entry = ttk.Entry(custom_item_frame, width=20)
custom_name_entry.grid(row=0, column=1, padx=5, pady=2)
ttk.Label(custom_item_frame, text="Price (₹):").grid(row=1, column=0, sticky="w", padx=5, pady=2)
custom_price_entry = ttk.Entry(custom_item_frame, width=10)
custom_price_entry.grid(row=1, column=1, padx=5, pady=2, sticky="w")
add_custom_btn = ttk.Button(custom_item_frame, text="Add", command=add_custom_item)
add_custom_btn.grid(row=0, column=2, rowspan=2, padx=10, sticky="ns")

# --- TAB 2: Charges and Finalization ---
charges_frame = ttk.LabelFrame(tab2, text="Additional Charges", padding="10")
charges_frame.pack(pady=10, fill="x")
ttk.Label(charges_frame, text="Tax (₹):").grid(row=0, column=0, sticky="w", pady=2)
tax_entry = ttk.Entry(charges_frame, width=12)
tax_entry.grid(row=0, column=1, padx=5, pady=2)
ttk.Label(charges_frame, text="Delivery (₹):").grid(row=1, column=0, sticky="w", pady=2)
delivery_entry = ttk.Entry(charges_frame, width=12)
delivery_entry.grid(row=1, column=1, padx=5, pady=2)
ttk.Label(charges_frame, text="Service (₹):").grid(row=2, column=0, sticky="w", pady=2)
service_entry = ttk.Entry(charges_frame, width=12)
service_entry.grid(row=2, column=1, padx=5, pady=2)

ttk.Separator(tab2, orient='horizontal').pack(fill='x', pady=20)

style.configure('Success.TButton', font=('Helvetica', 12, 'bold'))
generate_btn = ttk.Button(tab2, text="✅ Generate Invoice", command=generate_invoice_gui, style='Success.TButton')
generate_btn.pack(pady=15, ipady=8, fill='x')

# --- RIGHT FRAME: History and Deletion ---
ttk.Label(right_frame, text="🧾 Invoice History", font=("", 16, "bold")).pack(pady=(0, 10))
history_text_frame = ttk.Frame(right_frame)
history_text_frame.pack(fill="both", expand=True)
history_scrollbar = ttk.Scrollbar(history_text_frame)
history_scrollbar.pack(side="right", fill="y")
history_text = tk.Text(history_text_frame, wrap="word", font=("Courier New", 10), yscrollcommand=history_scrollbar.set, relief="solid", borderwidth=1)
history_text.pack(side="left", fill="both", expand=True)
history_scrollbar.config(command=history_text.yview)

delete_frame = ttk.Frame(right_frame, padding=(0, 10))
delete_frame.pack(fill="x")
ttk.Label(delete_frame, text="Delete by Date:").grid(row=0, column=0, padx=5)
date_combo = ttk.Combobox(delete_frame, state="readonly", width=15)
date_combo.grid(row=0, column=1, padx=5)
delete_btn = ttk.Button(delete_frame, text="🗑️ Delete", command=delete_history_by_date)
delete_btn.grid(row=0, column=2, padx=10)
clear_all_btn = ttk.Button(delete_frame, text="🧹 Clear All", command=clear_all_history)
clear_all_btn.grid(row=0, column=3, padx=10)

# --- Initial Display ---
update_history_display()
root.mainloop()