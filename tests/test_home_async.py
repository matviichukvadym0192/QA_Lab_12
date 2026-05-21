import pytest
import allure

@pytest.mark.asyncio
@allure.title("Головна сторінка зі знімком у Allure")
async def test_home(page):
    await page.goto("https://the-internet.herokuapp.com")
    
    # Прикріплення знімку до Allure (Завдання 3)
    allure.attach(
        await page.screenshot(),
        name="home_page",
        attachment_type=allure.attachment_type.PNG
    )
    
    assert await page.title() == "The Internet"