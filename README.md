# parse the BLER and Tput from du_stats_XXX.txt
```
Author: Dustin_Chen  Email:  Dustin_Chen@compal.com or chuhpsdustin@gmail.com
file: BlerTputParser.py
```

## Description
```
Input the du_stats_XXX.txt, then it will parse the ( DL-SUCC, DL-NEWTX, DL-RETX, BLER, SCH  DL Tpt, UL Tpt )  

BLER = DL-RETX / DL-SUCC

ex: 
【Input file】: du_stats_23_08_15_15_14_06.txt

---------------------------------------------------------------------------------------------
                       DL Instantaneous Statistics
---------------------------------------------------------------------------------------------
CELL-ID   CELL-DL-BANDWIDTH  CELL-UL-BANDWIDTH  AVG-DL-PRB  AVG-DL-PRB-BWP-0  AVG-DL-PRB-BWP-1  AVG-DL-PRB-BWP-2  AVG-DL-PRB-BWP-3  DL-OCC   DL-SUCC   DL-NEWTX    DL-RETX   DL-DTX   DL-NACK-RV[0]   DL-NACK-RV[1]   DL-NACK-RV[2]   DL-NACK-RV[3]   DL-DTX-RV[0]   DL-DTX-RV[1]   DL-DTX-RV[2]   DL-DTX-RV[3]   DL-BLER   
1         0                  0                  1.46        1.46              0.00              0.00              0.00              42001    24        17          7         0        10              0               0               0               0              0              0              0              71        

...

Total Number of UEs  : 1
	 EGTP DL Tpt : 0.00  UL Tpt 0.00
	 X2 EGTP DL Tpt : 0.00  UL Tpt 0.00
	 SCH  DL Tpt : 0.00  UL Tpt 0.00

【Output file】:
DL-SUCC: 24     DL-NEWTX: 17     DL-RETX: 7      BLER: 0.29167      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 43     DL-NEWTX: 25     DL-RETX: 18     BLER: 0.41860      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 17     DL-NEWTX: 15     DL-RETX: 2      BLER: 0.11765      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 26     DL-NEWTX: 18     DL-RETX: 8      BLER: 0.30769      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 17     DL-NEWTX: 15     DL-RETX: 2      BLER: 0.11765      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 25     DL-NEWTX: 19     DL-RETX: 6      BLER: 0.24000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 34     DL-NEWTX: 19     DL-RETX: 15     BLER: 0.44118      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 2      DL-NEWTX: 1      DL-RETX: 1      BLER: 0.50000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 6      DL-NEWTX: 5      DL-RETX: 1      BLER: 0.16667      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 39     DL-NEWTX: 25     DL-RETX: 14     BLER: 0.35897      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 75     DL-NEWTX: 46     DL-RETX: 29     BLER: 0.38667      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 47     DL-NEWTX: 11     DL-RETX: 36     BLER: 0.76596      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 35     DL-NEWTX: 9      DL-RETX: 26     BLER: 0.74286      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 24     DL-NEWTX: 6      DL-RETX: 18     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 59     DL-NEWTX: 30     DL-RETX: 29     BLER: 0.49153      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 36     DL-NEWTX: 21     DL-RETX: 15     BLER: 0.41667      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 16     DL-NEWTX: 4      DL-RETX: 12     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 28737  DL-NEWTX: 28682  DL-RETX: 55     BLER: 0.00191      SCH  DL Tpt: 636.24     UL Tpt: 0.0       
DL-SUCC: 41992  DL-NEWTX: 41987  DL-RETX: 5      BLER: 0.00012      SCH  DL Tpt: 931.52     UL Tpt: 0.0       
DL-SUCC: 41993  DL-NEWTX: 41982  DL-RETX: 11     BLER: 0.00026      SCH  DL Tpt: 931.65     UL Tpt: 0.0       
DL-SUCC: 41967  DL-NEWTX: 41951  DL-RETX: 16     BLER: 0.00038      SCH  DL Tpt: 931.16     UL Tpt: 0.0       
DL-SUCC: 13304  DL-NEWTX: 13276  DL-RETX: 28     BLER: 0.00210      SCH  DL Tpt: 294.37     UL Tpt: 0.0       
DL-SUCC: 38559  DL-NEWTX: 38499  DL-RETX: 60     BLER: 0.00156      SCH  DL Tpt: 854.28     UL Tpt: 0.0       
DL-SUCC: 41989  DL-NEWTX: 41981  DL-RETX: 8      BLER: 0.00019      SCH  DL Tpt: 930.24     UL Tpt: 0.0       
DL-SUCC: 41984  DL-NEWTX: 41977  DL-RETX: 7      BLER: 0.00017      SCH  DL Tpt: 930.71     UL Tpt: 0.0       
DL-SUCC: 36662  DL-NEWTX: 36647  DL-RETX: 15     BLER: 0.00041      SCH  DL Tpt: 812.97     UL Tpt: 0.0       
DL-SUCC: 36     DL-NEWTX: 9      DL-RETX: 27     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 28     DL-NEWTX: 7      DL-RETX: 21     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 35     DL-NEWTX: 9      DL-RETX: 26     BLER: 0.74286      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 32     DL-NEWTX: 8      DL-RETX: 24     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 96.78     
DL-SUCC: 41     DL-NEWTX: 11     DL-RETX: 30     BLER: 0.73171      SCH  DL Tpt: 0.0        UL Tpt: 175.39    
DL-SUCC: 47     DL-NEWTX: 12     DL-RETX: 35     BLER: 0.74468      SCH  DL Tpt: 0.0        UL Tpt: 175.43    
DL-SUCC: 49     DL-NEWTX: 15     DL-RETX: 34     BLER: 0.69388      SCH  DL Tpt: 0.01       UL Tpt: 125.31    
DL-SUCC: 6458   DL-NEWTX: 6362   DL-RETX: 96     BLER: 0.01487      SCH  DL Tpt: 141.45     UL Tpt: 0.0       
DL-SUCC: 52     DL-NEWTX: 13     DL-RETX: 39     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 32     DL-NEWTX: 8      DL-RETX: 24     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 24     DL-NEWTX: 6      DL-RETX: 18     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 36     DL-NEWTX: 9      DL-RETX: 27     BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       
DL-SUCC: 4121   DL-NEWTX: 4073   DL-RETX: 48     BLER: 0.01165      SCH  DL Tpt: 91.17      UL Tpt: 0.0       
DL-SUCC: 41990  DL-NEWTX: 41976  DL-RETX: 14     BLER: 0.00033      SCH  DL Tpt: 931.26     UL Tpt: 0.0       
DL-SUCC: 41993  DL-NEWTX: 41989  DL-RETX: 4      BLER: 0.00010      SCH  DL Tpt: 932.06     UL Tpt: 0.0       
DL-SUCC: 41985  DL-NEWTX: 41976  DL-RETX: 9      BLER: 0.00021      SCH  DL Tpt: 931.14     UL Tpt: 0.0       
DL-SUCC: 37882  DL-NEWTX: 37873  DL-RETX: 9      BLER: 0.00024      SCH  DL Tpt: 840.48     UL Tpt: 0.0       
DL-SUCC: 30195  DL-NEWTX: 30150  DL-RETX: 45     BLER: 0.00149      SCH  DL Tpt: 669.59     UL Tpt: 0.0       
DL-SUCC: 41984  DL-NEWTX: 41977  DL-RETX: 7      BLER: 0.00017      SCH  DL Tpt: 930.52     UL Tpt: 0.0       
DL-SUCC: 41976  DL-NEWTX: 41960  DL-RETX: 16     BLER: 0.00038      SCH  DL Tpt: 929.91     UL Tpt: 0.0       
DL-SUCC: 31626  DL-NEWTX: 31604  DL-RETX: 22     BLER: 0.00070      SCH  DL Tpt: 700.29     UL Tpt: 0.0       
DL-SUCC: 12     DL-NEWTX: 3      DL-RETX: 9      BLER: 0.75000      SCH  DL Tpt: 0.0        UL Tpt: 0.0       


```				   
