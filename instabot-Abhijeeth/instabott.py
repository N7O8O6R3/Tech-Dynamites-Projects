from selenium import webdriver
from time import sleep

class instabott:
    def __init__(self,username,pw):
        self.driver = webdriver.Chrome()
        self.username=username
        self.driver.get("https://www.instagram.com/")
       # self.driver.find_element_by_xpath("//*[@id="react-root"]/section/main/article/div[2]/div/div/div[3]/span/button")
        # self.driver.find_element_by_xpath("//a[contains(text(),'Switch accounts')]")\
        # .click()
        # sleep(2)
        # self.driver.find_element_by_xpath("//a[contains(text(),'Log in')]")\
        # .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
        .send_keys(username)
        # //sleep(3)
        # //self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
        #// .send_keys(username)
        # self.driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')\
        # .send_keys(username)
        #self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')\
        #.send_keys(pw)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")\
        .send_keys(pw)

        
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")\
        .click()
        sleep(4)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
        .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")\
        .click()
        sleep(2)
    def followers(self):
        #("//a[contains(@href,'/{}')]".format('ameeshsai'))
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")\
        .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div")\
        .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")\
        .click()
        sleep(2)
        followers=self._getname()
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")\
        .click()
        following=self._getnames()

        not_following = [user for user in following if user not in followers]
        print("These are the people you are following but they are not following you !!!!!!!!!!!!!!!!")
        for i in range(0, len(not_following)):
             print(not_following[i])
             print('\n')

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[1]/a/div/div/img')\
        .click()
    def _getname(self):
        #sugs= self.driver.find_element_by_xpath('//h4[contain(text(), Suggestions)]')
        #self.driver.execute_script('arguments[0].scrollIntoView()')
        sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        # self.driver.execute_script("""scroll_box.scrollIntoView();""")
        Last_ht,ht=0,1
        while Last_ht!= ht:
            Last_ht=ht
            sleep(2)
            ht= self.driver.execute_script(""" 
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """, scroll_box)

        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # for i in range(0, len(names)):
        #     print(names[i])
        #     print('\n')

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
        .click()
        return names;

        #####################################################################

        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')\
        .click()
    def _getnames(self):
        #sugs= self.driver.find_element_by_xpath('//h4[contain(text(), Suggestions)]')
        #self.driver.execute_script('arguments[0].scrollIntoView()')
        sleep(2)
        scroll_box1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        # self.driver.execute_script("""scroll_box.scrollIntoView();""")
        Last_ht1,ht1=0,1
        while Last_ht1!= ht1:
            Last_ht1=ht1
            sleep(2)
            ht1= self.driver.execute_script(""" 
            arguments[0].scrollTo(0,arguments[0].scrollHeight);
            console.log(arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            
            """, scroll_box1)

        links = scroll_box1.find_elements_by_tag_name('a')
        names1 = [name.text for name in links if name.text != '']
#        for i in range(0, len(names1)):
#            print(names1[i])
#            print('\n')

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
        .click()
        return names1;



   # def unfollowers(self):
        

    def logout(self):
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")\
        .click()
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div")\
        .click()
        sleep(15)

    def viewpost(self):
        sleep(3)
        # self.driver.execute_script('arguments[0].scrollIntoView')
        # sleep(3)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[1]/section/main")
        Last_ht,ht=0,1
        while Last_ht!=1:
            Last_ht=ht
            # ht = self.driver.execute_script(""" 
            # arguments[0].scrollTo(0,arguments[0].scrollHeight);
            # return arguments[0].scrollHeight;
            # """, scroll_box)
            # ht = self.driver.execute_script("""window.scrollTo(0,document.body.scrollHeight);
            # return document.body.scrollHeight;""",scroll_box)
            
            ht= self.driver.execute_script("""
            window.scrollBy(0,1);
            console.log(arguments[0].scrollHeight);
            return arguments[0].scrollHeight;
            """,scroll_box)
            Last_ht=0
            # self.driver.execute_script("""JavascriptExecutor jse = (JavascriptExecutor)driver;
            # jse.executeScript("scroll(0, 500);");""")

username = input('username')
passw=input('passw')

instabot=instabott(username,passw)
sleep(3)
# instabot.followers()

instabot.viewpost()


instabot.logout()
# abhi=input("username")
# cap=input("pass")  
#instabot.logout()

# instabott(abhi,cap)

