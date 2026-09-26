from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user.name@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path="../../browser-state.json")

    context_new = browser.new_context(storage_state="browser-state.json")
    contexted_page = context_new.new_page()

    contexted_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    courses_header = contexted_page.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_header).to_be_visible()
    expect(courses_header).to_have_text("Courses")

    courses_icon = contexted_page.get_by_test_id("courses-list-empty-view-icon")
    expect(courses_icon).to_be_visible()

    courses_text = contexted_page.get_by_test_id("courses-list-empty-view-title-text")
    expected_text = "There is no results"
    expect(courses_text).to_be_visible()
    expect(courses_text).to_have_text(expected_text)

    courses_subtext = contexted_page.get_by_test_id("courses-list-empty-view-description-text")
    expected_subtext = "Results from the load test pipeline will be displayed here"
    expect(courses_subtext).to_be_visible()
    expect(courses_subtext).to_have_text(expected_subtext)
