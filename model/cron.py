from crontab import CronTab

class Cron:
    @classmethod
    def start_cron_job(cls):
        cron = CronTab(user='ilina')
        job = cron.new(command='python3 /home/ilina/Python-101/Consumidos/model/listener')
        job.minute.every(1)
         
        cron.write()
        print('cron job started')
