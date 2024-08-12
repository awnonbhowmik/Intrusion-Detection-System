import unittest
from scapy.all import IP, TCP
from ids.detection import detect_port_scan, detect_brute_force

class TestPortScanDetection(unittest.TestCase):

    def create_mock_packet(self, ip_src, dport):
        """Creates a mock TCP SYN packet for testing."""
        packet = IP(src=ip_src)/TCP(dport=dport, flags="S")
        return packet

    def test_port_scan_detection(self):
        """Tests port scan detection logic."""
        packet = self.create_mock_packet("192.168.1.1", 80)
        for _ in range(11):  # Simulate 11 SYN packets from the same IP
            detect_port_scan(packet)
        # Assert can be added here to check if detection is working as expected

class TestBruteForceDetection(unittest.TestCase):

    def create_mock_packet(self, ip_src, dport):
        """Creates a mock TCP packet for testing."""
        packet = IP(src=ip_src)/TCP(dport=dport)
        return packet

    def test_brute_force_detection(self):
        """Tests brute-force detection logic."""
        packet = self.create_mock_packet("192.168.1.2", 22)
        for _ in range(6):  # Simulate 6 login attempts
            detect_brute_force(packet)
        # Assert can be added here to check if detection is working as expected

if __name__ == '__main__':
    unittest.main()
