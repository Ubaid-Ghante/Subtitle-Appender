#!/bin/bash
touch res.txt file1.txt file2.txt
:> res.txt
echo Enter the name of first srt file
read x
echo Enter the name of second srt file
read y
cat ${x} > file1.txt
cat ${y} > file2.txt
echo -----------------------------------------------------------------------
echo Merging....
python3 Merger.py
cat res.txt > Merged.srt
rm file1.txt file2.txt res.txt
echo Merging successful
echo Open your Merged.srt file in any text editor and go to the end of file replace the last timestamp to 9999 