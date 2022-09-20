import requests
import json
import datetime
import pandas as pd

class Baidu_spider(object):
    def __init__(self,keyword, start_date, end_date, area):
        self.keyword=keyword
        self. start_date= start_date
        self.end_date=end_date
        self.area=self.area_num(area)
        city, county = area.split(',')
        self.area_name_city=city
        self.area_name_county=county
    def area_num(self,area):
        BaiduIndexCitiesCode = {
            '北京市': 911, '天津市': 923,
            '石家庄市': 141, '唐山市': 261, '秦皇岛市': 146, '邯郸市': 292, '邢台市': 293, '保定市': 259, '张家口市': 144, '承德市': 145,
            '沧州市': 148, '廊坊市': 147, '衡水市': 143,
            '太原市': 231, '大同市': 227, '阳泉市': 236, '长治市': 228, '晋城市': 234, '朔州市': 235, '晋中市': 230, '运城市': 233, '忻州市': 229,
            '临汾市': 232, '吕梁市': 237,
            '呼和浩特市': 20, '包头市': 13, '乌海市': 16, '赤峰市': 21, '通辽市': 22, '鄂尔多斯市': 14, '呼伦贝尔市': 25, '巴彦淖尔市': 15,
            '乌兰察布市': 331, '兴安盟': 333, '锡林郭勒盟': 19, '阿拉善盟': 17,
            '沈阳市': 150, '大连市': 29, '鞍山市': 215, '抚顺市': 222, '本溪市': 220, '丹东市': 219, '锦州市': 217, '营口市': 221, '阜新市': 223,
            '辽阳市': 224, '盘锦市': 151, '铁岭市': 218, '朝阳市': 216, '葫芦岛市': 225,
            '长春市': 154, '吉林市': 270, '四平市': 155, '辽源市': 191, '通化市': 407, '白山市': 408, '松原市': 194, '白城市': 410,
            '延边朝鲜族自治州': 525,
            '哈尔滨市': 152, '齐齐哈尔市': 319, '鸡西市': 323, '鹤岗市': 301, '双鸭山市': 359, '大庆市': 153, '伊春市': 295, '佳木斯市': 320,
            '七台河市': 302, '牡丹江市': 322, '黑河市': 300, '绥化市': 324, '大兴安岭地区': 297,
            '上海市': 910,
            '南京市': 125, '无锡市': 127, '徐州市': 161, '常州市': 162, '苏州市': 126, '南通市': 163, '连云港市': 156, '淮安市': 157, '盐城市': 160,
            '扬州市': 158, '镇江市': 169, '泰州市': 159, '宿迁市': 172,
            '杭州市': 138, '宁波市': 289, '温州市': 149, '嘉兴市': 304, '湖州市': 305, '绍兴市': 303, '金华市': 135, '衢州市': 288, '舟山市': 306,
            '台州市': 287, '丽水市': 134,
            '合肥市': 189, '芜湖市': 188, '蚌埠市': 187, '淮南市': 178, '马鞍山市': 185, '淮北市': 183, '铜陵市': 173, '安庆市': 186, '黄山市': 174,
            '滁州市': 182, '阜阳市': 184, '宿州市': 179, '六安市': 181, '亳州市': 391, '池州市': 175, '宣城市': 176,
            '福州市': 50, '厦门市': 54, '莆田市': 51, '三明市': 52, '泉州市': 55, '漳州市': 56, '南平市': 253, '龙岩市': 53, '宁德市': 87,
            '南昌市': 5, '景德镇市': 137, '萍乡市': 136, '九江市': 6, '新余市': 246, '鹰潭市': 7, '赣州市': 10, '吉安市': 115, '宜春市': 256,
            '抚州市': 8, '上饶市': 9,
            '济南市': 1, '青岛市': 77, '淄博市': 81, '枣庄市': 85, '东营市': 82, '烟台市': 78, '潍坊市': 80, '济宁市': 352, '泰安市': 353,
            '威海市': 88, '日照市': 366, '临沂市': 79, '德州市': 86, '聊城市': 83, '滨州市': 76, '菏泽市': 84,
            '郑州市': 168, '开封市': 264, '洛阳市': 378, '平顶山市': 266, '安阳市': 370, '鹤壁市': 374, '新乡市': 263, '焦作市': 265, '濮阳市': 380,
            '许昌市': 268, '漯河市': 379, '三门峡市': 381, '南阳市': 262, '商丘市': 376, '信阳市': 373, '周口市': 375, '驻马店市': 371,
            '济源市': 667,
            '武汉市': 28, '黄石市': 30, '十堰市': 36, '宜昌市': 35, '襄阳市': 32, '鄂州市': 39, '荆门市': 34, '孝感市': 41, '荆州市': 31,
            '黄冈市': 33, '咸宁市': 40, '随州市': 37, '恩施土家族苗族自治州': 38, '仙桃市': 42, '潜江市': 74, '天门市': 73, '神农架林区': 687,
            '长沙市': 43, '株洲市': 46, '湘潭市': 47, '衡阳市': 45, '邵阳市': 405, '岳阳市': 44, '常德市': 68, '张家界市': 226, '益阳市': 48,
            '郴州市': 49, '永州市': 269, '怀化市': 67, '娄底市': 66, '湘西土家族苗族自治州': 65,
            '广州市': 95, '韶关市': 201, '深圳市': 94, '珠海市': 200, '汕头市': 212, '佛山市': 196, '江门市': 198, '湛江市': 197, '茂名市': 203,
            '肇庆市': 209, '惠州市': 199, '梅州市': 211, '汕尾市': 213, '河源市': 210, '阳江市': 202, '清远市': 208, '东莞市': 133, '中山市': 207,
            '潮州市': 204, '揭阳市': 205, '云浮市': 195,
            '南宁市': 90, '柳州市': 89, '桂林市': 91, '梧州市': 132, '北海市': 128, '防城港市': 130, '钦州市': 129, '贵港市': 93, '玉林市': 118,
            '百色市': 131, '贺州市': 92, '河池市': 119, '来宾市': 506, '崇左市': 665,
            '海口市': 239, '三亚市': 243, '三沙市': 460300, '儋州市': 244, '五指山市': 582, '琼海市': 242, '文昌市': 670, '万宁市': 241,
            '东方市': 456, '定安县': 681, '屯昌县': 684, '澄迈县': 675, '临高县': 680, '白沙黎族自治县': 689, '昌江黎族自治县': 683, '乐东黎族自治县': 679,
            '陵水黎族自治县': 674, '保亭黎族苗族自治县': 686, '琼中黎族苗族自治县': 690,
            '重庆市': 904,
            '成都市': 97, '自贡市': 111, '攀枝花市': 112, '泸州市': 103, '德阳市': 106, '绵阳市': 98, '广元市': 99, '遂宁市': 100, '内江市': 102,
            '乐山市': 107, '南充市': 104, '眉山市': 291, '宜宾市': 96, '广安市': 108, '达州市': 113, '雅安市': 114, '巴中市': 101, '资阳市': 109,
            '阿坝藏族羌族自治州': 457, '甘孜藏族自治州': 417, '凉山彝族自治州': 479,
            '贵阳市': 2, '六盘水市': 4, '遵义市': 59, '安顺市': 424, '毕节市': 426, '铜仁市': 422, '黔西南布依族苗族自治州': 588, '黔东南苗族侗族自治州': 61,
            '黔南布依族苗族自治州': 3,
            '昆明市': 117, '曲靖市': 339, '玉溪市': 123, '保山市': 438, '昭通市': 335, '丽江市': 342, '普洱市': 666, '临沧市': 350,
            '楚雄彝族自治州': 124, '红河哈尼族彝族自治州': 337, '文山壮族苗族自治州': 437, '西双版纳傣族自治州': 668, '大理白族自治州': 334, '德宏傣族景颇族自治州': 669,
            '怒江傈僳族自治州': 671, '迪庆藏族自治州': 672,
            '拉萨市': 466, '日喀则市': 516, '昌都市': 678, '林芝市': 656, '山南市': 677, '那曲市': 655, '阿里地区': 691,
            '西安市': 165, '铜川市': 271, '宝鸡市': 273, '咸阳市': 277, '渭南市': 275, '延安市': 401, '汉中市': 276, '榆林市': 278, '安康市': 272,
            '商洛市': 274,
            '兰州市': 166, '嘉峪关市': 286, '金昌市': 343, '白银市': 309, '天水市': 308, '武威市': 283, '张掖市': 285, '平凉市': 307, '酒泉市': 284,
            '庆阳市': 281, '定西市': 282, '陇南市': 344, '临夏回族自治州': 346, '甘南藏族自治州': 673,
            '西宁市': 139, '海东市': 652, '海北藏族自治州': 682, '黄南藏族自治州': 685, '海南藏族自治州': 676, '果洛藏族自治州': 688, '玉树藏族自治州': 659,
            '海西蒙古族藏族自治州': 608,
            '银川市': 140, '石嘴山市': 472, '吴忠市': 395, '固原市': 396, '中卫市': 480,
            '乌鲁木齐市': 467, '克拉玛依市': 317, '吐鲁番市': 310, '哈密市': 312, '昌吉回族自治州': 311, '博尔塔拉蒙古自治州': 318, '巴音郭楞蒙古自治州': 499,
            '阿克苏地区': 315, '克孜勒苏柯尔克孜自治州': 653, '喀什地区': 384, '和田地区': 386, '伊犁哈萨克自治州': 520, '塔城地区': 563, '阿勒泰地区': 383,
            '石河子市': 280, '阿拉尔市': 692, '图木舒克市': 693, '五家渠市': 661,
            '香港特别行政区': 933, '澳门特别行政区': 934
        }
        BaiduIndexProvinceCode = {
            '全国': 0,
            '北京市': 911, '天津市': 923, '河北省': 920, '山西省': 929, '内蒙古自治区': 905,
            '辽宁省': 907, '吉林省': 922, '黑龙江省': 921,
            '上海市': 910, '江苏省': 916, '浙江省': 917, '安徽省': 928, '福建省': 909, '江西省': 903, '山东省': 901,
            '河南省': 927, '湖北省': 906, '湖南省': 908, '广东省': 913, '广西自治区': 912, '海南省': 930,
            '重庆市': 904, '四川省': 914, '贵州省': 902, '云南省': 915, '西藏自治区': 932,
            '陕西省': 924, '甘肃省': 925, '青海省': 918, '宁夏自治区': 919, '新疆自治区': 926,
            '台湾省': 931, '香港特别行政区': 933, '澳门特别行政区': 934
        }
        city,county=area.split(',')
        try:
            return BaiduIndexCitiesCode[county]#返回城市编码
        except:
            print('请输入正确的城市')#如果报错可以看下BaiduIndexCitiesCode里面城市是不是有
            return None
    def get_html(self,url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36",
            "Host": "index.baidu.com",
            "Referer": "http://index.baidu.com/v2/main/index.html",
            "Cipher-Text": "1652425237825_1652501356206_VBpwl9UG8Dvs2fAi91KToRTSAP7sDsQU5phHL97raPDFJdYz3fHf9hBAQrGGCs+qJoP7yb44Uvf91F7vqJLVL0tKnIWE+W3jXAI30xx340rhcwUDQZ162FPAe0a1jsCluJRmMLZtiIplubGMW/QoE/0Pw+2caH39Ok8IsudE4wGLBUdYg1/bKl4MGwLrJZ7H6wbhR0vT5X0OdCX4bMJE7vcwRCSGquRjam03pWDGZ51X15fOlO0qMZ2kqa3BmxwNlfEZ81l3L9nZdrc3/Tl4+mNpaLM7vA5WNEQhTBoDVZs6GBRcJc/FSjd6e4aFGAiCp1Y8MD66chTiykjIN51s7gbJ44JfVS0NjBnsvuF55bs="
        }
        cookies = {
            'Cookie': 'BAIDUID=FB56826BD8B5D3A81D4C54B566F45BBC:FG=1; PSTM=1657062427; BIDUPSID=B459447D48BA0461AD1625C07EA41283; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BA_HECTOR=a4240h85a42ka10ha12h518e1hdsui717; ZFY=PFf1fOjTmmAkIHkdWdWr:A04gTXYrHOzziyO6w:BICA7M:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=2; H_PS_PSSID=36556_36461_36255_36824_36414_36949_36167_36816_36745_26350_36863; BCLID=10307383323193515656; BDSFRCVID=-ltOJexroG0leprDYNm-brdQZcpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKKymOTHrAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tR30WJbHMTrDHJTg5DTjhPrMqfvJWMT-MTryKKJs54JKsMT8hDcDK40uWxbjLbvkJGnRh4oNBUJtjJjYhfO45DuZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPU2fc9LUvH0mcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DDmjj-23e; BCLID_BFESS=10307383323193515656; BDSFRCVID_BFESS=-ltOJexroG0leprDYNm-brdQZcpWxY5TDYrELPfiaimDVu-VJeC6EG0Pts1-dEu-EHtdogKKymOTHrAF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tR30WJbHMTrDHJTg5DTjhPrMqfvJWMT-MTryKKJs54JKsMT8hDcDK40uWxbjLbvkJGnRh4oNBUJtjJjYhfO45DuZyxomtfQxtNRJQKDE5p5hKq5S5-OobUPU2fc9LUvH0mcdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLK-oj-DDmjj-23e; Hm_lvt_d101ea4d2a5c67dab98251f0b5de24dc=1658402725,1658617215,1658713928,1658794881; BDUSS=RMY2tMZHp1ZmpsZWFnVjF4LWdMSkY1b3J4Mkl3LTZjNnVheWU4bVItaFUyUVpqRUFBQUFBJCQAAAAAAQAAAAEAAAC10QUnU0RVc3R1ZGVudDEyMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFRM32JUTN9iLW; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04088136899PVcqe54jeqlSz5CxhXGMwhYf9EtBTtWMgqj7IqFWRd0egyfy2WsbSGkjoWWAv5svkmIneETmtNk/F+nzvvFnttSFNWLlNixgcX9B2oMhYKV3PRT5jeeYyqWkTRQviBUMKjlo//hUPIW86BG1XK/cEW/KCQ2CM6q1TQf3BmyneYkOzDc0vxuqVyD7M1scN8+4ulJGrKTSfKSbUU7hnYqyaBwRtWh8x/RTyZSEDIRSiybzl6mlcXz4oIaUEOj4BsjsFPbqsED5wGjEwBv0Ur4nkealZ79EqLwV9460kfvScG8=97051416948195543854040388705182; __cas__rn__=408813689; __cas__st__212=961dd1bf361860c2d5408d9776b0077c5780cd7bb403313085191feec50cb20a49dfb04bf005c5c114148b21; __cas__id__212=41526675; CPID_212=41526675; CPTK_212=480692446; Hm_up_d101ea4d2a5c67dab98251f0b5de24dc={"uid_":{"value":"4949660085","scope":1}}; bdindexid=vk99s9qkop1i36bl4hqmgf22h4; ab_sr=1.0.1_NDcwMGJiMmE0ODE2Nzg4ZTBhYTljZGEwMDhkZDg1MTAwMGVhOTNhMDE3MzNiMmI5ZWE2OWU5ZmY2NWFiOTVjN2MxMzJkZmQ3ZGE5NGNhNGZkYTJkNGFmNTAxZmNhZmVmMDI3YzcwZjczMDBkZWM4N2U4NGUxY2Q3NWNlMjY5M2I1MjYwMThjMzA5NTc4ZTgzNjE2ODI3YmRhYmNmYjg3ZQ==; RT="z=1&dm=baidu.com&si=ff68c673-8ad5-4e0d-8dd7-3f2245c8865c&ss=l61jfwlq&sl=0&tt=0&bcn=https://fclog.baidu.com/log/weirwood?type=perf"; Hm_lpvt_d101ea4d2a5c67dab98251f0b5de24dc=1658801513; BDUSS_BFESS=RMY2tMZHp1ZmpsZWFnVjF4LWdMSkY1b3J4Mkl3LTZjNnVheWU4bVItaFUyUVpqRUFBQUFBJCQAAAAAAQAAAAEAAAC10QUnU0RVc3R1ZGVudDEyMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFRM32JUTN9iLW'
        }
        response = requests.get(url, headers=headers, cookies=cookies)
        data = json.loads(response.text)
        if data['status'] !=0:
            print('请求错误')
        return response.text

    def decrypt(self,t, e):  # 解密
        n = list(t)
        a = {}
        result = []
        ln = int(len(n) / 2)
        start = n[ln:]
        end = n[:ln]
        for j, k in zip(start, end):
            a.update({k: j})
        for j in e:
            result.append(a.get(j))
        return ''.join(result)

    def get_ptbk(self,uniqid):
        url = 'http://index.baidu.com/Interface/ptbk?uniqid={}'
        resp = self.get_html(url.format(uniqid))
        return json.loads(resp)['data']

    def get_data(self):  # 获取百度接口搜索数据
        if self.area is not None:
            url = "https://index.baidu.com/api/SearchApi/index?area={}&word=[[%7B%22name%22:%22{}%22,%22wordType%22:1%7D]]&startDate={}&endDate={}".format(
                self.area, self.keyword, self.start_date, self.end_date)
            data = self.get_html(url)  # 百度趋势接口返回数据
            data = json.loads(data)  # 数据加密需要解密
            uniqid = data['data']['uniqid']
            data = data['data']['userIndexes'][0]['all']['data']
            ptbk = self.get_ptbk(uniqid)  # 解密需要的参数
            result = self.decrypt(ptbk, data)
            result = result.split(',')
            start = self.start_date.split("-")
            end = self.end_date.split("-")
            a = datetime.date(int(start[0]), int(start[1]), int(start[2]))
            b = datetime.date(int(end[0]), int(end[1]), int(end[2]))
            node = 0
            keyword_list = []
            area_city_list=[]
            area_county_list=[]
            data_list = []
            num_list = []
            for i in range(a.toordinal(), b.toordinal()):#每日数据保存为列表
                date = datetime.date.fromordinal(i)
                keyword_list.append(self.keyword)
                area_city_list.append(self.area_name_city)
                area_county_list.append(self.area_name_county)
                data_list.append(date)
                num_list.append(result[node])
                node += 1
            df = pd.DataFrame(keyword_list, columns=['关键词'])#存储数据
            df.insert(df.shape[1], '省', area_city_list)
            df.insert(df.shape[1], '市', area_county_list)
            df.insert(df.shape[1], '时间', data_list)
            df.insert(df.shape[1], '指数', num_list)
            try:
                df1 = pd.DataFrame(pd.read_excel('百度指数.xlsx', sheet_name='Sheet1'))  #
                df2 = pd.concat([df1, df], axis=0)  # 纵向合并 时间会变多00：00：00
                df2.to_excel('百度指数.xlsx', index=False)
            except Exception as e:
                df.to_excel('百度指数.xlsx', index=False)
if __name__ == '__main__':
    keyword = "贪污"
    start_date = "2017-01-01"
    end_date =   "2017-12-31"
    area = '江苏省,大庆市'
    baidu_spider=Baidu_spider(keyword, start_date, end_date, area)
    baidu_spider.get_data()
