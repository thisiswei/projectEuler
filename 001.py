def one():
    return sum(filter(lambda x: not x%3 or not x%5,list(range(1,1001))))
