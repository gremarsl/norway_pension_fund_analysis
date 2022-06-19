import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import data
from config import directory
from data import data_of_basic_materials_top_5


def get_invested_capital_in_each_sector():
    for filename in os.listdir(directory):
        df = pd.read_excel(directory + filename)
        i = 2002
        market_value_of_one_year = [i]
        for industry in data.industries:
            single_data = []
            single_data.append(industry)

            filter_by_industry = df.loc[df['Industry'] == industry]
            value = filter_by_industry["Market Value(USD)"].sum()
            single_data.append(value)

            market_value_of_one_year.append(single_data)
        i += 1


def get_company_names_by_industry_and_market_value(industry, number_of_companies):
    for filename in os.listdir(directory):
        df = pd.read_excel(directory + filename)

        df.sort_index(axis=1)

        filter_by_industry = df.loc[df['Industry'] == industry]

        filtered_and_sorted_values = filter_by_industry.sort_values(by='Market Value(USD)', ascending=False)

        result_first_x = filtered_and_sorted_values.iloc[:number_of_companies]

        # access to values in a column of the dataframe
        filter_by_name = result_first_x.loc[:, "Name"]

        array_companies = filter_by_name.to_numpy()

        array_all_companies.append(array_companies)

    # Create flat list with entries for each found company
    flat_list = [item for sublist in array_all_companies for item in sublist]

    # delete duplicated
    flat_list_without_douplicates = list(set(flat_list))

    print(flat_list_without_douplicates)
    print("There are {} companies to analyse:".format(len(flat_list_without_douplicates)))
    print("end of sort_and_filter_companies_by_market_value")
    return flat_list_without_douplicates


def sort_and_extract_data_by_market_value(industry, filename):
    df = pd.read_excel(directory + filename)

    df.sort_index(axis=1)
    filter_by_industry = df.loc[df['Industry'] == industry]

    result = filter_by_industry.sort_values(by='Market Value(USD)', ascending=False)

    array_complete_data = result.to_numpy()

    # filter columns from numpy array
    # Index(['Industry', 'Region', 'Country', 'Name', 'Market Value(NOK)''Market Value(USD)', 'Voting', 'Ownership', 'Incorporation Country'],
    selections = np.array([False, False, False, True, False, True, False, True, False])

    array_reduced_all_lines = array_complete_data[:, selections]
    return array_reduced_all_lines


def analyse_data(industry, companies_to_analyse):
    for element in companies_to_analyse:

        data_of_one_element = [element]

        for filename in os.listdir(directory):
            cutted = filename.split("_")
            year = cutted[1]
            # df_csv = pd.read_csv(directory_csv + filename,sep=';')
            extracted_data = sort_and_extract_data_by_market_value(industry, filename)

            for line in extracted_data:
                # compare
                if line[0] == element:
                    market_cap = line[1]
                    ownership = line[2]
                    data_of_one_element.append([year, market_cap, ownership])
                else:
                    continue
        data_of_all_elements.append(data_of_one_element)

    print(data_of_all_elements)

    return data_of_all_elements


# input from user
collect_companies_from_data = False
visualize_data = True

# required input from user if plot_data == True
data_to_visualize = data_of_basic_materials_top_5

# required input from user if plot_data is False (--> data collection)
industry_to_analyze = "Oil & Gas"
number_of_companies_to_analyze = 5

ownership = []
data_of_all_elements = []

if __name__ == '__main__':

    if collect_companies_from_data:
        companies_to_analyze = get_company_names_by_industry_and_market_value(industry_to_analyze,
                                                                              number_of_companies_to_analyze)

        data_of_all_elements = analyse_data(industry_to_analyze, companies_to_analyze)

    pd.set_option('display.max_columns', None)

    array_all_companies = []

    if visualize_data:

        for elem in data_to_visualize:

            fig, host = plt.subplots(figsize=(8, 5))

            par1 = host.twinx()

            company_name = elem[0]

            array_market_value = []
            array_ownership = []
            array_year = []
            for index in range(1, len(elem)):
                year = elem[index][0]
                year = int(year)
                market_value = elem[index][1]
                ownership = elem[index][2]

                array_year.append(year)
                array_ownership.append(ownership)
                array_market_value.append(market_value)

            # alternative:
            p1, = host.plot(array_year, array_market_value, color="red", label="USD")
            host.scatter(array_year, array_market_value, color="red", label="USD")

            p2, = par1.plot(array_year, array_ownership, color="green", label="Ownership")
            par1.scatter(array_year, array_ownership, color="green", label="Ownership")

            # show grid
            plt.grid(b=None, which='major', axis='both')

            host.set_ylim(0, max(array_market_value) + 1 * 10 ** 9)
            par1.set_ylim(0, max(array_ownership) + 0.2)

            # alternaive:
            host.set_xlim(2000, 2022, 1)

            plt.title('Ownership of Norway in {}: '.format(company_name))

            host.set_xlabel("Year")
            host.set_ylabel("USD")
            par1.set_ylabel("%")

            lns = [p1, p2]
            host.legend(handles=lns, loc='best')
            host.yaxis.label.set_color(p1.get_color())
            par1.yaxis.label.set_color(p2.get_color())

            host.xaxis.set_major_locator(plt.MaxNLocator(integer=True))

            fig.tight_layout()

            plt.legend()
            plt.show()
