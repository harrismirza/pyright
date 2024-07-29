# This sample tests the detection and reporting of unreachable code when using the TYPE_CHECKING

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from datetime import datetime
else:
    from datetime import timedelta as datetime


print(datetime())