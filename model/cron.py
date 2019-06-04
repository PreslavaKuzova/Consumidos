from crontab import CronTab
import os, getpass

class Cron:

    path = os.path.dirname(os.path.abspath(__file__))
    user = getpass.getuser()

    @classmethod
    def start_cron_job_listen_for_emails(cls, receiver):
        cron = CronTab(user=cls.user)
        if not next(cron.find_command(f'python3 {cls.path}/listener {receiver}'), None):
            job = cron.new(command=f'python3 {cls.path}/listener {receiver}')
            job.minute.every(1)
            cron.write()
            print('cron job started')
