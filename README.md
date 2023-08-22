# BlerTputParser
```
Author: Dustin_Chen  Email:  Dustin_Chen@compal.com or chuhpsdustin@gmail.com
```

## How to use
```
Input the du_stats_XXX.txt, then it will parse the ( DL-SUCC, DL-NEWTX, DL-RETX, DL_BLER, SCH  DL Tpt, UL-SUCC, UL-NEWTX, UL-RETX, UL_BLER, UL Tpt)  

Step:
1.	decompress the BlerTputParser.7z
2.	Put any type of du_stats_XXX log in the decompressed folder
3.	Execute the BlerTputParser.exe
4.	View the calculation results "parse_DL_UL_BLER_results.txt"

Calculation formula:
> dl_bler = dl_retx / (dl_newtx + dl_retx)
> ul_bler = ul_retx / (ul_newtx + ul_retx)
```

## Example
```
【Input】"du_stats_22_12_29_22_18_25.txt":
---------------------------------------------------------------------------------------------
                       DL Instantaneous Statistics
---------------------------------------------------------------------------------------------
CELL-ID   CELL-DL-BANDWIDTH  CELL-UL-BANDWIDTH  AVG-DL-PRB  AVG-DL-PRB-BWP-0  AVG-DL-PRB-BWP-1  AVG-DL-PRB-BWP-2  AVG-DL-PRB-BWP-3  DL-OCC   DL-SUCC   DL-NEWTX    DL-RETX   DL-DTX   DL-NACK-RV[0]   DL-NACK-RV[1]   DL-NACK-RV[2]   DL-NACK-RV[3]   DL-DTX-RV[0]   DL-DTX-RV[1]   DL-DTX-RV[2]   DL-DTX-RV[3]   DL-BLER   
1         0                  0                  255.10      255.10            0.00              0.00              0.00              48002    25545     25488       57        0        48              1               8               1               0              0              0              0              0         

---------------------------------------------------------------------------------------------
                       UL Instantaneous Statistics
---------------------------------------------------------------------------------------------
CELL-ID   AVG-UL-PRB  AVG-UL-PRB-BWP-0  AVG-UL-PRB-BWP-1  AVG-UL-PRB-BWP-2  AVG-UL-PRB-BWP-3  UL-OCC   UL-SUCC   UL-NEWTX   UL-RETX   UL-DATIND   UL-BLER ERR-PUCCH-NODE ERR-PUCCH-MSGLEN 
1         24          24                0                 0                 0                 0        6913      6913       0         6217        0       0              0                

Total Number of UEs  : 1
	 EGTP DL Tpt : 473.91  UL Tpt 0.26
	 X2 EGTP DL Tpt : 0.00  UL Tpt 0.00
	 SCH  DL Tpt : 475.50  UL Tpt 0.26	 
	 
【Output】"parse_DL_UL_BLER_results.txt"
DL-SUCC: 25545  DL-NEWTX: 25488  DL-RETX: 57     DL_BLER: 0.00223      SCH  DL Tpt: 475.5      UL-SUCC: 6913   UL-NEWTX: 6913   UL-RETX: 0      UL_BLER: 0.00000      UL Tpt: 0.26

```
