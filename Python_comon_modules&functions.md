# **********************
# PY核心模块方法
# **********************

## os模块:
* os.`remove()`         删除文件
* os.`unlink()`         删除文件 
* os.`rename()`         重命名文件 
* os.`listdir()`        列出指定目录下所有文件 
* os.`chdir()`          改变当前工作目录
* os.`getcwd()`         获取当前文件路径
* os.`mkdir()`          新建目录
* os.`rmdir()`          删除空目录(删除非空目录, 使用shutil.rmtree())
* os.`makedirs()`       创建多级目录
* os.`removedirs()`     删除多级目录
* os.`stat(file)`       获取文件属性
* os.`chmod(file)`      修改文件权限
* os.`utime(file)`      修改文件时间戳
* os.`name(file)`       获取操作系统标识
* os.`system()`        执行操作系统命令
* os.`execvp()`         启动一个新进程
* os.`fork()`           获取父进程ID，在子进程返回中返回0
* os.`execvp()`         执行外部程序脚本（Uinx）
* os.`spawn()`          执行外部程序脚本（Windows）
* os.`access(path, mode)` 判断文件权限(详细参考cnblogs)

## os.path模块：
* `os.path.split(filename)`         将文件路径和文件名分割(会将最后一个目录作为文件名而分离)
* `os.path.splitext(filename)`      将文件路径和文件扩展名分割成一个元组
* `os.path.dirname(filename)`       返回文件路径的目录部分
* `os.path.basename(filename)`      返回文件路径的文件名部分
* `os.path.join(dirname,basename)`  将文件路径和文件名凑成完整文件路径
* `os.path.abspath(name)`           获得绝对路径
* `os.path.splitunc(path)`          把路径分割为挂载点和文件名
* `os.path.normpath(path)`          规范path字符串形式
* `os.path.exists()`                判断文件或目录是否存在
* `os.path.isabs()`                 如果path是绝对路径，返回True
* `os.path.realpath(path)`          # 返回path的真实路径
* `os.path.relpath(path[, start])`  # 从start开始计算相对路径   
* `os.path.normcase(path)`          # 转换path的大小写和斜杠
* `os.path.isdir()`                 # 判断name是不是一个目录，name不是目录就返回false
* `os.path.isfile()`                判断name是不是一个文件，不存在返回false
* `os.path.islink()`                判断文件是否连接文件,返回boolean
* `os.path.ismount()`               指定路径是否存在且为一个挂载点，返回boolean
* `os.path.samefile()`              是否相同路径的文件，返回boolean
* `os.path.getatime()`              返回最近访问时间 浮点型
* `os.path.getmtime()`              返回上一次修改时间 浮点型
* `os.path.getctime()`              返回文件创建时间 浮点型
* `os.path.getsize()`               返回文件大小 字节单位
* `os.path.commonprefix(list)`      #返回list(多个路径)中，所有path共有的最长的路径
* `os.path.lexists`                 #路径存在则返回True,路径损坏也返回True
* `os.path.expanduser(path)`        #把path中包含的"~"和"~user"转换成用户目录
* `os.path.expandvars(path)`        #根据环境变量的值替换path中包含的”$name”和”${name}”
* `os.path.sameopenfile(fp1, fp2)`  #判断fp1和fp2是否指向同一文件
* `os.path.samestat(stat1, stat2)`  #判断stat tuple stat1和stat2是否指向同一个文件
* `os.path.splitdrive(path)`        #一般用在windows下，返回驱动器名和路径组成的元组
* `os.path.walk(path, visit, arg)`  #遍历path，给每个path执行一个函数详细见手册
* `os.path.supports_unicode_filenames()`     设置是否支持unicode路径名

##sys模块：
* `sys.argv`                命令行参数List，第一个元素是程序本身路径 
* `sys.path`                返回模块的搜索路径，初始化时使用PYTHONPATH环境变量的值 
* `sys.modules.keys()`      返回所有已经导入的模块列表
* `sys.modules`             返回系统导入的模块字段，key是模块名，value是模块 
* `sys.exc_info()`          获取当前正在处理的异常类,exc_type、exc_value、exc_traceback当前处理的异常详细信息
* `sys.exit(n)`             退出程序，正常退出时exit(0)
* `sys.hexversion`          获取Python解释程序的版本值，16进制格式如：0x020403F0
* `sys.version`             获取Python解释程序的版本信息
* `sys.platform`            返回操作系统平台名称
* `sys.stdout`              标准输出
* `sys.stdout.write('aaa')` 标准输出内容
* `sys.stdout.writelines()` 无换行输出
* `sys.stdin`               标准输入
* `sys.stdin.read()`        输入一行
* `sys.stderr`              错误输出
* `sys.exc_clear()`         用来清除当前线程所出现的当前的或最近的错误信息 
* `sys.exec_prefix`         返回平台独立的python文件安装的位置 
* `sys.byteorder`           本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little' 
* `sys.copyright`           记录python版权相关的东西 
* `sys.api_version`         解释器的C的API版本 
* `sys.version_info`        'final'表示最终,也有'candidate'表示候选，表示版本级别，是否有后继的发行 
* `sys.getdefaultencoding()`        返回当前你所用的默认的字符编码格式 
* `sys.builtin_module_names`        Python解释器导入的内建模块列表 
* `sys.executable`                  Python解释程序路径 
* `sys.getwindowsversion()`         获取Windows的版本 
* `sys.stdin.readline()`            从标准输入sys.stdout.write("a") 屏幕输出a
* `sys.setdefaultencoding(name)`    用来设置当前默认的字符编码(详细使用参考文档) 
* `sys.displayhook(value)`          如果value非空，这个函数会把他输出到sys.stdout(详细使用参考文档)

## datetime,date,time模块：
* `datetime.date.today()`           本地日期对象,(用str函数可得到它的字面表示(2014-03-24))
* `datetime.date.isoformat(obj)`    当前[年-月-日]字符串表示(2014-03-24)
* `datetime.date.fromtimestamp()`   返回一个日期对象，参数是时间戳,返回 [年-月-日]
* `datetime.date.weekday(obj)`      返回一个日期对象的星期数,周一是0
* `datetime.date.isoweekday(obj)`   返回一个日期对象的星期数,周一是1
* `datetime.date.isocalendar(obj)`  把日期对象返回一个带有年月日的元组
* `datetime.datetime.today()`       返回一个包含本地时间(含微秒数)的datetime对象 2014-03-24 23:31:50.419000
* `datetime.datetime.now([tz])`     返回指定时区的datetime对象 2014-03-24 23:31:50.419000
* `datetime.datetime.utcnow()`      返回一个零时区的datetime对象
* `datetime.fromtimestamp(timestamp[,tz])`      按时间戳返回一个datetime对象，可指定时区,可用于strftime转换为日期表示 
* `datetime.utcfromtimestamp(timestamp)`        按时间戳返回一个UTC-datetime对象
* `datetime.datetime.strptime('2014-03-16 12:21:21',"%Y-%m-%d %H:%M:%S")` 将字符串转为datetime对象
* `datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d %H%M%S')` 将datetime对象转换为str表示形式
* `datetime.date.today().timetuple()`           转换为时间戳datetime元组对象，可用于转换时间戳
* `datetime.datetime.now().timetuple()`
* `time.mktime(timetupleobj)`                   将datetime元组对象转为时间戳
* `time.time()`                     当前时间戳
* `time.localtime`
* `time.gmtime`   

## hashlib,md5模块：
* `hashlib.md5('md5_str').hexdigest()`      对指定字符串md5加密
* `md5.md5('md5_str').hexdigest()`          对指定字符串md5加

## random模块：
* `random.random()`             产生0-1的随机浮点数
* `random.uniform(a, b)`        产生指定范围内的随机浮点数
* `random.randint(a, b)`        产生指定范围内的随机整数
* `random.randrange([start], stop[, step])` 从一个指定步长的集合中产生随机数
* `random.choice(sequence)`     从序列中产生一个随机数
* `random.shuffle(x[, random])` 将一个列表中的元素打乱
* `random.sample(sequence, k)`  从序列中随机获取指定长度的片断
 
## MySQLdb模块：
* `MySQLdb.get_client_info()`           获取API版本
* `MySQLdb.Binary('string')`            转为二进制数据形式
* `MySQLdb.escape_string('str')`        针对mysql的字符转义函数
* `MySQLdb.DateFromTicks(1395842548)`   把时间戳转为datetime.date对象实例
* `MySQLdb.TimestampFromTicks(1395842548)`   把时间戳转为datetime.datetime对象实例
* `MySQLdb.string_literal('str')`       字符转义

## string模块：
* `str.capitalize()`            把字符串的第一个字符大写
* `str.center(width)`           返回一个原字符串居中，并使用空格填充到width长度的新字符串
* `str.ljust(width)`            返回一个原字符串左对齐，用空格填充到指定长度的新字符串
* `str.rjust(width)`            返回一个原字符串右对齐，用空格填充到指定长度的新字符串
* `str.zfill(width)`            返回字符串右对齐，前面用0填充到指定长度的新字符串
* `str.count(str,[beg,len])`    返回子字符串在原字符串出现次数，beg,len是范围
* `str.decode(encodeing[,replace])` 解码string,出错引发ValueError异常
* `str.encode(encodeing[,replace])` 解码string
* `str.endswith(substr[,beg,end])`  字符串是否以substr结束，beg,end是范围
* `str.startswith(substr[,beg,end])`  字符串是否以substr开头，beg,end是范围
* `str.expandtabs(tabsize = 8)`     把字符串的tab转为空格，默认为8个
* `str.find(str,[stat,end])`        查找子字符串在字符串第一次出现的位置，否则返回-1
* `str.index(str,[beg,end])`        查找子字符串在指定字符中的位置，不存在报异常
* `str.isalnum()`               检查字符串是否以字母和数字组成，是返回true否则False
* `str.isalpha()`               检查字符串是否以纯字母组成，是返回true,否则false
* `str.isdecimal()`             检查字符串是否以纯十进制数字组成，返回布尔值
* `str.isdigit()`               检查字符串是否以纯数字组成，返回布尔值
* `str.islower()`               检查字符串是否全是小写，返回布尔值
* `str.isupper()`               检查字符串是否全是大写，返回布尔值
* `str.isnumeric()`             检查字符串是否只包含数字字符，返回布尔值
* `str.isspace()`               如果str中只包含空格，则返回true,否则FALSE
* `str.title()`                 返回标题化的字符串（所有单词首字母大写，其余小写）
* `str.istitle()`               如果字符串是标题化的(参见title())则返回true,否则false
* `str.join(seq)`               以str作为连接符，将一个序列中的元素连接成字符串
* `str.split(str='',num)`       以str作为分隔符，将一个字符串分隔成一个序列，num是被分隔的字符串
* `str.splitlines(num)`         以行分隔，返回各行内容作为元素的列表
* `str.lower()`                 将大写转为小写
* `str.upper()`                 转换字符串的小写为大写
* `str.swapcase()`              翻换字符串的大小写
* `str.lstrip()`                去掉字符左边的空格和回车换行符
* `str.rstrip()`                去掉字符右边的空格和回车换行符
* `str.strip()`                 去掉字符两边的空格和回车换行符
* `str.partition(substr)`       从substr出现的第一个位置起，将str分割成一个3元组。
* `str.replace(str1,str2,num)`  查找str1替换成str2，num是替换次数
* `str.rfind(str[,beg,end])`    从右边开始查询子字符串
* `str.rindex(str,[beg,end])`   从右边开始查找子字符串位置 
* `str.rpartition(str)`         类似partition函数，不过从右边开始查找
* `str.translate(str,del='')`   按str给出的表转换string的字符，del是要过虑的字符
    

## urllib模块：
* `urllib.quote(string[,safe])`             对字符串进行编码。参数safe指定了不需要编码的字符
* `urllib.unquote(string)`                  对字符串进行解码
* `urllib.quote_plus(string[,safe])`        urllib.quote类似，但这个方法用'+'来替换' '，而quote用'%20'来代替' '
* `urllib.unquote_plus(string )`            对字符串进行解码
* `urllib.urlencode(query[,doseq])`         将dict或者包含两个元素的元组列表转换成url参数。
                                            例如 字典{'name':'wklken','pwd':'123'}将被转换为"name=wklken&pwd=123"
* `urllib.pathname2url(path)`               将本地路径转换成url路径
* `urllib.url2pathname(path)`               将url路径转换成本地路径
* `urllib.urlretrieve(url[,filename[,reporthook[,data]]])`  下载远程数据到本地
        filename：指定保存到本地的路径（若未指定该，urllib生成一个临时文件保存数据）
        reporthook：回调函数，当连接上服务器、以及相应的数据块传输完毕的时候会触发该回调
        data：指post到服务器的数据
* `rulrs = urllib.urlopen(url[,data[,proxies]])`     抓取网页信息，[data]post数据到Url,proxies设置的代理
* `urlrs.readline()`    跟文件对象使用一样
* `urlrs.readlines()`   跟文件对象使用一样
* `urlrs.fileno()`      跟文件对象使用一样
* `urlrs.close()`       跟文件对象使用一样
* `urlrs.info()`        返回一个httplib.HTTPMessage对象，表示远程服务器返回的头信息
* `urlrs.getcode()`     获取请求返回状态HTTP状态码
* `urlrs.geturl()`      返回请求的URL

## urllib2模块：   
* 1、基本用法

> * import urllib2
> * respose = urllib2.openurl('www.baidu.com').read()
> * request = urllib2.Request('www.baidu.com')
> * respose = urllib2.urlopen(request).read()

* 2、模拟POST请求
    
    查看Request的帮助help(urllib2.Request) 中发现，它的__init__ 构造函数是这样声明的
>__init__(self, url, data=None, headers={}, origin_req_host=None, unverifiable=False)

从声明上来看POST 的数据可以放到data 中，且我们还可以通过headers 设置http的请求头参数

> * import urllib
> * import urllib2
> * values = {}
> * values['username'] = "God"
> * values['password'] = "XXXX"
> * data = urllib.urlencode(values)  # 使用了urllib库中的urlencode方法
> * url = "http://xxxx.xxxxx/login"
> * request = urllib2.Request(url,data)
> * response = urllib2.urlopen(request)
> * print response.read()

* 3、设置HTTP请求头

通过headers参数修改http请求头的一些信息
> * import urllib
> * import urllib2
> * values = {}
> * values['username'] = "God"
> * values['password'] = "XXXX"
> * data = urllib.urlencode(values) 
> * url = "http://xxxx.xxxxx/login"
> * headers = {'User-Agent':'ozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0','Content-Type':'text/html; charset=utf-8','Referer':'http://www.baidu.com/'}
> * request = urllib2.Request(url,data,headers)
> * response = urllib2.urlopen(request)
> * print response.read()

## urlparse模块：    
    
    
## re模块：
* `import re`                           #导入re模块
* `re.compile(pattren, flags=0)`        #编译一个匹配正则表达式，返回一个匹配对象
* `re.match(pattern, string, flags=0)`  #利用正则表达式匹配一个字符串，如果匹配到返回匹配到的对象，如果没有则返回空
* `re.search(pattern, string, flags=0)`             
* `re.findall(pattern, string, flags=0)`
* `re.sub(pattern, repl, string, count=0)`  #将字符串中匹配正则表达式的部分替换为其他值
* `re.split(pattern, string, maxsplit=0)`
* `re.purge()`                              #Clear the regular expression cache