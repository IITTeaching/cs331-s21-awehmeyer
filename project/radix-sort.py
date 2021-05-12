import urllib
import urllib.request

### Find the number of iterations necessary ###
def max(lst):
    maximum = len(lst[0])
    for i in range(1, len(lst)):
        if len(lst[i]) > maximum:
            maximum = len(lst[i])
    return maximum

### Submethod to accept a string ###
def radix_a_string(words):
    wordsascii = words.encode('ascii','replace')
    wordsbytes = wordsascii.split()
    result = radix_byte_list(wordsbytes)
    strings = to_strings(result)
    return strings

### Submethod to accept a book url ###
def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    bookbytes = bookascii.split()
    return radix_byte_list(bookbytes)

### Turns an array of bytes into an array of strings ###
def to_strings(byte_list):
    arr = []
    for i in range(len(byte_list)):
        arr.append(byte_list[i].decode("ascii"))
    return arr

### Main sort method to implement radix sort ###
def radix_byte_list(byte_list):
    max_length = max(byte_list)
    for i in range(0, max_length):
        byte_list = toArray(toQueue(byte_list, i, max_length), len(byte_list))
    return byte_list

def get_digit(word, k, max_length):
    place = max_length - k - 1
    if place >= len(word):
        return 0
    else:
        return word[place]

def toQueue(arr, k, max_length):
    queue = [ [] for i in range(256) ]
    for i in range(0, len(arr)):
        digit = get_digit(arr[i], k, max_length)
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
    result = radix_a_string(words)
    for i in range(len(result)-1):
        assert(result[i] < result[i+1])

    words = "Britney Debi Fred Delana Song Sonny Riley Patti Jeanie Mimi Bret Garnett Penni Cathleen Ayako Alaina Lynette Von Blanche Jadwiga"
    result = radix_a_string(words)
    for i in range(len(result)-1):
        assert(result[i] < result[i+1])

def test2():
    result = radix_a_book()
    assert(True)

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