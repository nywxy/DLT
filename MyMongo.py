import pymongo
import urllib.request
from DLTNum import *
from calfunc import *
import time
import threading

#-----------------获取数据个位-------------------------------
#设置每年有多少期的数据
termEveyYear={
    '13':154,
    '14':152,
    '15':154,
    '16':153,
    '17':154,
    '18':153,
}

#计算a期与b期之间的期差
#a期晚于b期
def countTermSub(aTermID,bTermID):
    #首先对期数数据进行分割
    aYear = aTermID[:2]
    aTerm = aTermID[2:]
    bYear = bTermID[:2]
    bTerm = bTermID[2:]
    iv = 0
    for i in range(int(aYear)-int(bYear)):
        iv += termEveyYear[str(int(bYear)+i)]
    res = int(aTerm)-int(bTerm) +iv
    return res
#data为列表，返回列表数据元素的个位
def getDatasRight(data):
    res = []
    for d in data:
        res.append(Right(d))
    return res



class myDb:
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost',port=27017)
        #create or connect to jxluckynum database
        self.db = self.client['jxdltnum']
        #connect to TermTable
        self.tterm = self.db['TermTable']
        #if there is no data in TermTable,get data from internet and insert them
        self.tlucky = self.db['LuckyTable']
        self.tinterval = self.db['DataInterval']

        #最新开奖信息表
        self.__termlist = []
        self.isUpdate = False
        self.isOnline = True

        #待更新的开奖信息列表
        self.__updateInfo = []
        #计算函数起始信息，每页计算出来多少组数，主要根据这两个值确定，结束应为6的倍数
        self.__funcStart = 1
        self.__funcEnd = 435

        #程序初始化时需要先获取最新数据信息，如果获取不到就用以往数据
        self.getLastestTermData()
        if self.__termlist.__len__() < 1:
            print("获取最新数据失败，启用离线模式")
            self.isOnline = False

    def getUpdateInfo(self):
        return self.__updateInfo

    def getFuncStart(self):
        return self.__funcStart

    def getFuncEnd(self):
        return self.__funcEnd

    def setFuncStart(self,val):
        self.__funcStart = val

    def setFuncEnd(self,val):
        self.__funcEnd = val

    #删除开奖记录表数据
    def clearTermTable(self):
        self.tterm.remove({})

    #删除计算表
    def clearLuckyTable(self):
        self.tlucky.remove({})

    #删除概率周期表
    def clearDataInterval(self):
        self.tinterval.remove({})

    def getLastestTermData(self):
        self.__termlist = self.__getAllTerm()

    #-------------------开奖记录表相关------------------------------------
    #创建开奖记录表
    def createTermTable(self):
        #首先从网络上下载最新的开奖信息表
        #然后看数据库中是否有数据，
        #没有数据的话就创建表并填充数据
        if self.tterm.count() == 0 :
            if self.isOnline == False:
                print("无法使用缓存数据，请连接网络更新后再试！")
                return
            print('正在生成开奖信息表........')
            start = time.time()
            self.tterm.insert(self.__termlist)
            end = time.time()
            print('生成开奖信息数据完毕，用时:',end-start)
        else:
            if self.isOnline:
                self.isUpdate = True


    #更新开奖信息表
    def updataTermTable(self):
        if self.isUpdate:
            # 已经生成过开奖数据的话，就根据数据库中的最后一条数据与下载的最新数据进行比对，如果期数一致
            # 则退出，否则就提示更新，并自动进行更新
            dblastest = self.tterm.find().sort('termID', -1).limit(1)
            if dblastest['termID'] == self.__termlist[len(self.__termlist) - 1]:
                print("数据已是最新，无需更新")
            else:
                for index in range(len(self.__termlist)):
                    # 为快速查找到需更新的数据，termlist要倒着查
                    self.__termlist.reverse()
                    if self.__termlist[index]['termID'] != dblastest['termID']:
                        self.__updateInfo.append(self.__termlist[index])
                    else:
                        break
                if self.__updateInfo.__len__() > 0:
                    print("开始更新数据......")
                    start = time.time()
                    self.tterm.insert_many(self.__updateInfo.__dict__)
                    end = time.time()
                    self.isUpdate = False
                    print("数据更新完成，用时：", end - start)

    #从网站上获取所有的开奖数据
    def __getAllTerm(self,url="http://www.17500.cn/getData/dlt2.TXT"):
        page = urllib.request.urlopen(url)
        html = page.read()
        data = html.decode('utf-8')
        return self.__str2term(data)

    #获取到的开奖数据转换成开奖信息列表
    def __str2term(self, data):
        datas = data.split("\n")
        terms = []
        try:
            for d in datas:
                di = d.split(" ")
                termdata = term()
                termdata.termID = di[0]
                termdata.red = list(map(int,di[2:7]))
                termdata.blue = list(map(int,di[7:9]))
                terms.append(termdata.__dict__)
        finally:
            return terms

    #获取数据库中开奖数据
    #scope为开奖的期数，取多少期的数据
    def getTermDatas(self,scope):
        datas = self.tterm.find().sort("termID",-1).limit(scope+1)
        result = []
        for data in datas:
            result.append(data)
        result.sort(key=lambda x:x['termID'])
        return result


    #--------------------------概率计算表相关----------------------------

    # 调用函数计算每页所有的数据，并返回
    def __calFuncByGroup(self,funcStart,funcEnd,red,blue):
        result = []
        for x in range(funcStart,funcEnd+1):
            result.append(eval("jxM%d"%x)(red,blue))
        return result


    # 每组数据计算方法函数，函数在计算过程中可根据计算的数据去重个数及命中结果生成概率周期表的原始数据
    # page为哪一页
    # funcStart 计算函数开始为哪个函数
    # funcEnd 计算函数结束为哪个函数
    # termdata应该为本期未开奖的数据
    # resultdata为上期开奖结果
    # 私有方法，类外不可调用
    def __groupCal(self, page, funcStart, funcEnd, termdata, red,blue):
        pageData = []
        groupNum = int(funcEnd / 5)
        onePageNum = self.__calFuncByGroup(funcStart, funcEnd, red, blue)
        for g in range(groupNum):
            # 概率性数据集表
            calRes = luckyNum()
            calRes.moduleID = page
            calRes.termID = termdata['termID']
            calRes.groupID = g + 1
            calRes.dataID = calRes.termID + '{:0>3d}{:0>3d}'.format(calRes.moduleID, calRes.groupID)
            calRes.num = onePageNum[g * 5:(g + 1) * 5]
            calRes.numSize = len(list(set(calRes.num)))
            if termdata['red'] == []:
                calRes.rightNum = -1
            else:
                termRightData = getDatasRight(termdata['red'])
                # 开奖号码尾数去重
                termRightData = list(set(termRightData))
                calRes.rightNum = 0
                for val in termRightData:
                    if val in list(set(calRes.num)):
                        calRes.rightNum += 1
            pageData.append(calRes.__dict__)
            # 创建数据概率周期表基本数据
            # 待基本数据创建完成后周期表再进行自我计算出周期差
            if calRes.numSize >= 3 :
                if (calRes.rightNum >= 3 or calRes.rightNum == 0) or (termdata['red']==[]):
                    dataIn = dataInterval()
                    dataIn.dataID = calRes.dataID
                    dataIn.termID = calRes.termID
                    dataIn.moduleID = calRes.moduleID
                    dataIn.groupID = calRes.groupID
                    dataIn.numSize = calRes.numSize
                    dataIn.rightNum = calRes.rightNum
                    self.tinterval.insert(dataIn.__dict__)
        return pageData

    #--------创建表多少期多少页数据-----------------
    def createLuckyTable(self,scope,page):
        datas = self.getTermDatas(scope)
        if len(datas) < 1:
            print("请先生成开奖信息表！.......")
            return
        if page > 1 and page < 36:
            for index in range(len(datas)):
                for i in range(len(datas[index]['red'])):
                    datas[index]['red'][i] += page-1
                    if datas[index]['red'][i] >35:
                        datas[index]['red'][i] -= 35
        for index in range(len(datas)):
            if index >= 1:
                pageData = self.__groupCal(page, self.__funcStart, self.__funcEnd, datas[index],
                                           datas[index - 1]['red'],datas[index-1]['blue'])
                if len(pageData) > 0:
                    self.tlucky.insert_many(pageData)

    # --------创建表多少期多少页数据,包含数据翻滚-----------------
    def createLuckyTableWithZone(self, scope, page,zone,redNum):
        datas = self.getTermDatas(scope+zone-1)
        if len(datas) < 1:
            print("请先生成开奖信息表！.......")
            return
        #首先计算出算到第几组了，要不要翻滚上面的数据
        izone = int((page-1)/redNum)
        ipage = page%redNum
        if ipage ==0:
            ipage = 35
        #每一组里的第一页均为原始值
        for index in range(len(datas)):
            if index >= zone:
                # 定义一组红球和蓝球，每次回滚或自增时都需要改变
                red = []
                blue = []
                for r in datas[index-izone-1]['red']:
                    r += ipage-1
                    if r > 35:
                        r -= 35
                    red.append(r)
                blue = datas[index-izone-1]['blue']
                pageData = self.__groupCal(page,self.__funcStart,self.__funcEnd,datas[index],red,blue)
                if len(pageData) > 0:
                    self.tlucky.insert_many(pageData)

    #获取所有的计算统计数据
    def getAllLuckyNum(self):
        luckynums = self.tlucky.find()
        return luckynums

    #--------------概率周期表相关------------------
    #表的创建在生成数据表的时候同步进行，本表只存储5中5,5中4,5中3,5中0,4中4,4中3,及4中0,3中3及3中0的信息

    def getAllDataInterval(self):
        return self.tinterval.find().sort('dataID')

    #########################################################
    ########下面这段函数为计算相同数据周期之间的距离####################
    def updateInterval(self,dataIn):
        '''
        datas = self.tinterval.find({'moduleID':dataIn['moduleID'],
                                             'groupID':dataIn['groupID'],
                                             'numSize':dataIn['numSize'],
                                             'rightNum':dataIn['rightNum']}).sort('dataID')
        if datas.count() > 0:
            mod = []
            for data in datas:
                mod.append(data)

            #计算周期间隔
            #最早一个数据的周期间隔不计算，为9999
            #开线程进行处理
            lock = threading.Lock()
            def run(mod,index):
                lock.acquire()
                try:
                    if mod[index]['last55'] != -1 or mod[index]['last54'] != -1 \
                            or mod[index]['last53'] != -1 or mod[index]['last50'] != -1 \
                            or mod[index]['last44'] != -1 or mod[index]['last43'] != -1 \
                            or mod[index]['last40'] != -1 or mod[index]['last33'] != -1 \
                            or mod[index]['last30'] != -1:
                        return
                    else:
                        if index == 0:
                            mod[index]['last%d%d' % (mod[index]['numSize'], mod[index]['rightNum'])] = 9999
                        elif index > 0:
                            mod[index]['last%d%d' % (mod[index]['numSize'], mod[index]['rightNum'])] = \
                                countTermSub(mod[index]['termID'], mod[index - 1]['termID'])
                        self.tinterval.update({'dataID': mod[index]['dataID']},
                                              {'$set': {'last%d%d' % (mod[index]['numSize'],
                                                                      mod[index]['rightNum']): mod[index]['last%d%d' % (
                                                  mod[index]['numSize'], mod[index]['rightNum'])]}})
                        print("\033[1;33m更新：\033[3;32m",mod[index]['dataID'],'last%d%d' % (mod[index]['numSize'],mod[index]['rightNum']),
                              "=", mod[index]['last%d%d' % (mod[index]['numSize'], mod[index]['rightNum'])])
                finally:
                    lock.release()
            for index in range(len(mod)):
                T = threading.Thread(target=run,args=(mod,index))
                T.start()
                T.join()
        '''
        ########注释掉可缩短存储时间，但是数据间隔无法得出##############
        ########################################################

    def getIntervalDataByCondition(self,condition):
        datas = self.tinterval.find(condition)
        return datas
