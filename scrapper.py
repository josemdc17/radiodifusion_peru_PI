from playwright.sync_api import sync_playwright

def main(url):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto(url)

        # Replace these selectors with the actual ones for your dropdowns
        dropdown1_selector = "select#ContentPlaceHolder1_ddlDepa"
        dropdown2_selector = "select#ContentPlaceHolder1_ddlProvincia"
        dropdown3_selector = "select#ContentPlaceHolder1_ddlDistrito"

        # Replace these values with the options you want to select
        option1_value = "02"
        option2_value = "0208"
        option3_value = "020802"

        # Select options in each dropdown
        page.select_option(dropdown1_selector, value=option1_value)
        page.select_option(dropdown2_selector, value=option2_value)
        page.select_option(dropdown3_selector, value=option3_value)

        page.click("input#ContentPlaceHolder1_ibtnAceptar")

        page.wait_for_load_state("load", timeout=10000)

        span_value = page.evaluate(f'document.getElementById("ContentPlaceHolder1_lblAuto").textContent')

        print(span_value)

        browser.close()

if __name__ == "__main__":
    url = "https://rnf.mtc.gob.pe/"
    main(url)


