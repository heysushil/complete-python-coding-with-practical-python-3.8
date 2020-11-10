import matplotlib.pyplot as plt
import pandas as pd

gence_wise_csv = "D:/xampp/htdocs/htmldemo/complete-python-coding-with-practical-python-3.8/library/demo/gean_wise_data_Kinome_Cancer_Somatic_Mutations_Kinase_variation.csv"

cancer_wise_csv = "D:/xampp/htdocs/htmldemo/complete-python-coding-with-practical-python-3.8/library/demo/Cancer_wise_Kinome_Cancer_Somatic_Mutations_Download_Samples_KS_Details.csv"
# data = pd.read_excel(filename, sheet_name=0, index_col=0)

# Read the csv file
gence_wise_data = pd.read_csv(gence_wise_csv)
cancer_wise_data = pd.read_csv(cancer_wise_csv)

# get all geancse list
get_columns_of_gense_csv = pd.DataFrame(gence_wise_data)
list_of_columns_of_gens_csv = get_columns_of_gense_csv.columns.tolist()
list_of_all_genece = gence_wise_data['Hugo_symbol'].tolist()

# cancer csv file data
get_all_cancers_Data = pd.DataFrame(cancer_wise_data)
list_of_cancers = cancer_wise_data['Cancer'].tolist()

# single = gence_wise_data.get_value(3,'Char')
# print(gence_wise_data)
# print(list_of_columns_of_gens_csv)
# print('list_of_all_genece: \n', list_of_all_genece)
# print(get_columns_of_gense_csv._get_value(1,'BLCA'))

# for cancers
# print(list_of_cancers)

# All requried data get
print('\nIndex of BLCA: ', list_of_cancers.index('BLCA'), ' Cancer Name: ', get_all_cancers_Data._get_value(0, 'Cancer'), ' Total: ', get_all_cancers_Data._get_value(0, 'Cases'))

get_gen_cancer_case_num = get_columns_of_gense_csv._get_value(1,'BLCA')

# Gen file base varaibles
gen_name = get_columns_of_gense_csv._get_value(1,'Hugo_symbol')
gen_based_cancer_count = int(get_columns_of_gense_csv._get_value(1,'BLCA'))

# Cancer file base varaibles
gen_based_cancer_name = get_all_cancers_Data._get_value(0, 'Cancer')
total_cancer_number = int(get_all_cancers_Data._get_value(0, 'Cases'))

case_final_data = 'Gen Name: ', gen_name, ' Cancer Name: ', gen_based_cancer_name, ' Total: ', total_cancer_number, ' A: ', total_cancer_number - gen_based_cancer_count, ' B: ', gen_based_cancer_count
print(case_final_data)
print(type(gen_based_cancer_name))

# list_of_gence = list(getAllCSVData[['Hugo_symbol']])
# print(list(data.columns))
# print(getAllCSVData[['Hugo_symbol']])
# print(len(getAllCSVData[['Hugo_symbol']]))

# Use to pass data to plots
# getExcelData = data.head().plot()
# getExcelData = data.head().plot(kind="barh")

# print(getExcelData)
# print(getExcelData.shape)

# columns = getExcelData[['Gene', 'Unique Variants']]

# print(columns)
# print(getExcelData)
# plt.plot()
# plt.show()