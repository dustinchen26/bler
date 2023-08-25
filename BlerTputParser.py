"""
  Copyright © [2023] [Dustin_Chen]. All rights reserved.
  Author: Dustin_Chen
  Email:  Dustin_Chen@compal.com or chuhpsdustin@gmail.com
  
  Description: 
  Input the du_stats_XXX.txt, then it will parse the 
  (SCH  DL Tpt, UL Tpt, DL-TX, DL-RETX, DL-BLER, DL-MCS, UL-CRC-SUCC, UL-CRC-FAIL, UL-BLER, UL-MCS) results.
  formula:
    dl_bler = DL-RETX / (DL-RETX + DL-TX)
    ul_bler = UL-CRC-FAIL / (UL-CRC-SUCC + UL-CRC-FAIL)
"""  
import re
import os

# Check if the file parse_Tput_BLER_MCS_results.txt exists and delete it if it does
if os.path.exists("parse_Tput_BLER_MCS_results.txt"):
    os.remove("parse_Tput_BLER_MCS_results.txt")
    print("Deleted existing parse_Tput_BLER_MCS_results.txt")
else:
    print("parse_Tput_BLER_MCS_results.txt does not exist.")

# Define the function parse_stats to parse statistical data files and return parsed results
def parse_stats(filename):
    results = []
    with open(filename, 'r') as file:
        lines = file.readlines()

        sch_dl_tpt = None
        ul_tpt = None
        ue_info = None

        for i in range(len(lines)):
            line = lines[i]

            if "SCH  DL Tpt" in line:
                sch_dl_tpt_match = re.search(r'SCH\s+DL\s+Tpt\s+:\s+([\d.]+)', line)
                if sch_dl_tpt_match:
                    sch_dl_tpt = float(sch_dl_tpt_match.group(1))
                    ul_tpt_match = re.search(r'UL\s+Tpt\s+([\d.]+)', line)
                    if ul_tpt_match:
                        ul_tpt = float(ul_tpt_match.group(1))

            elif ue_info is None and re.match(r'\s*UE-ID\s+CELL-ID\s+ON-SUL\s+DL-TX\s+DL-RETX', line):
                ue_info = line.strip()

                try:
                    next_line_values = lines[i + 1].split()
                    if len(next_line_values) >= 31:
                        # ue_id = next_line_values[0]
                        # cell_id = next_line_values[1]
                        # on_sul = next_line_values[2]
                        dl_tx = next_line_values[3]
                        dl_retx = next_line_values[4]
                        # Expand the list to include all the parameters
                        # ack_tb_0 = next_line_values[5]
                        # nack_tb_0 = next_line_values[6]
                        # bler_tb_0 = next_line_values[7]
                        # dtx_tb_0 = next_line_values[8]
                        # ack_tb_1 = next_line_values[9]
                        # nack_tb_1 = next_line_values[10]
                        # bler_tb_1 = next_line_values[11]
                        # dtx_tb_1 = next_line_values[12]
                        dl_mcs = next_line_values[13]
                        # dl_ri_per = next_line_values[14]
                        # dl_cqi_per = next_line_values[15]
                        # ul_rx = next_line_values[16]
                        # ul_retx = next_line_values[17]
                        ul_crc_succ = next_line_values[18]
                        ul_crc_fail = next_line_values[19]
                        # ul_crc_dtx = next_line_values[20]
                        # ul_cqi = next_line_values[21]
                        ul_mcs = next_line_values[22]
                        # ul_ri = next_line_values[23]
                        # num_bsr = next_line_values[24]
                        # shr_bsr = next_line_values[25]
                        # st_bsr = next_line_values[26]
                        # lng_bsr = next_line_values[27]
                        # lt_bsr = next_line_values[28]
                        # num_csi = next_line_values[29]
                        # num_srs = next_line_values[30]
                    else:
                        dl_tx = dl_retx = dl_mcs = ul_crc_succ = ul_crc_fail = ul_mcs = "NaN"

                except (IndexError, ValueError):
                    dl_tx = dl_retx = dl_mcs = ul_crc_succ = ul_crc_fail = ul_mcs = "NaN"

                # Calculate dl_bler and ul_bler
                try:
                    dl_bler = float(dl_retx) / (float(dl_retx) + float(dl_tx))
                except ZeroDivisionError:
                    dl_bler = "NaN"

                try:
                    ul_bler = float(ul_crc_fail) / (float(ul_crc_succ) + float(ul_crc_fail))
                except ZeroDivisionError:
                    ul_bler = "NaN"

                # Convert dl_bler and ul_bler to strings
                dl_bler_str = format(dl_bler, ".4f") if isinstance(dl_bler, float) else str(dl_bler)
                ul_bler_str = format(ul_bler, ".4f") if isinstance(ul_bler, float) else str(ul_bler)

                output_line = "SCH  DL Tpt: {:>7.2f}  UL Tpt: {:>7.2f}".format(sch_dl_tpt, ul_tpt)
                output_line += "  DL-TX={:<6}  DL-RETX={:<6}  DL-BLER={:<6}".format(dl_tx, dl_retx, dl_bler_str)
                output_line += "  DL-MCS={:<6}  UL-CRC-SUCC={:<6}  UL-CRC-FAIL={:<6}  UL-BLER={:<6}  UL-MCS={:<6}".format(dl_mcs, ul_crc_succ, ul_crc_fail, ul_bler_str, ul_mcs)

                results.append(output_line)

                sch_dl_tpt = None
                ul_tpt = None
                ue_info = None

    return results

# Use the glob module to find all files matching the pattern du_stats_*.txt
file_list = [filename for filename in os.listdir() if filename.startswith("du_stats_") and filename.endswith(".txt")]

if file_list:
    for filename in file_list:
        results = parse_stats(filename)
        if results:
            with open("parse_Tput_BLER_MCS_results.txt", "a") as output_file:
                for result in results:
                    output_file.write(result)
                    output_file.write("\n")
                    print(result)
        else:
            print(f"No valid results found in {filename}")
else:
    print("No matching files found.")

