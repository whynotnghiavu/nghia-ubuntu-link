# sudo apt-get install python3-tk
import os
import tkinter as tk
from tkinter import filedialog

def choose_file_or_folder(event):


    home_directory = os.path.expanduser("~")
    path = None

    if event.state & 0x1:  # Kiểm tra xem Shift có được giữ không
        path = filedialog.askdirectory(initialdir=home_directory, title="Select a folder")
    else:
        path = filedialog.askopenfilename(initialdir=home_directory, title="Select a file")
    
    if path:
        print(f"Selected path: {path}")

        symlink_path = os.path.join(os.path.dirname(path), 'Shortcut_' + os.path.basename(path))

        if os.path.exists(symlink_path):
            print("The symbolic link already exists")
        else:
            try:
                os.symlink(path, symlink_path)
                print(f"Symbolic link created at {symlink_path}")
            except OSError as e:
                print(f"Failed to create symbolic link: {e}")

    exit()




root = tk.Tk()
root.title("nghia-ubuntu-link")

btn = tk.Button(root, text="Select File or Folder\n(Nhấn Shift để chọn folder)")
btn.pack(pady=20)

# Kiểm tra xem Shift có được giữ không
btn.bind("<Button-1>", choose_file_or_folder)

# Chạy vòng lặp sự kiện chính
root.mainloop()
