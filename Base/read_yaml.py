import os
import yaml
class ReadYAML():
    def __init__(self,filename):
        # 动态组装文件路径及文件名
        self.file_path = os.getcwd() + os.sep + "Data" + os.sep + filename

    # 通过pytest命令执行时所有
    def read_yaml(self):
        with open(self.file_path,"r",encoding="utf-8") as f:
            return yaml.load(f)

    # 以下方法 作为右键运行调试所用
    def read_yaml01(self):
        with open("../Data/address_data.yaml","r",encoding="utf-8")as f:
            # yaml 的load方法进行读取
            return yaml.load(f)
"""
    期望结果值：[(),()]
    说明：
        values()获取字典内所有平级键名所对应的值；
"""
if __name__ == '__main__':

    # 自定义空列表
    arrs=[]
    # 获取出的结果为列表，列表内单个元素值为字典 datas.values()
    datas=ReadYAML("address_data.yaml").read_yaml01()
    # for data in datas.get("add_address").values():
    #     # arrs.append((data.get("name"),data.get("phone"),data.get("sheng"),data.get("shi"),data.get("qu"),data.get("addressinfo"),data.get("postcode")))
    #     print(data)
    # print(arrs)
    # [(李四，18611110000，河南。。。)]
    desc=datas.get("add_address")
    arrs.append((desc.get("name"),desc.get("phone"),desc.get("sheng"),desc.get("shi"),desc.get("qu"),desc.get("addressinfo"),desc.get("postcode")))
    print(arrs)