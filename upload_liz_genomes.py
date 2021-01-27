import ftplib
import sys
import os
import argparse

# 1. adding Argparse
parser = argparse.ArgumentParser()

parser.add_argument("-f","-folder",action='store', help="Folder containing all files",required = True)
parser.add_argument("-e","-extension",action="store", help= "File extension from files",required = False, default="fastq.gz")
parser.add_argument("-u","-username",action='store', help="NCBI - Username",required = True)
parser.add_argument("-p","-password",action='store', help= "NCBI - Password",required = True)

args = parser.parse_args()

file_ext = args.e
foldername = args.f
username = args.u
password = args.p



# 2. List of names of genomes to be uploaded

genome_list = [ foldername+"/"+i for i in os.listdir(foldername) if file_ext in i]


"""
3. Update the `username` and `password` 
"""


ftp = ftplib.FTP("ftp-private.ncbi.nlm.nih.gov", username, password)


"""
4. Create a directory using FTP, once you've logged in and you have your own address like `emilyncosta_gmail.com_xxxxx` and create a directory where you'll upload submission `africanum`
"""

ftp.cwd("uploads/lizaspinasse_gmail.com_ojGYyyaI")
ftp.mkd("WGSMTB")


# 5. Change the location of the directory 

ftp.cwd("uploads/lizaspinasse_gmail.com_ojGYyyaI/WGSMTB")

# 6. The next code is uploading the file one by one 

for a_file in genome_list:
    print("\n@@@@\n\n=> ", a_file,"\n\n@@@")
    with open(a_file ,'rb') as f:
        ftp.storbinary('STOR %s' % f.name , f)

# 7. As a confirmation, after everything is uploaded we confirm from the server 

print("\n\n###\n\nList of all Genomes uploaded via FTP:\n\n ")

for f in ftp.nlst():
    print(f)

# 8. We close the FTP connection

ftp.quit()


# 9. Now we close the python program

print("\n\n$$$\n\nDONE\n\n$$$")

####

