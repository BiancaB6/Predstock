Scope of file:
- Explain solution
- Give indication for setup

  Solution:
  As per requirements, implemented a function that reads a certain number of files from each of the folders provided
  The prefered language for this task was Python
  The function takes as parameter the number of files to be read.
  I implemented the function such as the folders given as input are in a folder named 'stock_price_data_files', this folder being in the same location as the python script.
  The function will iterate through the folders from 'stock_price_data_files' folder, in each folder will read 1 or 2 .csv file (as per input), and predict the next 3 values.
  The output will be a .csv file that will contain the original file's content + next 3 predicted values. It is saved in the same folder as the original file. Nam format = Original_file_name_predicted.csv
  More details regarding the implementation are available in the code as comments

  #prerequisites
  having pandas library intalled
  
