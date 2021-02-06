# Find keywords in pdf files
Searches in a folder with pdf files for a list of specified keywords. Writes the result into a csv file.
usage: 
```
findkeywordsinpdfs.py [-h] [-i] keywordfile pdffolder
```
The keywordfile should contain one keyword per line. The script will write the results to a file keywordsinpdfs.csv, which contains in each line: first the pdf filename, then the keywords found in that file.