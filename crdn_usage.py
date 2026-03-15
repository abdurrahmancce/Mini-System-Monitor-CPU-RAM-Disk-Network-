import psutil
import tkinter as tk
from tkinter import ttk
import time
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.animation as animation

# -----------------------------
# Data storage for graphs
# -----------------------------
cpu_data, ram_data, disk_data, net_data, time_data = [], [], [], [], []

# -----------------------------
# GUI setup
# -----------------------------
root = tk.Tk()
root.title("System Performance Dashboard")
root.geometry("1000x700")

# --- Progress Bars Section ---
frame_top = tk.Frame(root)
frame_top.pack(pady=10)

cpu_label = tk.Label(frame_top, text="CPU Usage: 0%", font=("Arial", 14))
cpu_label.pack(pady=5)
cpu_bar = ttk.Progressbar(frame_top, length=400, maximum=100)
cpu_bar.pack(pady=5)

ram_label = tk.Label(frame_top, text="RAM Usage: 0%", font=("Arial", 14))
ram_label.pack(pady=5)
ram_bar = ttk.Progressbar(frame_top, length=400, maximum=100)
ram_bar.pack(pady=5)

disk_label = tk.Label(frame_top, text="Disk Usage: 0%", font=("Arial", 14))
disk_label.pack(pady=5)
disk_bar = ttk.Progressbar(frame_top, length=400, maximum=100)
disk_bar.pack(pady=5)

net_label = tk.Label(frame_top, text="Network Activity: 0 KB/s", font=("Arial", 14))
net_label.pack(pady=5)

# --- Graph Section ---
fig, ax = plt.subplots(4, 1, figsize=(8, 8))
plt.tight_layout()

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# -----------------------------
# Background thread: update progress bars
# -----------------------------
def update_bars():
    old_net = psutil.net_io_counters()
    while True:
        # Collect system stats
        cpu_usage = psutil.cpu_percent(interval=0.5)
        ram_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        new_net = psutil.net_io_counters()
        net_speed = (new_net.bytes_recv - old_net.bytes_recv +
                     new_net.bytes_sent - old_net.bytes_sent) / 1024  # KB/s
        old_net = new_net

        # Update labels
        cpu_label.config(text=f"CPU Usage: {cpu_usage:.2f}%")
        ram_label.config(text=f"RAM Usage: {ram_usage:.2f}%")
        disk_label.config(text=f"Disk Usage: {disk_usage:.2f}%")
        net_label.config(text=f"Network Activity: {net_speed:.2f} KB/s")

        # Update progress bars
        cpu_bar['value'] = cpu_usage
        ram_bar['value'] = ram_usage
        disk_bar['value'] = disk_usage

        time.sleep(1)

# -----------------------------
# Graph animation
# -----------------------------
def animate(i):
    cpu_usage = psutil.cpu_percent(interval=0.5)
    ram_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    net_usage = psutil.net_io_counters().bytes_sent / 1024  # KB

    # Append new data
    time_data.append(len(time_data))
    cpu_data.append(cpu_usage)
    ram_data.append(ram_usage)
    disk_data.append(disk_usage)
    net_data.append(net_usage)

    # Keep only last 50 points
    if len(time_data) > 50:
        time_data.pop(0)
        cpu_data.pop(0)
        ram_data.pop(0)
        disk_data.pop(0)
        net_data.pop(0)

    # CPU graph
    ax[0].clear()
    ax[0].plot(time_data, cpu_data, color="blue")
    ax[0].set_title("CPU Usage (%)")
    ax[0].set_ylim(0, 100)

    # RAM graph
    ax[1].clear()
    ax[1].plot(time_data, ram_data, color="green")
    ax[1].set_title("RAM Usage (%)")
    ax[1].set_ylim(0, 100)

    # Disk graph
    ax[2].clear()
    ax[2].plot(time_data, disk_data, color="red")
    ax[2].set_title("Disk Usage (%)")
    ax[2].set_ylim(0, 100)

    # Network graph
    ax[3].clear()
    ax[3].plot(time_data, net_data, color="purple")
    ax[3].set_title("Network Activity (KB sent)")
    ax[3].set_ylim(0, max(net_data) + 100 if net_data else 100)

# -----------------------------
# Run everything
# -----------------------------
threading.Thread(target=update_bars, daemon=True).start()
ani = animation.FuncAnimation(fig, animate, interval=1000)
root.mainloop()
