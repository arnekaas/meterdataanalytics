import schedule
import time

def job():
    print("P1 read started...")
    execfile("process_p1_telegram.py") 

schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)