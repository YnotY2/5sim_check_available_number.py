# 5SIM Number Availability Checker

## Overview

The 5SIM Number Availability Checker is a Python script designed to check the availability of phone numbers provided by the 5SIM service. It specifically focuses on the "bolt" service and determines if there are any available numbers for a given operator and country.

## Prerequisites

No specific prerequisites are needed to run this script. You only need Python installed on your system.

## Usage

To use the **5SIM Number Availability Checker**, follow these steps:

1. **Specify Operator and Country**

   In the script, you can specify the operator and country for which you want to check the number availability. Modify the following variables in the script:
   
```python
# Specify the operator and service you would like to use:
operator_1 = 'virtual38'
operator_2 = 'virtual4'
country = 'germany'
service = 'openai'
```

2. **Run LamdaTest_Env_Check.py**
   
   ```bash
   python3 5sim_buy_available_numbers.py
   ```

## Ouput 
```bash
Currently requesting live available 'bolt' service numbers from 5SIM...
Operator: virtual38
Country: germany
no available numbers from; "virtual38"
Currently requesting live available 'bolt' service numbers from 5SIM...
Operator: virtual4
Country: netherlands
Successful API call!
---------------------
Bolt Qty:           20300
Bolt Price:         38.7 (0,36$)
operator is available;    True
operator is available;    virtual4

```
## Blessed 0-0
```---```
Don't worry the ouput is more colorfull on the real terminal. YnotY2 
