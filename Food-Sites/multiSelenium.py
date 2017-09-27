import time
import queue as Queue
import urllib
import threading
from selenium import webdriver
from bs4 import BeautifulSoup

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
        "http://ibm.com", "http://apple.com"]
queue = Queue.Queue()
out_queue = Queue.Queue()

class Login_Driver(threading.Thread):
#def __init__(self, driver):
    def __init__(self, queue, out_queue, driver):
        threading.Thread.__init__(self)
        self.queue = queue
        self.out_queue = out_queue
        self.driver = driver
        print("In init first class..")
    def run(self):
        while True:
            #grabs host from queue
            host = self.queue.get()
            #grabs urls of hosts and then grabs chunk of webpage
            self.driver.get(host)
            chunk = self.driver.page_source
            #place chunk into out queue
            self.out_queue.put(chunk)
            #signals to queue job is done
            print(self.driver.title)
            self.queue.task_done()
class Poster(threading.Thread):
    def __init__(self, out_queue, driver):
        threading.Thread.__init__(self)
        self.out_queue = out_queue
        self.driver = driver
        print("In init a second class..")
    def run(self):
        while True:
            #grabs host from queue
            chunk = self.out_queue.get()
            #parse the chunk
            soup = BeautifulSoup(chunk)
            print(soup.findAll(['title']))
            #signals to queue job is done
            print(self.driver.name)
            self.out_queue.task_done()
start = time.time()
def main():
    #spawn a pool of threads, and pass them queue instance
    for i in range(5):
        driver = webdriver.Chrome('/Users/cloudy/anaconda/lib/python3.6/site-packages/selenium/chromedriver')
        t = Login_Driver(queue, out_queue, driver)
        t.setDaemon(True)
        t.start()
        print("Started webdriver: --- "+str(i)+" --- from main")
    print("All started")
    time.sleep(3)
    #populate queue with data

    for host in hosts:
        queue.put(host)
        print("Opening website: "+host)
    print("All sites passed for opening..")
    time.sleep(3)
    for i in range(5):
        dt = Poster(out_queue, driver)
        dt.setDaemon(True)
        dt.start()
        print("Starting second class/title and name beautifull soup and webdriver: --- "+str(i)+" --- from main")
    print("Started secound class..")
    time.sleep(3)
    #wait on the queue until everything has been processed
    queue.join()
    out_queue.join()
    print("out_queue.join()")
main()
print("Elapsed Time: %s" % (time.time() - start))