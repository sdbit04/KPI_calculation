from KPI_calculation.huawei_Kpi.app import parse_input_xml, write_to_excel, read_mandatory_kpi
import argparse
import os 
import re

xml_file = re.compile(r".*.xml")
gz_file = re.compile(r".*.gz")

def run_huawei_lte_kpi_calc(Input_folder, output_folder,filter_file):
    mandatory_kpi = read_mandatory_kpi(filter_file)
    input_dict = {}
    for a, b, filenames in os.walk(Input_folder):
        for filename in filenames:
            print("Processing file name {}".format(filename))
            file_path = os.path.join(a, filename)
            if re.search(xml_file, filename):
                input_dict = parse_input_xml(file_path,mandatory_kpi,input_dict= input_dict)

    print(input_dict)
    print("**********Writing into excel file***************")
    write_to_excel(input_dict,output_folder)
    print(mandatory_kpi)

if __name__ == "__main__":
    A_Input_folder = r"D:\D_drive_BACKUP\study\PycharmProjects\KPI_calculation\Input_folder"
    A_mandatory_kpi = set([50332573,50332574,50342574,50342575,50342635,50342636,50332582,50332583,50332584,50332586,50342584,50342585,50342586,50342587,50342606,50342607,50342608,50342609,50342632,50342633,50332582,50332583,50332584,50332586,50342584,50342585,50342586,50342587,50342606,50342607,50342608,50342609,50342632,50342633,50332582,50332583,50332584,50332586,50342584,50342585,50342586,50342587,50342606,50342607,50342608,50342609,50342632,50342633,50332627,50332627,50332627,1526727075,1526727076,1526727077,1526727078,1526727079,1526727080,1542455297,1542455298,1542455299,1542455300,1542455301,1542455302,1542455303,1542455304,1542455305,1542455306,1542455307,1542460296,1542460297,1542455297,1542455298,1542455299,1542455300])
    A_output_folder = r"D:\D_drive_BACKUP\study\PycharmProjects\KPI_calculation\output_folder"
    run_huawei_lte_kpi_calc(A_Input_folder,A_output_folder,A_mandatory_kpi)





