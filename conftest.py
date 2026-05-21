import os
import pytest
import allure
import pytest_asyncio
import asyncio
from playwright.async_api import async_playwright

# Крок 1. Хук для автоматичного скріншоту при падінні (адаптований під асинхронність)
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    
    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            # Оскільки хук синхронний, запускаємо асинхронний скріншот у поточному event loop
            try:
                loop = asyncio.get_event_loop()
                if loop.is_running():
                    # Створюємо задачу на скріншот
                    screenshot = loop.run_until_complete(page.screenshot())
                    allure.attach(
                        screenshot,
                        name="failure_screenshot",
                        attachment_type=allure.attachment_type.PNG
                    )
            except Exception as e:
                print(f"\n[Allure Screenshot Error] Не вдалося зробити знімок: {e}")

# Крок 2 та 3. Асинхронна фікстура з увімкненим Tracing
@pytest_asyncio.fixture
async def page(request):
    test_name = request.node.name
    # Переконуємося, що папка для трасування існує
    os.makedirs("traces", exist_ok=True)
    
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        context = await browser.new_context()
        
        # Увімкнення tracing
        await context.tracing.start(screenshots=True, snapshots=True)
        
        page = await context.new_page()
        
        yield page
        
        # Збереження trace після завершення тесту
        trace_path = f"traces/{test_name}.zip"
        await context.tracing.stop(path=trace_path)
        
        # Прикріплення trace.zip до Allure-звіту
        if os.path.exists(trace_path):
            with open(trace_path, "rb") as f:
                allure.attach(
                    f.read(),
                    name=f"trace_{test_name}",
                    attachment_type=allure.attachment_type.ZIP
                )
                
        await browser.close()