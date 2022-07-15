import os
import data

directory_of_execution = os.getcwd()

#START - Path to directory of EQ_Norway Data
directory = directory_of_execution + '\\EQ_Norway\\Industry\\'
#END - Path to directory of EQ_Norway Data


# START PATH - DATA COLLECT
collect_companies_from_data = 1
industry_to_analyze = "Financials"
number_of_companies_to_analyze = 1

#for information purpose only:
industries = ["Basic Materials",
              "Consumer Goods",
              "Consumer Services",
              "Financials",
              "Health Care",
              "Industrials",
              "Oil & Gas",
              "Technology",
              "Telecommunications",
              "Utilities"]

# END PATH - DATA COLLECT


# START PATH - VISUALIZE
visualize_data = 1
data_to_visualize = data.my_collected_data
# END PATH - VISUALIZE
