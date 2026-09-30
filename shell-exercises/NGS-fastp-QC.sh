#!/usr/bin/env bash
#Run fastp quality filtering on every pair of paired-end .fastq files in a directory.
#Each sample_R1*.fastq file is processed together with its matching sample_R2*.fastq file;
#an R1 file with no R2 partner is skipped with a warning.
#Trimmed reads go to <outdir>/, and an HTML + JSON QC report is written for each sample.
#
#Usage: ./NGS-fastp-QC.sh [input_dir] [output_dir] [threads]
#   defaults: input_dir=.  output_dir=fastp_output  threads=4

set -euo pipefail

input_dir="${1:-.}"
output_dir="${2:-fastp_output}"
threads="${3:-4}"

#Quality settings - adjust to suit your data
min_qual=20      #Phred score a base must reach to count as "qualified"
min_length=50    #discard reads shorter than this after trimming

mkdir -p "$output_dir/reports"
shopt -s nullglob

#only list the R1 files - each one's R2 partner is found inside the loop
files=("$input_dir"/*_R1*.fastq)
if [ ${#files[@]} -eq 0 ]; then
    echo "No *_R1*.fastq files found in $input_dir" >&2
    exit 1
fi

count=0
for file in "${files[@]}"; do
    name=$(basename "$file")
    r2="$input_dir/${name/_R1/_R2}"

    if [ ! -e "$r2" ]; then
        echo "Warning: no R2 partner for $name, skipping" >&2
        continue
    fi

    #strip the extension and _R1 to get the sample name
    sample="${name%.fastq}"
    sample="${sample/_R1/}"

    echo "[$sample] $name + $(basename "$r2")"
    fastp \
        -i "$file" -I "$r2" \
        -o "$output_dir/${sample}_R1.trimmed.fastq" \
        -O "$output_dir/${sample}_R2.trimmed.fastq" \
        --detect_adapter_for_pe \
        -q "$min_qual" -l "$min_length" \
        -w "$threads" \
        -h "$output_dir/reports/${sample}.html" \
        -j "$output_dir/reports/${sample}.json" \
        2> "$output_dir/reports/${sample}.log"
    count=$((count + 1))
done

echo "Done: $count sample(s) processed. Output in $output_dir/"
