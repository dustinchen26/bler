"""
  Copyright © [2023] [Dustin_Chen]. All rights reserved.
  Author: Dustin_Chen
  Email:  Dustin_Chen@compal.com or chuhpsdustin@gmail.com
  
  Description: 
  Input the du_stats_XXX.txt, then it will parse the ( DL-SUCC, DL-NEWTX, DL-RETX, BLER, SCH  DL Tpt, UL Tpt )  
  (Note) BLER = DL-RETX / (DL-NEWTX + DL-RETX )
"""  

import glob # glob 用於尋找匹配檔案
import re # regular expression 
import os # os 用於檔案系統操作。

# Check if parse_DL_BLER_results.txt exists and delete it if it does
if os.path.exists("parse_DL_BLER_results.txt"):
    os.remove("parse_DL_BLER_results.txt")
    print("Deleted existing parse_DL_BLER_results.txt")
else:
    print("parse_DL_BLER_results.txt does not exist.")

#定義函式 parse_stats，用於解析統計資料檔案，並回傳解析的結果。
def parse_stats(filename): 
    results = []

    #打開指定的檔案，讀取所有行的內容，初始化變數用於儲存解析後的結果。
    with open(filename, 'r') as file: 
        lines = file.readlines()

        dl_succ, dl_newtx, dl_retx, bler, sch_dl_tpt, ul_tpt = None, None, None, None, None, None
        dl_stats_match = None

        index = 0

        # 使用 enumerate 函式來迭代每一行的內容，同時取得行數的索引值（從 0 開始）。
        for index, line in enumerate(lines):
            dl_succ_found = False  # Track whether DL-SUCC information is found for the current entry

            # 如果當前行包含 "DL-SUCC DL-NEWTX DL-RETX" 且還有下一行存在：
            if "DL-SUCC   DL-NEWTX    DL-RETX" in line and len(lines) > index + 1:

                # 解析下一行的值，將所需的資訊（DL-SUCC、DL-NEWTX、DL-RETX）解析為整數。
                next_line_values = lines[index + 1].split()
                dl_succ = int(next_line_values[9])
                dl_newtx = int(next_line_values[10])
                dl_retx = int(next_line_values[11])

                # 如果 DL-SUCC 是 0，表示需要尋找下一個含有 DL-SUCC DL-NEWTX DL-RETX 的行，直到找到為止。
                if dl_succ == 0:
                    # Find the next "DL-SUCC   DL-NEWTX    DL-RETX" line
                    while index < len(lines):
                        index += 1
                        if index < len(lines) and "DL-SUCC   DL-NEWTX    DL-RETX" in lines[index]:
                            break

                # 否則，計算 BLER，並開始尋找 SCH DL Throughput 和 UL Throughput 的資訊。
                else:
                    #bler = dl_retx / dl_succ
                    bler = dl_retx / (dl_newtx + dl_retx)

                    # Continue searching for SCH DL Throughput and UL Throughput
                    while index < len(lines):
                        if "SCH  DL Tpt" in lines[index]:
                            sch_dl_tpt_match = re.search(r'SCH\s+DL\s+Tpt\s+:\s+(\d+\.\d+)', lines[index])
                            if sch_dl_tpt_match:
                                sch_dl_tpt = float(sch_dl_tpt_match.group(1))
                                if "UL Tpt" in lines[index]:
                                    ul_tpt_match = re.search(r'UL\s+Tpt\s+(\d+\.\d+)', lines[index])
                                    if ul_tpt_match:
                                        ul_tpt = float(ul_tpt_match.group(1))
                                        results.append((dl_succ, dl_newtx, dl_retx, bler, sch_dl_tpt, ul_tpt))
                                        dl_succ_found = True  # Set dl_succ_found to True to break the while loop
                                    break  # Stop searching once both data are found
                        index += 1

            if dl_succ_found:  # If DL-SUCC information was found, reset dl_succ for the next entry
            	dl_succ = None
            	
            # 增加行索引，繼續解析下一行。
            index += 1
            
    #回傳解析的結果。
    return results

# 使用 glob 模組找到所有符合 du_stats_*.txt 模式的檔案名稱，初始化用於儲存所有結果的列表。
file_list = glob.glob("du_stats_*.txt")
all_results = []  # Initialize a list to store results from all files

if file_list:
    for filename in file_list:
        results = parse_stats(filename)
        if results:
            all_results.extend(results)  # Append results from the current file to the overall list
            for dl_succ, dl_newtx, dl_retx, bler, sch_dl_tpt, ul_tpt in results:
                if bler is not None:
                    formatted_bler = "{:.5f}".format(bler)
                else:
                    formatted_bler = "N/A"
                output_line = "DL-SUCC: {:<6} DL-NEWTX: {:<6} DL-RETX: {:<6} BLER: {:<12} SCH  DL Tpt: {:<10} UL Tpt: {:<10}".format(dl_succ, dl_newtx, dl_retx, formatted_bler, sch_dl_tpt, ul_tpt)
                print(output_line)
                # Output to file (optional)
                with open("parse_DL_BLER_results.txt", "a") as output_file:
                    output_file.write(output_line + "\n")
        else:
            print(f"No valid results found in {filename}")
else:
    print("No matching files found.")

# Print all results after processing all files (optional)
for dl_succ, dl_newtx, dl_retx, bler, sch_dl_tpt, ul_tpt in all_results:
    if bler is not None:
        formatted_bler = "{:.5f}".format(bler)
    else:
        formatted_bler = "N/A"

