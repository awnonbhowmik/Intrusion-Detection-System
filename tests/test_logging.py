import unittest
import logging
import os
from ids.logging.logger import Logger

class TestLogger(unittest.TestCase):

    def setUp(self):
        self.logger = Logger()
        self.log_file = "ids_log.log"
        # Clear log file before each test
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_packet(self):
        """Tests that packet logging works."""
        mock_packet_summary = "Packet: IP src=192.168.1.1 dst=192.168.1.2"
        self.logger.log_packet(mock_packet_summary)
        with open(self.log_file, "r") as f:
            logs = f.read()
            self.assertIn(mock_packet_summary, logs)

    def test_log_alert(self):
        """Tests that alert logging works."""
        mock_alert_message = "[ALERT] Potential port scan detected"
        self.logger.log_alert(mock_alert_message)
        with open(self.log_file, "r") as f:
            logs = f.read()
            self.assertIn(mock_alert_message, logs)

if __name__ == '__main__':
    unittest.main()
