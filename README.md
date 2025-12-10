# BigBountyRecon - Python Tkinter Version

BigBountyRecon tool utilises 58 different techniques using various Google dorks and open source tools to expedite the process of initial reconnaissance on the target organisation. Reconnaissance is the most important step in any penetration testing or a bug hunting process.

This is the Python Tkinter port of the original C# Windows Forms application.

## Features

- 58+ reconnaissance techniques
- Google dork searches
- Third-party service searches (GitHub, Pastebin, LinkedIn, etc.)
- Security tool integrations (Shodan, Censys, ThreatCrowd, etc.)
- Archive searches (Wayback Machine, etc.)
- All searches open in Chrome browser

## Requirements

- Python 3.6 or higher
- Tkinter (usually included with Python)
- Chrome browser installed (for opening search results)

## Installation

1. Clone or download this repository
2. Navigate to the `PythonRecon` directory
3. No additional packages required - all dependencies are in Python standard library

## Usage

### Option 1: Double-click to run (Easiest)

**On macOS:**
- Double-click `run.command` in Finder
- The application will launch in Terminal

**On Windows:**
- Double-click `run.bat` in File Explorer
- The application will launch in a command window

### Option 2: Using the executable script from terminal

**On macOS/Linux:**
```bash
./run.sh
```
or
```bash
./run.command
```

**On Windows:**
```batch
run.bat
```

### Option 3: Direct Python execution

```bash
python src/main.py
```
or
```bash
python3 src/main.py
```

### Using the Application

1. Enter the target domain in the input field

3. Click on any button to perform a specific reconnaissance search

4. The search will open in Chrome browser automatically

## Available Searches

### File Searches
- Directory Listing
- Configuration Files
- Database Files
- Log Files
- Backup Files
- Documents
- Apache Config
- .htaccess/phpinfo
- phpinfo
- Install/Setup Files
- Backdoors
- robots.txt
- crossdomain.xml
- .git Folder

### WordPress
- WordPress
- WordPress Exposure
- WordPress Wayback

### Authentication & Errors
- Login Pages
- SQL Errors
- Open Redirects
- Apache Struts

### Subdomains
- Subdomains
- Sub-subdomains
- CT Logs (crt.sh)
- Reverse IP

### Third-party Services
- GitHub
- Gist
- GitLab
- Pastebin
- Throwbin
- StackOverflow
- LinkedIn Employees
- Reddit
- YouTube
- Third-party Exposure
- BitBucket & Atlassian

### Security Tools
- Shodan
- Censys (IPv4, Domain, Certificates)
- ThreatCrowd
- RiskIQ
- Security Headers
- OpenBugBounty
- DomainEye
- What CMS
- PublicWWW
- Google CSE

### Archive & Wayback
- Wayback Machine
- SWF (Google)
- SWF (Yandex)
- SWF (Wayback)
- SWF (Wayback MIME)

### Cloud Storage
- S3 Buckets
- DigitalOcean Spaces

### API & Services
- WSDL Files
- SharePoint RCE
- Traefik

## Browser Configuration

The application is configured to open all links in Chrome browser. If Chrome is not available, it will fall back to the default browser.

## Building Executables

To create standalone executables (.exe for Windows, .app/.dmg for macOS, binary for Linux), see [BUILD.md](BUILD.md) for detailed instructions.

### Quick Start:

**Windows:**
```bash
build_windows.bat
```

**macOS:**
```bash
chmod +x build_macos.sh
./build_macos.sh
```

**Linux:**
```bash
chmod +x build_linux.sh
./build_linux.sh
```

**Prerequisites:**
```bash
pip install pyinstaller
```

For macOS DMG creation:
```bash
brew install create-dmg
```

## Notes

- Some searches may trigger Google CAPTCHA - simply solve the puzzle and continue
- Results depend on search engine indexing and may vary
- Always ensure you have proper authorization before performing reconnaissance

## Original Project

This is a Python port of the original C# Windows Forms application:
- Original: [BigBountyRecon](https://github.com/Viralmaniar/BigBountyRecon)
- Author: [@ManiarViral](https://twitter.com/maniarviral)

## License

Creative Commons Attribution 4.0 International License

## Contributing

Any suggestions or ideas for this tool are welcome!

