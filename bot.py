import datetime
import time
import datetime
from datetime import datetime
from dateutil import relativedelta
from datetime import date
from mastodon import Mastodon

# get two dates
d1 = date.today().strftime('%d/%m/%Y')
d2 = '25/2/2023'

# convert string to date object
start_date = datetime.strptime(d1, "%d/%m/%Y")
end_date = datetime.strptime(d2, "%d/%m/%Y")

# Get the relativedelta between two dates
delta = relativedelta.relativedelta(end_date, start_date)

delta2 = start_date - end_date

content = 'Time until KSP 2 release:\n'
content += f'{delta.months} months, {delta.days} days'

content += f'\n\nT{delta2.days} DAYS'

#   Set up Mastodon
mastodon = Mastodon(
    access_token = 'token',
    api_base_url = 'https://mstdn.social/'
)

mastodon.status_post(content) 
