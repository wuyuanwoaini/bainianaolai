"""
    以下为百年奥莱登录数据：
"""
from selenium.webdriver.common.by import By
# 点击 我
login_me=By.ID,"com.yunmall.lc:id/tab_me"
# 点击 已有账号去登录
login_name_ok_link=By.ID,"com.yunmall.lc:id/textView1"
# 输入用户名
login_username=By.ID,"com.yunmall.lc:id/logon_account_textview"
# 输入密码
login_password=By.ID,"com.yunmall.lc:id/logon_password_textview"
# 点击登录
login_btn=By.ID,"com.yunmall.lc:id/logon_button"
# 昵称
login_nickname=By.ID,"com.yunmall.lc:id/tv_user_nikename"
# 设置
login_setting=By.ID,"com.yunmall.lc:id/ymtitlebar_left_btn_image"
"""从消息推送-->滑到-->修改密码"""
# 修改密码
login_modify_pwd=By.ID,"com.yunmall.lc:id/setting_modify_pwd"
# 消息推送
login_msg_send=By.ID,"com.yunmall.lc:id/setting_notification"
# 退出按钮
login_logout=By.ID,"com.yunmall.lc:id/setting_logout"
# 确认退出
login_logout_ok=By.ID,"com.yunmall.lc:id/ymdialog_right_button"

"""
    以下为百年奥莱地址管理数据：
"""
# 地址管理
address_manage=By.ID,"com.yunmall.lc:id/setting_address_manage"
# 新增地址
address_add_new_btn=By.ID,"com.yunmall.lc:id/address_add_new_btn"
# 收件人
address_receipt_name=By.ID,"com.yunmall.lc:id/address_receipt_name"
# 手机号
address_add_phone=By.ID,"com.yunmall.lc:id/address_add_phone"
# 所在地区
address_province=By.ID,"com.yunmall.lc:id/address_province"
# 详细地址
address_detail_addr_info=By.ID,"com.yunmall.lc:id/address_detail_addr_info"
# 邮编
address_post_code=By.ID,"com.yunmall.lc:id/address_post_code"
# 设为默认地址
address_default=By.ID,"com.yunmall.lc:id/address_default"
# 收件人 电话
address_name_phone=By.ID,"com.yunmall.lc:id/receipt_name"
# 确认删除
address_delete_ok=By.ID,"com.yunmall.lc:id/ymdialog_left_button"