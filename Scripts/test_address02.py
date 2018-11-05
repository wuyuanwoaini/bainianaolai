import sys,os
sys.path.append(os.getcwd())
import pytest
import allure
from Base.read_yaml import ReadYAML
from Page.page_in import PageIn

def get_data(type_data):
    # 自定义空列表
    arrs=[]
    if type_data=="add":
        # 获取出的结果为列表，列表内单个元素值为字典
        desc=ReadYAML("address_data.yaml").read_yaml().get("add_address")
        arrs.append((desc.get("name"),desc.get("phone"),desc.get("sheng"),desc.get("shi"),desc.get("qu"),desc.get("addressinfo"),desc.get("postcode")))
        return arrs
    elif type_data=="update":
        desc=ReadYAML("address_data.yaml").read_yaml().get("update_address")
        arrs.append((desc.get("name"),desc.get("phone"),desc.get("sheng"),desc.get("shi"),desc.get("qu"),desc.get("addressinfo"),desc.get("postcode")))
        return arrs
		
class TestAdress():
    # setup
    def setup_class(self):
        # 实例化统一入口类
        self.page=PageIn()
        # 调用 封装的page_login登录方法
        self.page.page_get_login().page_login_address()
        # 实例化 地址管理页面
        self.address=self.page.page_get_address()
        # 点击地址管理
        self.address.page_address_manage()
    # teardown
    def teardown_class(self):
        self.page.driver.quit()
    # test_new_address
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,addressinfo,postcode",get_data("add"))
    def test_new_address(self,name,phone,sheng,shi,qu,addressinfo,postcode):
        # 点击新增地址
        self.address.page_address_add_new_btn()
        # 输入收件人
        self.address.page_address_receipt_name(name)
        # 输入手机号
        self.address.page_address_add_phone(phone)
        # 点击选择区域
        self.address.page_address_province(sheng,shi,qu)
        # 输入详细地址
        self.address.page_address_detail_addr_info(addressinfo)
        # 输入邮编
        self.address.page_address_post_code(postcode)
        # 点击默认
        self.address.page_address_default()
        # 点击保存
        self.address.page_click_save()
        # 断言
        try:
            # 组装字符串 格式："张三  18610000000"
            name_phone=name+"  "+phone
            print("组装后的字符串格式：",name_phone)
            # 获取所有收件人 电话
            text_list=self.address.page_get_list_text()
            print("所有收件人电话为：",text_list)
            assert name_phone in text_list
        except:
            # 截图
            self.address.base_get_screenshot()
            # 失败图片写入报告
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败原因请查看附加图：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("name,phone,sheng,shi,qu,addressinfo,postcode",get_data("update"))
    def test_update_address(self,name,phone,sheng,shi,qu,addressinfo,postcode):
        # 点击编辑
        self.address.page_click_edit()
        # 点击修改
        self.address.page_click_update()
        # 输入收件人
        self.address.page_address_receipt_name(name)
        # 输入手机号
        self.address.page_address_add_phone(phone)
        # 点击选择区域
        self.address.page_address_province(sheng,shi,qu)
        # 输入详细地址
        self.address.page_address_detail_addr_info(addressinfo)
        # 输入邮编
        self.address.page_address_post_code(postcode)
        # 保存
        self.address.page_click_save()
        # 断言
        try:
            # 组装字符串 格式："张三  18610000000"
            name_phone=name+"  "+phone
            # 获取所有收件人 电话
            assert name_phone in self.address.page_get_list_text()
        except:
            # 截图
            self.address.base_get_screenshot()
            # 失败图片写入报告
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败原因请查看附加图：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise

    @pytest.mark.run(order=3)
    def test_delete_address(self):
        # 调用删除方法
        self.address.page_delete_address()
        try:
            # 断言 列表地址是否删除干净
            assert self.address.page_is_delete_ok()
        except:

            # 截图
            self.address.base_get_screenshot()
            # 失败图片写入报告
            with open("./Image/faild.png", "rb") as f:
                allure.attach("失败原因请查看附加图：", f.read(), allure.attach_type.PNG)
            # 抛异常
            raise
