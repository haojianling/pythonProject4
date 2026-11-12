import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.baidu.com/")

    with page.expect_popup() as page1_info:
        page.get_by_role("link", name=" 在孩子们心中播撒真善美的种子").click()
    page1 = page1_info.value
    page1.locator("#content_left").get_by_role("link", name="把美的种子播撒在孩子心中").click()
    expect(page1.get_by_role("img").nth(5)).to_be_visible()
    expect(page1.locator("b")).to_contain_text("网页")
    expect(page1.locator("#chat-textarea")).to_have_value("把美的种子播撒在孩子心中");
    expect(page1.locator("#content_left")).to_match_aria_snapshot("- img \"头像\"\n- text:  新华社")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
