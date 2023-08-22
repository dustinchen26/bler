"""
  Copyright © [2023] [Dustin_Chen]. All rights reserved.
  Author: Dustin_Chen
  Email:  Dustin_Chen@compal.com or chuhpsdustin@gmail.com
  
  Description: 
  Input the du_stats_XXX.txt, then it will parse the ( DL-SUCC, DL-NEWTX, DL-RETX, DL_BLER, SCH  DL Tpt, UL Tpt )  
  (Note) DL_BLER = DL-RETX / (DL-NEWTX + DL-RETX )
"""  
import glob
import re
import os

# Check if the file parse_DL_UL_BLER_results.txt exists and delete it if it does
if os.path.exists("parse_DL_UL_BLER_results.txt"):
    os.remove("parse_DL_UL_BLER_results.txt")
    print("Deleted existing parse_DL_UL_BLER_results.txt")
else:
    print("parse_DL_UL_BLER_results.txt does not exist.")

# Define the function parse_stats to parse statistical data files and return parsed results
def parse_stats(filename):
    results = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        index = 0

        while index < len(lines):
            line = lines[index]
            
            if "DL-SUCC   DL-NEWTX    DL-RETX" in line and len(lines) > index + 1:
                next_line_values = lines[index + 1].split()
                
                if len(next_line_values) >= 12:  # Check if there are enough values
                    dl_succ = int(next_line_values[9])
                    dl_newtx = int(next_line_values[10])
                    dl_retx = int(next_line_values[11])
                    dl_bler = None
                    if dl_succ != 0:
                        dl_bler = dl_retx / (dl_newtx + dl_retx)

                    # Parsing UL statistics
                    ul_section_found = False
                    for ul_index in range(index + 1, len(lines)):
                        ul_line = lines[ul_index]
                        if "UL-NEWTX   UL-RETX" in ul_line:
                            ul_stats = lines[ul_index + 1].split()
                            if len(ul_stats) >= 10:
                                ul_succ = int(ul_stats[7])
                                ul_newtx = int(ul_stats[8])
                                ul_retx = int(ul_stats[9])
                                if ul_succ != 0:
                                    ul_bler = ul_retx / (ul_newtx + ul_retx)
                                else:
                                    ul_bler = None
                                ul_section_found = True
                                break

                    if ul_section_found:
                        while index < len(lines):
                            if "SCH  DL Tpt" in lines[index]:
                                sch_dl_tpt_match = re.search(r'SCH\s+DL\s+Tpt\s+:\s+(\d+\.\d+)', lines[index])
                                if sch_dl_tpt_match:
                                    sch_dl_tpt = float(sch_dl_tpt_match.group(1))
                                    if "UL Tpt" in lines[index]:
                                        ul_tpt_match = re.search(r'UL\s+Tpt\s+(\d+\.\d+)', lines[index])
                                        if ul_tpt_match:
                                            ul_tpt = float(ul_tpt_match.group(1))
                                            results.append((dl_succ, dl_newtx, dl_retx, dl_bler, sch_dl_tpt, ul_succ, ul_newtx, ul_retx, ul_bler, ul_tpt))
                                            break
                            index += 1

            index += 1
            
    return results

# Use the glob module to find all files matching the pattern du_stats_*.txt
file_list = glob.glob("du_stats_*.txt")

if file_list:
    for filename in file_list:
        results = parse_stats(filename)
        if results:
            for dl_succ, dl_newtx, dl_retx, dl_bler, sch_dl_tpt, ul_succ, ul_newtx, ul_retx, ul_bler, ul_tpt in results:
                formatted_dl_bler = "{:.5f}".format(dl_bler) if dl_bler is not None else "N/A"
                formatted_ul_bler = "{:.5f}".format(ul_bler) if ul_bler is not None else "N/A"
                output_line = "DL-SUCC: {:<6} DL-NEWTX: {:<6} DL-RETX: {:<6} DL_BLER: {:<12} SCH  DL Tpt: {:<10} UL-SUCC: {:<6} UL-NEWTX: {:<6} UL-RETX: {:<6} UL_BLER: {:<12} UL Tpt: {:<10}".format(dl_succ, dl_newtx, dl_retx, formatted_dl_bler, sch_dl_tpt, ul_succ, ul_newtx, ul_retx, formatted_ul_bler, ul_tpt)
                
                print(output_line)
                with open("parse_DL_UL_BLER_results.txt", "a") as output_file:
                    output_file.write(output_line + "\n")
        else:
            print(f"No valid results found in {filename}")
else:
    print("No matching files found.")
