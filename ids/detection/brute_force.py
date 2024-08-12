from collections import defaultdict
import time
from ids.alerts import send_email_alert, send_sms_alert  # Import alert functions

login_attempts = defaultdict(list)

def detect(packet):
    if packet.haslayer("TCP") and packet["TCP"].dport == 22:  # SSH default port
        ip_src = packet["IP"].src
        current_time = time.time()
        
        login_attempts[ip_src].append(current_time)
        login_attempts[ip_src] = [t for t in login_attempts[ip_src] if current_time - t < 10]  # 10-second window
        
        if len(login_attempts[ip_src]) > 5:  # Threshold for detecting brute-force
            alert_message = f"[ALERT] Potential brute-force attack detected from {ip_src} on SSH"
            print(alert_message)
            send_email_alert("Brute-Force Attack Detected", alert_message, "admin@example.com")
            send_sms_alert(alert_message, "+1234567890")
            login_attempts[ip_src] = []  # Reset after detection
