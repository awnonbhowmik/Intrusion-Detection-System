import os

def block_ip(ip):
    """
    Blocks the specified IP address using the system's firewall (iptables).
    
    :param ip: The IP address to block.
    """
    try:
        # The following command adds a rule to iptables to drop all traffic from the given IP
        command = f"sudo iptables -A INPUT -s {ip} -j DROP"
        os.system(command)
        print(f"[ACTION] IP {ip} has been blocked.")
    except Exception as e:
        print(f"[ERROR] Failed to block IP {ip}: {e}")
