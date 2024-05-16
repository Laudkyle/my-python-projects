# Define the base IP prefix and the starting IP suffix
base_ip = "10.0.2."
start_ip_suffix = 101

# Open the file in write mode to start with a clean file
with open('etho.txt', 'w') as f:
    for i in range(1, 421):
        if start_ip_suffix > 255:  # move to the next subnet if needed
            start_ip_suffix = 0
            base_ip = "10.0.3."
        ip_suffix = start_ip_suffix
        text = f"""
auto eth0:{i}
iface eth0:{i} inet static
    address {base_ip}{ip_suffix}
    netmask 255.255.255.0
"""
        f.write(text)
        start_ip_suffix += 1
