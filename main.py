# import threading
# from my_watchdog import OnMyWatch
# from my_scheduler import do_schedule
# import logging


# def sample():
#     return None

# if __name__ == '__main__':
#     watch = OnMyWatch()
#     t1 = threading.Thread(target=watch.run())
#     t2 = threading.Thread(target=do_schedule())


# t1.start()
# t2.start()
# t1.join()
# t2.join()

import schedule
import time

def job():
    print("Hello, World!")

schedule.every().minute.at(":10").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    














