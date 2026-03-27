import os
import subprocess

print("FETCH PROGRAM")

hostname = os.uname().nodename
user = os.getlogin()
print(f"{user}@{hostname}")

CPU = subprocess.check_output(
    ['grep', '-m1', 'model name', '/proc/cpuinfo'],
    text=True
).split(':', 1)[1].strip()
print(f"CPU: {CPU}")

gpu_output = subprocess.check_output(
    "lspci | grep ' VGA ' | awk -F': ' '{print $2}' | sed 's/ (rev.*)//'",
    shell=True,
    text=True
).strip().split('\n')
for i in range(len(gpu_output)):
    print(f"GPU: {gpu_output[i]}")

OS = subprocess.check_output(
    ['grep', '-m1', 'PRETTY_NAME', '/etc/os-release'],
    text=True
).split('=', 1)[1].strip().replace('"', '')
print(f"OS: {OS}")


mem_total_output = subprocess.check_output(
    "grep 'MemTotal:' /proc/meminfo | awk '{print $2}'",
    shell=True,
    text=True
).strip()
mem_available_output = subprocess.check_output(
    "grep 'MemAvailable:' /proc/meminfo | awk '{print $2}'",
    shell=True,
    text=True
).strip()
mem_total = int(mem_total_output) / 1000
mem_available = int(mem_available_output) / 1000
mem_used = mem_total - mem_available

print(f"Memory: {int(mem_used)} MB/{int(mem_total)} MB")