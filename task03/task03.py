import time
from datetime import datetime

def convertTimestampToYYYYMMDD(ts):
    """ Given a unix epoch timestamp of form "1651192385",
    returns a string in the form "20220428" """

    return datetime.strftime(datetime.fromtimestamp(ts), '%Y%m%d')


def convertYYYYMMDDtoTimestamp(timestring):
    """ Given a string in the form "20220428",
    returns a unix epoch timestamp integer of form "1651129200" """

    return int(time.mktime(datetime.strptime(timestring, "%Y%m%d").timetuple()))


if __name__ == '__main__':

    example_timestamp = int(time.time())
    example_timestring = '20220428'

    print(f'example_timestamp: {example_timestamp}')
    print(f'converted timestring: {convertTimestampToYYYYMMDD(example_timestamp)}')

    print(f'example_timestring: {example_timestring}')
    print(f'converted timestamp: {convertYYYYMMDDtoTimestamp(example_timestring)}')
