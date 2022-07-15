# Norges Fund Analysis

## Motivation
I am kind of interested in economics and fascinated by norway and its fund. All three combined, has led me to write irregularly (since 2020) but every now and then on this little Python script.

### Prerequisites
Python Interpreter: v3.09 is installed and functioning on the computer.
With Python v3.10 I had incompatibilities.
The Python packages are installed and ready for usage.

### Where does the data for a company analysis come from ?
Norges Bank provides all data and investments. 
For an analysis the files are required and can be downloaded here: https://www.nbim.no/en/the-fund/investments/#/
Afterwards please reference the file path in  `user_config.py`.

#### How the program works 
For the execution of the script there are basically only two paths.
1. Retrieve / collect the desired data from the Excel-sheets previously downloaded and stored from the Norges-Bank website. 
   
   You enter this path when you configure in `user_config.py` the parameter `collect_companies_from_data` to one:
   e.g. `collect_companies_from_data = 1`  
2. Visualization of the data
   You enter this second path when you configure in `user_config.py` the parameter `visualize_data` to one:  
   `visualize_data = 1`  

### Usage
| WARNING: From transition of 1. path to 2. path a manual step by the user is necessary! |
|----------------------------------------------------------------------------------------|

Der rechenintensive Pfad ist eindeutig Pfad 1, das Sammeln und Auslesen der Daten aus den Excel-sheets.
Deshalb bietet es sich an, die Datensammlung von der Visualisierung in zwei Programmausführungen zu trennen.
Was ich damit meine: 
1. Programmausführung - lediglich Pfad 1:
   1. `collect_companies_from_data = 1` und `visualize_data = 0` 
   2. Anschließend wird das ausgegebne Array / die Matrize mit den Unternehmensdaten in `data.py` kopiert.
      Zu kopieren ist die Datenstruktur, die in der Konsole erscheint zwischen: 
      `print("####COPY THIS DATA BELOW TO data.py #####")`
      `COPY THIS HERE`
      `print("####COPY THIS DATA ABOVE TO data.py #####")`
   3. Gib der Matrize einen Namen. bpsw. my_collected_data
   4. Referenziere diesen Namen in `user_config.py`

2. Dann erfolgt eine weitere Programmausführung (Pfad 2 wird gegangen). Diesmal mit:
   1. `collect_companies_from_data = 0` und `visualize_data = 1` 


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
   4. Give the matrix a name e.g. my_collected_data
   5. Reference this name in `user_config.py`.

2. then another program execution can take place (path 2 is gone). This time with:
   1. `collect_companies_from_data = 0` and `visualize_data = 1`. 

## Possible Improvements
- Improved Config adujstments 
- Error Handling.

## Contribution
If you like and use this program, feel free to donate here: 
[Donate this program](https://www.paypal.com/donate/?hosted_button_id=FR84QT6MVPKFS)

## Licence
Standard Github license. Feel free to view and fork this project for personal use.

## Get in contact 

Github - [gremarsl](https://github.com/gremarsl)\
E-Mail:  [startwitharduino@gmail.com ](startwitharduino@gmail.com)
