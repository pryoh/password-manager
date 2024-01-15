from gui.password_manager_gui import PasswordManagerGUI
import tkinter as tk

def main():
    root = tk.Tk()
    gui = PasswordManagerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
