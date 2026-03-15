💻 System Performance Dashboard

A simple desktop dashboard application built with Python that monitors your computer’s real-time system performance.
It shows CPU, RAM, Disk usage, and Network activity using progress bars and live graphs.

This project demonstrates how to combine system monitoring, GUI development, and data visualization in Python.

📊 Features

-Real-time CPU usage monitoring

-Real-time RAM usage monitoring

-Disk usage tracking

-Network activity measurement

-Live animated graphs for system metrics

-Interactive Tkinter desktop interface

-Uses multithreading to keep the interface responsive

🖼️ Dashboard Overview

The dashboard contains two main sections:

1️⃣ System Usage Indicators

Displays system statistics using progress bars:

-CPU Usage (%)

-RAM Usage (%)

-Disk Usage (%)

-Network Activity (KB/s)

2️⃣ Live Performance Graphs

-Four graphs update every second:

-CPU Usage

-RAM Usage

-Disk Usage

⚙️ How the Project Works

1. System Data Collection

The project uses the psutil library to collect system statistics:

-psutil.cpu_percent() → CPU usage

-psutil.virtual_memory() → RAM usage

-psutil.disk_usage() → Disk usage

-psutil.net_io_counters() → Network traffic

-Network Activity

These graphs show the last 50 data points, allowing you to observe short-term system trends.

2. Background Thread
3. Live Graph Animation

🚀 Future Improvements

Possible upgrades:

-GPU usage monitoring

-Temperature monitoring

-Dark mode dashboard

-Export performance reports

-Web-based monitoring

-Email alerts for high CPU usage

-Modern UI using PyQt
