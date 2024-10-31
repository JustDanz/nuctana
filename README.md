# NUCTANA

Welcome to NUCTANA! This is a terminal-based tool installation script designed for Linux systems, specifically tailored to install Nuclei and Katana tools from ProjectDiscovery.

## Features

- **Easy Installation**: Automatically installs the Nuclei or Katana tools using Go.
- **OS Compatibility Check**: Ensures the script runs on Linux systems.
- **Go Installation**: Checks for the Go programming language and installs it if it's not already present.

## Tools

### Nuclei
Nuclei is a fast and flexible tool for targeted scanning based on templates. It can be used for various security assessments, including vulnerability scanning and detection.

### Katana
Katana is a powerful tool for reconnaissance and automated enumeration of targets. It helps security professionals gather information effectively.

## Requirements

- Linux operating system (Debian-based recommended, e.g., Ubuntu, Kali Linux)
- Go programming language

## Installation

1. Clone the repository:
   ```bash
   https://github.com/JustDanz/nuctana.git
   cd nuctana
   ```

2. Make the script executable:
   ```bash
   chmod +x nuctana.py
   ```

3. Run the script:
   ```bash
   python3 nuctana.py
   ```

4. Follow the on-screen prompts to install your desired tool.

## Usage

When you run the script, it will display a menu where you can select which tool to install (Nuclei or Katana). The script will check for the Go programming language and install it if it's not already present. Then, it will install the selected tool and move it to `/usr/local/bin/`.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please feel free to submit a pull request or open an issue.

## Acknowledgments

- Tools powered by [ProjectDiscovery](https://github.com/projectdiscovery)
- Code made by Justdanz
