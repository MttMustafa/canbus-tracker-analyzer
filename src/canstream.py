import os
import can
import pandas as pd
import numpy as np
from can.interface import Bus

can.rc['interface'] = 'socketcan'
can.rc['channel'] = 'vcan0'
can.rc['bitrate'] = 500000


read_dict = {}

def extract_msg_data(msg):
    row = [hex(msg.arbitration_id)[2:]]

    for i in range(0, 9):
        if(i >= msg.dlc):
            row.append('')
        else:
            row.append(str(hex(msg.data[i])[2:]))

    row[2:3] = [''.join(row[2:4])]
    row[4:] = [''.join(row[5:])] 
    

    read_dict[row[0]] = row

with Bus() as bus:
    for msg in bus:
        if(msg.arbitration_id > 1408 and msg.arbitration_id < 1535) or (msg.arbitration_id > 1536 and msg.arbitration_id < 1663):
            extract_msg_data(msg)   
        os.system('clear')
        read_arr = read_dict.values()
        read_df = pd.DataFrame(read_arr, columns = list(["ID", "Specifier", "Index", "SubIndex", "Data"]))
        print(read_df)

print(read_arr)

