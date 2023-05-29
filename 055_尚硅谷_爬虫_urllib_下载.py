import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'
#
# # url代表的是下载的路径  filename文件的名字
# # 在python中 可以变量的名字  也可以直接写值
# urllib.request.urlretrieve(url_page,'baidu.html')

# 下载图片
url_img = 'https://image.baidu.com/search/detail?ct=503316480&z=undefined&tn=baiduimagedetail&ipn=d&word=lisa&step_word=&ie=utf-8&in=&cl=2&lm=-1&st=undefined&hd=undefined&latest=undefined&copyright=undefined&cs=2199722019,2117815958&os=4217647971,225113843&simid=2199722019,2117815958&pn=15&rn=1&di=7214885350303334401&ln=1773&fr=&fmq=1683549483449_R&fm=&ic=undefined&s=undefined&se=&sme=&tab=0&width=undefined&height=undefined&face=undefined&is=0,0&istype=0&ist=&jit=&bdtype=0&spn=0&pi=0&gsm=1e&objurl=https%3A%2F%2Fgimg2.baidu.com%2Fimage_search%2Fsrc%3Dhttp%253A%252F%252Fc-ssl.duitang.com%252Fuploads%252Fitem%252F202003%252F22%252F20200322095654_2fTzQ.jpeg%26refer%3Dhttp%253A%252F%252Fc-ssl.duitang.com%26app%3D2002%26size%3Df9999%2C10000%26q%3Da80%26n%3D0%26g%3D0n%26fmt%3Dauto%3Fsec%3D1686141482%26t%3De470f219095720bab4bb8440ac3d1bdf&rpstart=0&rpnum=0&adpicid=0&nojc=undefined&dyTabStr=MCwxLDYsMyw0LDUsMiw3LDgsOQ%3D%3D'

urllib.request.urlretrieve(url= url_img,filename='lisa.jpg')

# 下载视频
# url_video = 'https://vd3.bdstatic.com/mda-mhkku4ndaka5etk3/1080p/cae_h264/1629557146541497769/mda-mhkku4ndaka5etk3.mp4?v_from_s=hkapp-haokan-tucheng&auth_key=1629687514-0-0-7ed57ed7d1168bb1f06d18a4ea214300&bcevod_channel=searchbox_feed&pd=1&pt=3&abtest='
#
# urllib.request.urlretrieve(url_video,'hxekyyds.mp4')