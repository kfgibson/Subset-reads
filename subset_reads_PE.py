#November 23, 2019
#Purpose: subset fastq reads to the same sampling depth

import argparse
import random

random.seed(99)

parser = argparse.ArgumentParser(description = "Subset fastq reads to the same sampling depth.")
parser.add_argument('-f', '--files', dest="fastq_files", nargs="+", help='list of fastq files in the format file1_R1 file1_R2, file2_R1, file2_R2')
args = parser.parse_args()

input_files = args.fastq_files

#function to find the minimum read count in the list of input files
def calc_subsample(in_files):
    #num of input files
    num_files = len(in_files)
    #indices of the R1 files 
    index = range(0,num_files,2)
    R1_reads = [in_files[i] for i in index]

    num_reads = []

    for R1 in R1_reads:
        num = sum(1 for _ in open(R1))/4
        num_reads.append(int(num))

    subsample_num = min(num_reads)

    return subsample_num

#function to produce the subsampled files 
def subsample_files(input_files, subsample_num):
    
    num_files = len(input_files)

    #modify list of input files for processing
    files_list = []
    for i in range(0, num_files, 2):
        files_list.append(input_files[i:i+2])

    for files in files_list:
        #number of records in file
        records = int(sum(1 for _ in open(files[0]))/4)
        #randomly select and sort records
        rand_records = sorted(random.sample(list(range(0,records)), k=subsample_num))
       
        #print(rand_records)

        R1, R2 = open(files[0]), open(files[1])
        sub_R1, sub_R2 = open(files[0] + ".subsample", "w+"), open(files[1] + ".subsample", "w+")

        rec_no = 0

        for rr in rand_records:
            #print(rec_no)

            while rec_no < rr:
                rec_no += 1
                for i in range(4): R1.readline()
                for i in range(4): R2.readline()
            for i in range(4):
                sub_R1.write(R1.readline())
                sub_R2.write(R2.readline())
            rec_no += 1

        print(("Wrote to {}, {}").format(sub_R1.name, sub_R2.name))

    return



##########################################
#main
subsample_num = calc_subsample(input_files)
subsample_files(input_files, subsample_num)
