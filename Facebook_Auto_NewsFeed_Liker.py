from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

id = '__facebook-email-OR-username__'
passd = '__facebook-password__'
url = 'http://facebook.com'
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get(url)
driver.maximize_window()

assert "Facebook" in driver.title
username = driver.find_element_by_id('email')
password = driver.find_element_by_id('pass')

username.send_keys(id)
password.send_keys(passd)
password.send_keys(Keys.ENTER)

time.sleep(5)


#elem = driver.find_element_by_class_name('_khz')
for i in range(0,5):
    elem = driver.execute_script("""function sleep(milliseconds) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
}
var elems = document.getElementsByClassName('UFILikeLink _4x9- _4x9_ _48-k');
for(var i= 0;i<elems.length;i++)
{elems[i].click(); sleep(5000);}
""")
    time.sleep(4)

assert "Not found" not in driver.page_source


