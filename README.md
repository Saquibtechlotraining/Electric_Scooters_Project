# Electric Scooters Project
Dashboard Link: https://www.novypro.com/project/electric-scooters-dashboard-power-bi

Note:- For this project, I scraped data from the website [91wheels](https://www.91wheels.com/electric-scooters) of 10th of November, 2023.

### • Loading Data also in SQL Server Management Studio(SSMS)
ScreenShot [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/Screenshots/Load_Data_in_SQL(SSMS).png)

###  Project Overview
    • Background 
    • Project Goal
    • Key Components

➡  Background

In today's world, the surge in popularity of electric vehicles is evident, driven by factors such as affordability and environmental friendliness. The transition from fuel-based to electric vehicles marks a significant shift in consumer preferences. As a result, electric scooters have become a focal point of interest of the two vehicle drivers, reflecting the rapid evolution and adoption of electric scooters.
In India, there are 85 companies which manufacturing of total 288 scooters with 436 variants. This project aims to delve into this evolving landscape, examining manufacturers, specifications, and the changing preferences of consumers.

➡ Project Goal

The primary goal of this project is to compile, analyze, and present comprehensive data on electric scooters in India.
     
     The main focus of this project are:-

     ① Provide real-time information about electric scooters available for sale in India.
     ② Offer a detailed list of technical information and characteristics for each brand of electric scooter and the availability in different parts of India.
     ③ Explore and present information about the 85 companies actively manufacturing electric scooters in India.
     ④ Understand and illustrate how consumer preferences have shifted from fuel-based vehicles to electric scooters.

➡ Key Components

The Electric Scooters Pipeline comprises four crucial stages:-
        
        ① Data Collection
        ② Data Storage
        ③ Data Extraction and Data Preprocessing 
        ④ Data Visualization

Each stage is meticulously designed to ensure the accuracy, integrity, and reliability of the extracted information.

## Project Pipeline:-

### Pipeline 1: Data Collection and Data Storage

#### ➼ 1.1 Web Scraping from 91wheels.com website
    At the heart of our project lies the data collection process, where we employ webscraping techniques to gather a representative of electric scooters currently available in India. 
    This involves the use of cutting-edge technologies to navigate through individual electric scooter webpage to extract relevant information, and transform it into structured data.

-------------------------------------------------------------------------------------------------------------------------------------------------      
#### ‣ Code Description                        

• Using this code extract all URL from electric scooter webpage  - [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/url_extract_company_wise.py)  (Used for Data Extraction)

• Using this code extract all scooter company's URL - [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/company_wise_url.py)  (Used for Data Extraction)

• All electric scooter URL          -  [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/ALL_EVs_URLS.py)  (Used for Data Extraction)

------------------------------------------------------------------------------------------------------------------------------------------------------------------

#### ‣ Data Extract for the Project 

##### Electric Scooters Overview ⁃
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_Overview.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_Overview.py)

##### Electric Scooters Cities and Prices ⁃
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_EVs_cities_and_prices.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_cities_and_prices.py)

##### Electric Scooters Variants and Prices ⁃
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_EVs_variant_and_prices.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_variant_and_prices.py)

##### Reviewer's Data ⁃
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_EVs_Reviewer's_data.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_Reviwer's_data.py)

#### ➼ 1.2 Azure SQL Database Integration
    • To ensure seamless and efficient data management, we leverage Azure SQL Database, a powerful cloud-based relational database service. 
    • Our collected data are stored securely, guaranteeing data availability, scalability, and robustness.
    • This integration facilitates easy data retrieval and forms the foundation for subsequent analysis.
[Database Connection Information](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/My%20Azure%20resource_group_admin_%26password.txt)

### Pipeline 2: Data Extraction and Preprocessing Using Pyspark

#### ➼ 2.1 Data Extraction with Pyspark
     • In this section, we navigate the technical intricacies of data preprocessing, initially utilizing Pyspark for the extraction phase. 
     • Pyspark, a powerful tool for large-scale data analysis, efficiently processes and extracts the raw data. 
     • Following the extraction, the data is stored in CSV file format in the local system.
     • The subsequent preprocessing stage is then seamlessly executed using Pyspark again.

All Raw Data's file in CSV format : [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/tree/main/All_Raw_Data)
     
#### ➼ 2.2 Preprocessing Using Pyspark 
     • We embark on an exploratory journey to uncover hidden patterns, anomalies.
     • Employing Exploratory Data Analysis (EDA) techniques, we visualize and summarize the data. 
     • The process provides an initial glimpse into customer's rating and reviews, electric scooters features and characteristic, availability in different part of India.

Data Preprocessing using Pyspark : [All File Click](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/tree/main/EDA_by_Pyspark)

All Clean Data's file in CSV format : [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/tree/main/All_Clean_Data)

### Pipeline 3: Data Visualization using all Clean Data

#### ➼ For Visualization use Power Bi
    • After obtaining All Clean Data's file in CSV format, utilize Power BI for creating interactive and visually appealing dashboards and reports.
    • Power BI allows for seamless visualization of insights, making it easy to communicate and interpret complex information.

### Conclusion

#### ➡ Business Implications

Brand Image Enhancement:
 
    Leverage insights to enhance the brand image by aligning electric scooters with features that resonate positively with consumers.

Sustainability Messaging:
      
      Use consumer preferences and reviews to emphasize the environmental benefits of electric scooters, contributing to sustainability messaging.

Customer-Centric Improvements:

    Focus on customer-centric improvements by addressing issues raised in reviews, leading to enhanced customer satisfaction and loyalty.

#### ➡  Project Impact Assessment:
    Reflect on how the project contributes to the evolution of the electric industry and fosters a culture of data-driven decision-making.

#### ➡ Lessons Learned
    • No project is without its challenges and learning experiences. 
    • In this subsection, we candidly discuss the hurdles we encountered during the project's lifecycle and the strategies we employed to overcome them.
    • These insights serve as a valuable resource for future endeavors.

#### ➡ Future Enhancements
    • As technology and data science methodologies evolve, so too will our project.
    • We outline potential avenues for future enhancements, including the integration of additional data sources, implementation of more advanced analytics, and exploration of predictive modeling.
    

### Dashboard View

![Screenshot 2023-12-11 112331](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/e1fd668f-d702-4cc3-a47e-5065d516fb4b)

![Screenshot 2023-12-11 112421](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/d79f5733-64d1-46bb-9936-1caa1d475fbf)

![Screenshot 2023-12-11 112454](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/57c3cd64-3cf5-4658-a67f-2b9ae49b334f)

![Screenshot 2023-12-11 112517](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/2bb40cd4-56be-4567-9888-7ed69f9bfdee)

### Model View 

![Screenshot 2023-12-13 114836](https://github.com/Saquibtechlotraining/image-added-readme/assets/91885135/a3ccadc7-2826-4bb2-9a35-c44e79b1f846)

### Tools Used:
• Webscraping - Python

• Data Storage - Azure SQL Database

• Data Extraction and Preprocessing - Pyspark

• Data Visualization - Power Bi
