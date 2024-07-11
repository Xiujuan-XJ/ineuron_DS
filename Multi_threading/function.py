def test():
    print('this is my multiprocessing program')
    
def square(n):
    return n**2

def producer(q): #queue up
    for i in ['my','name','is','xiu','juan']:
        q.put(i)
        
def consume(q): #eliminate
    while True:
        item=q.get()
        if item is None:
            break
        print(item)
        
def square1(index,value):
    value[index]=value[index]**2


def sender(conn,msg): # pipe will set up the connection
    for i in msg:
        conn.send(i)
    conn.close()
    
def receive(conn):
    while True:
        try:
            msg=conn.recv()
        except Exception as e:
            print(e)
            break
        print(msg)