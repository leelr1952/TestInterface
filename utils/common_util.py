class CommonUtil(object):
    def iscontain(self,str_one,str_two):
        '''
        判断一个字符串是否在另一个字符串中
        '''
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag