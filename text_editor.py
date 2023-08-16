import tkinter as tk
from tkinter import filedialog, messagebox

class TextEditor:
    # Initialize the TextEditor with a root window
    def __init__(self, root):
        self.root = root
        # Set the title of the root window
        self.root.title("Simple Text Editor")
        # Create a Text widget for text editing and word wrapping
        self.text_area = tk.Text(self.root, wrap="word")
        # Pack the Text widget to fill the available space
        self.text_area.pack(fill="both", expand=True)

        # Create a menu bar for the root window
        self.menu_bar = tk.Menu(self.root)
        # Configure the root window's menu with the created menu bar
        self.root.config(menu=self.menu_bar)

        # Create a submenu under "File" in the menu bar
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        # Add commands to the "File" submenu
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)

    # Method to clear the text area
    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    # Method to open a file using a file dialog
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=
                                               [("Text files", "*.txt")])
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    # Method to save the content of the text area to a file using 
    # a file dialog
    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            content = self.text_area.get("1.0", tk.END)
            with open(file_path, "w") as file:
                file.write(content)

    # Method to start the main event loop
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    # Create a root window using tk.Tk()
    root = tk.Tk()
    # Create an instance of TextEditor with the root window
    editor = TextEditor(root)
    # Run the GUI application by starting the event loop
    editor.run()
