import datetime
import threading

def retrieve_data(threadNum):
    # Add your implementation here
    None

if __name__ == '__main__':
    dbStore = DBStore()
    cacheStore = CacheStore()

    # Add your initialization code here

    start = datetime.datetime.now()

    threads = [None] * 10
    for i in range(10):
        thread = threading.Thread(target = retrieve_data, args = (i, ))
        thread.start()
        threads[i] = thread

    for thread in threads:
        thread.join()

    print "Total time %f seconds" % (datetime.datetime.now() - start).total_seconds()
