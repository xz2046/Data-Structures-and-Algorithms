def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos]) * pos

    return sum % tablesize


print(hash('abc', 11))
print(hash('acb', 11))

'''
【完美散列函数】特征：由任意长度的数据生成【唯一】长度固定的指纹，在一定数量范围内是可能的
【压缩性】：无穷大的数据也是这个
【易计算性】：得到哈希值容易，而反推元数据不可能
【抗修改性】：对原数据的微小变动，都会引起哈希值的极大改变
【抗冲突性】：找到对应同一个哈希的两个元数据是非常困难的
MD5函数：Message Digest将任何长度的数据变换为固定长为128位-16字节的摘要。
SHA 函数：Secure Hash Algorithm是另一组散列函数 SHA-0/1输出哈希值160位。SHA-256/224 输出256位，224位，还有512.384等。160位二进制相当于10的48次方，水分子数量是10的47次方，宇宙所有基本例子大约是72-87次方。
Python自带hashlib，包括了md5，sha1，sha224，sha256，sha384，sha512等6种哈希函数。

冲突解决：
【开放定址】
方法1：为冲突数据项再找一个空槽，从冲突槽开始向后遍历，没有的话再从头遍历-寻找空槽-开放定址法，open addressing
逐个槽寻找-linear probing线性探测。
在查找时，也要进行顺序查找，直到碰到空槽返回失败。
缺点：clustering连锁式影响其他数据项的插入
改进：跳跃式探测，例如步长改为+3；
【数据项链Chaining】
将槽扩大为容纳数据项集合/对数据项链表的引用
缺点：查找时需要遍历集合，查找时间会增加
'''
