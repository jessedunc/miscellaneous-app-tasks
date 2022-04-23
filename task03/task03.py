from datetime import *


def convertTimestampToYYYYMMDD(ts):
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
    print(convertTimestampToYYYYMMDD(1650473094))
    print(convertYYYYMMDDtoTimestamp('20220420'))
