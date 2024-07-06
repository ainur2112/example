class LoginPageLocators:
    """ Элементы страницы авторизации """

    USERNAME_FIELD = ("xpath", "//input[@name='username']")
    PASSWORD_FIELD = ("xpath", "//input[@name='password']")
    SUBMIT_BUTTON = ("xpath", "//button[@type='submit']")
    INVALID_CREDS_TEXT = ("xpath", "//div[@role='alert']/div/p")