import re

file_path = "os_scan.txt"

windows = 0
linux = 0
mac = 0
unknown = 0
total = 0

with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    data = f.read()

# Split per host
hosts = re.split(r"Nmap scan report for", data)[1:]

for host in hosts:
    total += 1
    host_lower = host.lower()

    if "service info: os: windows" in host_lower:
        windows += 1

    elif "mac address" in host_lower and "apple" in host_lower:
        mac += 1

    elif "running: apple macos" in host_lower:
        mac += 1

    elif "linux" in host_lower or "ubuntu" in host_lower:
        linux += 1

    elif "running (just guessing):" in host_lower:
        if "windows" in host_lower:
            windows += 1
        elif "mac" in host_lower or "apple" in host_lower:
            mac += 1
        elif "linux" in host_lower:
            linux += 1
        else:
            unknown += 1

    elif "microsoft" in host_lower:
        windows += 1

    elif "apache" in host_lower or "ssh" in host_lower:
        linux += 1

    else:
        unknown += 1

# Print results
print(f"Total hosts analyzed: {total}\n")

def percent(x):
    return round((x/total)*100, 2) if total else 0

print("OS Distribution:")
print(f"Windows: {windows} ({percent(windows)}%)")
print(f"Linux: {linux} ({percent(linux)}%)")
print(f"macOS: {mac} ({percent(mac)}%)")
print(f"Unknown: {unknown} ({percent(unknown)}%)")