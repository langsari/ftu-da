from s3v3 import *
import csv

# ORIGINAL VERSION - Leaves file open
# def write_to_file(filename, data_sample):
# 	example = csv.writer(open(filename, 'w', encoding='utf-8'), dialect='excel') # example is the variable of the new file that is open and which we can write to (using utf-8 encoding and an excel dialect). 
# 	example.writerows(data_sample) # write rows is going to take the rows in the data sample and write them to the example (i.e. the file name we passed in)

# NEW VERSION - Closes file at end
def write_to_file(filename, data_sample):
    with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
        example = csv.writer(csvfile, dialect='excel')
        example.writerows(data_sample)

write_to_file("_data/s4-silk_ties.csv", silk_ties) # this is going to create a new csv located in the _data directory, named s4-silk_ties.csv and it is going to contain all of that data from the silk_ties list which we created in s3v2 (silk_ties = filter_col_by_string(data_from_csv, "material", "_silk"))
	# returned an error because the directory and the file did not exist. Going to create the directory and try again to see if it will create the file. It worked! It needs a directory, but it can create the file from scratch