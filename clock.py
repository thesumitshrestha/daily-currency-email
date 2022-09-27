from apscheduler.schedulers.blocking import BlockingScheduler
from currency_scapper import send_email

sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10:45)
def scheduled_job():
    print('This job is run every weekday at 10:45 AM.')
    send_email()


sched.start()
