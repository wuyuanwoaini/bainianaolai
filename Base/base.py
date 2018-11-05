import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class Base():
    """
        __init__()说明：
            1. 在创建实例化的时候，此函数首先自动被执行
            2. 因为init首先会被执行，正在实例化Base类时，执行init函数，发现需要一个参数()

    """
    def __init__(self,driver):
        self.driver=driver
    # 查找元素方法 封装-->此方法给click、input等方法使用
    def base_find_element(self,loc,timeout=30,poll=0.5):
        """
            1. 封装查找元素的时候，记得使用 显示等待
            2. 使用driver.find_element(By.XPAHT,"....")
            3. 最后要通过return进行返回元素
        """
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))
    # 查找一组元素封装
    def base_find_elements(self,loc,timeout=30,poll=0.5):
        """
            1. 封装查找元素的时候，记得使用 显示等待
            2. 使用driver.find_element(By.XPAHT,"....")
            3. 最后要通过return进行返回元素
        """
        return WebDriverWait(self.driver,timeout,poll_frequency=poll).until(lambda x:x.find_elements(*loc))
    # 点击方法 封装
    def base_click(self,loc):
        self.base_find_element(loc).click()
    # 输入方法 封装
    def base_input(self,loc,text):
        """输入方法：要先清除操作"""
        el=self.base_find_element(loc)
        # 清除操作
        el.clear()
        # 输入元素内容
        el.send_keys(text)
    # 截图方法 封装
    def base_get_screenshot(self):
        # 组合图片保存路径及文件名：
        # 注意：调用的时候使用的是pytest，一定要路径问题 建议使用 os.getcwd（）
        img_path=os.getcwd()+os.sep+"Image"+os.sep+"faild.png"
        self.driver.get_screenshot_as_file(img_path)
    # 获取toast 封装
    def base_get_toast(self,message):
        msg=By.XPATH,"//*[contains(@text,'"+message+"')]"
        # 查找元素 方法 调用获取文本方法，并返回
        return self.base_find_element(msg,poll=0.1).text

    # 获取元素文本方法 封装
    def base_get_text(self,loc):
        """注意事项：必须以return返回"""
        return self.base_find_element(loc).text

    # 滑动方法封装 从一个元素滑到另一个元素
    def base_drag_and_drop(self,el1,el2):
        """
        :param el1: 起点元素
        :param el2: 落点元素
        """
        self.driver.drag_and_drop(el1,el2)

    # 封装传入文本，根据文本查找元素，然后在进行点击操作
    def base_xpath_text_click(self,text):
        # 组装 元祖
        loc=By.XPATH,"//*[contains(@text,'"+text+"')]"
        # 查找元素 并点击
        self.base_find_element(loc).click()

    # 封一个返回所有列表文本的方法
    def base_get_list_text(self,loc):
        return [i.text for i in self.base_find_elements(loc)]

    # 根据文本，返回包含此文本的所有元素
    def base_input_text_get_elements(self,text):
        loc = By.XPATH, "//*[contains(@text,'" + text + "')]"
        return self.base_find_elements(loc)

    # 传入列表 把列表内的个元素 进行点击操作
    def base_list_click(self,elements,num=0):
        # 获取当前元素的 文本
        text=elements[num].text
        # 对当前元素进行删除
        elements[num].click()
        # 把获取的文本返回  断言使用
        return text
