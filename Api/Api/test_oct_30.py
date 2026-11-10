
from pathlib import Path
from PIL import Image, ImageChops
import pytest
from playwright.async_api import async_playwright


# Screenshot paths
SCREENSHOT_DIR = Path(__file__).parent / "screenshots"

BASELINE = SCREENSHOT_DIR / "baseline.png"
ACTUAL = SCREENSHOT_DIR / "actual.png"
DIFF = SCREENSHOT_DIR / "diff.png"


@pytest.mark.asyncio
async def test_visual_regression():

    # Create screenshots folder
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        context = await browser.new_context(
            viewport={"width": 1366, "height": 768},
            device_scale_factor=1,
            ignore_https_errors=True
        )

        page = await context.new_page()

        # Open website
        response = await page.goto(
            "https://parabank.parasoft.com/parabank/index.htm",
            wait_until="domcontentloaded",
            timeout=60000
        )

        print("Page title:", await page.title())
        print("Response status:", response.status if response else None)

        # Check website response
        assert response is not None and response.ok, (
            f"Website failed to load. Status: "
            f"{response.status if response else 'No response'}"
        )

        # Capture screenshot
        if not BASELINE.exists():

            await page.screenshot(
                path=str(BASELINE),
                full_page=True
            )

            print("Baseline screenshot created successfully!")

            await browser.close()
            return

        else:

            await page.screenshot(
                path=str(ACTUAL),
                full_page=True
            )

            print("Actual screenshot captured successfully!")

        await browser.close()

    # Compare baseline and actual screenshots
    with Image.open(BASELINE) as img1, Image.open(ACTUAL) as img2:

        baseline = img1.convert("RGB")
        actual = img2.convert("RGB")

        # Check image dimensions
        if baseline.size != actual.size:

            pytest.fail(
                f"Image dimensions differ: "
                f"{baseline.size} vs {actual.size}"
            )

        # Calculate image differences
        diff = ImageChops.difference(
            baseline,
            actual
        )

        changed_pixels = sum(
            1 for pixel in diff.getdata()
            if pixel != (0, 0, 0)
        )

        total_pixels = baseline.width * baseline.height

        difference_ratio = changed_pixels / total_pixels

        # Save difference image
        diff.save(DIFF)

        print("Changed pixels:", changed_pixels)

        print(
            f"Difference ratio: {difference_ratio:.4%}"
        )

        print("Difference image saved:", DIFF)

        # Allow maximum 1% difference
        assert difference_ratio <= 0.01, (
            f"Visual difference exceeds 1%: "
            f"{difference_ratio:.4%}"
        )

        print("Visual regression test passed!")


