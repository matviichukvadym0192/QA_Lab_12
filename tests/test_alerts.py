import pytest
import allure

@pytest.mark.asyncio
@allure.title("Обробка JavaScript Alerts")
async def test_alert(page):
    await page.goto("https://the-internet.herokuapp.com/javascript_alerts")
    alert_text = []
    
    # Крок 1: реєстрація асинхронного обробника події діалогу
    async def handle_dialog(dialog):
        alert_text.append(dialog.message)
        await dialog.dismiss()  # Скасовує діалог (натискає Cancel)
        
    page.on("dialog", handle_dialog)
    await page.click("button[onclick='jsConfirm()']")
    
    # Крок 2: перевірка тексту алерту
    assert alert_text[0] == "I am a JS Confirm"
    
    # Крок 3: перевірка результату після закриття
    assert await page.locator("#result").text_content() == "You clicked: Cancel"