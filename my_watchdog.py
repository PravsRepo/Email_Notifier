import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from my_scheduler import decide_flag
import schedule

 
 
class OnMyWatch:
    # Set the directory on watch
    watchDirectory = "C:\\Users\\LEAP\\send_mail\\data"
 
    def __init__(self):
        self.observer = Observer()
        print("Watchdog Initiated")
 
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(60)
                
        except:
            self.observer.stop()
            print("Observer Stopped")
 
        self.observer.join()
 
 
class Handler(FileSystemEventHandler):
 
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            print(f"Event type: {event.event_type}")
            print(f"New file created: {event.src_path}")

        elif event.event_type == 'modified':
            # Event is modified, you can process it now
            flag = True
            print("Watchdog received modified event - % s." % event.src_path)
            # decide_flag(event.src_path)
            return event.src_path


def run_watchdog():
    watch = OnMyWatch()
    watch.run()

# schedule.every().minute.at(":10").do(run_watchdog)
# schedule.every().day.at("12:10").until("10:00").do(watch.run())

# while True:
#     schedule.run_pending()
#     time.sleep(60)