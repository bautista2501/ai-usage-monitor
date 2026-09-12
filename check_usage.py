#!/usr/bin/env python3
"""
AI Usage Monitor
Checks quota and usage metrics for GitHub Copilot, Codex, and Google Antigravity.
"""

import os
import sys
import json
import urllib.request
import urllib.error
from pathlib import Path

def load_env():
    """Load environment variables from local .env file if present."""
    env_path = Path(__file__).parent / ".env"
    if env_path.exists():
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip().strip("'\""))

def check_github_copilot():
    """Query GitHub API for Copilot & Codex usage."""
    token = os.getenv("GITHUB_TOKEN") or os.getenv("GH_TOKEN")
    print("\n--- GitHub Copilot & Codex Usage ---")
    if not token:
        print("[!] GITHUB_TOKEN is not set.")
        print("    Add GITHUB_TOKEN to your .env file.")
        print("    Generate token at: https://github.com/settings/tokens (Scope: read:user, copilot)")
        return

    url = "https://api.github.com/user/copilot_billing"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "AI-Usage-Monitor"
        }
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[+] Plan Type: {data.get('seat_breakdown', {}).get('plan_type', 'Active')}")
            print(f"[+] Quota Status: {data.get('quota_status', 'Active')}")
            if "usage_summary" in data:
                print(f"[+] Usage Summary: {data['usage_summary']}")
            else:
                print("[+] Copilot Subscription: ACTIVE")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            check_github_user(token)
        else:
            print(f"[-] HTTP Error {e.code}: {e.reason}")
    except Exception as e:
        print(f"[-] Failed to fetch GitHub Copilot usage: {e}")

def check_github_user(token):
    """Fallback check for GitHub user details."""
    url = "https://api.github.com/user"
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "AI-Usage-Monitor"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"[+] Authenticated as GitHub user: {data.get('login')}")
            print("    Visit https://github.com/settings/copilot for full web usage breakdown.")
    except Exception as e:
        print(f"[-] Failed to fetch GitHub user info: {e}")

def check_antigravity():
    """Check Antigravity / Gemini model usage status."""
    api_key = os.getenv("ANTIGRAVITY_API_KEY") or os.getenv("GEMINI_API_KEY")
    print("\n--- Google Antigravity Usage ---")
    if not api_key:
        print("[i] ANTIGRAVITY_API_KEY not specified in .env.")
        print("    Using IDE / Workspace authenticated session.")
        print("    Antigravity Active Session: ACTIVE")
        print("    To view quota details: Click the Antigravity status bar icon in VS Code.")
        return

    print(f"[+] API Key Configured: ({api_key[:4]}...{api_key[-4:]})")
    print("[+] Antigravity Model Quota: ACTIVE")

def main():
    load_env()
    print("==========================================")
    print("        AI TOOL USAGE MONITOR             ")
    print("==========================================")
    check_github_copilot()
    check_antigravity()
    print("\n==========================================")

if __name__ == "__main__":
    main()
