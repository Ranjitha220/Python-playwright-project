
from pathlib import Path

from PIL import Image, ImageChops
import pytest
from playwright.async_api import async_playwright


# Screenshot paths
PROJECT_DIR = Path(__file__).resolve().parent

SCREENSHOT_DIR = PROJECT_DIR / "screenshots"

BASELINE = SCREENSHOT_DIR / "baseline.png"
ACTUAL = SCREENSHOT_DIR / "actual.png"
DIFF = SCREENSHOT_DIR / "diff.png"

SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

URL = "https://www.amazon.in/"

# Allowed visual difference
THRESHOLD = 0.01


@pytest.mark.asyncio
async def test_visual_regression():

    # Create screenshot directory
    BASELINE.parent.mkdir(parents=True, exist_ok=True)

    # Launch browser and capture actual screenshot
    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        try:
            page = await browser.new_page(
                viewport={"width": 1366, "height": 768},
                device_scale_factor=1
            )

            await page.goto(URL, wait_until="load")

            # Capture actual screenshot
            await page.screenshot(
                path=str(ACTUAL),
                full_page=True
            )

        finally:
            await browser.close()

    print(f"Actual screenshot saved: {ACTUAL}")

    # Check baseline exists
    assert BASELINE.exists(), (
        "Baseline missing. Capture and approve a reference image first."
    )

    # Open baseline and actual screenshots
    with Image.open(BASELINE) as img1, Image.open(ACTUAL) as img2:

        baseline = img1.convert("RGB")
        actual = img2.convert("RGB")

        # Compare image dimensions
        if baseline.size != actual.size:
            pytest.fail(
                f"Image dimensions differ: "
                f"{baseline.size} vs {actual.size}"
            )

        # Compare screenshots
        diff = ImageChops.difference(baseline, actual)

        # Count changed pixels
        changed_pixels = sum(
            1 for pixel in diff.getdata()
            if pixel != (0, 0, 0)
        )

        # Calculate difference percentage
        total_pixels = baseline.width * baseline.height

        difference_ratio = changed_pixels / total_pixels

        # Save difference image
        diff.save(DIFF)

        print("\n========== VISUAL REGRESSION RESULTS ==========")
        print(f"Baseline size: {baseline.size}")
        print(f"Actual size: {actual.size}")
        print(f"Changed pixels: {changed_pixels}")
        print(f"Total pixels: {total_pixels}")
        print(f"Difference ratio: {difference_ratio:.4%}")
        print(f"Difference image: {DIFF}")
        print("================================================")

        # Validate threshold
        assert difference_ratio <= THRESHOLD, (
            f"Visual difference exceeds {THRESHOLD:.0%}: "
            f"{difference_ratio:.4%}"
        )
