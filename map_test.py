
import ujson

from collections import Iterable

if __name__ == '__main__':
    results = list()
    map(lambda x: results.append(x[0]), [])
    results.append((123, 'aaa'))
    a = ujson.dumps([])
    print(a)
    aa = ujson.loads(a)
    print(isinstance(aa, Iterable))