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

## Repository

* **GitHub URL:** [https://github.com/bautista2501/ai-usage-monitor](https://github.com/bautista2501/ai-usage-monitor)

---

## Pushing Updates to GitHub

```bash
git add .
git commit -m "Update documentation"
git push origin main
```


