# One-click test execution script for Windows PowerShell
param (
    [string]$Mode = "parallel",
    [string]$Browser = "chromium"
)

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "  Oyendri Sana Portfolio Test Runner" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan

switch ($Mode) {
    "smoke" {
        Write-Host "Running Smoke Tests..." -ForegroundColor Yellow
        pytest -m smoke --browser $Browser
    }
    "bdd" {
        Write-Host "Running BDD Feature Scenarios..." -ForegroundColor Yellow
        pytest tests/step_defs -v --browser $Browser
    }
    "headed" {
        Write-Host "Running in Headed Mode (Visual Inspection)..." -ForegroundColor Yellow
        pytest tests/test_hero.py --headed --slowmo 500
    }
    default {
        Write-Host "Running Full Parallel Suite across 3 workers..." -ForegroundColor Yellow
        pytest -n 3 --browser $Browser
    }
}

Write-Host "==========================================" -ForegroundColor Green
Write-Host "Done! Fresh HTML report generated in ./reports/" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

