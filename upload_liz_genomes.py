import ftplib
import sys
import os


# 1. List of names of genomes to be uploaded

genome_list = [ i for i in os.listdir(sys.argv[1] if "fastq.gz" in list(i))]


"""
2. Update the `username` and `password` 
"""
username = sys.argv[2]
password = sys.argv[3]

ftp = ftplib.FTP("ftp-private.ncbi.nlm.nih.gov", username, password)


"""
3. Create a directory using FTP, once you've logged in and you have your own address like `emilyncosta_gmail.com_xxxxx` and create a directory where you'll upload submission `africanum`
"""

ftp.cwd("uploads/lizaspinasse_gmail.com_ojGYyyaI")
ftp.mkd("WGSMTB")


# 4. Change the location of the directory 

ftp.cwd("uploads/lizaspinasse_gmail.com_ojGYyyaI/WGSMTB")

# 5. The next code is uploading the file one by one 

for a_file in genome_list:
    print("\n@@@@\n\n=> ", a_file,"\n\n@@@")
    with open(a_file ,'rb') as f:
        ftp.storbinary('STOR %s' % f.name , f)

# 6. As a confirmation, after everything is uploaded we confirm from the server 

print("\n\n###\n\nList of all Genomes uploaded via FTP:\n\n ")

for f in ftp.nlst():
    print(f)

# 7. We close the FTP connection

ftp.quit()


# 8. Now we close the python program

print("\n\n$$$\n\nDONE\n\n$$$")

####

