from operator import index
import re

def email_validator(email, domains):
    """
    >>> email_validator("oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@gmail.com", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@berkeley.com", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeley.edu", ["yahoo.com"])
    False
    >>> email_validator("xX123_iii_OSKI_iii_123Xx@berkeley.edu", ["berkeley.edu", "gmail.com"])
    True
    >>> email_validator("oski@oski@berkeley.edu", ["berkeley.edu", "gmail.com"])
    False
    >>> email_validator("oski@berkeleysedu", ["berkeley.edu", "gmail.com"])
    False
    """
    pattern = r"^\w+@("
    for domain in domains:
        if domain == domains[-1]:
            pattern += domain[:-4] + "\\." + domain[-3:] + ")$"
        else:
            pattern += domain[:-4] + "\\." + domain[-3:] + "|"               #此处可选择用r-string，亦可选择用\\
    return bool(re.search(pattern, email))