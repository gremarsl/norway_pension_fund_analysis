import os
import data


# input from user
collect_companies_from_data = 0
visualize_data = 1

# required input from user if plot_data == True
data_to_visualize = data.data_of_financials

# required input from user if plot_data is False (--> data collection)

#AVAILABLE INDUSTRIES
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

industry_to_analyze = "Financials"
number_of_companies_to_analyze = 1

ownership = []
data_of_all_elements = []

directory_of_execution = os.getcwd()

directory = directory_of_execution + '\\EQ_Norway\\Industry\\'



