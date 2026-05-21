import pytest
import allure

@pytest.mark.asyncio
@allure.title("Відкриття головної сторінки")
async def test_home_page(page):
    # Відкриття сторінки
    await page.goto("https://the-internet.herokuapp.com")
    
    # Крок 1: перевірка URL
    assert page.url == "https://the-internet.herokuapp.com/"
    
    # Крок 2: перевірка тексту заголовку (додано await)
    assert await page.locator("h1").text_content() == "Welcome to the-internet"
    
    # Крок 3: знімок екрана (додано await)
    await page.screenshot(path="screenshots/home.png")