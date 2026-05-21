BASE_URL = "https://the-internet.herokuapp.com"

class CheckboxesPage:
    URL = f"{BASE_URL}/checkboxes"

    def __init__(self, page):
        self.page  = page
        self.cb1   = page.locator("input[type='checkbox']").nth(0)
        self.cb2   = page.locator("input[type='checkbox']").nth(1)

    async def open(self):
        await self.page.goto(self.URL)

    async def check_first(self):
        await self.cb1.check()

    async def uncheck_second(self):
        await self.cb2.uncheck()
