from playwright.sync_api import sync_playwright
import dataprep


def get_data_web(value_1, value_2, value_3):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://rnf.mtc.gob.pe/")

        # Replace these selectors with the actual ones for your dropdowns
        dropdown1_selector = "select#ContentPlaceHolder1_ddlDepa"
        dropdown2_selector = "select#ContentPlaceHolder1_ddlProvincia"
        dropdown3_selector = "select#ContentPlaceHolder1_ddlDistrito"

        # Replace these values with the options you want to select
        option1_value = value_1
        option2_value = value_2
        option3_value = value_3

        # Select options in each dropdown
        page.select_option(dropdown1_selector, value=option1_value)
        page.select_option(dropdown2_selector, value=option2_value)
        page.select_option(dropdown3_selector, value=option3_value)

        page.click("input#ContentPlaceHolder1_ibtnAceptar")

        page.wait_for_load_state("load", timeout=20000)

        span_departamento = page.evaluate(
            f'document.getElementById("ContentPlaceHolder1_rptUbigeo_lblDepa_0").textContent')

        span_provincia = page.evaluate(
            f'document.getElementById("ContentPlaceHolder1_rptUbigeo_lblProv_0").textContent')

        span_distrito = page.evaluate(
            f'document.getElementById("ContentPlaceHolder1_rptUbigeo_lblDis_0").textContent')

        span_canalizadas = page.evaluate(
            f'document.getElementById("ContentPlaceHolder1_lblCana").textContent')

        span_autorizadas = page.evaluate(
            f'document.getElementById("ContentPlaceHolder1_lblAuto").textContent')

        return f"Departamento: {span_departamento} \nProvincia: {span_provincia} \nDistrito: {span_distrito} \nCanalizadas: {span_canalizadas} \nAutorizadas: {span_autorizadas} \n\n"

        browser.close()


if __name__ == "__main__":
    get_data_web()
