from argparse import ArgumentParser
import re
from KPI_calculation.huawei_Kpi.drive_huawei_kpi_calc import run_huawei_lte_kpi_calc

def read_configuration(config_file_path):
    config_dict = {}
    with open(config_file_path) as configob:
        for line in configob.readlines():
            if re.search(re.compile(r"^input_folder" , re.IGNORECASE), line):
                input_folder = line.strip().split("=")[1].strip()
            elif re.search(re.compile(r"^output_folder", re.IGNORECASE), line):
                output_folder = line.strip().split("=")[1].strip()
            elif re.search(re.compile(r"^filter_file_path", re.IGNORECASE), line):
                filter_file_path = line.strip().split("=")[1].strip()
            elif re.search(re.compile(r"^vendor", re.IGNORECASE), line):
                vendor = line.strip().split("=")[1].strip()
            elif re.search(re.compile(r"^technology", re.IGNORECASE), line):
                technology = line.strip().split("=")[1].strip()
        config_dict["input_folder"] = input_folder
        config_dict["output_folder"] = output_folder
        config_dict["filter_file_path"] = filter_file_path
        config_dict["vendor"] = vendor
        config_dict["technology"] = technology
    return config_dict


def run_correct_module(config_input:dict):
    if config_input['vendor'].upper() == "HUAWEI":
        if config_input['technology'].upper() == "LTE":
            print("run huawei LTE module")
            input_directory = config_input["input_folder"]
            output_directory = config_input["output_folder"]
            filter_file = config_input["filter_file_path"]
            run_huawei_lte_kpi_calc(input_directory,output_directory,filter_file)

        elif config_input['technology'].upper() == "UMTS":
            print("run huawei UMTS")
            input_directory = config_input["input_folder"]
            output_directory = config_input["output_folder"]
            filter_file = config_input["filter_file_path"]
        else:
            print(config_input['technology'].upper() + " is not supported technology for HUAWEI")
    elif config_input['vendor'].upper() == "ERICSSON":
        if config_input['technology'].upper() == "LTE":
            print("run ERICSSON LTE module")
            input_directory = config_input["input_folder"]
            output_directory = config_input["output_folder"]
            filter_file = config_input["filter_file_path"]
        elif config_input['technology'].upper() == "UMTS":
            print("run ERICSSON UMTS")
            input_directory = config_input["input_folder"]
            output_directory = config_input["output_folder"]
            filter_file = config_input["filter_file_path"]

        else:
            print( config_input['technology'].upper() + " is not supported technology for ERICSSON")
    else:
        print(str(config_input['vendor']).upper() + " vendor support is comming soon .... rise demand to increase priotiry")


if __name__ == "__main__":
    parser = ArgumentParser(description="to get the path for config file")
    parser.add_argument("config_path", help="Please provide the config file's path")
    args = parser.parse_args()
    config_path = args.config_path
    config_dict = read_configuration(config_path)
    run_correct_module(config_dict)



