import logging
import time
import os
import psutil
from logging.handlers import TimedRotatingFileHandler


def create_timed_rotating_log(path):
    logger = logging.getLogger("Rotating Log")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(path, when="m", interval=1, backupCount=5)
    logger.addHandler(handler)
    interval=int(input("Enter the Time Interal"))
    listOfProcObjects=[]
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            listOfProcObjects.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    logger.info(listOfProcObjects)
    print()
    time.sleep(interval)

if __name__ == "__main__":
    log_file=os.path.abspath("log.log")
    create_timed_rotating_log(log_file)
    print("Log file created")