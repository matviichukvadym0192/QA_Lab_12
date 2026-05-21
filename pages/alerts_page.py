BASE_URL = "https://the-internet.herokuapp.com"

class AlertsPage:
    URL = f"{BASE_URL}/javascript_alerts"

    def __init__(self, page):
        self.page       = page
        self.result_msg = page.locator("#result")

    async def open(self):
        await self.page.goto(self.URL)

    async def get_result(self):
        return await self.result_msg.text_content()
