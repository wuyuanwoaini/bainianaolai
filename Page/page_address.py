import Page
from Base.base import Base
class PageAddress(Base):
    # 点击地址管理
    def page_address_manage(self):
        self.base_click(Page.address_manage)
    # 点击新增地址
    def page_address_add_new_btn(self):
        self.base_click(Page.address_add_new_btn)
    # 输入收件人
    def page_address_receipt_name(self,name):
        self.base_input(Page.address_receipt_name,name)
    # 输入手机号
    def page_address_add_phone(self,phone):
        self.base_input(Page.address_add_phone,phone)
    # 选择区域
    def page_address_province(self,sheng,shi,qu):
        # 点击选择区域
        self.base_click(Page.address_province)
        # 点击 省
        self.page_click_sheng(sheng)
        # 点击 市
        self.page_click_shi(shi)
        # 点击 区
        self.page_click_qu(qu)
    # 输入详细地址
    def page_address_detail_addr_info(self,addressinfo):
        self.base_input(Page.address_detail_addr_info,addressinfo)
    # 省
    def page_click_sheng(self,sheng):
        self.base_xpath_text_click(sheng)
    """
        注意：
            1. 省、市、区、保存、可以不在此地方封装，在执行脚本时直接调用
    """
    # 市
    def page_click_shi(self,shi):
        self.base_xpath_text_click(shi)
    # 区
    def page_click_qu(self,qu):
        self.base_xpath_text_click(qu)
    # 输入邮编
    def page_address_post_code(self,postcode):
        self.base_input(Page.address_post_code,postcode)
    # 点击默认地址
    def page_address_default(self):
        self.base_click(Page.address_default)
    # 点击保存
    def page_click_save(self):
        self.base_xpath_text_click("保存")
    # 返回所有 收件人 电话
    def page_get_list_text(self):
        return self.base_get_list_text(Page.address_name_phone)

    # 点击编辑
    def page_click_edit(self):
        self.base_xpath_text_click("编辑")
    # 点击修改
    def page_click_update(self):
        # 获取所有修改元素
        elements=self.base_input_text_get_elements("修改")
        # 点击所有元素中的第一个元素
        self.base_list_click(elements)

    # 删除地址方法
    def page_delete_address(self):
        # 获取地址列表长度
        name_list=self.page_get_list_text()
        # 遍历地址列表  要删除循环多少次
        for i in range(len(name_list)):
            # 点击编辑
            self.base_xpath_text_click("编辑")
            # 获取 包含 删除 文字的列表
            elements=self.base_input_text_get_elements("删除")
            # 获取地址列表第一个元素文本
            result_text=self.base_find_elements(Page.address_name_phone)[0].text
            # 调用封装的方法  根据列表 删除第一个元素
            self.base_list_click(elements)
            # 点击确认删除
            self.base_click(Page.address_delete_ok)
            # 断言 获取地址列表所有的 收件人 电话 有个大坑
            print("获取删除元素文本为：",result_text)
            # 如果能知道地址列表元素，那么就进行 单个元素断言操作
            if self.page_element_is_ok():
                try:
                    assert result_text not in self.page_get_list_text()
                except:
                    print(result_text,"地址列表删除失败！")
                    raise

    # 封装方法 判断元素是否存在
    def page_element_is_ok(self):
        try:
            self.base_find_elements(Page.address_name_phone,timeout=3)
            return True
        except:
            return False

    # 判断是否删除干净
    def page_is_delete_ok(self):
        # 找不到列表地址为False
        if self.page_element_is_ok()==False:
            # 删除干净 返回True
            return True
        else:
            # 未删除干净
            return False