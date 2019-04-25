import ftplib
import sys


# 1. List of names of genomes to be uploaded

genome_list = [
"MTB1.1.fastq.gz",
"MTB8.1.fastq.gz",
"MTB16.1.fastq.gz",
"MTB24.1.fastq.gz",
"MTB31.1.fastq.gz",
"MTB38.1.fastq.gz",
"MTB46.1.fastq.gz",
"MTB1.2.fastq.gz",
"MTB8.2.fastq.gz",
"MTB16.2.fastq.gz",
"MTB24.2.fastq.gz",
"MTB31.2.fastq.gz",
"MTB38.2.fastq.gz",
"MTB46.2.fastq.gz",
"MTB2.1.fastq.gz",
"MTB9.1.fastq.gz",
"MTB17.1.fastq.gz",
"MTB25.1.fastq.gz",
"MTB32.1.fastq.gz",
"MTB39.1.fastq.gz",
"MTB47.1.fastq.gz",
"MTB2.2.fastq.gz",
"MTB9.2.fastq.gz",
"MTB17.2.fastq.gz",
"MTB25.2.fastq.gz",
"MTB32.2.fastq.gz",
"MTB39.2.fastq.gz",
"MTB47.2.fastq.gz",
"MTB3.1.fastq.gz",
"MTB10.1.fastq.gz",
"MTB18.1.fastq.gz",
"MTB26.1.fastq.gz",
"MTB33.1.fastq.gz",
"MTB41.1.fastq.gz",
"MTB48.1.fastq.gz",
"MTB3.2.fastq.gz",
"MTB10.2.fastq.gz",
"MTB18.2.fastq.gz",
"MTB26.2.fastq.gz",
"MTB33.2.fastq.gz",
"MTB41.2.fastq.gz",
"MTB48.2.fastq.gz",
"MTB4.1.fastq.gz",
"MTB11.1.fastq.gz",
"MTB19.1.fastq.gz",
"MTB27.1.fastq.gz",
"MTB34.1.fastq.gz",
"MTB42.1.fastq.gz",
"MTB49.1.fastq.gz",
"MTB4.2.fastq.gz",
"MTB11.2.fastq.gz",
"MTB19.2.fastq.gz",
"MTB27.2.fastq.gz",
"MTB34.2.fastq.gz",
"MTB42_2.fastq.gz",
"MTB49.2.fastq.gz",
"MTB5.1.fastq.gz",
"MTB13.1.fastq.gz",
"MTB20.1.fastq.gz",
"MTB28.1.fastq.gz",
"MTB35.1.fastq.gz",
"MTB43.1.fastq.gz",
"MTB50.1.fastq.gz",
"MTB5.2.fastq.gz",
"MTB13.2.fastq.gz",
"MTB20.2.fastq.gz",
"MTB28.2.fastq.gz",
"MTB35.2.fastq.gz",
"MTB43.2.fastq.gz",
"MTB50.2.fastq.gz",
"MTB6.1.fastq.gz",
"MTB14.1.fastq.gz",
"MTB21.1.fastq.gz",
"MTB29.1.fastq.gz",
"MTB36.1.fastq.gz",
"MTB44.1.fastq.gz",
"MTB51.1.fastq.gz",
"MTB6.2.fastq.gz",
"MTB14.2.fastq.gz",
"MTB21.2.fastq.gz",
"MTB29.2.fastq.gz",
"MTB36.2.fastq.gz",
"MTB44.2.fastq.gz",
"MTB51.2.fastq.gz",
"MTB7.1.fastq.gz",
"MTB15.1.fastq.gz",
"MTB22.1.fastq.gz",
"MTB30.1.fastq.gz",
"MTB37.1.fastq.gz",
"MTB45.1.fastq.gz",
"MTB7.2.fastq.gz",
"MTB15.2.fastq.gz",
"MTB22.2.fastq.gz",
"MTB30.2.fastq.gz",
"MTB37.2.fastq.gz",
"MTB45.2.fastq.gz"
    ]


"""
2. Update the `username` and `password` 
"""

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

