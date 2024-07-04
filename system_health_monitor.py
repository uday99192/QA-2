import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f"High CPU usage detected: {cpu_usage}%")
    else:
        logging.info(f"CPU usage is normal: {cpu_usage}%")

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    if memory_info.percent > MEMORY_THRESHOLD:
        logging.warning(f"High memory usage detected: {memory_info.percent}%")
    else:
        logging.info(f"Memory usage is normal: {memory_info.percent}%")

def check_disk_usage():
    disk_info = psutil.disk_usage('/')
    if disk_info.percent > DISK_THRESHOLD:
        logging.warning(f"High disk usage detected: {disk_info.percent}%")
    else:
        logging.info(f"Disk usage is normal: {disk_info.percent}%")

def check_running_processes():
    processes = psutil.pids()
    logging.info(f"Number of running processes: {len(processes)}")

def monitor_system():
    logging.info("Starting system health check...")
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()
    logging.info("System health check completed.")

if __name__ == "__main__":
    monitor_system()
