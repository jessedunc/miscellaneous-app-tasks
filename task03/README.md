# Task 03

Write two functions to convert timestamp to timestring.

Each node's `core_props` contains two timestamps, `date_created` and `date_updated`. 

Timestamps are 10-digit integers which are literally the number of seconds since January 1, 1970, in UTC. Timestamps are usually created as a float where the year, month, and day are to the left of the period and the hours and seconds are to the right of the decimal. We only care about the year, month, day, so we use an integer.

An example 10-digit timestamp is `1650473094`.

The corresponding timestring for that timestamp is `20220420`. 

The two functions should look something like this:

1. `convertTimestampToYYYYMMDD(ts)` takes an integer and returns a string.

1. `convertYYYYMMDDtoTimestamp(timestamp)` takes a string and returns an integer.

Use the language of your choice.


