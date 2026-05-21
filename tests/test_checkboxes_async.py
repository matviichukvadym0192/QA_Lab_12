import pytest
import allure
from pages.checkboxes_page import CheckboxesPage

@pytest.mark.asyncio
@allure.title("Перевірка чекбоксів через POM")
async def test_checkboxes(page):
    cb_page = CheckboxesPage(page)
    
    with allure.step("Відкрити сторінку чекбоксів"):
        await cb_page.open()
        
    with allure.step("Відмітити перший чекбокс"):
        await cb_page.check_first()
        
    with allure.step("Зняти відмітку з другого чекбоксу"):
        await cb_page.uncheck_second()
        
    # Крок 3: Знімок чекбоксів
    with allure.step("Знімок чекбоксів"):
        allure.attach(
            await page.screenshot(),
            name="checkboxes",
            attachment_type=allure.attachment_type.PNG
        )