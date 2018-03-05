from collections import Counter


if __name__ == '__main__':
    a = ['beijing','shanghai','chengdu','beijing','hangzhou','hanzhou','guangzhou','shanghai','beijing']
    morewords = ['beijing','guangzhou','hangzhou','beijing','chengdu']

    c_a = Counter(a)
    print(c_a.most_common(1))

    for word in morewords:
        c_a[word] += 1

    print(c_a)