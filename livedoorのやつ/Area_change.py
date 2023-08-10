import re
import json

with open("primary_area.txt", encoding="utf-8", mode="r") as f:
    text = f.read().replace("\n",'')

    results_district = re.findall("<pref title=\"(.*?)\">(.*?)</pref>", text)
    # print(results_district[0])

    areaName_to_id = {}
    for district_contents in results_district:
        district_name, district_xml = district_contents
        results = re.findall("<city title=\"(.*?)\" id=\"(.*?)\"", district_xml)

        results_dict = {}
        for dist, id in results:
            results_dict[dist] = id 
        
        # print(results_dict)
        areaName_to_id[district_name] = results_dict
        # print(district_name, results)
        # print(areaName_to_id)
        # break
    print(areaName_to_id["大分県"])

if True:
    path = "./areaName_to_id.json"
    json_file = open(path, mode="w", encoding="utf-8")
    json.dump(areaName_to_id, json_file, indent=2, ensure_ascii=False)
    json_file.close()