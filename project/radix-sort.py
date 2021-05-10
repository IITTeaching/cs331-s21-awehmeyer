import urllib
import urllib.request

### Submethod to accept a string ###
def radix_a_string(words):
    wordsascii = words.encode('ascii','replace')
    wordsbytes = wordsascii.split()
    return radix_byte_list(wordsbytes)

### Submethod to accept a book url ###
def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    bookbytes = bookascii.split()
    return radix_byte_list(bookbytes)

### Main sort method to implement radix sort ###
def radix_byte_list(btye_list):
    for i in range(0, 31): ###SET LENGTH OF WORDS###
        btye_list = toArray(toQueue(btye_list, i), len(btye_list))
    return btye_list

def get_digit(word, k):
    if k >= len(word):
        return 0 ### ascii code for 'NULL'
    else:
        return word[k]

def toQueue(arr, k):
    queue = [ [] for i in range(256) ]
    for i in range(0, len(arr)):
        digit = get_digit(arr[i], k)
        queue[digit].append(arr[i])
    return queue

def toArray(queues, number_of_values):
    nums = [ [] for i in range(number_of_values) ]
    index = 0
    for i in range(0, len(queues)):
        current_queue = queues[i]
        while len(current_queue) > 0:
            nums[index] = current_queue.pop(0)
            index += 1
    return nums


def test1():
    words = "g f e d c b a"
    byte_list = radix_a_string(words)
    for i in range(len(byte_list)-1):
        assert(byte_list[i] < byte_list[i+1])

def test2():
    radix_a_book()

def say_test(f):
    print(80 * "#" + "\n" + f.__name__ + "\n" + 80 * "#" + "\n")

def say_success():
    print("----> SUCCESS")

def main():
    for t in [test1, test2]:
        say_test(t)
        t()
        say_success()
    print(80 * "#" + "\nALL TEST CASES FINISHED SUCCESSFULLY!\n" + 80 * "#")

if __name__ == '__main__':
    main()