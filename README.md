# Subset-reads
Subsets the reads in each file from a group of fastq files to the number of reads in the file with the smallest number of reads. 

This script was written for downstream processing of paired-end fastq files that required each file to have the same number of reads. Subsetting the reads is accomplished by finding the file with the smallest number of reads and randomly sampling all of the other files without replacement to that number of reads.  
