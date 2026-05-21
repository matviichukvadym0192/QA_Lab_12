import pytest
import allure
import os

@pytest.mark.asyncio
@allure.title("Знімки екрана після логіну та нової вкладки")
async def test_screenshot_tasks(page):
    # Створення папки screenshots заздалегідь
    os.makedirs("screenshots", exist_ok=True)

    # Крок 1: знімок після логіну
    await page.goto("https://the-internet.herokuapp.com/login")
    await page.fill("#username", "tomsmith")
    await page.fill("#password", "SuperSecretPassword!")
    await page.click("button[type='submit']")
    await page.screenshot(path="screenshots/login_after.png")

    # Крок 3: знімок нової вкладки
    await page.goto("https://the-internet.herokuapp.com/windows")
    async with page.context.expect_page() as page_event:
        await page.click("a[href='/windows/new']")

    # ДОДАНО AWAIT ТУТ:
    new_page = await page_event.value
    
    await new_page.screenshot(path="screenshots/new_window.png")
    await new_page.close()