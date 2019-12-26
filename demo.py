# official document : https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/
# 安裝beautifulsoup

pip3 install beautifulsoup4

# 使用案例ptt 八卦版

def fetch(url):
    response = requests.get(url)
    response = requests.get(url, cookies={'over18': '1'})  # 一直向 server 回答滿 18 歲了 !
    return response
    
url = 'https://www.ptt.cc/bbs/Gossiping/index.html'
resp = fetch(url)  # step-1
soup = BeautifulSoup(resp.text, 'html.parser')

for link in soup.find_all('div','title'):
    print(link.a.string)
    
#	Re: [問卦] 如果殺了習近平會怎樣？
#	[問卦] 山坡上是窮人還是富人住的
#	[新聞] 「長腿熟女」夯到接海外廣告...慘被遣返
#	Re: [新聞] 台灣淪為籌碼　時代雜誌：川普暫緩對台F-
#	[臉書] 邱泰然
#	[問卦] 輕小說算宅嗎
#	[問卦] 看howhow你們真的笑得出來？
#	[新聞] 羽球》無緣篡位球后戴資穎 中國球迷這樣
#	Re: [問卦] 為什麼人民幣最大幣值才100元
#	[問卦] 有沒有整個清明節都在吃芭樂的八卦？
#	[問卦] 為什麼最近要辣的這麼多？
#	Re: [新聞] 民問「台獨有什麼好處？」 蔡英文：台灣
#	[問卦] 台灣近幾十年有出現類似南韓山火事件嗎？
#	[問卦] 外勞是不是比很多台灣人強多了
#	Re: [問卦] 中國一直爆炸是什麼套路
#	[公告] 八卦板板規(2019.02.21)
#	[協尋]中和明禮街-3/29下午6點左右車禍(更新地址~)
#	[公告] 四月份置底閒聊區^Q^

# 臺灣資安大會slides

import requests
from bs4 import BeautifulSoup
def fetch(url):
    response = requests.get(url)
    return response

url = 'https://cyber.ithome.com.tw/slides'
resp = fetch(url)  # step-1
soup = BeautifulSoup(resp.text, 'html.parser')

for link in soup.find_all('div','col-md-3 col-xs-6 slide-session'):
    print(link.a['href'])

"""
https://s.itho.me/cybersec/2019/slides/321/F_ 大會堂 分堂/0321F41450張櫂閔.pdf
https://s.itho.me/cybersec/2019/slides/321/H_世貿二/0321H11130王宏仁.pdf
https://s.itho.me/cybersec/2019/slides/321/A_102/0321A11130孫雅麗.pdf
https://s.itho.me/cybersec/2019/slides/321/A_102/0321A61700Turkey Melody.pdf
https://s.itho.me/cybersec/2019/slides/320/G_世貿第一/0320G31450陳忠信.pdf
https://s.itho.me/cybersec/2019/slides/319/C_TICC 201BC/0319C41615蔡馥冲.pdf
https://s.itho.me/cybersec/2019/slides/320/C_TICC 201 BC/0320C21400Tommi Maekilae.pdf
https://s.itho.me/cybersec/2019/slides/320/B_TICC 201 AF/0320B21400邢廣耀.pdf
https://s.itho.me/cybersec/2019/slides/320/H_世貿第二/0320H21400符傳威.pdf
https://s.itho.me/cybersec/2019/slides/321/F_ 大會堂 分堂/0321F61700徐千洋.pdf
https://s.itho.me/cybersec/2019/slides/319/C_TICC 201BC/0319C51705林家正.pdf
https://s.itho.me/cybersec/2019/slides/320/Keynote/0320Keynote51100游峯鵬.pdf
https://s.itho.me/cybersec/2019/slides/319/H_世貿二/0319H21405X1.pdf
https://s.itho.me/cybersec/2019/slides/319/J_世貿五/0319J21405Serkan Cetin.pdf
https://s.itho.me/cybersec/2019/slides/320/D_TICC 201 DE/0320D21400張士龍曹家通.pdf
https://s.itho.me/cybersec/2019/slides/321/C_201 BC/金融安全座談.zip
https://s.itho.me/cybersec/2019/slides/321/A_102/0321A51610Cameron Townshend.pdf
https://s.itho.me/cybersec/2019/slides/320/A_TICC 102/0320A51700蔣盛文.pdf
"""
