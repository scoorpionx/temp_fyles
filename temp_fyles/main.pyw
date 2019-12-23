"""
Thanks for using my code.
Checkout my Github profile:
https://github.com/scoorpionx/

And here's the link to the repo that have these scripts:
https://github.com/scoorpionx/temp_fyles
Any suggestions, you can reach me on Github or you can send a mail to joto.x42@gmail.com
Enjoy the code and always search for knowledge.

"""

from adobeCache.adobeCache import adobe_cache
from tempDesktop.tempDesktop import tempDesktop
from tempUser.tempUser import tempUser
from time import sleep
from os import getlogin


def __main__():
    adobe_cache(getlogin())
    tempUser(getlogin())
    tempDesktop()
    sleep(1080)
    __main__()

__main__()