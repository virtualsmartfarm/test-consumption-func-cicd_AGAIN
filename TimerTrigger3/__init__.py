import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    # from datetime import datetime
    vic_todays_date = datetime.datetime.now(
        pytz.timezone('Australia/Melbourne')).strftime("%Y-%m-%d")
    logging.info(vic_todays_date)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)
