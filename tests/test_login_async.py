import pytest
import allure
from pages.login_page import LoginPage

@pytest.mark.asyncio
@allure.title("Успішний логін через POM")
async def test_login(page):
    login = LoginPage(page)
    
    with allure.step("Відкрити сторінку логіну"):
        await login.open()
        
    with allure.step("Ввести облікові дані"):
        await login.login("tomsmith", "SuperSecretPassword!")
        
    # Крок 1: Знімок після логіну
    with allure.step("Знімок після логіну"):
        allure.attach(
            await page.screenshot(),
            name="after_login",
            attachment_type=allure.attachment_type.PNG
        )
        
    with allure.step("Перевірити повідомлення про успіх"):
        message = await login.get_flash_message()
        assert "secure area" in message