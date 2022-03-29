import os,re

def get_filelists(file_dir='.'):
    list_directory = os.listdir(file_dir)
    filelists = []
    for directory in list_directory:
        if(os.path.isdir(directory)):
            filelists.append(directory)
    return filelists

if __name__ == '__main__':
    print('本程序由github:asky88完成\n将自动化删除潜渊症mod内自带的无关参数，避免游戏将其自动删除\n使用前请先将mod解压到与exe同目录下')
    #loc=os.path.dirname(__file__)
    #os.chdir(loc)#尝试将cwd硬改到当前目录，可能失败
    print('当前工作路径'+os.getcwd()+'\n如果与实际不符，请检查目录中是否含有空格，关闭程序并更换路径，建议在纯英文路径下执行程序')
    input('单击回车继续')
    a=get_filelists()
    print('\n\n已获得与程序同级文件夹（以空格分割）：',end='')
    for i in a:
        print(i+' ',end='')
    input('\n请检查目录是否与预期一致，按回车键继续')
    for i in a:
        print('正在对文件夹'+i+'进行操作，获取文件夹下的filelist.xml')
        try:
            f=open(i+'/filelist.xml','r',encoding='utf-8')
        except(FileNotFoundError):
            print(i+'文件夹下没有filelist.xml文件\n')
            continue
        t=f.read()
        t=re.sub(' steamworkshopid=.*?>','>',t)
        f.close()
        f=open(i+'/filelist.xml','w',encoding='utf-8')
        f.write(t)
        f.close()
        print('写入'+i+'/filelist.xml成功\n')
        #f=open('./'+i+'filelist.xml','r')#仅debug用
    input('程序已完成，按回车键退出')