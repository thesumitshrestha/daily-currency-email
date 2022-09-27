from apscheduler.schedulers.blocking import BlockingScheduler
from currency_scapper import send_email

sched = BlockingScheduler()


@sched.scheduled_job('interval', minutes=1)
def timed_job():
    print('This job is run every weekday at 11 AM.')
    send_email()


sched.start()
