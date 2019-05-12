
def average():
    #print("first average called")
    sum = 0.0
    cnt = 0
    while 1:
        print("average before yield")
        age = yield
        if age is None:
            break;
        sum += age
        cnt += 1

    return sum / cnt


def average_group(results, key):
    while 1:
        print('before average_group')
        results[key] = yield from average()
        print('after average_group %s' % results[key])


def main(data):
    results = {}
    for key, values in data.items():
        group = average_group(results, key)
        next(group)
        [group.send(x) for x in values]
        group.send(None)


    for key, value in results.items():
        print('key: %s, value: %s' % (key, value))


if __name__ == '__main__':
    data = {
        'children': [1, 2, 3],
        'adult': [30, 31, 32]
    }
    main(data)