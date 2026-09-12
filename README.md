# AI Usage Monitor

A standalone command-line tool to check remaining usage and quota for **GitHub Copilot**, **Codex**, and **Google Antigravity**.

---

## Features

- **GitHub Copilot & Codex:** Queries the GitHub REST API for Copilot subscription status, quota usage, and billing reset dates.
- **Google Antigravity:** Checks active workspace session status and API key quota.
- **Portable & Lightweight:** Uses standard Python 3 with zero required external dependencies (optional `python-dotenv` support).

---

## Setup & Configuration

1. **Clone or navigate to the directory:**
   ```bash
   cd C:\Users\leste\apps\ai-usage-monitor
   ```

2. **Configure your API keys:**
   Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
   Add your GitHub personal access token (`GITHUB_TOKEN`) to `.env`.

3. **Run the script:**
   ```bash
   python check_usage.py
   ```

---

## How to Push to GitHub

Initialize git and create a repository using the GitHub CLI:

```bash
git init
git add .
git commit -m "Initial commit of AI Usage Monitor"
gh repo create ai-usage-monitor --public --source=. --remote=origin --push
```
