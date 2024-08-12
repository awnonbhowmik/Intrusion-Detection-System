from collections import defaultdict
import time
from ids.alerts import send_email_alert, send_sms_alert  # Import alert functions

attempts = defaultdict(list)

def detect(packet):
    if packet.haslayer("TCP") and packet["TCP"].flags == "S":  # TCP SYN flag
        ip_src = packet["IP"].src
        port_dst = packet["TCP"].dport
        current_time = time.time()
        
        attempts[ip_src].append(current_time)
        attempts[ip_src] = [t for t in attempts[ip_src] if current_time - t < 10]  # 10-second window
        
        if len(attempts[ip_src]) > 10:  # Threshold for detecting a scan
            alert_message = f"[ALERT] Potential port scan detected from {ip_src} targeting port {port_dst}"
            print(alert_message)
            send_email_alert("Port Scan Detected", alert_message, "admin@example.com")
            send_sms_alert(alert_message, "+1234567890")
            attempts[ip_src] = []  # Reset after detection
