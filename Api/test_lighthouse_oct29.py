
import json
import shutil
import subprocess
from pathlib import Path

import pytest
from playwright.async_api import async_playwright, expect


# --------------------------------------------------
# Configuration
# --------------------------------------------------

URL = "https://parabank.parasoft.com/parabank/register.htm"

REPORT_DIR = Path(
    r"C:\Users\RANJITHA\Desktop\playwright project\tests\Light_house"
)

REPORT_DIR.mkdir(parents=True, exist_ok=True)

REPORT_FILE = REPORT_DIR / "lighthouse.json"


# --------------------------------------------------
# Test 1: Lighthouse Report
# --------------------------------------------------

@pytest.mark.asyncio
async def test_lighthousejson():

    # Find npx.cmd on Windows
    npx_path = shutil.which("npx.cmd") or shutil.which("npx")

    if not npx_path:
        pytest.fail(
            "npx was not found. Install Node.js and check the PATH environment variable."
        )

    print("Npx location:", npx_path)

    # Run Lighthouse
    command = [
        npx_path,
        "--yes",
        "lighthouse",
        URL,
        "--chrome-flags=--headless",
        "--output=json",
        f"--output-path={REPORT_FILE}",
    ]

    result = subprocess.run(
        command,
        cwd=str(REPORT_DIR),
        capture_output=True,
        text=True,
        timeout=300,
        shell=False,
    )

    print("Lighthouse output:")
    print(result.stdout)

    if result.stderr:
        print("Lighthouse errors:")
        print(result.stderr)

    assert result.returncode == 0, (
        f"Lighthouse execution failed.\n"
        f"Return code: {result.returncode}\n"
        f"Error: {result.stderr}"
    )

    # Check whether report was generated
    assert REPORT_FILE.exists(), "Lighthouse JSON report was not generated."

    # Read JSON report
    with open(REPORT_FILE, "r", encoding="utf-8") as file:
        report = json.load(file)

    # Extract Lighthouse scores
    categories = report.get("categories", {})

    performance = categories.get("performance", {}).get("score")
    accessibility = categories.get("accessibility", {}).get("score")
    best_practices = categories.get("best-practices", {}).get("score")
    seo = categories.get("seo", {}).get("score")

    print("\n========== LIGHTHOUSE SCORES ==========")
    print(f"Performance:   {performance * 100 if performance is not None else 'N/A'}")
    print(f"Accessibility: {accessibility * 100 if accessibility is not None else 'N/A'}")
    print(f"Best Practices:{best_practices * 100 if best_practices is not None else 'N/A'}")
    print(f"SEO:           {seo * 100 if seo is not None else 'N/A'}")
    print("=======================================\n")


# --------------------------------------------------
# Test 2: DOM Validation
# --------------------------------------------------

@pytest.mark.asyncio
async def test_dom_validation():

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        try:
            await page.goto(URL, wait_until="domcontentloaded")

            # 1. Verify page title
            title = await page.title()

            print("Page title:", title)

            assert title.strip(), "Page title is missing."

            # 2. Verify images have alt attributes
            missing_alt = await page.locator("img:not([alt])").count()

            print("Images without alt attribute:", missing_alt)

            assert missing_alt == 0, (
                f"{missing_alt} image(s) are missing alt attributes."
            )

            # 3. Verify main landmark
            main_count = await page.locator("main").count()

            print("Main landmark count:", main_count)

            assert main_count >= 1, "Main landmark is missing."

            print("DOM validation completed successfully.")

        finally:
            await browser.close()
