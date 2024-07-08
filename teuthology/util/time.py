import re

from datetime import timedelta

def parse_offset(offset: str) -> timedelta:
    """
    offset: A string consisting of digits followed by one of the following
            characters:
                s: seconds
                m: minutes
                h: hours
                d: days
                w: weeks
    """
    err_msg = "Offsets must either be an ISO 8601-formatted timestamp or " \
        f"a relative value like '2w', '1d', '7h', '45m', '90s'. Got: {offset}"
    match = re.match(r'(\d+)(s|m|h|d|w)$', offset)
    if match is None:
        raise ValueError(err_msg)
    num = int(match.groups()[0])
    unit = match.groups()[1]
    match unit:
        case 's':
            return timedelta(seconds=num)
        case 'm':
            return timedelta(minutes=num)
        case 'h':
            return timedelta(hours=num)
        case 'd':
            return timedelta(days=num)
        case 'w':
            return timedelta(weeks=num)
        case _:
            raise ValueError(err_msg)
