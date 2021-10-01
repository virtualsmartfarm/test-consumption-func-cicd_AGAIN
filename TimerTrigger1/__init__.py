import datetime
import logging

import azure.functions as func
import pytz

def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    def is_dst(datetime_now, timezone):
        aware_dt = timezone.localize(datetime_now)
        return aware_dt.dst() != datetime.timedelta(0,0)

    victorian_timezone = pytz.timezone("Australia/Melbourne")

    logging.info(datetime.datetime.now())
    is_dst(datetime.datetime.now(), victorian_timezone)
    
    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
