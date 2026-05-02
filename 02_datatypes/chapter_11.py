import arrow

brewing_time = arrow.utcnow()
brewing_time.to("Europe/Rome")

from collections import namedtuple
coffeeProfile = namedtuple("coffeeProfile", ["flavor", "aroma"])