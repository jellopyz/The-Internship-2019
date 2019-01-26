"""
For the internship programs 2019
This script for convert XML to Json
Developer:Thanakorn Amnajsatit
"""

import json
import xmltodict


def main():
    while(True):
        inFile = input("Enter XML file name:\n") #รับค่าชื่อfileเช่น weather.xml
        name_inFile = inFile.split(".")[0] #แยกเพื่อเอาแต่ชื่อไฟล์ ตัดนามสกุลออก

        #พิมexitเมื่อต้องการหยุดการทำงาน
        if inFile == "exit":
            break
        else:   
            #เปิดไฟล์จาก inFile อ่านค่าเก็บในรูปแบบString
            try:
                with open(inFile, 'r') as f:
                    xmlString = f.read()
            except:
                print("!!!Can't read from "+inFile)
                break

            #ใช้library xmltodict แปลงรูปแบบxmlไปเป็นdictได้OrderedDict
            #นำdictที่ได้ใช้แปลงต่อไปเป็นjsonผ่านฟังก์ชั่นdumps
            try:
                jsonString = json.dumps(xmltodict.parse(xmlString), indent=2)
            except:
                print("!!!Not a XML format in your file")
                break

            #สร้างไฟล์.jsonแล้วเขียนformat jsonลงไปในไฟล์
            try:
                with open(name_inFile+".json", 'w') as f:
                    f.write(jsonString)
            except:
                print("!!!Can't write to .json file!!!")
                break
            print("!!!Successfully convert XML to JSON")
            print("!!!Output is "+name_inFile+".json")

main()