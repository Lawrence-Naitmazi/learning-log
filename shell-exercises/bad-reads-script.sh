#This script pulls out all reads that contain 10 or more consecutive Ns from the untrimmed fastq files in the current directory and outputs them to a file called scripted_bad_reads.txt.
grep -B1 -A2 -h NNNNNNNNNN *.fastq | grep -v '^--' > scripted_bad_reads.txt
echo "Scripted bad reads have been output to scripted_bad_reads.txt"
