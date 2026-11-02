
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright


async def capture_baseline():

    baseline = Path("C:/Users/RANJITHA/Desktop/playwright project/tests/node_modules/baseline.png")
    baseline.parent.mkdir(parents=True, exist_ok=True)

    async with async_playwright() as p:

        browser = await p.chromium.launch(headless=True)

        try:
            page = await browser.new_page(
                viewport={"width": 1366, "height": 768},
                device_scale_factor=1
            )

            await page.goto(
                "https://www.amazon.in/",
                wait_until="load"
            )

            await page.screenshot(
                path=str(baseline),
                full_page=True
            )

            print("Baseline screenshot captured successfully.")

        finally:
            await browser.close()


asyncio.run(capture_baseline())
