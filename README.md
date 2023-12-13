# Electric Scooters Project
Dashboard Link: https://www.novypro.com/project/electric-scooters-dashboard

Note:- For this Project, I scraped data from the 10th of November, 2023.

All Raw Data [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/tree/main/All_Raw_Data)

All Clean Data [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/tree/main/All_Clean_Data)

### • Loading Data also in SQL Server Management Studio(SSMS)
ScreenShot [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/Screenshots/Load_Data_in_SQL(SSMS).png)

## TABLE OF CONTENT
### 1) Project Overview
    1.1 Background 
    1.2 Project Goal
    1.3 Key Components

### 2) Data Collection and Storage
    2.1 Web Scraping from 91wheels.com website

   Code Explain
   
   ➡ URL Extract Company Wise [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/url_extract_company_wise.py)
   
   ➡ Company Wise URL [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/company_wise_url.py)
   
   ➡ ALL Electric Scooters URL [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/ALL_EVs_URLS.py)

##### Electric Scooters Overview 
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_Overview.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_Overview.py)

##### Electric Scooters Cities and Prices
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_EVs_cities_and_prices.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_cities_and_prices.py)

##### Electric Scooters Variants and Prices
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_EVs_variant_and_prices.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_variant_and_prices.py)

##### Reviewer's Data 
1) Table Creation Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/table_EVs_Reviewer's_data.py)
2) Data Extracted Code [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/EVs_Reviwer's_data.py)

       2.2 Azure SQL Database Integration

   [Click Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/blob/main/My%20Azure%20resource_group_admin_%26password.txt)

### 3) Data Processing and Analysis Using Pyspark
    3.1 Data Preprocessing and Analysis
    3.2 Exploratory Data Analysis (EDA)
[Cliclk Here](https://github.com/Saquibtechlotraining/Electric_Scooters_Project/tree/main/EDA_by_Pyspark)

#### 4) Results and Insights
     4.1 Extracted Insights
     4.2 Visualization of Findings
     4.3 Business Implications
     5) Conclusion 

#### 5) Conclusion
    5.1 Lessons Learned
    5.2 Future Enhancements
    
## Content
### 1) Project Overview
    1.1 Background 
    1.2 Project Goal
    1.3 Key Components

1.1 Background

In today's world, the surge in popularity of electric vehicles is evident, driven by factors such as affordability and environmental friendliness. The transition from fuel-based to electric vehicles marks a significant shift in consumer preferences. As a result, electric scooters have become a focal point of interest of the two vehicle drivers, reflecting the rapid evolution and adoption of electric scooters.
In India, there are 85 companies which manufacturing of total 288 scooters with 436 variants. This project aims to delve into this evolving landscape, examining manufacturers, specifications, and the changing preferences of consumers.

1.2 Project Goal

The primary goal of this project is to compile, analyze, and present comprehensive data on electric scooters in India.
     
     The main focus of this project are:-

     1) Provide real-time information about electric scooters available for sale in India.
     2) Offer a detailed list of technical information and characteristics for each brand of electric scooter and the availability in different parts of India.
     3) Explore and present information about the 85 companies actively manufacturing electric scooters in India.
     4) Understand and illustrate how consumer preferences have shifted from fuel-based vehicles to electric scooters.

1.3 Key Components
The Electric Scooters Pipeline comprises four crucial stages: data collection, data storage, data processing, and insights generation. Each stage is meticulously designed to ensure the accuracy, integrity, and reliability of the extracted information.

### 2) Data Collection and Storage
       2.1 Web Scraping from 91wheels.com website
       2.2 Azure SQL Database Integration

2.1 Web Scraping from 91wheels.com website

At the heart of our project lies the data collection process, where we employ web scraping techniques to gather a representative sample of electric scooters currently available in India. This involves the use of cutting-edge technologies to navigate through web pages, extract relevant information, and transform it into structured data.

2.2 Azure SQL Database Integration

To ensure seamless and efficient data management, we leverage Azure SQL Database, a powerful cloud-based relational database service. Our collected data are stored securely, guaranteeing data availability, scalability, and robustness. This integration facilitates easy data retrieval and forms the foundation for subsequent analysis.

### 3) Data Processing and Analysis
    3.1 Data Extraction with Pyspark 
    3.2 Exploratory Data Analysis (EDA)

3.1 Data Extraction with Pyspark 
In this section, we navigate the technical intricacies of data preprocessing, initially utilizing Pyspark for the extraction phase. Pyspark, a powerful tool for large-scale data analysis, efficiently processes and extracts the raw data. Following the extraction, the data is stored in CSV file format in the local system. The subsequent preprocessing stage is then seamlessly executed using Pyspark again.

3.2 Exploratory Data Analysis (EDA)
With the preprocessed data in hand, we embark on an exploratory journey to uncover hidden patterns, anomalies. Employing Exploratory Data Analysis (EDA) techniques, we visualize and summarize the data. The process provides an initial glimpse into customer's rating and reviews, electric scooters features and characteristic, availability in different part of India.

### 4) 4) Results and Insights
       4.1 Extracted Insights
       4.2 Visualization of Findings

4.1 Extracted Insights

The culmination of our efforts is the extraction of invaluable insights from the vast pool of electric scooters. These insights shed light on critical aspects such as rating, features of scooters, availability in different part of India and many more.

4.2 Visualization of Findings

Visual representation of data plays a pivotal role in conveying complex information concisely. In this section, we showcase a variety of visually appealing graphs, charts, tables, gauge, slicer, page navigation, Treemap that encapsulate the essence of our analyses. These visualizations make it easy to grasp the implications of the data at a glance.

### 5) Conclusion 
    5.1 Lessons Learned
    5.2 Future Enhancements

5.1 Lessons Learned

No project is without its challenges and learning experiences. In this subsection, we candidly discuss the hurdles we encountered during the project's lifecycle and the strategies we employed to overcome them. These insights serve as a valuable resource for future endeavors.

5.2 Future Enhancements

As technology and data science methodologies evolve, so too will our project. We outline potential avenues for future enhancements, including the integration of additional data sources, implementation of more advanced analytics, and exploration of predictive modeling.
