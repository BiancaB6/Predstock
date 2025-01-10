import pandas as pd
import numpy as np
import os
import datetime

def get_10_consecutive_data_points(file_path):
    df = pd.read_csv(file_path, header=None)
    #get random index
    start_idx = np.random.randint(0, len(df)-10)
    #return 10 data sets starting from random index
    return df.iloc[start_idx::start_idx+10]
#    return df[-10:]

def predict_next_3_values(data_points):
    n_plus_1 = (data_points.iloc[-2])[2]
    n_plus_2 = ((data_points.iloc[-1])[2] - n_plus_1)/2
    n_plus_3 = (n_plus_1 +n_plus_2)/4

    return n_plus_1,n_plus_2, n_plus_3

def process_files(stock_exchange_folder, num_files):
    files = [f for f in os.listdir(stock_exchange_folder) if f.endswith('.csv')]
    files_to_process = files[:num_files]

    for file in files_to_process:
       # data_points = get_10_consecutive_data_points(os.path.join(stock_exchange_folder, file))
        filepath = os.path.join(stock_exchange_folder,file)
        df = pd.read_csv(filepath, header=None)
        
        #get last 10 data points from 
        data_points = df[-10:]

        #get predictions
        n_plus_1, n_plus_2, n_plus_3 = predict_next_3_values(data_points)

        output_data = df.copy()

        #starting from the last timestamp in the input, compute next 3 days for the predictions
        dateinfo = pd.to_datetime((output_data.iloc[-1])[1], dayfirst=True).date()
        dateinfo1 = (dateinfo + datetime.timedelta(days=1))
        dateinfo2 = dateinfo1 + datetime.timedelta(days=1)
        dateinfo3 = dateinfo2 + datetime.timedelta(days=1)

        #append to the existing info from the procesed file, the 3 new prediction
        output_data.loc[len(output_data)] = [(output_data.iloc[-1])[0],
                                             dateinfo1.strftime('%d-%m-%Y'),
                                             n_plus_1]
        output_data.loc[len(output_data)] = [(output_data.iloc[-1])[0],
                                            dateinfo2.strftime('%d-%m-%Y'),
                                             n_plus_2]
        output_data.loc[len(output_data)] = [(output_data.iloc[-1])[0],
                                             dateinfo3.strftime('%d-%m-%Y'),
                                             n_plus_3]
        print("Processed file: "+ filepath)
                                  
        output_data.to_csv(f"{filepath.split('.csv')[0]}_predicted.csv", index=False, sep =',', header=None)
        print("Write results to: "+ f"{filepath.split('.csv')[0]}_predicted.csv")   

#usage
def process_folders(num_files):
    # files_num = int(input("Enter the recommended number of files to be sampled for each Stock Exchange: "))
    # print(f"You have entered: {files_num}.")

    #within the current folder, all subfoders will be checked
    directory_path = 'stock_price_data_files'
    folders = [f for f in os.listdir(directory_path) if os.path.isdir(os.path.join(directory_path, f))]
    for folder in folders:
        folder_path = os.path.join(directory_path,folder)
        #for each subfolder, will process files
        process_files(folder_path,num_files)

process_folders(1)