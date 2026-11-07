# QA Test Case Wiki: Oyendri Sana Portfolio Automation

> **Application Under Test (AUT):** [https://myportfolio-virid-nine-58.vercel.app/](https://myportfolio-virid-nine-58.vercel.app/)  
> **Automation Stack:** Python 3.10+ | Playwright | Pytest | pytest-bdd | pytest-html  
> **Repository:** [Anjandas2005/friendly-portfolio-qa-playwright-python](https://github.com/Anjandas2005/friendly-portfolio-qa-playwright-python)  
> **Last Updated:** November 2026  
> **Total Test Cases:** 40 automated tests across 10 functional suites  

---

## 📖 Table of Contents
1. [Framework Architecture & POM Overview](#1-framework-architecture--pom-overview)
2. [Master Test Case Traceability Matrix](#2-master-test-case-traceability-matrix)
3. [Suite 1: Smoke & Deployment Availability](#3-suite-1-smoke--deployment-availability)
4. [Suite 2: Navigation & Routing](#4-suite-2-navigation--routing)
5. [Suite 3: Hero Section & Call-to-Actions](#5-suite-3-hero-section--call-to-actions)
6. [Suite 4: Featured Projects Showcase](#6-suite-4-featured-projects-showcase)
7. [Suite 5: About & Academic Credentials](#7-suite-5-about--academic-credentials)
8. [Suite 6: Contact Channels & External Security](#8-suite-6-contact-channels--external-security)
9. [Suite 7: Responsive Viewport Breakpoints](#9-suite-7-responsive-viewport-breakpoints)
10. [Suite 8: Accessibility & Semantic Compliance](#10-suite-8-accessibility--semantic-compliance)
11. [Suite 9: Performance & Asset Integrity](#11-suite-9-performance--asset-integrity)
12. [Suite 10: BDD Feature Scenarios (Gherkin)](#12-suite-10-bdd-feature-scenarios-gherkin)
13. [Test Execution & HTML Reporting Guide](#13-test-execution--html-reporting-guide)

---

## 1. Framework Architecture & POM Overview

The testing framework employs the **Page Object Model (POM)** pattern integrated with **Pytest**, **pytest-playwright**, and **pytest-bdd**:

```text
Portfolio/
├── features/               # Gherkin BDD business scenarios (.feature)
│   ├── navigation.feature  # User journey: header & routing
│   ├── projects.feature    # User journey: featured project cards
│   ├── contact.feature     # User journey: email & social links
│   └── about.feature       # User journey: credentials & skills
├── pages/                  # Page Object Model locators & helper methods
│   ├── base_page.py        # Generic browser interactions & waits
│   ├── home_page.py        # Main landing page aggregator
│   ├── about_page.py       # CV page (about.html) aggregator
│   └── components/         # Modular UI component wrappers
│       ├── navbar.py       # Header, navigation links & branding
│       ├── hero.py         # Hero landing section & CTA buttons
│       ├── projects.py     # Featured projects grid & card elements
│       ├── contact.py      # Contact links, icons & mail actions
│       └── footer.py       # Footer copyright component
├── tests/                  # Executable test suites
│   ├── conftest.py         # Dynamic reporting & auto-purge hooks
│   ├── step_defs/          # Step definition bindings for BDD features
│   ├── test_smoke.py       # Health checks & deployment validation
│   ├── test_navigation.py  # Header links & smooth scroll anchors
│   ├── test_hero.py        # Hero typography & CTA jumps
│   ├── test_projects.py    # Project card counts & tech tags
│   ├── test_about.py       # Education timeline & skills categories
│   ├── test_contact.py     # Communication buttons & security checks
│   ├── test_responsive.py  # Layout checks across 5 viewports
│   ├── test_a11y.py        # Accessibility & semantic HTML
│   └── test_performance.py # Network assets & page load latency
├── reports/                # Auto-generated fresh HTML reports
└── workflows/              # GitHub Actions CI/CD pipeline template
```

---

## 2. Master Test Case Traceability Matrix

| Test ID | Suite / Module | Scenario Title | Priority | Type | Status |
| :--- | :--- | :--- | :---: | :---: | :---: |
| **TC-SMK-01** | Smoke | Homepage Deployment & Title Validation | P0 | Smoke | ✅ Passed |
| **TC-SMK-02** | Smoke | About Page Deployment & Title Validation | P0 | Smoke | ✅ Passed |
| **TC-SMK-03** | Smoke | Viewport Meta Tag & Stylesheet Loading | P1 | Smoke | ✅ Passed |
| **TC-NAV-01** | Navigation | Navbar Structure, Branding Logo & Link Count | P1 | Functional | ✅ Passed |
| **TC-NAV-02** | Navigation | Navigate to About Page via Navbar & Active Styling | P1 | Functional | ✅ Passed |
| **TC-NAV-03** | Navigation | Return to Homepage from About Page | P1 | Functional | ✅ Passed |
| **TC-NAV-04** | Navigation | In-Page Anchor Links Smooth Scrolling | P2 | Functional | ✅ Passed |
| **TC-HER-01** | Hero | Hero Typography, Highlighted Name & Bio Paragraph | P1 | UI / Visual | ✅ Passed |
| **TC-HER-02** | Hero | "View My Work" Button Scrolls to Projects Section | P1 | Functional | ✅ Passed |
| **TC-HER-03** | Hero | "Know More About Me" Button Navigates to About Page | P1 | Functional | ✅ Passed |
| **TC-PRJ-01** | Projects | Section Heading & Total Project Cards Count | P1 | UI | ✅ Passed |
| **TC-PRJ-02** | Projects | Exact Verification of Project Card Titles | P1 | Content | ✅ Passed |
| **TC-PRJ-03** | Projects | Technology Stack Badges & Card Descriptions | P2 | Content | ✅ Passed |
| **TC-ABT-01** | About | About Page Headings & Summary Card Verification | P1 | UI | ✅ Passed |
| **TC-ABT-02** | About | Education Timeline Items (B.Tech, Class XII, Class X) | P1 | Content | ✅ Passed |
| **TC-ABT-03** | About | Technical Skills Grid & Category Structure | P2 | Content | ✅ Passed |
| **TC-ABT-04** | About | Certifications & Business Pitch Achievements | P2 | Content | ✅ Passed |
| **TC-CNT-01** | Contact | Contact Section Header & Button Labels | P1 | UI | ✅ Passed |
| **TC-CNT-02** | Contact | External Link Tab Security (`target="_blank"`) | P1 | Security | ✅ Passed |
| **TC-CNT-03** | Contact | Gmail Compose Direct Link with Target Address | P1 | Integration | ✅ Passed |
| **TC-CNT-04** | Contact | LinkedIn & GitHub Profile URLs | P1 | Integration | ✅ Passed |
| **TC-RSP-01** | Responsive | Desktop Full HD (1920×1080) Zero Overflow | P1 | Responsive | ✅ Passed |
| **TC-RSP-02** | Responsive | Standard Laptop (1366×768) Zero Overflow | P1 | Responsive | ✅ Passed |
| **TC-RSP-03** | Responsive | Tablet iPad (768×1024) Zero Overflow | P1 | Responsive | ✅ Passed |
| **TC-RSP-04** | Responsive | Mobile iPhone 13/14 (390×844) Zero Overflow | P0 | Responsive | ✅ Passed |
| **TC-RSP-05** | Responsive | Mobile iPhone SE (375×667) Zero Overflow | P0 | Responsive | ✅ Passed |
| **TC-RSP-06** | Responsive | Project Cards Dynamic Stacking on Mobile | P1 | Responsive | ✅ Passed |
| **TC-A11-01** | A11y | Root HTML Language Attribute (`<html lang="en">`) | P2 | Compliance | ✅ Passed |
| **TC-A11-02** | A11y | Single Primary `<h1>` Heading Rule | P2 | Compliance | ✅ Passed |
| **TC-A11-03** | A11y | Accessible Text or Labels on All Anchor Elements | P2 | Compliance | ✅ Passed |
| **TC-A11-04** | A11y | Safe Protocols & External Link Rel Guard | P2 | Compliance | ✅ Passed |
| **TC-A11-05** | A11y | Keyboard Tab Focus Progression on Interactive Elements | P2 | Compliance | ✅ Passed |
| **TC-PRF-01** | Performance | Zero Failed Network Requests on Homepage | P1 | Performance | ✅ Passed |
| **TC-PRF-02** | Performance | Navigation Timing Latency API (DOM & Page Load) | P2 | Performance | ✅ Passed |
| **TC-PRF-03** | Performance | Zero Failed Network Requests on About Page | P1 | Performance | ✅ Passed |
| **BDD-NAV-01** | BDD | Scenario: User visits homepage and views branding | P1 | BDD | ✅ Passed |
| **BDD-NAV-02** | BDD | Scenario: User navigates from Home to About page and back | P1 | BDD | ✅ Passed |
| **BDD-PRJ-01** | BDD | Scenario: View featured project cards and technologies | P1 | BDD | ✅ Passed |
| **BDD-CNT-01** | BDD | Scenario: Verify external contact channels | P1 | BDD | ✅ Passed |
| **BDD-ABT-01** | BDD | Scenario: Verify education and technical skills | P1 | BDD | ✅ Passed |

---

## 3. Suite 1: Smoke & Deployment Availability

*File: [`tests/test_smoke.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_smoke.py)*

### TC-SMK-01: Homepage Deployment & Title Validation
- **Objective:** Verify target Vercel URL responds with HTTP 200 without deployment errors.
- **Steps:**
  1. Send GET request to `https://myportfolio-virid-nine-58.vercel.app/`.
  2. Wait until `domcontentloaded`.
- **Assertions:**
  - `response.status == 200`
  - Document text does not contain `DEPLOYMENT_NOT_FOUND`.
  - Document title equals `"Oyendri Sana | Curriculum Vitae"`.

### TC-SMK-02: About Page Deployment & Title Validation
- **Objective:** Verify dedicated CV page (`about.html`) is live and accessible.
- **Steps:**
  1. Navigate to `/about.html`.
- **Assertions:**
  - `response.status == 200`
  - Document title equals `"About Me | Oyendri Sana"`.

### TC-SMK-03: Viewport Meta Tag & Stylesheet Loading
- **Objective:** Ensure responsive layout meta tag and primary CSS link exist in `<head>`.
- **Assertions:**
  - `<meta name="viewport">` has content `"width=device-width, initial-scale=1.0"`.
  - `<link rel="stylesheet" href="style.css">` count is exactly 1.

---

## 4. Suite 2: Navigation & Routing

*File: [`tests/test_navigation.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_navigation.py)*

### TC-NAV-01: Navbar Structure & Branding Logo
- **Objective:** Verify navigation bar displays brand logo and all primary menu options.
- **Assertions:**
  - Logo locator has text `"Oyendri Sana"`.
  - Exactly 4 navigation links exist: `["Home", "About", "Projects", "Contact"]`.

### TC-NAV-02: Navigate to About Page via Navbar
- **Objective:** Clicking "About" in navbar loads `about.html` and activates styling.
- **Assertions:**
  - URL matches `about\.html$`.
  - Title updates to `"About Me | Oyendri Sana"`.
  - Active link `ul.nav-links li a.active` has text `"About"`.

### TC-NAV-03: Return to Homepage from About Page
- **Objective:** Clicking "Home" from `about.html` navigates back to index.
- **Assertions:**
  - URL ends with `index.html` or `.app/`.
  - Title reverts to `"Oyendri Sana | Curriculum Vitae"`.

### TC-NAV-04: Anchor Links Smooth Scrolling
- **Objective:** Clicking "#projects" and "#contact" scrolls respective sections into view.
- **Assertions:**
  - `home_page.projects.section` is in viewport.
  - `home_page.contact.section` is in viewport.

---

## 5. Suite 3: Hero Section & Call-to-Actions

*File: [`tests/test_hero.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_hero.py)*

### TC-HER-01: Hero Typography & Intro Bio
- **Objective:** Validate hero headline, highlighted name, and professional summary statement.
- **Assertions:**
  - Heading contains `"Hi, I'm"`.
  - `.highlight` span contains `"Oyendri Sana"`.
  - Bio paragraph matches `"B.Tech CSE Student & Web Developer passionate about building efficient, user-friendly software."`.

### TC-HER-02: "View My Work" CTA Interaction
- **Objective:** Primary CTA button scrolls user directly to featured projects.
- **Assertions:**
  - Button text equals `"View My Work"`.
  - Projects section enters viewport upon click.

### TC-HER-03: "Know More About Me" CTA Interaction
- **Objective:** Secondary CTA button routes to `about.html`.
- **Assertions:**
  - Button text equals `"Know More About Me"`.
  - URL updates to `about.html`.

---

## 6. Suite 4: Featured Projects Showcase

*File: [`tests/test_projects.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_projects.py)*

### TC-PRJ-01: Section Heading & Project Cards Count
- **Objective:** Verify section heading and total featured projects.
- **Assertions:**
  - Heading text equals `"Featured Projects"`.
  - Card count is exactly 3.

### TC-PRJ-02: Project Titles Validation
- **Objective:** Validate title of each displayed project card.
- **Expected Titles:**
  1. `"Netflix Clone"`
  2. `"Energy Bill Optimization"`
  3. `"Intelligent Health Assistant(in progress)"`

### TC-PRJ-03: Technology Stack Badges & Descriptions
- **Objective:** Verify each project card details technology chips and non-empty description.
- **Expected Tech Stacks:**
  - Card 0: `["HTML", "CSS", "JavaScript"]`
  - Card 1: `["Utility Management", "Dashboard"]`
  - Card 2: `["Data Processing", "Web UI"]`
  - Description length > 20 characters for each card.

---

## 7. Suite 5: About & Academic Credentials

*File: [`tests/test_about.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_about.py)*

### TC-ABT-01: Main Heading & Profile Card
- **Objective:** Validate layout structure on `about.html`.
- **Assertions:**
  - Main heading equals `"About Me"`.
  - Summary card contains `"Professional Profile"`.

### TC-ABT-02: Education History Entries
- **Objective:** Verify chronological education history items.
- **Assertions:**
  - Education count is 3.
  - Primary degree: `"B.Tech in Computer Science Engineering"`.
  - University/College: `"Gargi Memorial Institute of Technology, Kolkata"`.
  - Meta timeframe: `"2023 – 2027"`.

### TC-ABT-03: Technical Skills Categories
- **Objective:** Verify categorized skills grid.
- **Expected Categories:**
  1. `"Programming Languages"`
  2. `"Web & Frontend"`
  3. `"Core CS Concepts"`

### TC-ABT-04: Certifications & Achievements
- **Objective:** Verify professional certifications and business competition entries.
- **Assertions:**
  - First entry mentions `"Ardent Computech Pvt. Ltd."`.
  - Second entry mentions `"TiE Kolkata"`.

---

## 8. Suite 6: Contact Channels & External Security

*File: [`tests/test_contact.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_contact.py)*

### TC-CNT-01: Section Header & Buttons Presence
- **Objective:** Verify "Get In Touch" section and communication options.
- **Assertions:**
  - Button texts: `["Email Me", "LinkedIn", "GitHub"]`.

### TC-CNT-02: External Tab Security (`target="_blank"`)
- **Objective:** Ensure external profile links open safely in a new browser tab.
- **Assertions:**
  - All 3 buttons contain `target="_blank"`.

### TC-CNT-03: Gmail Compose Direct Link
- **Objective:** Clicking "Email Me" triggers Gmail compose with recipient pre-filled.
- **Assertions:**
  - `href` contains `"https://mail.google.com/mail/?view=cm&fs=1&to=oyendri.sana.in@gmail.com"`.

### TC-CNT-04: LinkedIn & GitHub Profile URLs
- **Assertions:**
  - LinkedIn `href` equals `"https://linkedin.com/in/oyendri-sana-14b73035a"`.
  - GitHub `href` equals `"https://github.com/oyendrisana"`.

---

## 9. Suite 7: Responsive Viewport Breakpoints

*File: [`tests/test_responsive.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_responsive.py)*

### TC-RSP-01 to TC-RSP-05: Horizontal Overflow Audit
- **Objective:** Ensure no unwanted horizontal scrolling across standard device sizes.
- **Tested Resolutions:**
  - `1920×1080` (Desktop Full HD)
  - `1366×768` (Standard Laptop)
  - `768×1024` (Tablet iPad)
  - `390×844` (Mobile iPhone 13/14)
  - `375×667` (Mobile iPhone SE)
- **Assertion:**
  - `document.documentElement.scrollWidth <= window.innerWidth` across all viewports.

### TC-RSP-06: Mobile Project Cards Dynamic Stacking
- **Objective:** On mobile screens (390px), project cards must stack vertically with comfortable touch dimensions.
- **Assertion:**
  - Card bounding box width > 250px.

---

## 10. Suite 8: Accessibility & Semantic Compliance

*File: [`tests/test_a11y.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_a11y.py)*

### TC-A11-01: Document Language (`lang="en"`)
- **Assertion:** Root `<html>` element has `lang="en"`.

### TC-A11-02: Single Primary `<h1>` Heading Rule
- **Assertion:** Exactly one `<h1>` heading exists on the homepage.

### TC-A11-03: Accessible Anchor Names
- **Assertion:** All `<a>` tags have non-empty accessible text or `aria-label`.

### TC-A11-04: Safe External Link Protocols
- **Assertion:** All `target="_blank"` links point to valid `http`/`https` URLs.

### TC-A11-05: Keyboard Tab Focus Progression
- **Assertion:** Pressing `Tab` cycles focus to an interactive element (`<a>`, `<button>`).

---

## 11. Suite 9: Performance & Asset Integrity

*File: [`tests/test_performance.py`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/tests/test_performance.py)*

### TC-PRF-01: Zero Broken Assets on Homepage
- **Assertion:** Zero 4xx or 5xx HTTP response codes for all stylesheet, font, and image requests.

### TC-PRF-02: Navigation Timing API Thresholds
- **Thresholds:**
  - `DOMContentLoaded` < 5000ms.
  - Full Page Load < 8000ms.

### TC-PRF-03: Zero Broken Assets on About Page
- **Assertion:** Zero failed network requests when navigating through `/about.html`.

---

## 12. Suite 10: BDD Feature Scenarios (Gherkin)

*Directory: [`features/`](file:///C:/Users/pc/Desktop/Testing%20Practice/Oyendri/Portfolio/features)*

### BDD-NAV-01 & BDD-NAV-02: Navigation & Routing
```gherkin
Feature: Portfolio Navigation & Routing
  Scenario: User visits the homepage and views branding
    Given the user opens the portfolio homepage
    Then the navigation bar should display logo "Oyendri Sana"
    And the page title should be "Oyendri Sana | Curriculum Vitae"

  Scenario: User navigates from Home to About page and back
    Given the user opens the portfolio homepage
    When the user clicks on the "About" navigation link
    Then the page title should change to "About Me | Oyendri Sana"
    And the current URL should include "about.html"
    When the user clicks on the "Home" navigation link
    Then the current URL should be the homepage
```

### BDD-PRJ-01: Projects Showcase
```gherkin
Feature: Featured Projects Showcase
  Scenario: View featured project cards and technologies
    Given the user opens the portfolio homepage
    When the user views the "Featured Projects" section
    Then there should be 3 project cards displayed
    And the projects should include "Netflix Clone", "Energy Bill Optimization", and "Intelligent Health Assistant(in progress)"
```

### BDD-CNT-01: Contact Channels
```gherkin
Feature: Contact & Professional Links
  Scenario: Verify external contact channels
    Given the user opens the portfolio homepage
    When the user scrolls to the "Get In Touch" section
    Then the email button should link to Gmail compose for "oyendri.sana.in@gmail.com"
    And the LinkedIn button should link to "https://linkedin.com/in/oyendri-sana-14b73035a"
    And the GitHub button should link to "https://github.com/oyendrisana"
    And all social links should open in a new tab
```

### BDD-ABT-01: Academic Credentials
```gherkin
Feature: About Me and Academic Credentials
  Scenario: Verify education and technical skills
    Given the user navigates directly to the About page
    Then the main heading should be "About Me"
    And there should be 3 education history items listed
    And the primary degree should be "B.Tech in Computer Science Engineering"
    And the technical skills should include "Programming Languages", "Web & Frontend", and "Core CS Concepts"
```

---

## 13. Test Execution & HTML Reporting Guide

### Quick Execution Commands

```powershell
# Run all 40 tests in parallel across 3 worker threads
pytest -n 3

# Run BDD feature scenarios only
pytest tests/step_defs -v

# Run smoke tests only
pytest -m smoke

# Run single suite (e.g. accessibility)
pytest tests/test_a11y.py -v

# Run with headed browser for visual inspection
pytest tests/test_hero.py --headed --slowmo 500

# Run with one-click PowerShell runner
.\run_tests.ps1
```

### Dynamic Auto-Cleaning Reports
Every execution automatically removes prior report files in `reports/` and generates a single fresh HTML report:
- **Location:** `reports/report_YYYY-MM-DD_HH-MM-SS.html`
- **Features:** Self-contained single-file HTML including execution graphs, timing metrics, environment metadata, and assertion details.
