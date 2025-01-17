class PersonalPageLocators:
    """Элементы со страниуы с персональными данными"""
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    MIDDLE_NAME_FIELD = ("xpath", "//input[@name='middleName']")
    LAST_NAME_FIELD = ("xpath", "//input[@name='lastName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")
    CONTACT_DETAILS = ("xpath", "//a[.='Contact Details']")
    ADD_BUTTON = ("xpath", "//button[text()=' Add ']")
    FILE_INPUT = ("xpath", "//input[@type='file']")
    CHECK_ADD_FILE_DIV = ("xpath", "//div[@class='oxd-file-input-div']")
    COMMENT_TEXTAREA = ("xpath", "//textarea[@placeholder='Type comment here']")
    FILE_SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[2]")
    SUCCESSFULLY_NOTIFICATION_VALUE = ("xpath", "//p[text()='Success']")
    DIV_WITH_SECRET_COMMENT = ("xpath", "//div[text()='SECRET_COMMENT']")
    DELETE_BUTTON = ("xpath", "//button/i[@class='oxd-icon bi-trash']")
    ACCEPT_DELETE_BUTTON = ("xpath", "//button[text()=' Yes, Delete ']")