# external modules
import time
import pytz
from datetime import datetime


class ABTime:
    """
        ABTime class will provide time infrasctructure
    """

    def __init__(self) -> None:
        pass
    
    def get_local_datetime(self):
        current_time = datetime.now()
        tz = pytz.timezone('Asia/Jakarta')
        return current_time.astimezone(tz)
        
    def convert_date_to_string(self):
        local_time = self.get_local_datetime()
        return local_time.strftime('%Y_%m_%d_%H_%M_%S')

    def convert_date_to_iso(self):
        local_time = self.get_local_datetime()
        return local_time.isoformat()
    
    def ab_time():
        """
        ab_time will help us to get current time 

        Return:
            will return the time as a floating point number expressed in seconds since the epoch, in UTC.

            Example :
                1670394692.9053845
        """
        return time.time()

    def ab_strftime(format):
        """
        ab_strftime will generate time using the selected format

        Args:
            format (str): contain time format in string
            
            Example:
                "%Y-%m-%d %H:%M:%S"
        
        Return:
            string data of timestamp with format

            Example :
                2022-12-05 11:14:07
        """    
        return time.strftime(format, time.localtime())

    def ab_sleep(second):
        """
        ab_sleep will help us to add delay in the execution of a program
        
        Args:
            second (numeric) : time to delay in seconds
            
            Example:
                second: 2
        
        Return:
            time.sleep
        """
        return time.sleep(second)


    def ab_timestamp(self):
        """
        ab_timestamp will help us to get current timestamp 

        Return:
            string data of timestamp with format YYYY-MM-DD hh:mm:ss

            Example :
                2022-12-05 11:14:07
        """
        return ABTime.ab_strftime("%Y-%m-%d %H:%M:%S")


    def ab_timestamp_t(self):
        """
        ab_timestamp_t will help us to get current timestamp with T format

        Return:
            string data of timestamp with format YYYY-MM-DDThh:mm:ss

            Example :
                2022-12-05T11:14:07
        """
        return ABTime.ab_strftime("%Y-%m-%dT%H:%M:%S")


    def ab_timestamp_tz(self, is_utc: bool = False):
        """
        ab_timestamp_tz will help us to get current timestamp with T format with 000 and time zone

        Args:
            is_utc (bool, optional): utc flag Defaults to False.
            
            Example:
                is_utc: False

        Return:
            string data of timestamp with format YYYY-MM-DDThh:mm:ss.000Z

            Example :
                2022-12-05T11:17:30.000SE Asia Standard Time
        """
        if is_utc:
            return ABTime.ab_strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())
        else:
            return ABTime.ab_strftime("%Y-%m-%dT%H:%M:%S.000%Z")


    def ab_timestamp_underscore(self):
        """
        ab_timestamp_underscore will help us to get current timestamp with _ format

        Return:
            string data of timestamp with format YYYY-MM-DD_hh:mm:ss

            Example :
                2022-12-05_11:20:57
        """
        return ABTime.ab_strftime("%Y-%m-%d_%H:%M:%S")

    def ab_timestamp_full_underscore(self):
        """
        ab_timestamp_full_underscore will help us to get current timestamp with _ format

        Return:
            string data of timestamp with format YYYY_MM_DD_hh_mm_ss

            Example :
                2022_12_05_11_20_57
        """
        return ABTime.ab_strftime("%Y_%m_%d_%H_%M_%S")


    def ab_timestamp_t_zone(self):
        """
        ab_timestamp_t_zone will help us to get current timestamp with T format with time zone

        Return:
            string data of timestamp with format YYYY-MM-DDThh:mm:ssz

            Example :
                2022-12-05T11:22:53+0700
        """
        return ABTime.ab_strftime("%Y-%m-%dT%H:%M:%S%z")


    def ab_timestamp_ms(self):
        """
        ab_timestamp_ms will help us to get current timestamp with miliseconds format

        Return:
            string data of timestamp with miliseconds format

            Example :
                1670214370290
        """
        return round(time.time() * 1000)


    def ab_get_today(self):
        """
        ab_get_today will help us to get today date

        Return:
            string data of timestamp with format YYYY-MM-DD

            Example :
                2022-12-05
        """
        return ABTime.ab_strftime("%Y-%m-%d")
