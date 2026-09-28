#Convert a FASTQ file format (4 lines per sequence) to a FAST file format by
#dropping the quality scores and changing the header symbol
#This applies to every .FASTQ file in the directory
for file in *.fastq; do
    output_name="${file%.fastq}.fasta"
    sed -n '1~4s/^@/>/p; 2~4p' "$file" > "$output_name"
done
