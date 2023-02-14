# external modules
import logging

class ABLogger:
    """
        ABLogger class will provide logging infrasctructure
    """

    def __init__(self) -> None:
        """
            Default attribute for ABLogger
            [2022-12-28 10:13:14,123] [INFO] [vehicle_counter.py] - vehicle_counter function at line 34 - pesan percobaan
        """
        logging.basicConfig(format='[%(asctime)s] [%(levelname)s] [%(filename)s] - %(funcName)s at line %(lineno)d - %(message)s', level=logging.INFO)
        pass

    def info(self, log_message: str) -> None:
        """
            INFO logger will help us to monitor our system status

            Args:
                log_message (str): Message for current logging status
                
                Example:
                    log_message: pesan percobaan

            Console Output:
                [2022-12-28 10:13:14,123] [INFO] [vehicle_counter.py] - vehicle_counter at line 34 - pesan percobaan
        """
        logging.info(msg=log_message, stacklevel=3)

    def warning(self, log_message: str) -> None:
        """
            WARNING logger will warn us about our current status

            Args:
                log_message (str): Message for current logging status
                
                Example:
                    log_message: pesan percobaan

            Console Output:
                [2022-12-28 10:13:14,123] [WARNING] [vehicle_counter.py] - vehicle_counter at line 34 - pesan percobaan
        """
        logging.warning(msg=log_message, stacklevel=3)

    def error(self, log_message: str) -> None:
        """
            ERROR logger will help us to monitor any catched error in our system.

            Args:
                log_message (str): Message for current logging status
                
                Example:
                    log_message: error found!

            Console Output:
                [2022-12-28 10:13:14,123] [ERROR] [vehicle_counter.py] - vehicle_counter at line 34 - error found! Operation error
                Traceback (most recent call last):
                File "c:\Alfa_beta\etl-python\src\ab_infra\logger\logger_infra.py", line 8, in my_function
                    c = a / b
                ZeroDivisionError: division by zero
        """
        logging.error(exc_info=True, msg=log_message, stacklevel=3)
        
    def error_no_trace(self, log_message: str) -> None:
        """
            error_no_trace logger will help us to monitor any catched error in our system without tracing

            Args:
                log_message (str): Message for current logging status
                
                Example:
                    log_message: error found!

            Console Output:
                [2022-12-28 10:13:14,123] [ERROR] [vehicle_counter.py] - vehicle_counter at line 34 - error found!
        """
        logging.error(msg=log_message, stacklevel=3)


if __name__ == "__main__":
    logs = ABLogger()
    logs.info("Service logging starts...")
