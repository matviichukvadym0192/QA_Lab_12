import pytest
import allure

@pytest.mark.asyncio
@allure.title("Успішний логін")
async def test_successful_login(page):
    await page.goto("https://the-internet.herokuapp.com/login")
    await page.fill("#username", "tomsmith")
    await page.fill("#password", "SuperSecretPassword!")
    await page.click("button[type='submit']")
    
    message = await page.locator("#flash").text_content()
    # Перевірка успішного логіну
    assert "secure area" in message
    
    # Крок 3: знімок після логіну
    await page.screenshot(path="screenshots/login_success.png")

@pytest.mark.asyncio
@allure.title("Логін із хибним паролем")
async def test_failed_login(page):
    await page.goto("https://the-internet.herokuapp.com/login")
    
    # Крок 1: введення хибних даних
    await page.fill("#username", "tomsmith")
    await page.fill("#password", "WrongPassword!")
    await page.click("button[type='submit']")
    
    # Крок 2: перевірка тексту помилки
    message = await page.locator("#flash").text_content()
    assert "Your password is invalid!" in message
    
    # Крок 3: знімок після невдалого логіну
    await page.screenshot(path="screenshots/login_failed.png")