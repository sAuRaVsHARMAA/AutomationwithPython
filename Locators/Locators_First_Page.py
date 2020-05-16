class LocatorFirstPage:
    contact_us_xpath = "//div[@id='contact-link']//a[contains(text(),'Contact us')]"
    sign_in_xpath = "//a[@class='login']"
    cart_xpath = "//b[contains(text(),'Cart')]"
    search_box_id = "search_query_top"
    search_button_name = "submit_search"
    women_tab_xpath = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
    w_tops_xpath = "//a[@class='sf-with-ul'][contains(text(),'Tops')]"
    w_tshirt_xpath = "//ul[@class='submenu-container clearfix first-in-line-xs']//ul//li//a[contains(text(),'T-shirts')]"
    w_blouse_xpath = "//ul[@class='submenu-container clearfix first-in-line-xs']//ul//li//a[contains(text(),'Blouses')]"
    dress_xpath = "//*[@id='block_top_menu']/ul/li[2]/a"
    d_casual_xpath = "//*[@id='block_top_menu']/ul/li[2]/ul/li[1]/a"
    d_evening_xpath = "//*[@id='block_top_menu']/ul/li[2]/ul/li[2]/a"
    d_summer_xpath = "//*[@id='block_top_menu']/ul/li[2]/ul/li[3]/a"
    tshirt_xpath = "//ul[@class='sf-menu clearfix menu-content sf-js-enabled sf-arrows']/li/a[contains(text(),'T-shirts')]"
    sign_in_email_id = "email"
    sign_in_password_id = "passwd"
    sign_in_button_id = "SubmitLogin"
    women_list_xpath = [w_tshirt_xpath, w_tops_xpath, w_blouse_xpath]








