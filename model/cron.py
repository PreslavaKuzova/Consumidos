from crontab import CronTab
import os, getpass

class Cron:
    path = os.path.dirname(os.path.abspath(__file__))
    user = getpass.getuser()

    @classmethod
    def start_cron_job(cls):
        cron = CronTab(user=cls.user)
        job = cron.new(command=f'python3 {cls.path}/listener')
        job.minute.every(1)
         
        cron.write()
        print('cron job started')
