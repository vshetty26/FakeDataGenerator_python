import tkinter as tk
from tkinter import messagebox, filedialog
import json
from faker import Faker

fake = Faker()

class FakeDataGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Fake Data Generator")
        self.root.geometry("500x500")  

        self.style_var = tk.StringVar(value="Tech Blue")

        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        font_large = ("Arial", 20)  
        entry_font = ("Arial", 22) 

        self.name_label = tk.Label(self.root, text="Name:", font=font_large)
        self.name_label.pack(pady=5)
        self.name_text = tk.Entry(self.root, width=40, font=entry_font, bd=3)
        self.name_text.pack(pady=5, ipady=5)

        self.email_label = tk.Label(self.root, text="Email:", font=font_large)
        self.email_label.pack(pady=5)
        self.email_text = tk.Entry(self.root, width=40, font=entry_font, bd=3)
        self.email_text.pack(pady=5, ipady=5)

        self.address_label = tk.Label(self.root, text="Address:", font=font_large)
        self.address_label.pack(pady=5)
        self.address_text = tk.Entry(self.root, width=40, font=entry_font, bd=3)
        self.address_text.pack(pady=5, ipady=5)

        button_font = ("Arial", 20, "bold")
        self.generate_button = tk.Button(self.root, text="Generate", font=button_font, command=self.generate_data, width=20, height=2)
        self.generate_button.pack(pady=5)

        self.copy_button = tk.Button(self.root, text="Copy to Clipboard", font=button_font, command=self.copy_data, width=20, height=2)
        self.copy_button.pack(pady=5)

        self.surprise_button = tk.Button(self.root, text="Surprise Me!", font=button_font, command=self.surprise_me, width=20, height=2)
        self.surprise_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Export to JSON", font=button_font, command=self.export_json, width=20, height=2)
        self.save_button.pack(pady=5)

        self.theme_menu = tk.OptionMenu(self.root, self.style_var, "Tech Blue", "Paper Theme", command=self.apply_theme)
        self.theme_menu.config(font=button_font)
        self.theme_menu.pack(pady=10)

    def generate_data(self):
        """Generates a random name, email, and address."""
        self.name_text.delete(0, tk.END)
        self.name_text.insert(0, fake.name())

        self.email_text.delete(0, tk.END)
        self.email_text.insert(0, fake.email())

        self.address_text.delete(0, tk.END)
        self.address_text.insert(0, fake.address())

    def copy_data(self):
        """Copies generated data to clipboard."""
        data = f"Name: {self.name_text.get()}\nEmail: {self.email_text.get()}\nAddress: {self.address_text.get()}"
        self.root.clipboard_clear()
        self.root.clipboard_append(data)
        self.root.update()
        messagebox.showinfo("Copied", "Data copied to clipboard!")

    def surprise_me(self):
        """Generates random name only."""
        self.generate_data()

    def export_json(self):
        """Exports generated data to a JSON file."""
        data = {
            "name": self.name_text.get(),
            "email": self.email_text.get(),
            "address": self.address_text.get()
        }
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            with open(file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            messagebox.showinfo("Saved", "Data exported successfully!")

    def apply_theme(self, *args):
        """Applies selected theme."""
        theme = self.style_var.get()

        if theme == "Tech Blue":
            self.root.configure(bg="#001f3f")  
            color, text_color = "#001f3f", "white"
            entry_bg, entry_fg = "#003366", "white"
        else:
            self.root.configure(bg="#f5f5dc") 
            color, text_color = "#f5f5dc", "black"
            entry_bg, entry_fg = "white", "black"

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.configure(bg=color, fg=text_color)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg=entry_bg, fg=entry_fg, insertbackground="white")  
            elif isinstance(widget, tk.Button):
                widget.configure(bg="gray", fg="black") 

if __name__ == "__main__":
    root = tk.Tk()
    app = FakeDataGenerator(root)
    root.mainloop()
q