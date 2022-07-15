# Pension Fund of Norway - An Analysis

## Motivation
I am kind of interested in economics and fascinated by norway and its fund.  
All three combined, has led me to write irregularly (since 2020) but sometimes on this little Python script.

## Objective 
The aim of this script is to get a graphical overview of which companies the Norwegian fund has invested in and how high the investment is. 
For a modular, dedicated view of individual industries, the respective industry can be selected in the configuration of the script.  
Available are for example: Financial industry, Telecommunications and Technology.
In this way, new companies can be found out and analyzed afterwards. Subsequently, a private investment can be considered.

## Prerequisites
Python Interpreter: v3.09 is installed and functioning on the computer.  
With Python v3.10 I faced incompatibilities.  
The Python packages are installed and ready for usage.

## Explanation and Preparation
### Where does the data for the norway pension fund analysis come from?
The Norges Bank provides all data and investments.  
For a fund analysis with this script the files are required and can be downloaded here:  
https://www.nbim.no/en/the-fund/investments/#
Where we can best store or reference them I describe in Preparations

### Preparations
Please download and save all excelsheet in one folderstructure named: `EQ_Norway\Industry`.  
Afterwards please reference the filepath in  `user_config.py`.  
Respective parameter is: `directory` in  `user_config.py`.  
By default, I can recommend to have the structure as shown below:  
├── EQ_Norway  
│   └── Industry  
│        ├── EQ_2002_Industry.xlsx  
│        ├── EQ_2003_Industry.xlsx  
│        ├── ...  
│        ├── EQ_2020_Industry.xlsx  
│        └── EQ_2020_Industry.xlsx  
├── data.py  
├── main.py  
└── README.md  

But feel free to adjust to your preferences.

### How the program works
For the execution of the script there are basically only two paths.
1. Retrieve / collect the desired data from the Excel-sheets previously downloaded and stored from the Norges-Bank website. 
   
   You enter this path when you configure in `user_config.py` the parameter `collect_companies_from_data` to one:  
   e.g. `collect_companies_from_data = 1`  
2. Visualization of the data
   You enter this second path when you configure in `user_config.py` the parameter `visualize_data` to one:  
   `visualize_data = 1`  

### The first Execution
With a prepared python environment and the locally available excelsheets, nothing stands in the way of a first program execution.  
For the first execution both pathes are executed. The collected data will be printed in the console.  
Let the execution continue. 
After a further seconds, the first graph will be displayed. It will show a company investment of the norges bank / the pension fund.  
If you want to continue to the next graph / next company investment, press X on the graphic plot.

### Usage
| WARNING: From transition of 1. path to 2. path a manual step by the user is necessary! |
|----------------------------------------------------------------------------------------|

The computationally intensive path is clearly path 1, the collection and reading of the data from the Excel sheets.
Therefore, it makes sense to separate the data collection from the visualization in two program executions.
What I mean by this: 
1. program execution - only path 1:
   1. by setting the parameters:  
      `collect_companies_from_data = 1` and  
      `visualize_data = 0`. 
   2. After the data collection an array / matrix will be printed to the console like:  
      `####COPY THIS DATA BELOW TO data.py #####`  
      `STRUCTURE TO COPY`  
      `"####COPY THIS DATA ABOVE TO data.py #####`
   3. Copy this structure into `data.py`.
   4. Give the matrix a name e.g. `my_collected_data`
   5. Reference this variable `my_collected_data` with the parameter `data_to_visualize` in `user_config.py`.

2. then another program execution can take place (this time path 2). With:  
   1. `collect_companies_from_data = 0` and `visualize_data = 1`. 

## Improved usage
Here's some more info if you're already a little more familiar with the parameters described above.

### Performance - Number of companies to analyze
As briefly mentioned above, the first path is very computationally and time intensive. The execution time of the data collection depends decisively on the 
number of companies to be analyzed.  
Simple: More companies -> more data collection actions.   
Here, there is no longer a linear relationship between execution time <-> number of companies. 
The number of companies to be considered can be limited with: `number_of_companies_to_analyze` in `user_config.py`. 

### Analyze other industries
You can analyze further industries and can choose among the list `industries`. 
Lets say you want to analyze the investments of the norway pension fund in the consumer goods industry, just assign  
`industry_to_analyze = "Consumer Goods"`  in `user_config.py`.

## Possible Improvements
- Improved Config adujstments 
- Error Handling

## Contribution
If you like and use this program, feel free to donate here: 
[Donate this program](https://www.paypal.com/donate/?hosted_button_id=FR84QT6MVPKFS)

## Licence
Standard Github license. Feel free to view and fork this project for personal use.

## Get in contact 

Github - [gremarsl](https://github.com/gremarsl)\
E-Mail:  [startwitharduino@gmail.com ](startwitharduino@gmail.com)
