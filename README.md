# Portfolio Automated Test Suite (Python + Playwright)

Comprehensive end-to-end (E2E) automated test framework built with **Python**, **Playwright**, and **Pytest** for testing the [Oyendri Sana Portfolio](https://myportfolio-virid-nine-58.vercel.app/) web application.

---

## 🚀 Features

- **Comprehensive Test Case Wiki:** Full scenario-by-scenario documentation, traceability matrix, and assertions cataloged in [`TEST_CASES_WIKI.md`](TEST_CASES_WIKI.md).
- **Page Object Model (POM):** Decoupled, modular architecture separating test logic from page locators and user interactions.
- **Cross-Browser Ready:** Out-of-the-box support for Chromium, Firefox, and WebKit (Safari).
- **Responsive Testing:** Automated viewport validations across Desktop (1920×1080), Tablet (768×1024), and Mobile (390×844 & 375×667) ensuring zero horizontal overflow.
- **BDD Gherkin Feature Files:** Behavior-driven scenarios written in `.feature` files and mapped via `pytest-bdd` to Page Object Model actions.
- **Auto-Cleaning Timestamped Reports:** Automatically purges older reports before every test run, keeping only the fresh, timestamped HTML report (`reports/report_YYYY-MM-DD_HH-MM-SS.html`).
- **Fail-Safe Diagnostics:** Captures screenshots, execution videos, and full Playwright traces automatically on test failure.
- **Console Error Guard:** Global fixture actively intercepts unhandled JavaScript exceptions and failed console logs.
- **Fast Parallel Execution:** Supports multi-worker parallel execution via `pytest-xdist`.
- **CI/CD Integration:** Includes pre-configured GitHub Actions workflow with report artifact preservation.

---

## 📁 Repository Structure

```text
Portfolio/
├── workflows/
│   └── playwright.yml       # GitHub Actions CI/CD automated test pipeline template
├── .gitignore               # Git ignore rules for test results, caches, and envs
├── pytest.ini               # Pytest configurations, default browser, markers, flags
├── requirements.txt         # Python dependencies (Playwright, Pytest, Pytest-BDD, etc.)
├── README.md                # Project documentation and execution guide
├── features/                # BDD Gherkin feature files
│   ├── navigation.feature   # Header, logo, and cross-page routing behavior
│   ├── projects.feature     # Featured project cards and tech stack behavior
│   ├── contact.feature      # Contact links and external profiles behavior
│   └── about.feature        # Academic credentials and skills behavior
├── pages/                   # Page Object Model (POM) classes
│   ├── base_page.py         # Common base class with shared browser helpers
│   ├── home_page.py         # Aggregator for index.html sections
│   ├── about_page.py        # Page object for about.html (CV page)
│   └── components/          # Reusable UI component wrappers
│       ├── navbar.py        # Header & navigation bar
│       ├── hero.py          # Hero landing section & CTA buttons
│       ├── projects.py      # Project grid & cards
│       ├── contact.py       # Contact links & social buttons
│       └── footer.py        # Footer component
├── tests/                   # Test suites
│   ├── conftest.py          # Dynamic timestamped HTML reporting, fixtures & hooks
│   ├── step_defs/           # BDD step definitions mapping .feature files to POM
│   │   ├── test_navigation_steps.py
│   │   ├── test_projects_steps.py
│   │   ├── test_contact_steps.py
│   │   └── test_about_steps.py
│   ├── test_smoke.py        # Deployment & health check tests (P0)
│   ├── test_navigation.py   # Routing, anchor scrolling, and active link states
│   ├── test_hero.py         # Hero typography, bio, and CTA interactions
│   ├── test_projects.py     # Featured project cards and tech stack badges
│   ├── test_about.py        # Detailed education timeline, skills & achievements
│   ├── test_contact.py      # Communication buttons and external link security
│   ├── test_responsive.py   # Viewport breakpoints and mobile usability
│   └── test_a11y.py         # Accessibility & semantic compliance tests
└── reports/                 # Auto-generated fresh report (older runs auto-purged)
    └── report_YYYY-MM-DD_HH-MM-SS.html  # Single active timestamped execution report
```

---

## 🛠️ Prerequisites & Installation

### 1. Requirements
- Python 3.10+ (tested on Python 3.14)
- Pip package manager

### 2. Setup Virtual Environment (Optional but Recommended)
```bash
python -m venv .venv
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On Linux/macOS:
source .venv/bin/activate
```

### 3. Install Dependencies & Playwright Browsers
```bash
pip install -r requirements.txt
playwright install chromium firefox
```

---

## 🧪 Running the Tests

### 1. Run the Entire Test Suite (with Parallel Execution)
```bash
pytest -n 3
```

### 2. Run Smoke Tests Only (Fast Health Check)
```bash
pytest -m smoke
```

### 3. Run Specific Test Modules
```bash
# Navigation suite
pytest tests/test_navigation.py

# Responsive mobile & tablet layout suite
pytest tests/test_responsive.py

# About & CV page suite
pytest tests/test_about.py
```

### 4. Run BDD Feature Scenarios
```bash
pytest tests/step_defs -v
```

### 5. Run in Headed Mode (Visual Inspection)
```bash
pytest tests/test_hero.py --headed --slowmo 500
```

### 6. Run Across Multiple Browsers
```bash
# Run on Firefox
pytest tests/test_smoke.py --browser firefox

# Run across Chromium & Firefox in parallel
pytest -n auto --browser chromium --browser firefox
```

### 7. Override Base URL (e.g., Localhost or Staging)
```bash
pytest --base-url http://localhost:3000
```

---

## 📊 HTML Test Reports & Diagnostics

### 1. Automated Clean Timestamped Reports
Every time tests are executed, all older report files in `reports/` are automatically deleted to keep your workspace clean. A single, fresh self-contained HTML report is generated with the exact date and timestamp:
- **Location:** `reports/report_YYYY-MM-DD_HH-MM-SS.html` (e.g., `reports/report_2026-11-08_01-04-04.html`)

Open any report directly in your browser:
- Overall pass/fail statistics and execution duration
- Detailed step-by-step test logs and assertion messages
- System metadata (browser, platform, Python version)

### 2. Failure Diagnostic Artifacts
When a test fails, Playwright automatically captures:
- **Screenshots:** Saved under `test-results/` for failing assertions.
- **Execution Videos:** Retained upon test failure for step-by-step playback.
- **Playwright Trace Viewer:** Inspect the timeline, network calls, and DOM snapshots using:
  ```bash
  playwright show-trace test-results/<test-folder>/trace.zip
  ```

---

## 🔄 CI/CD Workflow & Scheduled Email Delivery (GitHub Actions)

A pre-configured GitHub Actions workflow is located at `.github/workflows/playwright.yml`. It:
1. **Daily Execution at 6:00 AM IST:** Automated cron schedule (`cron: '30 0 * * *'`) runs every morning at 06:00 AM IST (00:30 UTC).
2. **Push & Pull Request Triggers:** Also runs automatically on every push and pull request to `main` / `master`.
3. **Manual Trigger (`workflow_dispatch`):** Allows on-demand execution via GitHub Actions web console.
4. **Environment Setup:** Provisions Python 3.11 and installs Playwright browsers (Chromium & Firefox).
5. **Parallel Test Suite Execution:** Runs the full Playwright suite across multiple worker threads (`pytest -n auto`).
6. **Artifact Archiving:** Uploads test reports and failure traces to GitHub run artifacts (`reports/` and `test-results/`).
7. **Automated Email Dispatch:** Emails the generated self-contained HTML test report directly to **`anjan.das.dev@zohomail.in`**.

### ⚙️ Setting Up Email Secrets on GitHub
To enable the workflow to send emails from your Zoho account:
1. Navigate to your GitHub repository -> **Settings** -> **Secrets and variables** -> **Actions**.
2. Click **New repository secret** and add the following:
   - `MAIL_USERNAME`: Your Zoho Mail email address (e.g. `anjan.das.dev@zohomail.in`).
   - `MAIL_PASSWORD`: Your Zoho Mail **App Password** (generated from Zoho Account Security -> App Passwords).
   - *(Optional)* `MAIL_SERVER`: `smtp.zoho.in` (defaulted in workflow).
   - *(Optional)* `MAIL_PORT`: `465` (defaulted in workflow).
   - *(Optional)* `MAIL_FROM`: Custom sender name (e.g. `Playwright QA Bot <anjan.das.dev@zohomail.in>`).

---

## 📋 Test Coverage Matrix

| Test Suite | Module | Description | Markers |
| :--- | :--- | :--- | :--- |
| **Smoke** | `test_smoke.py` | Validates HTTP 200, title, meta viewport, and `style.css` loading | `@pytest.mark.smoke` |
| **Navigation** | `test_navigation.py` | Header links, cross-page routing to `about.html`, and anchor jumps | `@pytest.mark.navigation` |
| **Hero** | `test_hero.py` | Title typography, highlighted name, bio, and CTA button jumps | `@pytest.mark.hero` |
| **Projects** | `test_projects.py` | Project card counts, card titles, descriptions, and tech stacks | `@pytest.mark.projects` |
| **About** | `test_about.py` | Education timeline items, technical skills categories, and achievements | `@pytest.mark.about` |
| **Contact** | `test_contact.py` | Gmail compose link, LinkedIn, GitHub URLs, and `target="_blank"` | `@pytest.mark.contact` |
| **Responsive**| `test_responsive.py`| Validates 5 screen viewports with zero horizontal overflow | `@pytest.mark.responsive` |
