from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://thiagojuliani009-ops.github.io/html-css/")
    print(page.title())
    browser.close()

