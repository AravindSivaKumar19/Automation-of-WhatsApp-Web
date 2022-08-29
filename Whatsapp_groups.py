
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time


select_type = int(input("Select type of MESSAGE\nEnter 1 to send group messages(Asking for roles)\n2 to send personal messages(Asking people to join/take up roles\checking with them)\n3 to send messages personally in 2 blocks(begging personally)\n4 to not send any message(checking what it'll open)\n to spam a sticker:"))
select_file = int(input("\nSelect Contacts\nEnter 1 to send messages in Groups\n2 to send messages Peronally to other members\n3 to send messages to club members\n4 to send messages to mentors\n5 to send messages to people who took roles\n6 to send messages to people who didn't\n7 to test how the message is being sent: "))

#save contacts/group names in a text file
if select_file==1:
    file_name='GroupNames.txt'
if select_file==2:
    file_name='PersonalMessages.txt'
if select_file==3:
    file_name='BroadcastingToClub.txt'
if select_file==4:
    file_name='Mentors.txt'
if select_file==5:
    file_name='Tookroles.txt'
if select_file==6:
    file_name='Deadpeople.txt'
if select_file==7:
    file_name='test.txt'
time.sleep(5)
opt=Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver=webdriver.Chrome(executable_path="path", chrome_options=opt)
driver.get("http://web.whatsapp.com")
time.sleep(10) 
chat_names=[]
with open(file_name) as f:
    chat_names = [line.rstrip('\n') for line in f]
name_to_greet=()
name_to_greet=tuple(chat_names)
no_of_groups_to_send=len(name_to_greet)

#sending in groups
if select_type==1:
    for i in range(no_of_groups_to_send):
        search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        search.send_keys(chat_names[i])
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        enter_message=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        message_to_send="Hello world"
        for part in message_to_send.split('\n'):
            enter_message.send_keys(part)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        time.sleep(5)
        enter_message.send_keys(Keys.ENTER)
        time.sleep(5)
        search.clear()

#sending personally
if select_type==2:
    for i in range(no_of_groups_to_send):
        search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        search.send_keys(chat_names[i])
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        enter_message=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        message="Hello world "+name_to_greet[i]+"How are you"
        message_to_send=message
        for part in message_to_send.split('\n'):
            enter_message.send_keys(part)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        time.sleep(5)
        enter_message.send_keys(Keys.ENTER)
        time.sleep(5)
        search.clear()

#sending personally 2 different messages at once
if select_type==3:
    for i in range(no_of_groups_to_send):
        search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        search.send_keys(chat_names[i])
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        enter_message=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]")
        #message1
        greeting_message="Hello world "+name_to_greet[i]+"Hello world"
        message_to_send=greeting_message
        for part in message_to_send.split('\n'):
            enter_message.send_keys(part)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        time.sleep(5)
        enter_message.send_keys(Keys.ENTER)
        #message2
        message_to_broadcast="Hello world 2"
        for part in message_to_broadcast.split('\n'):
            enter_message.send_keys(part)
            ActionChains(driver).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()
        time.sleep(5)
        enter_message.send_keys(Keys.ENTER)
        time.sleep(5)
        search.clear()

if select_type==4:
    for i in range(no_of_groups_to_send):
        search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        search.send_keys(chat_names[i])
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(5)
        search.clear()

#sending in groups
if select_type==5:
    for i in range(no_of_groups_to_send):
        search = driver.find_element_by_xpath("//*[@id='side']/div[1]/div/label/div/div[2]")
        search.send_keys(chat_names[i])
        time.sleep(5)
        search.send_keys(Keys.ENTER)
        time.sleep(3)
        select_emoji=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[2]/div/span")
        select_emoji.click()
        select_sticker=driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div/span[2]/div/div[1]/div[1]/button[4]/div/span")
        select_sticker.click()
        
        time.sleep(5)
        enter_message.send_keys(Keys.ENTER)
        time.sleep(5)
        search.clear()