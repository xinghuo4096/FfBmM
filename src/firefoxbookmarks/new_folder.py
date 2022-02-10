import time
import uuid
from random import Random

from firefoxbookmarks.MozPlaceContainer import MozPlaceContainer


def getguid(name):
    """
        UUID主要有五个算法,也就是五种方法来实现:

        uuid1()——基于时间戳 由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性, 但MAC的使用同时带来安全性问题,局域网中可以使用IP来代替MAC。 

        uuid2()——基于分布式计算环境DCE(Python中没有这个函数) 算法与uuid1相同,不同的是把时间戳的前4位置换为POSIX的UID。 实际中很少用到该方法。 

        uuid3()——基于名字的MD5散列值 通过计算名字和命名空间的MD5散列值得到,保证了同一命名空间中不同名字的唯一性, 和不同命名空间的唯一性,但同一命名空间的同一名字生成相同的uuid。 

        uuid4()——基于随机数 由伪随机数得到,有一定的重复概率,该概率可以计算出来。 
        
        uuid5()——基于名字的SHA-1散列值 算法与uuid3相同,不同的是使用 Secure Hash Algorithm 1 算法 

    """
    u1 = uuid.uuid1()
    x = uuid.uuid3(u1, name)
    a = Random()

    return str(x)[24:]


def new_folder(name, index, id) -> MozPlaceContainer:

    sdt = now_time()    
    folder = MozPlaceContainer(getguid(name), name, index, sdt, sdt, id, 2,
                               'text/x-moz-place-container', '', [])
    return folder


def now_time():
    t = time.time()
    sdt = int(t * pow(10, 6))
    return sdt
