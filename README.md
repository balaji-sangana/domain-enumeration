<h1 align="center">🛡️ domain-enumeration</h1>

<p align="center">
  <b>Passive OSINT Domain Reconnaissance Framework</b><br>
  Clean • Safe • Professional • CLI-First
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OSINT-Passive-2ECC71?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Security-Authorized_Testing-F39C12?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-95A5A6?style=for-the-badge"/>
</p>

<p align="center">
  🔍 <b>Discover subdomains using passive intelligence sources</b><br>
  🛡️ Built with legality, safety, and clean CLI UX in mind
</p>

<hr>

<p align="center">
  <b>domain-enumeration</b> is a <b>modular and professional reconnaissance tool</b> designed to enumerate
  <b>subdomains</b> using <b>passive OSINT techniques</b> only.
</p>

<p align="center">
  Ideal for <b>Security Researchers</b>, <b>Bug Bounty Hunters</b>, <b>Blue Teams</b>, and <b>Cybersecurity Students</b>.
</p>

---

## 🚀 Features

### 🔍 Passive Recon (Safe by Default)
- Subdomain enumeration using:
  - **crt.sh** (Certificate Transparency)
  - **BufferOver DNS**
  - **RapidDNS**
  - **HackerTarget**
- Automatic duplicate removal
- Source tagging (know *where* each result came from)
- Source filtering (`--sources`)
- Positional domain input
- Graceful handling when sources are unavailable

### 🎛️ CLI & UX
- Clean ASCII banner (always visible)
- `--quiet` → banner shown, only results
- `--verbose` → detailed source activity logs
- `--version` → banner + version only
- Automation-friendly output

### 🛡️ Legal & Ethical Design
- Passive OSINT only
- No brute-force or exploitation
- Explicit legal disclaimer
- Designed for **authorized security testing and education**

---

## 📦 Installation

🔹 Clone the Repository
```bash
git clone https://github.com/<your-username>/domain-enumeration.git
cd domain-enumeration
```
🔹 Install Dependencies
```bash
pip install requests
```
🔹 Run the Tool
```bash
python3 subnum.py example.com -ds
```
### ▶️ Usage Examples
🔹 Basic Subdomain Enumeration
```bash
python3 subnum.py example.com -ds
```
🔹 Use Specific Sources
```bash
python3 subnum.py example.com -ds --sources crtsh,rapiddns
```
🔹 Verbose Mode (Detailed Logs)
```bash
python3 subnum.py example.com -ds --verbose
```
🔹 Quiet Mode (Minimal Output)
```bash
python3 subnum.py example.com -ds --quiet
```
🔹 Show Version
```bash
python3 subnum.py -v
```
### 🧩 Command-Line Options
```bash
usage: subnum.py [options] example.com

positional arguments:
  domain                Target domain (example.com)

options:
  -ds, --domains         Enumerate subdomains
  --sources              Filter sources (crtsh,bufferover,rapiddns,hackertarget)
  --quiet                Suppress non-result output
  --verbose              Show detailed source activity
  -v, --version          Show version information
  -o                     Output file name
  -h, --help             Show help message
```
### 📂 Output
📄 Example Output File (example.com.txt)
```bash
api.example.com
mail.example.com 
www.example.com
```
- Results are deduplicated
- Sorted output
- Each subdomain is tagged with its source(s)

🧠 How It Works
- Takes a target domain as input
- Queries selected passive OSINT sources
- Normalizes and deduplicates results
- Tags each subdomain with discovery source
- Saves clean output to a file
- No active interaction with the target system is performed.

### ⚠️ Legal Disclaimer
**This tool is intended only for educational purposes and authorized security testing.
The author is not responsible for any illegal or unethical use.
Always obtain explicit permission before testing any domain.**

### 📜 License
This project is licensed under the MIT License.

⭐ If you find this project useful, consider giving it a star on GitHub!












