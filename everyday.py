# -*- coding: utf-8 -*-

import os
import run
from apscheduler.schedulers.blocking import BlockingScheduler

def tick():
    run.run()

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(tick, 'cron', hour='5-22', minute=27)
    print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C    '))

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass