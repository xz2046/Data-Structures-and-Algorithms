import random


class Task:
    def __init__(self, time):
        self.timetamp = time  # 生成时间戳
        self.page = random.randint(1, 21)  # 随机生成任务页数

    def getStamp(self):
        return self.timetamp

    def getPages(self):
        return self.page

    def waitTime(self, currentTime):
        return currentTime - self.timetamp

