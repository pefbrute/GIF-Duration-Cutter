import tkinter as tk
from tkinter import filedialog
import subprocess
import os

def get_gif_info(gif_path):
    """ Get the number of frames in the GIF. """
    try:
        output = subprocess.check_output(['gifsicle', '--info', gif_path]).decode()
        # Find the line that contains 'images' and extract the number of frames.
        for line in output.split('\n'):
            if 'images' in line:
                print(line)
                return line.split()[-2] + " frames"
    except subprocess.CalledProcessError as e:
        return "Error: Could not read GIF info."

def cut_gif(gif_path, from_frame, to_frame, output_path):
    """ Cut the GIF from one frame to another. """
    try:
        # Using subprocess.Popen for more control over input and output
        with open(output_path, 'wb') as output_file:
            process = subprocess.Popen(['gifsicle', gif_path, f'#{from_frame}-{to_frame}', '-O3'], stdout=subprocess.PIPE)
            output_file.write(process.stdout.read())

        if process.wait() != 0:
            print("Error cutting GIF: Non-zero exit status.")
    except subprocess.CalledProcessError as e:
        print("Error cutting GIF:", e)

def upload_gif():
    """ Upload a GIF and display its frame information. """
    file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
    if file_path:
        gif_info.set(get_gif_info(file_path))
        uploaded_gif.set(file_path)

def process_gif():
    """ Process the uploaded GIF based on user input. """
    from_frame = from_frame_entry.get()
    to_frame = to_frame_entry.get()
    if uploaded_gif.get():
        # Extract the directory of the uploaded GIF
        gif_directory = os.path.dirname(uploaded_gif.get())
        # Create a new filename with 'cut_' prefix
        new_filename = f'cut_{os.path.basename(uploaded_gif.get())}'
        # Join the directory with the new filename to create the output path
        output_file = os.path.join(gif_directory, new_filename)
        # Call cut_gif with the new output path
        cut_gif(uploaded_gif.get(), from_frame, to_frame, output_file)

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

from_frame_entry = tk.Entry(root)
from_frame_entry.pack()
from_frame_entry_text = 0
from_frame_entry.insert(0, from_frame_entry_text)

to_frame_entry = tk.Entry(root)
to_frame_entry.pack()
to_frame_entry.insert(0, "To Frame")

process_button = tk.Button(root, text="Cut GIF", command=process_gif)
process_button.pack()

root.mainloop()
