import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def get_gif_info(gif_path):
    """ Get the number of frames in the GIF. """
    try:
        output = subprocess.check_output(['gifsicle', '--info', gif_path]).decode()
        for line in output.split('\n'):
            if 'images' in line:
                total_frames = int(line.split()[-2])
                gif_info.set(f"{total_frames} frames")
                return total_frames
    except subprocess.CalledProcessError as e:
        gif_info.set("Error: Could not read GIF info.")
        return None

def cut_gif(gif_path, from_frame, to_frame, output_path):
    try:
        with open(output_path, 'wb') as output_file:
            process = subprocess.Popen(['gifsicle', gif_path, f'#{from_frame}-{to_frame}', '-O3'], stdout=subprocess.PIPE)
            output_file.write(process.stdout.read())
        if process.wait() != 0:
            messagebox.showerror("Error", "Error cutting GIF: Non-zero exit status.")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Error cutting GIF: {e}")

def upload_gif():
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    if file_path:
        total_frames = get_gif_info(file_path)
        if total_frames:
            to_frame_entry.delete(0, tk.END)
            to_frame_entry.insert(0, str(total_frames - How_many_frames_to_subtract_from_the_total_number))
        uploaded_gif.set(file_path)

def process_gif():
    try:
        from_frame = int(from_frame_entry.get())
        to_frame = int(to_frame_entry.get())
        if uploaded_gif.get():
            gif_directory = os.path.dirname(uploaded_gif.get())
            new_filename = f'cut_{os.path.basename(uploaded_gif.get())}'
            output_file = os.path.join(gif_directory, new_filename)
            cut_gif(uploaded_gif.get(), from_frame, to_frame, output_file)
            messagebox.showinfo("Success", f"GIF cut successfully: {output_file}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid frame numbers.")

From_which_frame_crop_by_default = 0
How_many_frames_to_subtract_from_the_total_number = 20

# GUI Setup
root = tk.Tk()
root.title("GIFsicle GUI")

uploaded_gif = tk.StringVar()
gif_info = tk.StringVar()

# Widgets
upload_button = tk.Button(root, text="Upload GIF", command=upload_gif)
upload_button.pack()

info_label = tk.Label(root, textvariable=gif_info)
info_label.pack()

tk.Label(root, text="From Frame").pack()
from_frame_entry = tk.Entry(root)
from_frame_entry.pack()

from_frame_entry.insert(0, From_which_frame_crop_by_default)

tk.Label(root, text="To Frame:").pack()
to_frame_entry = tk.Entry(root)
to_frame_entry.pack()

process_button = tk.Button(root, text="Cut GIF", command=process_gif)
process_button.pack()

root.mainloop()
