from seleniumbase import Driver
from seleniumbase import SB

#keeping web browser open
# driver = Driver(uc=True)
# url = 'https://csgo-skins.com/'
# driver.



with SB(uc=True, test=True, locale="en") as sb:
    url = "https://csgo-skins.com/"
    sb.activate_cdp_mode(url)
    sb.uc_gui_click_captcha()
    sb.sleep(60)



