class Printer:
    def __init__(self, pmm):
        self.pagerate = pmm  # 打印速度
        self.currentTask = None  # 打印任务
        self.timeRemaing = 0  # 等待时间

    def tick(self):  # 打印机工作一秒
        if self.currentTask != None:
            self.timeRemaing = self.timeRemaing - 1
            if self.timeRemaing <= 0:
                self.currentTask = None

    def bush(self):  # 判断打印机是否忙
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaing = newTask.getPages() * 60 / self.pagerate
