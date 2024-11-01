from rich.console import Console
from rich.panel import Panel
from rich import box
import os
import platform
import subprocess
import sys

def check_and_install_python_dependencies():
    # List of required Python packages
    required_packages = ['rich']

    # Install missing packages
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            print(f"{package} is not installed. Installing...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
            print(f"{package} has been installed.")

def check_and_install_go():
    # Check if Go is installed
    if subprocess.call(["which", "go"]) != 0:
        print("Go is not installed. Installing Go...")
        os.system("sudo apt update && sudo apt install -y golang")
        print("Go has been installed.")
    else:
        print("Go is already installed.")

def install_tool(choice):
    # Check if the operating system is compatible
    os_type = platform.system()
    if os_type != "Linux":
        print("This script is intended for Linux systems.")
        return

    # Ensure Go is installed before proceeding
    check_and_install_go()

    # Install selected tool based on user choice
    if choice == "1":
        print("Installing Nuclei...")
        os.system("go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest")
        os.system("sudo mv ~/go/bin/nuclei /usr/local/bin/")
        print("Nuclei has been installed and moved to /usr/local/bin.")
    elif choice == "2":
        print("Installing Katana...")
        os.system("go install github.com/projectdiscovery/katana/cmd/katana@latest")
        os.system("sudo mv ~/go/bin/katana /usr/local/bin/")
        print("Katana has been installed and moved to /usr/local/bin.")
    else:
        print("Invalid choice. Exiting...")

def main():
    # Clear screen
    os.system("clear" if os.name == "posix" else "cls")

    # Create console object
    console = Console()

    # Display banner
    console.print(Panel(
        "[bold green]NUCTANA[/bold green]",
        subtitle="Welcome to NUCTANA Terminal",
        border_style="bold yellow",
        padding=(1, 10),
        box=box.DOUBLE_EDGE
    ))

    # ASCII Art "Toilet" Style
    message = """
███╗   ██╗██╗   ██╗ ██████╗████████╗ █████╗ ███╗   ██╗ █████╗ 
████╗  ██║██║   ██║██╔════╝╚══██╔══╝██╔══██╗████╗  ██║██╔══██╗
██╔██╗ ██║██║   ██║██║        ██║   ███████║██╔██╗ ██║███████║
██║╚██╗██║██║   ██║██║        ██║   ██╔══██║██║╚██╗██║██╔══██║
██║ ╚████║╚██████╔╝╚██████╗   ██║   ██║  ██║██║ ╚████║██║  ██║
╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
    """
    console.print(Panel(
        f"[bold red]{message}[/bold red]",
        title="ASCII Toilet Style",
        title_align="center",
        border_style="bold cyan",
        padding=(1, 2),
        box=box.ROUNDED
    ))

    # Credit text for ProjectDiscovery
    console.print(
        "[bold magenta]Tools Made by [link=https://github.com/projectdiscovery]ProjectDiscovery[/link][/bold magenta]",
        justify="center"
    )

    # Custom "Made by Justdanz" text
    console.print(
        "[bold green]Code Made by Justdanz[/bold green]",
        justify="center"
    )

    # Check and install Python dependencies
    check_and_install_python_dependencies()

    # Display installation options
    console.print("[bold yellow]Select a tool to install:[/bold yellow]")
    console.print("[1] Nuclei")
    console.print("[2] Katana")
    choice = input("Enter your choice (1 or 2): ")

    # Install selected tool
    install_tool(choice)

if __name__ == "__main__":
    main()
