import random
from unittest import TestCase

################################################################################
# EXTENSIBLE HASHTABLE
################################################################################
class ExtensibleHashTable: ###should these be kv pairs???

    def __init__(self, n_buckets=1000, fillfactor=0.5):
        self.n_buckets = n_buckets
        self.fillfactor = fillfactor
        self.buckets = [None] * n_buckets
        self.nitems = 0

    def expand(self):
        olddata = self.buckets
        newdata = [None] * 2 * self.n_buckets
        self.buckets = newdata
        self.n_buckets *= 2
        self.nitems = 0
        for el in olddata:
            self.__setitem__(el[0], el[1])

    def find_bucket(self, key): ### return the index of the bucket
        h = hash(key) % self.n_buckets
        for i in range(h, self.n_buckets):
            if self.buckets[i][0] == key:
                return i
        for i in range(0, h):
            if self.buckets[i][0] == key:
                return i
        raise KeyError

    def __getitem__(self, key):
        return self.buckets[self.find_bucket(key)][1]

    def __setitem__(self, key, value):
        if self.nitems / self.n_buckets > self.fillfactor:
            self.expand()
        h = hash(key) % self.n_buckets
        if self.buckets[h]:
            print(self.buckets[h])
            for i in range(h, self.n_buckets):
                if not self.buckets[i]:
                    self.buckets[i] = (key, value)
                    self.nitems += 1
                    return
            for i in range(0, h):
                if not self.buckets[i]:
                    self.buckets[i] = (key, value)
                    self.nitems += 1
                    return       
        else:
            self.buckets[h] = (key, value)
            self.nitems += 1

    def __delitem__(self, key):
        index = self.find_bucket(key)
        self.buckets[index] = (None, None) ##special item telling you something was there
        self.nitems -= 1

    def __contains__(self, key):
        try:
            _ = self[key]
            return True
        except:
            return False

    def __len__(self):
        return self.nitems

    def __bool__(self):
        return self.__len__() != 0

    def __iter__(self):
        for i in range(0, self.n_buckets):
            if self.buckets[i]:
                yield self.buckets[i]

    def keys(self):
        return iter(self)

    def values(self):
        for i in range(0, self.n_buckets):
            if self.buckets[i]:
                yield self.bucket[i][1]

    def items(self):
        for i in range(0, self.n_buckets):
            if self.buckets[i]:
                yield self.buckets[i]

    def __str__(self):
        return '{ ' + ', '.join(str(k) + ': ' + str(v) for k, v in self.items()) + ' }'

    def __repr__(self):
        return str(self)

################################################################################
# TEST CASES
################################################################################
# points: 20
def test_insert():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100000)

    for i in range(1,10000):
        h[i] = i
        tc.assertEqual(h[i], i)
        tc.assertEqual(len(h), i)

    random.seed(1234)
    for i in range(1000):
        k = random.randint(0,1000000)
        h[k] = k
        tc.assertEqual(h[k], k)

    for i in range(1000):
        k = random.randint(0,1000000)
        if i == 28:
            print("found")
        h[k] = "testing"
        tc.assertEqual(h[k], "testing")

# points: 10
def test_getitem():
    tc = TestCase()
    h = ExtensibleHashTable()

    for i in range(0,100):
        h[i] = i * 2

    with tc.assertRaises(KeyError):
        h[200]


# points: 10
def test_iteration():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100)
    entries = [ (random.randint(0,10000), i) for i in range(100) ]
    keys = [ k for k, v in entries ]
    values = [ v for k, v in entries ]

    for k, v in entries:
        h[k] = v

    for k, v in entries:
        tc.assertEqual(h[k], v)

    tc.assertEqual(set(keys), set(h.keys()))
    tc.assertEqual(set(values), set(h.values()))
    tc.assertEqual(set(entries), set(h.items()))

# points: 20
def test_modification():
    tc = TestCase()
    h = ExtensibleHashTable()
    random.seed(1234)
    keys = [ random.randint(0,10000000) for i in range(100) ]

    for i in keys:
        h[i] = 0

    for i in range(10):
        for i in keys:
            h[i] = h[i] + 1

    for k in keys:
        tc.assertEqual(h[k], 10)

# points: 20
def test_extension():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100,fillfactor=0.5)
    nitems = 10000
    for i in range(nitems):
        h[i] = i

    tc.assertEqual(len(h), nitems)
    tc.assertEqual(h.n_buckets, 25600)

    for i in range(nitems):
        tc.assertEqual(h[i], i)


# points: 20
def test_deletion():
    tc = TestCase()
    h = ExtensibleHashTable(n_buckets=100000)
    random.seed(1234)
    keys = [ random.randint(0,1000000) for i in range(10) ]
    for k in keys:
        h[k] = 1

    for k in keys:
        del h[k]

    tc.assertEqual(len(h), 0)
    with tc.assertRaises(KeyError):
        h[keys[0]]

    with tc.assertRaises(KeyError):
        h[keys[3]]

    with tc.assertRaises(KeyError):
        h[keys[5]]

################################################################################
# TEST HELPERS
################################################################################
def say_test(f):
    print(80 * "*" + "\n" + f.__name__)

def say_success():
    print("SUCCESS")

################################################################################
# MAIN
################################################################################
def main():
    for t in [test_insert,
              test_iteration,
              test_getitem,
              test_modification,
              test_deletion,
              test_extension]:
        say_test(t)
        t()
        say_success()

if __name__ == '__main__':
    main()
