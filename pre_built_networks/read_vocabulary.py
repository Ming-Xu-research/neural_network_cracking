import collections


def read_vocabulary(filename, threshold=10000):
    vocabulary = collections.defaultdict(int)
    with open(filename) as f:
        for line in f.readlines():
            vocabs = line.strip('\n').split(' ')
            for vocab in vocabs:
                vocabulary[vocab] += 1
    return {k: v for k, v in vocabulary.items() if v > threshold}


if __name__ == '__main__':
    print(len(read_vocabulary('data/out_train.txt')))
    print(set(read_vocabulary('data/out_train.txt').keys()))
    print(set(read_vocabulary('data/out_train.txt').keys()) | set('abcdefg'))
