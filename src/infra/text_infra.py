# external package
import re
from pyrootutils import setup_root

# root path configuration
root = setup_root(
    search_from=__file__,
    indicator=[".git", "pyproject.toml"],
    pythonpath=True,
    dotenv=True,
)

# internal package
from src.infra.logger_infra import ABLogger
from src.infra.data_infra import *

class ABText:
    """
        ABText class will provide text processing infrasctructure
    """

    def __init__(self) -> None:
        self.logger = ABLogger()
        self.logger.info("[ABText] running!")
    
    def split_text_numb(data: str):
        """
        split_text_numb will generate list of string alphabet and string number form string data

        Args:
            data (str): string data
            
            Example: 
                data: "B4882DTN"

        Return:
            result (str): list of string data
            
            Example: 
                result: ["B", "4882", "DTN"]
        """
        result = re.findall('(\d+|\D+)', data)
        
        return result

    def dict_to_string(data: dict) -> str:
        result = ""
        for key, value in data.items():
            if key == "passcode":
                continue
            result += f"{key} = '{value}', "
        return result[:-2]

    def dict_value_validator(data:dict)->dict:
        result = {key: value for key, value in data.items() if value is not None}
        return result
    
    def vehicle_map(vehicle_raw: str):
        pre_vehicle = vehicle_raw.replace(" ", "").lower()
        if pre_vehicle in VEHICLE_MAP.keys():
            return VEHICLE_MAP[pre_vehicle]
        else:
            return "motorcycle" # "unknown"
