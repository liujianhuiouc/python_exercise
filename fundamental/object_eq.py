


class Data(object):
    def __init__(self, id):
        self._id = id

    def __eq__(self, other):
        return self._id == other._id

    def __repr__(self):
        return "id %s" % self._id

    def __hash__(self):
        return self._id

if __name__ == '__main__':
    data_set = set()
    data1 = Data(1)
    data2 = Data(2)
    data_set.add(data1)
    data_set.add(data2)
    print(data1 is data2)
    print(data1 == data2)
    print(data_set)