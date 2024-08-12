
# Intrusion Detection System (IDS)

## Overview

This Intrusion Detection System (IDS) is designed to monitor network traffic, detect potential intrusions such as port scans and brute-force attacks, and provide real-time alerts. The IDS is implemented in Python and includes features such as process monitoring, file system monitoring, network activity monitoring, and automated response mechanisms.

## Features

- **Packet Sniffing:** Captures and analyzes network traffic in real-time.
- **Port Scan Detection:** Identifies potential port scanning activities.
- **Brute Force Detection:** Detects brute-force login attempts.
- **Logging:** Records detected events and network activity for audit purposes.
- **Real-Time Alerts:** Sends email and SMS alerts when suspicious activity is detected.
- **Automated Responses:** Automatically blocks suspicious IP addresses.
- **Web Interface:** Provides a dashboard for viewing logs and managing the IDS.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**

   \`\`\`bash
   git clone https://github.com/yourusername/ids_project.git
   cd ids_project
   \`\`\`

2. **Create and activate a virtual environment:**

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   \`\`\`

3. **Install dependencies:**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage

The IDS can be run from the command line. You can monitor network traffic, detect intrusions, and view the logs through the web interface.

### Running the IDS

To run the IDS with all monitoring features enabled:

\`\`\`bash
python run_ids.py
\`\`\`

### Accessing the Web Interface

The web interface can be accessed at \`http://localhost:5000\`. It provides real-time views of logs, alerts, and system status.

### Command-Line Options

- \`--scan-processes\`: Scan the system for suspicious processes.
- \`--monitor-files\`: Monitor specified directories for suspicious file activity.
- \`--monitor-network\`: Monitor network connections for suspicious outbound activity.

### Monitoring Logs and Alerts

- Logs are stored in \`ids_log.log\` in the root directory of the project.
- Alerts are sent via email and SMS as configured in \`config.py\`.

## Configuration

The IDS can be configured through the \`config.py\` file.

### Email Alert Settings

Configure the SMTP settings for sending email alerts:

\`\`\`python
EMAIL_SETTINGS = {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "from_email": "your_email@example.com",
    "password": "your_password",
    "to_email": "admin@example.com"
}
\`\`\`

### Twilio SMS Alert Settings

Configure Twilio settings for sending SMS alerts:

\`\`\`python
TWILIO_SETTINGS = {
    "account_sid": "your_account_sid",
    "auth_token": "your_auth_token",
    "from_number": "your_twilio_number",
    "to_number": "+1234567890"
}
\`\`\`

### Network Interface Configuration

Specify the network interface to monitor in \`run_ids.py\`:

\`\`\`python
interface = "eth0"  # Replace with your network interface
\`\`\`

## Deployment

### Docker Deployment

The IDS can be containerized using Docker for easy deployment.

1. **Build the Docker image:**

   \`\`\`bash
   docker build -t ids_project .
   \`\`\`

2. **Run the Docker container:**

   \`\`\`bash
   docker run -p 5000:5000 ids_project
   \`\`\`

### Executable Packaging

To create a standalone executable, you can use \`pyinstaller\`:

\`\`\`bash
pip install pyinstaller
pyinstaller --onefile run_ids.py
\`\`\`

The executable will be created in the \`dist\` directory.

## Testing

The IDS includes unit tests to verify its functionality.

### Running Unit Tests

To run the unit tests:

\`\`\`bash
python -m unittest discover -s tests
\`\`\`

This command will discover and run all tests in the \`tests\` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on GitHub if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the \`LICENSE\` file for more details.
