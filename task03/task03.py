import time
from datetime import *

def convertTimestampToYYYYMMDD(ts):

    ts.datetime.strftime('%Y-%m-%d')

def convertTimestampToYYYYMMDD2(ts):
    days = ts / 86400  # find amount of days in the ts

    timestampstart = date(1970, 1, 1)

    newDate = timestampstart + timedelta(days=days)  # add amount of days to timestamp start

    return str(newDate).replace('-', '')


def convertYYYYMMDDtoTimestamp(timestring):
    timestampstart = date(1970, 1, 1)

    timestring = datetime.strptime(timestring, '%Y%m%d').date()  # convert timestring to date object

    days = (timestring - timestampstart).days  # find amount of days from timestamp start to timestring

    return days * 86400


if __name__ == '__main__':

    example_timestamp = int(time.time())
    example_timestring = '20220420'

    print(convertTimestampToYYYYMMDD(example_timestamp))
    print(convertYYYYMMDDtoTimestamp(example_timestring))
