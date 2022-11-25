import time
import datetime
from datetime import datetime
from dateutil import relativedelta
from datetime import date
from mastodon import Mastodon

    #   Set up Mastodon
 mastodon = Mastodon(
    access_token = 'ng1xe9-rf25zYLyqg2XcoSeWZx7uuAjpfn9g-gI9Pf4', # Your Mastodon bot access key
    api_base_url = 'https://mstdn.social/' # Base URL of Mastodon instance of choice
)

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

    mastodon.status_post(content) 
    
mastodon.status_post(content) 

while True:
    if (datetime.now().hour == 7) and (datetime.now().minute == 10) and (datetime.now().second == 10):
        try:
            post()
            print("\nSuccesfully posted at ", datetime.now())
        except Exception as error:
            print("\nError encountered at ")
            print(f"\nↆ ERROR LISTED BELOW ↆ \n{error}")
            
            f = open("error", "w")
            f.write(error)
            f.close

        time.sleep(10000)
