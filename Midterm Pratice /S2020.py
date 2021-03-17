def build_index(doc):
    d = {}
    for string in doc:
        words = d[string].split()
        for w in words:
            if w in d:
                if string in d[w]:
                    d[w][string] += 1
                else:
                    d[w][string] = 1
            else:
                d[w] = {string:1}
    return d

def search_index(index, query):
    words = query.split()
    docs = {}
    for w in words:
        if w in index:
            for d in index[w]:
                if d in docs:
                    docs[d] += index[w][d]
                else:
                    docs[d] = index[w][d]
    return docs

### No idea what is going on ###