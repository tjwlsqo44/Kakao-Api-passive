import schedule
import _thinkcon, _wevity

def run():
    _wevity.cycle()
    _thinkcon.cycle()

schedule.every(12).hours.do(run)

def cron():
    while True:
        schedule.run_pending()