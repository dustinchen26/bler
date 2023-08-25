# Tput_BLER_MCS_parser
```
Author: Dustin_Chen  Email:  Dustin_Chen@compal.com or chuhpsdustin@gmail.com
```

## Description
```
Input the du_stats_XXX.txt, then it will parse the 
(SCH  DL Tpt, UL Tpt, DL-TX, DL-RETX, DL-BLER, DL-MCS, UL-CRC-SUCC, UL-CRC-FAIL, UL-BLER, UL-MCS)
  formula:
    dl_bler = DL-RETX / (DL-RETX + DL-TX)
    ul_bler = UL-CRC-FAIL / (UL-CRC-SUCC + UL-CRC-FAIL)
```
## How to use
```
Step:
1.	decompress the BlerTputParser.7z
2.	Put any type of du_stats_XXX log in the decompressed folder
3.	Execute the BlerTputParser.exe
4.	View the calculation results "parse_Tput_BLER_MCS_results.txt"
```

## Example
```
【Input】"du_stats_22_12_29_22_18_25.txt":
Total Number of UEs  : 1
	 EGTP DL Tpt : 0.00  UL Tpt 0.00
	 X2 EGTP DL Tpt : 0.00  UL Tpt 0.00
	 SCH  DL Tpt : 0.00  UL Tpt 0.00
	 
---------------------------------------------------------------------------------------------
                       UE MAC-Scheduler Instantaneous Statistics
---------------------------------------------------------------------------------------------
UE-ID   CELL-ID   ON-SUL   DL-TX   DL-RETX   ACK-TB[0] NACK-TB[0]  BLER-TB[0]  DTX-TB[0] ACK-TB[1] NACK-TB[1]  BLER-TB[1]  DTX-TB[1] DL-MCS  DL-RI-PER   DL-CQI-PER     UL-RX   UL-RETX  UL-CRC-SUCC   UL-CRC-FAIL   UL-CRC-DTX   UL-CQI  UL-MCS  UL-RI   NUM-BSR   SHR-BSR ST-BSR  LNG-BSR LT-BSR  NUM-CSI   NUM-SRS   
17017   1         0        635     83        634       83          13          0         0         0           0           0         21      1           8              1419    6        1419          4             0            11      20      0       1394      348     0       1046    0       0         0         

【Output】parse_Tput_BLER_MCS_results.txt
SCH  DL Tpt:    0.00  UL Tpt:    0.00  DL-TX=635     DL-RETX=83      DL-BLER=0.1156  DL-MCS=21      UL-CRC-SUCC=1419    UL-CRC-FAIL=4       UL-BLER=0.0028  UL-MCS=20    
```
