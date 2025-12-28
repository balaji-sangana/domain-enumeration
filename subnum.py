#!/usr/bin/env python3
# ==========================================================
# domain-enumeration
# File    : subnum.py
# Author  : Balaji Sangana
# Version : 1.0.0
# ==========================================================
# ⚠ For educational and authorized security testing only
# ⚠ We are not responsible for any illegal actions
# ==========================================================

import argparse
import requests
import time
import random
import sys

VERSION = "1.0.0"

# =========================================================
# Banner (ALWAYS SHOWN)
# =========================================================
def banner():
    print("""
============================================================
██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

              DOMAIN ENUMERATION FRAMEWORK
------------------------------------------------------------
      Passive OSINT  |  Authorized Active Recon
------------------------------------------------------------
  ⚠ For educational and authorized security testing only
  ⚠ We are not responsible for any illegal actions
------------------------------------------------------------
             Author : Balaji Sangana
============================================================
""")

# =========================================================
# Utils
# =========================================================
USER_AGENTS = [
    "Mozilla/5.0",
    "curl/7.88.1",
    "ReconTool",
    "domain-enumeration/1.2.1"
]

def ua():
    return {"User-Agent": random.choice(USER_AGENTS)}

def vprint(msg, verbose):
    if verbose:
        print(f"[+] {msg}")

def qprint(msg, quiet):
    if not quiet:
        print(msg)

# =========================================================
# Passive Subdomain Sources (Tagged)
# =========================================================
def crtsh(domain, verbose):
    vprint("Querying crt.sh", verbose)
    res = {}
    urls = [
        f"http://crt.sh/?q=%25.{domain}&output=json",
        f"https://crt.sh/?q=%25.{domain}&output=json"
    ]
    for _ in range(3):
        for url in urls:
            try:
                r = requests.get(url, headers=ua(), timeout=20)
                if r.status_code != 200:
                    continue
                if "application/json" not in r.headers.get("Content-Type", ""):
                    continue
                for entry in r.json():
                    for name in entry.get("name_value", "").split("\n"):
                        name = name.strip().lower().lstrip("*.")
                        if name.endswith(domain):
                            res.setdefault(name, set()).add("crtsh")
                if res:
                    return res
            except:
                pass
        time.sleep(2)
    return res

def bufferover(domain, verbose):
    vprint("Querying BufferOver DNS", verbose)
    res = {}
    try:
        r = requests.get(f"https://dns.bufferover.run/dns?q=.{domain}", headers=ua(), timeout=15)
        if r.status_code == 200:
            data = r.json()
            for rec in data.get("FDNS_A", []) + data.get("RDNS", []):
                sub = rec.split(",")[-1].strip().lower()
                if sub.endswith(domain):
                    res.setdefault(sub, set()).add("bufferover")
    except:
        pass
    return res

def rapiddns(domain, verbose):
    vprint("Querying RapidDNS", verbose)
    res = {}
    try:
        r = requests.get(f"https://rapiddns.io/subdomain/{domain}?full=1", headers=ua(), timeout=20)
        if r.status_code == 200:
            for line in r.text.splitlines():
                if "<td>" in line and domain in line:
                    sub = line.split("<td>")[1].split("</td>")[0].strip().lower()
                    if sub.endswith(domain):
                        res.setdefault(sub, set()).add("rapiddns")
    except:
        pass
    return res

def hackertarget(domain, verbose):
    vprint("Querying HackerTarget", verbose)
    res = {}
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", headers=ua(), timeout=15)
        if r.status_code == 200 and "error" not in r.text.lower():
            for line in r.text.splitlines():
                sub = line.split(",")[0].strip().lower()
                if sub.endswith(domain):
                    res.setdefault(sub, set()).add("hackertarget")
    except:
        pass
    return res

SOURCE_MAP = {
    "crtsh": crtsh,
    "bufferover": bufferover,
    "rapiddns": rapiddns,
    "hackertarget": hackertarget
}

def enumerate_subdomains(domain, sources, verbose):
    combined = {}
    for src in sources:
        data = SOURCE_MAP[src](domain, verbose)
        for sub, tags in data.items():
            combined.setdefault(sub, set()).update(tags)
    return combined

# =========================================================
# Main
# =========================================================
def main():
    parser = argparse.ArgumentParser(description="domain-enumeration framework")

    parser.add_argument("domain", nargs="?", help="Target domain (example.com)")
    parser.add_argument("-ds", "--domains", action="store_true", help="Enumerate subdomains")
    parser.add_argument("--sources", help="crtsh,bufferover,rapiddns,hackertarget")
    parser.add_argument("--quiet", action="store_true", help="Only show results")
    parser.add_argument("--verbose", action="store_true", help="Verbose output")
    parser.add_argument("-v", "--version", action="store_true", help="Show version")
    parser.add_argument("-o", help="Output file")

    args = parser.parse_args()

    # Banner ALWAYS
    banner()

    if args.version:
        print(f"domain-enumeration version {VERSION}")
        sys.exit(0)

    if not args.domain:
        qprint("[-] Domain is required", args.quiet)
        sys.exit(1)

    sources = list(SOURCE_MAP.keys())
    if args.sources:
        sources = [s for s in args.sources.split(",") if s in SOURCE_MAP]

    if args.domains:
        subs = enumerate_subdomains(args.domain, sources, args.verbose)
        if subs:
            outfile = args.o if args.o else f"{args.domain}.txt"
            with open(outfile, "w") as f:
                for sub in sorted(subs.items()):
                    f.write(f"{sub}\n")

            qprint(f"[✓] Subdomains found: {len(subs)}", args.quiet)
            qprint(f"[✓] Saved to: {outfile}", args.quiet)
        else:
            qprint("[-] No subdomains found", args.quiet)

if __name__ == "__main__":
    main()
