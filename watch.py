import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
class MyHandler(FileSystemEventHandler):
	
	def on_modified(self,event):
		print("update detected")
		
#start of program  
#watch.py path or watch.py
if __name__ == "__main__":
	logging.basicConfig(level=logging.INFO,
		format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
	# take in list of paths.  If none given, watch CWD
	print(sys.argv[1])
	paths = open(sys.argv[1], 'r') if len(sys.argv) > 1 else '.'
	observer = Observer()
	# Empty list of observers .
	observers = []
    #path = sys.argv[1] if len(sys.argv) > 1 else '.' # directory to look
	# iterate through paths and attach observers
	event_handler = MyHandler()
	for line in paths:
    # convert line into string and strip newline character
		targetPath = str(line).rstrip()
		# Schedules watching of a given path
		observer.schedule(event_handler, targetPath, recursive=True)
		# Add observable to list of observers
		observers .append(observer)  
    
	observer.start()
	try:
		while True:
			# poll every second
			time.sleep(1)
	except KeyboardInterrupt:
		for o in observers:
			o.unschedule_all()
			# stop observer if interrupted
			o.stop()
	for o in observers:
		# Wait until the thread terminates before exit
		o.join()