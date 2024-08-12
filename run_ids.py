from ids.packet_sniffer import PacketSniffer
from ids.ui.web_interface import app
import threading

def start_sniffer(interface):
    """Start packet sniffer in a separate thread."""
    sniffer = PacketSniffer(interface)
    sniffer.start()

if __name__ == "__main__":
    interface = "eth0"  # Replace with your network interface
    sniffer_thread = threading.Thread(target=start_sniffer, args=(interface,))
    sniffer_thread.start()

    # Start the Flask web server for the UI
    app.run(host="0.0.0.0", port=5000)
