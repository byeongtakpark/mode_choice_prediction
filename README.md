# mode_choice_prediction
This repository contains code and experiments on predicting travelers' mode choice using machine learning techniques (XgBoost, Random Forest, etc.).

## Data Overview
The data for creating a predictive model, located at `data/survey_data`, is from the **Personal Trip Survey** conducted from October to December 2021 in the Seoul metropolitan area (Seoul-si, Incheon-si, Gyeonggi-do).
The survey data consists of travel information from individual travelers in a total of 1,114 administrative districts (In Korean, 행정동) in the metropolitan area, including information such as the mode of transportation used, origin and destination, purpose of travel, and travel time. 
Note that due to policy data sharing restrictions, only **100 samples** are available in this repository.

## Data Column Description 
### Basic Information
- `index`: Index of data
- `origin`: Origin trip zone (Unit: Administrative district)
- `destination`: Destination trip zone (Unit: Administrative district)
- `admin`: Binary parameter for whether the traveler's origin and destination are both an urban area.
- `station`: Binary parameter for whether there are subway stations at both traveler's origin and destination.

### Travel Purpose and Mode Selection
- `purpose`: Purpose of the trip (e.g., business, commuting, , etc.)
- `choice`: Chosen transportation mode 
- `actualtime`: Actual travel time (in minutes)

### Attributes of Private Car Mode
- `dist_auto`: Travel distance by car (km)
- `invehicletime_auto`: In-vehicle travel time by car (minutes)
- `outvehicletime_auto`: Time spent outside the vehicle (e.g., parking, getting in/out) (minutes)
- `totaltime_auto`: Total travel time by car (minutes)
- `totalcost_auto`: Total cost of travel by car (KRW)

### Attributes of Taxi Mode
- `dist_taxi`: Travel distance by taxi (km)
- `invehicletime_taxi`: In-vehicle travel time by taxi (minutes)
- `outvehicletime_taxi`: Time spent outside the taxi (minutes)
- `totaltime_taxi`: Total travel time by taxi (minutes)
- `totalcost_taxi`: Total cost of travel by taxi (KRW)

### Attributes of Bus Mode
- `dist_bus`: Travel distance by bus (km)
- `totaltime_bus`: Total travel time by bus (minutes)
- `invehicletime_bus`: In-vehicle travel time by bus (minutes)
- `outvehicletime_bus`: Time spent outside the bus (minutes)
- `trans_bus`: Number of bus transfers
- `totalcost_bus`: Total cost of travel by bus (KRW)

### Attributes of Subway Mode
- `dist_subway`: Travel distance by subway (km)
- `totaltime_subway`: Total travel time by subway (minutes)
- `invehicletime_subway`: In-vehicle travel time by subway (minutes)
- `outvehicletime_subway`: Time spent outside the subway (minutes)
- `trans_subway`: Number of subway transfers
- `totalcost_subway`: Total cost of travel by subway (KRW)

### Attributes of Integrated Transport Mode
(For trips using multiple transport modes)
- `dist_integmode`: Travel distance using an integrated transport mode (km)
- `totaltime_integmode`: Total travel time using an integrated transport mode (minutes)
- `invehicletime_integmode`: In-vehicle travel time (minutes)
- `outvehicletime_integmode`: Time spent outside the vehicle (minutes)
- `trans_integmode`: Number of transfers
- `totalcost_integmode`: Total cost of travel using an integrated transport mode (KRW)
---
