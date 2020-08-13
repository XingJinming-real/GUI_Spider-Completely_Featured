import tkinter as tk
import tkinter.messagebox
import os
import re
import requests
from bs4 import BeautifulSoup
import time

os.chdir('D:\\')

def download_img():
        if not os.path.exists('xjmssg.gif'):
            try:
                r=requests.get('https://pic.ibaotu.com/gif/19/50/56/22Q888piCaBv.gif!fwpaa50',
                               headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Safari/537.36 Edg/85.0.564.30'})
                f=open('xjmssg.gif','wb')
                f.write(r.content)
                f.close()
            except:
                print('Download Error')

                pass
        if not os.path.exists('second_img.gif'):
            r=requests.get('https://preview.qiantucdn.com/58pic/36/40/33/57K58PIC8m8zabcHtd239_PIC2018.gif!w1024_new_small',
                               headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.59 Safari/537.36 Edg/85.0.564.30'})
                               
            f=open('second_img.gif','wb')
            f.write(r.content)
            f.close()
            
        
        else:
            pass
        
def main_tk():
        
    window=tk.Tk()
    window.title('Log In')
    window.geometry('494x520')

    def view_it():
        tk.messagebox.showinfo(title='Be discreet',message='Your password is '+var_pw.get())
        pass

    tk.Label(window,bg='yellow',text='Welcome to the Spider-Program'.center(40)).pack()
    canvas=tk.Canvas(window,width=658,height=494)
    file_img=tk.PhotoImage(file='xjmssg.gif')
    img=canvas.create_image(0,0,anchor='nw',image=file_img)
    canvas.place(x=75,y=30)
        
    tk.Label(window,text='User name:').place(x=50,y=400)
    tk.Label(window,text='Password:').place(x=50,y=450)
    tk.Button(window,text='View it',command=view_it).place(x=295,y=450)
    var_un=tk.StringVar()
    var_pw=tk.StringVar()
    var_un.set('Example@126.com')
        
    t_un=tk.Entry(window,textvariable=var_un)
    t_pw=tk.Entry(window,textvariable=var_pw,show='*')
    t_un.place(x=150,y=400)
    t_pw.place(x=150,y=450)


    def login():
        f=open('password.txt','rt')
        for i in f:
            info=i.split(',')
            user_name=info[0]
            keys[user_name]=info[1].replace('\n','')
        if t_un.get()=='':
            tk.messagebox.showwarning(title='Warning',message='Please input your account')
            
        elif t_un.get() not in keys.keys():
            k=tk.messagebox.askquestion(title='Warning',message='You have not signed up!\
     Sign up now?')
            if k=='yes':
                sign_up()
            else:
                pass
        else:   
            if not t_pw.get()==keys[t_un.get()]:
                tk.messagebox.showinfo(title='Warning',message='Password error')
            else:
                tk.messagebox.showinfo(title='Welcome',message='Logined')
                window.destroy()
                open_new()
        pass
            
    def open_new():

        window_new=tk.Tk()
        window_new.title('Console')
        window_new.geometry('600x400')
        menubar=tk.Menu(window_new)
        back_menu=tk.Menu(menubar,tearoff=0)#  待完善menubar
        menubar.add_cascade(label='Back',menu=back_menu)
        def donate():
            window_donate=tk.Tk()
            tk.Label(window_donate,text='作者不易，打个赏吧~',font=('华文行楷',20)).pack()
        def about_author():
            tk.messagebox.showinfo(title='About_the_author',message=' I\'m a digital and utmost stone.\n My Github account is XingJinming-real.\n Like me, then give me a star on my Github.\n APPRECIATE IT !')
        about_menu=tk.Menu(window_new,tearoff=0)
        menubar.add_cascade(label='About',menu=about_menu)
        about_menu.add_command(label='About the author',command=about_author)
        about_menu.add_separator()
        img=tk.PhotoImage(file='C:\\Users\\邢金明\\Desktop\\donate.gif')
        about_menu.add_command(label='Donate',command=donate,image=img)
        
        def back_step():
            k=tk.messagebox.askquestion(title='Warning',message='Are you sure to quit out?')
            if k=='yes':
                window_new.destroy()
                main()
        back_menu.add_command(label='Back to the previous step',command=back_step)

        var_txt=tk.StringVar()
        scrollbar=tk.Scrollbar(window_new)
        scrollbar.place(x=550,y=50,height=300)
        text=tk.Text(window_new, font=10,yscrollcommand=scrollbar.set)#yscrollcommand=scrollbar.set设置滑动条
        text.place(x=350,y=50,width=200,height=300)
        scrollbar.config(command=text.yview)#.config(command=text.yview)同步text内容
        
        text.see('end')

        def acquire_all():
            tk.messagebox.showwarning(title='Warning',message='想得美')
            pass
        def acquire_heroes():
            if not os.path.exists('D:\\王者荣耀Resources'):
                os.mkdir('D:\\王者荣耀Resources')
            url='http://news.4399.com/gonglue/wzlm/'+'yingxiong'+'/'
            html=get(url)
            text.insert('end','正在存储Heros,请等待\n\n')
            resources=get_all_hero_fuwen_url(html)
            get_load_chuzhuang(resources)
            get_load_hero_fuwen_recommend(resources)
            get_load_hero_jiexi(resources)
            resources=process_heros_html(html)
            try:
                for i in range(len(resources)):
                    time.sleep(0.15)
                    text.insert('end','正在存储 '+resources[i][0][0]+'.png,请等待\n\n')
                    text.see(tk.END)
                    text.update()
                store_yingxiong_resources(resources)
                text.insert('end','成功')
            except:
                print('请彻底删除已获取的文件后重试')
            pass
        def acquire_skins():
            
            url='http://news.4399.com/gonglue/wzlm/'+'pifu'+'/'
            html=get(url)
            if not os.path.exists('D:\\王者荣耀Resources'):
                os.mkdir('D:\\王者荣耀Resources')
            text.insert('end','正在存储Skins,请等待\n\n')
            resources=process_skins_html(html)
            for i in range(len(resources)):
                time.sleep(0.15)
                text.insert('end','正在存储 '+resources[i][0]+'.png,请等待\n\n')
                text.see(tk.END)
                text.update()
            store_pifu_resources(resources)
            text.insert('end','成功')
            pass
        def acquire_outfits():
            
            url='http://news.4399.com/gonglue/wzlm/'+'daoju'+'/'
            html=get(url)
            if not os.path.exists('D:\\王者荣耀Resources'):
                os.mkdir('D:\\王者荣耀Resources')
            text.insert('end','正在存储Outfits,请等待\n\n')
            resources=process_properties_html(html)
            try:
                for i in range(len(resources)):
                    time.sleep(0.15)
                    text.insert('end','正在存储 '+resources[i][0]+'.png,请等待\n\n')
                    text.see(tk.END)
                    text.update()
                store_daoju_resources(resources)
                text.insert('end','成功')
            except:
                print('请彻底删除已获取的文件后重试')
            pass
        
        tk.Button(window_new,text='Acquire All',command=acquire_all).place(x=80,y=200)
        tk.Button(window_new,text='Acquire Heroes',command=acquire_heroes).place(x=80,y=50)
        tk.Button(window_new,text='Acquire Outfits',command=acquire_outfits).place(x=80,y=100)
        tk.Button(window_new,text='Acquire Skins',command=acquire_skins).place(x=80,y=150)
        tk.Label(window_new,text='Author\'s Email: xjm0801@126.com. Call me for any problem.',font=('华文行楷',20)).place(x=25,y=350)

        
        window_new.config(menu=menubar)
        pass

    def sign_up():
        su_window=tk.Tk()
        su_window.title('Sign up')
        su_window.geometry('300x400')
        def direction():#  待完善menubar
            tk.messagebox.showinfo(title='Help',message='Input randomly whatever you want !')
            pass
        def send_email():#  待完善menubar
            tk.messagebox.showinfo(title='Send Email',message='Please send your problem to xjm0801@126.com for more help!')
        menubar=tk.Menu(su_window)
        help_menu=tk.Menu(menubar,tearoff=0)#  待完善menubar
        menubar.add_cascade(label='Help',menu=help_menu)
        help_menu.add_command(label='Directions',command=direction)
        more_menu=tk.Menu(help_menu,tearoff=0)
        help_menu.add_cascade(label='More',menu=more_menu)
        more_menu.add_command(label='Send Email',command=send_email)
        help_menu.add_separator()
        help_menu.add_command(label='Exit',command=window.quit())
        su_window.config(menu=menubar)
        
        tk.Label(su_window,text='Your email address:').place(x=20,y=50)
        e_email=tk.Entry(su_window)
        e_email.place(x=140,y=50)
        tk.Label(su_window,text='Your password:').place(x=20,y=110)
        ps=tk.Entry(su_window)
        ps.place(x=140,y=110)
        tk.Label(su_window,text='Confirm password:').place(x=20,y=170)
        ps_confirm=tk.Entry(su_window)
        ps_confirm.place(x=140,y=170)
        def sign_up_check():
            if e_email.get() in keys.keys():
                tk.messagebox.showwarning(title='Warning',message='This account has already existed')
            if not re.match(r'\w+@\w{3,8}\.com',e_email.get()):
                tk.messagebox.showerror(title='Error',message='Please rectify the pattern of your email \
    address!')
                su_window.destroy()
                sign_up()
            else:
                pass
            
            if not ps_confirm.get()==ps.get():
                tk.messagebox.showerror(title='Error',message='Please make sure your password is \
    same!')
                su_window.destroy()
                sign_up()
            else:
                keys[e_email.get()]=ps_confirm.get()
                tk.messagebox.showinfo(title='Welcome',message='Welcome '+e_email.get()+' !'+' Now please login!')

                
                f=open('password.txt','at')
                f.write('\n')
                f.write(e_email.get()+','+ps.get())
                f.close()
                su_window.destroy()
        check_b=tk.Button(su_window,text='sign up',bg='yellow',command=sign_up_check)
        check_b.place(x=220,y=350)
        pass


    keys={}
    b_login=tk.Button(window,text='Log in',command=login)
    b_sign_up=tk.Button(window,text='Sign up',command=sign_up)
    b_login.place(x=350,y=480)
    b_sign_up.place(x=420,y=480)
    menubar=tk.Menu(window)
    back_menu=tk.Menu(menubar,tearoff=0)#  待完善menubar
    menubar.add_cascade(label='Back',menu=back_menu)
    def back_step():
        k=tk.messagebox.askquestion(title='Warning',message='Are you sure to quit out?')
        if k=='yes':
            window.destroy()
    back_menu.add_command(label='Back to the previous step',command=back_step)

    window.config(menu=menubar)

    
    window.mainloop()

    
if not os.path.exists('password.txt'):
    f=open('password.txt','wt')
    f.write('admin,admin')
    f.close()
else:
    os.remove('password.txt')
    f=open('password.txt','wt')
    f.write('admin,admin')
    f.close()















#####以下为爬虫部分######








def get(url):
    try:
        r=requests.get(url,headers=hd)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        html=r.text
        return html
    except:
        print("被墙")
        pass
def process_properties_html(html):#先抓取图片 还有武器详细介绍，resources格式为[[imgname,url],[imgname,url],...]
    resources=[]
    soup=BeautifulSoup(html,'html.parser')
    mid_ls_tag=soup.find_all('img')
    mid_ls_tag=mid_ls_tag[40:145] 
    for i in range(len(mid_ls_tag)):
        resource_single=[]
        resource_single.append(mid_ls_tag[i].get('alt'))
        resource_single.append(mid_ls_tag[i].get('lz_src'))
        resources.append(resource_single)
    return resources

def process_heros_html(html):#有名字和视频演示  resources有视频格式为[[[imgname,url],[mkvurl]],[[imgname,url],[mkvurl]],.....]  没有视频的格式为[[[imgname,url]],[[imgname,url]],.....]
    global px
    resources=[]    
    mkvls=[]            #以上两维列表为[[名字，地址]....[]]
    soup=BeautifulSoup(html,'html.parser')
    mid_ls_tag=soup.find_all('img')
    mid_ls_tag=mid_ls_tag[35:137]
    for i in range(len(mid_ls_tag)):    #此处为获取imgls[]
        resources_sec=[]
        imgls=[]
        imgls.append(mid_ls_tag[i].get('alt')[4:])
        imgls.append(mid_ls_tag[i].get('lz_src'))
        resources_sec.append(imgls)
        resources.append(resources_sec)
    mid_ls_tag=soup.find_all('a','yxvideo')
    for i in range(len(mid_ls_tag)):
        mkvls=[]
        mkvls.append(mid_ls_tag[i].get('href'))
        resources[i].append(mkvls)
    return resources

def process_skins_html(html):#resources 结构为[[name,url],[name,url],....]
    resources=[]
    soup=BeautifulSoup(html,'html.parser') 
    mid_ls_tag=soup.find_all('img')
    mid_ls_tag=mid_ls_tag[40:340]
    for i in range(len(mid_ls_tag)):
        mid_ls=[]
        mid_ls.append(mid_ls_tag[i].get('alt'))
        mid_ls.append(mid_ls_tag[i].get('lz_src'))
        resources.append(mid_ls)
    return resources

def store_all_csv(resources,name):
    os.chdir('D:\\王者荣耀Resources\\')
    f=open(name+'_url.txt','at')
    for i in range(len(resources)):
        try:
            f.write(str(resources[i])+'\n')
        except:
            continue
    f.close()
    pass

def store_pifu_resources(resources):
    if not os.path.exists('D:\\王者荣耀Resources\\Skin_img'):#创建照片位置
        os.mkdir('D:\\王者荣耀Resources\\Skin_img')
    os.chdir('D:\\王者荣耀Resources\\Skin_img')
    print('请等待')
    for i in range(len(resources)):
        r=requests.get(resources[i][1],headers=hd)
        r.raise_for_status()
        f=open(resources[i][0]+'.png','wb')
        f.write(r.content)
        f.close()
    print("成功".center(25))
    pass

def store_yingxiong_resources(resources):
    if not os.path.exists('D:\\王者荣耀Resources\\YingXiong_img'):#创建照片位置
        os.mkdir('D:\\王者荣耀Resources\\YingXiong_img')
    os.chdir('D:\\王者荣耀Resources\\YingXiong_img')  #先存照片转到照片文件夹
    print('请等待')
    for i in range(len(resources)):
        try:
            r=requests.get(resources[i][0][1],headers=hd)
            r.raise_for_status()
            f=open(resources[i][0][0]+'.png','wb')
            f.write(r.content)
            f.close()
        except:
            print('被墙')
            continue
    print("成功存入英雄照片".center(25))
    if px==1:
        if not os.path.exists('D:\\王者荣耀Resources\\YingXiong_mkv'):
            os.mkdir('D:\\王者荣耀Resources\\YingXiong_mkv')
        os.chdir('D:\\王者荣耀Resources\\YingXiong_mkv')
        for i in range(len(resources)):#  存视频
            try:
                r=requests.get(resources[i][1][0],headers=hd)
                r.raise_for_status()
                f=open(resources[i][0][0]+'.mkv','wb')
                f.write(r.content)
                f.close()
            except:
                print('被墙')
                continue
        print("成功存入英雄视频".center(25))
    pass

def store_daoju_resources(resources):
    if not os.path.exists('D:\\王者荣耀Resources\\DaoJu_img'):#创建照片位置
        os.mkdir('D:\\王者荣耀Resources\\DaoJu_img')
    os.chdir('D:\\王者荣耀Resources\\DaoJu_img')
    print('请等待')
    for i in range(len(resources)):
        try:
            r=requests.get(resources[i][1],headers=hd)
            r.raise_for_status()
            f=open(resources[i][0]+'.png','wb')
            f.write(r.content)
            f.close()
        except:
            print('被墙')
            continue
    print("成功".center(25))
    pass

def get_load_hero_fuwen_recommend(resources):
    regix=re.compile(r'\w{2}\*\d{1,2}')
    if not os.path.exists('D:\\王者荣耀Resources\\Mingwen'):
        os.mkdir('D:\\王者荣耀Resources\\Mingwen')
    os.chdir('D:\\王者荣耀Resources\\Mingwen')
    for i in range(len(resources)):
        try:
            fuwen=[]
            fuwen_ls=[]
            html=get(resources[i][1])
            soup=BeautifulSoup(html,'html.parser')
            fuwen_tag=soup.find_all('p')[6:9]
            for j in range(len(fuwen_tag)):
                fuwen_ls.append(re.findall(regix,str(fuwen_tag[j])))  #为[[fuwen,fuwen],[fuwen,fuwen]...]
            f=open(resources[i][0]+'出装+铭文+解析.txt','at')
            for i in range(len(fuwen_ls)):
                f.write(fuwen_ls[i][0]+',')
                f.write(fuwen_ls[i][1]+'\n')
            f.close()
        except:
            continue
    pass

def get_load_chuzhuang(resources):
    regix=re.compile(r'\王\者\荣\耀.{4}')
    
    for i in range(len(resources)):
        try:
            chu_zhuang_tag=[]
            chu_zhuang_ls=[]
            html=get(resources[i][1])
            soup=BeautifulSoup(html,'html.parser')
            chu_zhuang_tag=soup.find_all('img',alt=regix,lzimg='1')
            for j in range(len(chu_zhuang_tag)):
                chu_zhuang_ls.append(chu_zhuang_tag[j].get('alt')+'\n')             #为[chuzhuang1,chuzhuang2...]
            if not os.path.exists('D:\\王者荣耀Resources\\Chu_Zhuang'):
                os.mkdir('D:\\王者荣耀Resources\\Chu_Zhuang')
            os.chdir('D:\\王者荣耀Resources\\Chu_Zhuang')
            f=open(resources[i][0]+'出装+铭文+解析.txt','at')
            for i in range(len(chu_zhuang_ls)):
                f.write(chu_zhuang_ls[i])
                
            f.close()
        except:
            continue
    pass

def get_all_hero_fuwen_url(html):  #返回[[name,url],[name,url]...]
    global text
    resources=[]
    name_ls_mid=[]
    url_ls_mid=[]
    name_ls=[]
    url_ls=[]
    soup=BeautifulSoup(html,'html.parser')
    name_ls_tag=soup.find_all('span')[26:127]
  
    for i in range(len(name_ls_tag)):
        name_ls_mid=[]
        name_ls_mid.append(name_ls_tag[i].string)
        name_ls.append(name_ls_mid)
    mid_ls_tag=soup.find_all('a')[79:381:3]  
    for i in range(len(mid_ls_tag)):
        name_ls[i].append(mid_ls_tag[i].get('href'))
    resources=name_ls
    return resources

def get_load_hero_jiexi(resources):   #jiexi为一行字符
    regix=re.compile(r'dis\w*')
    if not os.path.exists('D:\\王者荣耀Resources\\Jiexi'):
        os.mkdir('D:\\王者荣耀Resources\\Jiexi')
    os.chdir('D:\\王者荣耀Resources\\Jiexi')
    for i in range(len(resources)):
        try:
            html=get(resources[i][1])
            soup=BeautifulSoup(html,'html.parser')
            f=open(resources[i][0]+'出装+铭文+解析.txt','at')            
            f.write(soup.find('li',style=regix).string+'\n')
            f.close()
        except:
            continue
    pass
    
def main():
    global text
    index=input("请输入要获得的数据,英雄yx/皮肤pf/装备zb：")
    indexls={'英雄':'yingxiong','皮肤':'pifu','装备':'daoju','yx':'yingxiong','zb':'daoju','pf':'pifu'}
    keyword=indexls.get(index,'请正确输入：')
    if(keyword=='请正确输入'):
        print('请正确输入')
        return
    url='http://news.4399.com/gonglue/wzlm/'+keyword+'/'
    if not os.path.exists('D:\\王者荣耀Resources'):
        os.mkdir('D:\\王者荣耀Resources')
    html=get(url)
    if keyword=='yingxiong':
        resources=get_all_hero_fuwen_url(html)
        if(eval(input('是否要英雄出装? 是请按1，否请按0：'))):
            print('请等待'.center(25))
            get_load_chuzhuang(resources)
            print('完成'.center(25))
        if(eval(input('是否要英雄铭文? 是请按1，否请按0：'))):
            print('请等待'.center(25))
            get_load_hero_fuwen_recommend(resources)
            print('完成'.center(25))
        if(eval(input('是否要英雄技能简介? 是请按1，否请按0：'))):
            print('请等待'.center(25))
            get_load_hero_jiexi(resources)
            print('完成'.center(25))
        resources=process_heros_html(html)
        try:
            store_yingxiong_resources(resources)
        except:
            print('请彻底删除已获取的文件后重试')
    elif keyword=='pifu':
        resources=process_skins_html(html)
        try:
            store_pifu_resources(resources)
        except:
            print('请彻底删除已获取的文件后重试')
    elif keyword=='daoju':
        resources=process_properties_html(html)
        try:
            store_daoju_resources(resources)
        except:
            print('请彻底删除已获取的文件后重试')
    store_all_csv(resources,keyword)
    pass


    


hd={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.68 Safari/537.36 Edg/84.0.522.28','Referer':'http://newsimg.5054399.com/wzlm/v3/css/style.css'}
download_img()
main_tk()
