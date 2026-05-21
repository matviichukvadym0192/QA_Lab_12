BASE_URL = "https://the-internet.herokuapp.com"

class LoginPage:
    URL = f"{BASE_URL}/login"

    def __init__(self, page):
        self.page = page
        self.username  = page.locator("#username")
        self.password  = page.locator("#password")
        self.login_btn = page.locator("button[type='submit']")
        self.flash_msg = page.locator("#flash")

    async def open(self):
        await self.page.goto(self.URL)

    async def login(self, user, pwd):
        await self.username.fill(user)
        await self.password.fill(pwd)
        await self.login_btn.click()

    async def get_flash_message(self):
        return await self.flash_msg.text_content()
