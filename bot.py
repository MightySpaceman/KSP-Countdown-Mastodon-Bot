import schedule
import time
import datetime
from datetime import datetime
from dateutil import relativedelta
from datetime import date
from mastodon import Mastodon

def post():
    d1 = date.today().strftime('%d/%m/%Y')
    d2 = '25/2/2023'

    # convert string to date object
    start_date = datetime.strptime(d1, "%d/%m/%Y")
    end_date = datetime.strptime(d2, "%d/%m/%Y")

     # Get the relativedelta between two dates
    delta = relativedelta.relativedelta(end_date, start_date)

    delta2 = start_date - end_date
    
    content = '(Functionality test)\n\n'
    content += 'Time until KSP 2 release:\n'
    content += f'{delta.months} months, {delta.days} days'
    content += f'\n\nT{delta2.days} DAYS'

    #   Set up Mastodon
    mastodon = Mastodon(
        access_token = 'ng1xe9-rf25zYLyqg2XcoSeWZx7uuAjpfn9g-gI9Pf4', # Your Mastodon bot access key
        api_base_url = 'https://mstdn.social/' # Base URL of Mastodon instance of choice
    )

    mastodon.status_post(content) 


def job():
    print("Job run at:", time.ctime())

# Schedule the function to run at a specific time every day
schedule.every().day.at("7:10").do(post)

# Start the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)

