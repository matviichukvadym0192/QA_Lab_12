import pytest
import allure

@pytest.mark.asyncio
@allure.title("Перевірка роботи чекбоксів")
async def test_checkboxes(page):
    await page.goto("https://the-internet.herokuapp.com/checkboxes")
    
    checkbox1 = page.locator("input[type='checkbox']").nth(0)
    checkbox2 = page.locator("input[type='checkbox']").nth(1)
    
    # Крок 1: застосування .check() для першого чекбоксу
    await checkbox1.check()
    assert await checkbox1.is_checked()
    
    # Крок 2: .uncheck() для другого чекбоксу
    await checkbox2.uncheck()
    assert not await checkbox2.is_checked()
    
    # Крок 3: знімок екрана
    await page.screenshot(path="screenshots/checkboxes.png")