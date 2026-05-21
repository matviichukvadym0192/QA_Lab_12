import pytest
import allure
from pages.alerts_page import AlertsPage

@pytest.mark.asyncio
@allure.title("Обробка JS Confirm через POM")
async def test_alert(page):
    alerts_page = AlertsPage(page)
    
    with allure.step("Відкрити сторінку алертів"):
        await alerts_page.open()
        
    async def handle_dialog(dialog):
        allure.attach(
            dialog.message,
            name="alert_text",
            attachment_type=allure.attachment_type.TEXT
        )
        await dialog.accept()
        
    with allure.step("Зареєструвати обробник діалогу"):
        page.on("dialog", handle_dialog)
        
    with allure.step("Натиснути кнопку JS Alert"):
        await page.click("button[onclick='jsAlert()']")
        
    with allure.step("Перевірити результат"):
        result = await alerts_page.get_result()
        # Виправлено очікуваний текст під кнопку jsAlert()
        assert result == "You successfully clicked an alert"