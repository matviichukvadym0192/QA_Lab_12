import pytest
import allure

@pytest.mark.asyncio
@allure.title("Робота з новими вкладками браузера")
async def test_new_window(page):
    await page.goto("https://the-internet.herokuapp.com/windows")

    # Використовуємо асинхронний контекстний менеджер async with
    async with page.context.expect_page() as page_event:
        await page.click("a[href='/windows/new']")

    # ДОДАНО AWAIT ТУТ:
    new_page = await page_event.value

    # Крок 2: перевірка URL та заголовку нової вкладки
    assert new_page.url == "https://the-internet.herokuapp.com/windows/new"
    assert "New Window" in await new_page.title()

    # Крок 1: закрити нову вкладку
    await new_page.close()

    # Крок 3: перевірити повернення до першої вкладки
    assert page.url == "https://the-internet.herokuapp.com/windows"