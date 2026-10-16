import threading
def task():
 print("Thread ID:", threading.get_ident())
t1 = threading.Thread(target=task)
t1.start()
t1.join()