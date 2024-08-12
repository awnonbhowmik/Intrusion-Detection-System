import logging

class Logger:
    def __init__(self):
        # Configure the logging
        logging.basicConfig(
            filename="ids_log.log",  # Log file name
            level=logging.INFO,      # Log level
            format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
            datefmt="%Y-%m-%d %H:%M:%S"  # Date format
        )

    def log_packet(self, packet):
        """Logs a summary of the packet."""
        log_msg = f"Packet: {packet.summary()}"
        logging.info(log_msg)
        print(log_msg)  # Optionally print to console

    def log_alert(self, message):
        """Logs an alert message."""
        logging.warning(message)
        print(message)  # Optionally print to console

    def log_custom(self, message, level=logging.INFO):
        """Logs a custom message with a specified log level."""
        logging.log(level, message)
        print(message)  # Optionally print to console
