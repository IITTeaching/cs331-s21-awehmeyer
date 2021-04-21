class MultiQueue:
  
       class Node:
           def __init__(self, val, next=None):
               self.val = val
               self.next = next
  
       def __init__(self, num_queues=3):
           self.num_queues = num_queues
           self.lengths = [0] * num_queues
           self.heads = [None] * num_queues
           self.tails = [None] * num_queues
  
       def enqueue(self,item):   
            min = self.lengths[0]
            index = 0
            for i in range(0, len(self.lengths)):
                if self.lengths[i] < min:
                    index = i
                    min = self.lengths[i]

            cur_head = self.heads[index]
            cur_tail = self.tails[index]

            n = MultiQueue.Node(item, None)
            if cur_tail:
                cur_tail.next = n
            else:
                cur_head = n
            cur_tail = n

            self.heads[index] = cur_head
            self.tails[index] = cur_tail
            self.lengths[index] += 1

       def dequeue(self):
            assert(self)
            maxval = self.lengths[0]
            index = 0
            for i in range(0, len(self.lengths)):
                if self.lengths[i] > maxval:
                    index = i
                    maxval = self.lengths[i]
                    
            cur_head = self.heads[index]
            cur_tail = self.tails[index]

            assert(cur_head) ### not empty
            n = cur_head
            cur_head = cur_head.next
            if n == cur_tail:
                cur_tail = None
            
            self.heads[index] = cur_head
            self.tails[index] = cur_tail
            self.lengths[index] -= 1

            return n.val

       def __len__(self):
           return sum(self.lengths)
  
       def __bool__(self):
           return len(self) > 0
  
       def __str__(self):
           return self.__repr__()
  
       @staticmethod
       def listrepr(head):
           c = head
           s = []
           while c:
               s.append(str(c.val))
               c = c.next
           return "[" + ",".join(s) + "]"
  
       def __repr__(self):
           return "\n".join([ MultiQueue.listrepr(self.heads[i]) for i in range(self.num_queues) ])


m = MultiQueue()
for i in range(7):
    m.enqueue(i)

print(m)
print(m.dequeue())
print(m)