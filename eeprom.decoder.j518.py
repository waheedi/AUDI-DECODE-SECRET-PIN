import tkinter as tk
from tkinter import filedialog, messagebox
import binascii
import os

def read_eeprom(path):
    try:
        with open(path, 'rb') as f:
            data = f.read()
    except Exception as e:
        return f"Error: {e}"

    def get(offset, length):
        return data[offset:offset+length].hex()

    def get_rev(offset, length):
        raw = data[offset:offset+length]
        return ''.join(f"{b:02x}" for b in reversed(raw))

    def to_ascii(offset, length):
        try:
            return data[offset:offset+length].replace(b'\xFF', b'').decode('ascii')
        except:
            return "(non-ascii)"

    def hex_to_dec(hs):
        try:
            return str(int(hs, 16))
        except:
            return "(invalid)"

    result = []
    result.append("=== EZS EEPROM Decode ===")
    result.append(f"VIN: {to_ascii(0x54, 17)}")
    result.append(f"EZS ECU CS: {get(0x106, 6)}")
    result.append(f"EZS CS2: {get(0x100, 6)}")

    # PIN
    pin_hex = get_rev(0x154, 2)
    result.append(f"EZS PIN: {hex_to_dec(pin_hex) if pin_hex != 'ffff' else '(not set)'}")

    # Power class
    pc = get(0x160, 1)
    result.append(f"Power Class: {pc}")

    # Keys
    result.append(f"EZS KEY0: {get(0x17C, 4)}")
    result.append(f"EZS KEY1: {get(0x180, 4)}")
    result.append(f"EZS KEY2: {get(0x184, 4)}")
    result.append(f"EZS KEY3: {get(0x188, 4)}")

    # Key count
    kc = get(0x1BE, 1)
    result.append(f"EZS Key Count: {kc}")

    return "\n".join(result)

def select_file():
    filepath = filedialog.askopenfilename(filetypes=[("BIN files", "*.bin"), ("All files", "*.*")])
    if filepath:
        result = read_eeprom(filepath)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, result)

# GUI setup
root = tk.Tk()
root.title("Audi EZS EEPROM Decoder")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=10)

btn = tk.Button(frame, text="Select EEPROM .bin File", command=select_file)
btn.pack()

text_output = tk.Text(root, wrap=tk.WORD, font=("Courier", 10))
text_output.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

root.mainloop()

