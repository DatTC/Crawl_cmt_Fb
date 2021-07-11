from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# open browser and go to the post 
browser = webdriver.Chrome(executable_path="./chromedriver.exe")
browser.get("https://www.facebook.com/truongnguoita.vn/posts/1419482211780851")
sleep(5)

show_cmt = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div[4]/a")
show_cmt.click()
sleep(5)

# click btn '1.4K binh luan'
show_cmt = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[2]/div[1]/div/div[3]/span[1]/a")
show_cmt.click()
sleep(3)

# click btn 'xem them binh luan'
show_more_cmt = browser.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/form/div/div[3]/div[2]/div/a")
show_more_cmt.click()
sleep(3)

cmt_list = browser.find_elements_by_xpath("//div[@aria-label='Bình luận']")

# display acc and content of comment
for i in range(3):
# for i in range(len(cmt_list)):
    # if(cmt_list[i].find_element_by_class_name("_2txe")):
    #     continue
    user_cmt = cmt_list[i].find_element_by_class_name("_6qw4")
    content_cmt = cmt_list[i].find_element_by_class_name("_3l3x")
    print("* ", user_cmt.text,": ", content_cmt.text)
    print("type1: ",type(user_cmt))
    print("type2: ",type(content_cmt))
    print('y') if isinstance(user_cmt, WebElement) else print('n')

sleep(3)
browser.close()


# <class 'selenium.webdriver.remote.webelement.WebElement'>