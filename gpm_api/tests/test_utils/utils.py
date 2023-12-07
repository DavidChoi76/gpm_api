import datetime
import numpy as np
from typing import Union


def create_fake_datetime_array_from_hours_list(hours: Union[list, np.ndarray]) -> np.ndarray:
    """Convert list of integers and NaNs into a np.datetime64 array"""

    datetimes = []
    for hour in hours:
        if np.isnan(hour):
            datetimes.append(np.datetime64("NaT"))
        else:
            datetimes.append(
                np.datetime64(
                    datetime.datetime(2020, 12, 31, 0, 0, 0) + datetime.timedelta(hours=int(hour))
                )
            )

    return np.array(datetimes)


def get_time_range(start_hour: int, end_hour: int) -> np.ndarray:
    return create_fake_datetime_array_from_hours_list(np.arange(start_hour, end_hour))
