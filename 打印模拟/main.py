from Queue import Queue
import random
from printer import Printer
from task import Task

# 随机判断是否有作业产生
def newPrintTask():
    num = random.randint(0, 180)
    if num == 1:
        return True
    else:
        return False


def simulation(numSeconds, pages) -> int:
    labprinter = Printer(pages)
    printQueue = Queue()
    waitingTimes = []
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)
        if (not labprinter.bush()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)

        labprinter.tick()

    avgWaitTime = sum(waitingTimes) / len(waitingTimes)
    return f'打印机完成了{len(waitingTimes)}个任务平均用时{round(avgWaitTime,2)}秒，还有{printQueue.size()}个任务在等待。'


def main():
    for i in range(10):
        print(simulation(3600, 5))


if __name__ == '__main__':
    main()

'''
一个具体的实例配置如下:
一个实验室，在任意的一个小时内，大约有10名学生在场，
这一小时中，每人会发起2次左右的打印，每次1～20页
打印机的性能是:
以草稿模式打印的话，每分钟10页，
以正常模式打印的话，打印质量好，但速度下降为每分钟5页。

问题是:怎么设定打印机的模式，让大家都不会等太久的前提下尽量提高打印质量?
这是一个典型的决策支持问题，但无法通过规则直接计算
令我们要用一段程序来模拟这种打印任务场景，然后对程序运行结果进行分析，以支持对打印机模式设定的决策。

'''
