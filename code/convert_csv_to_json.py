import csv
import json
import sys

json_result = {
    "creator": "ZAYAR PHYO",
    "header": [],
    "data": []
}

def create_new(row):
    dump_dict = {}
    dump_dict["country_code"] = row[0]
    dump_dict["country_name"] = row[1]
    dump_dict["country_border"] = [{
        "code": row[2],
        "name": row[3]
    }]
    return dump_dict

def loadingBar(count,total,size):
    percent = float(count)/float(total)*100
    sys.stdout.write("\r" + str(int(count)).rjust(3,'0')+"/"+str(int(total)).rjust(3,'0') + ' [' + '='*int(percent/10)*size + ' '*(10-int(percent/10))*size + ']')

def main():
    with open("../GEODATASOURCE-COUNTRY-BORDERS.csv", 'r') as file:
        csv_reader = csv.reader(file)
        is_header = True
        for row in csv_reader:
            if is_header:
                # insert header
                json_result["header"].append(row)
                is_header = False
            else:
                if len(json_result["data"]) == 0:
                    json_result["data"].append(create_new(row))
                else:
                    if json_result["data"][-1]["country_code"] != row[0]:
                        json_result["data"].append(create_new(row))
                    else: # record already exist and insert only border country name
                        json_result["data"][-1]["country_border"].append({
                            "code" : row[2],
                            "name": row[3]
                        })
    json_object = json.dumps(json_result, indent=4)
    with open("../geodatasource-country-borders.json", "w") as outfile:
        outfile.write(json_object)

main()
