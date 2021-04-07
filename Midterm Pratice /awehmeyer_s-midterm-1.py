def pickevery(l,n):
    a = []
    cur = self.head.next
    for i in range(0, self.length, n):
        a.append(cur.val)
        for j in range(0, n):
            cur = cur.next
    return a