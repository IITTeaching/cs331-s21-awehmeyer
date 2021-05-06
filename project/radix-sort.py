import urllib
import urllib.request

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    print("Book to ASCII: STARTING")
    ascii_chars = book_to_words(book_url)
    print("Book to ASCII: DONE")
    print("Sorting: STARTING")
    for i in range(0, 31):
        ascii_chars = toArray(toQueue(ascii_chars, i), len(ascii_chars))
        print(f'{i/31 * 100}%')
    print("Sorting: DONE")
    return ascii_chars

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


### MAIN PROGRAM ###

#sort = radix_a_book()

### TEST CASES ###

def sort(words):
    print("Sorting: STARTING")
    for i in range(0, 31):
        words = toArray(toQueue(words, i), len(words))
        print(f'{i//31 * 100}%')
    print("Sorting: DONE")
    return words

words = [b'Gnd', b'Bnd', b'And', b'End', b'Dnd', b'Fnd', b'Bnd']
words = sort(words)
print(words)