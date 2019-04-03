import ftplib
import sys




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





ftp = ftplib.FTP("ftp-private.ncbi.nlm.nih.gov", "subftp", "w4pYB9VQ")



# ftp.cwd("uploads/lizaspinasse_gmail.com_ojGYyyaI")
# ftp.mkd("WGSMTB")



ftp.cwd("uploads/lizaspinasse_gmail.com_ojGYyyaI/WGSMTB")


for a_file in genome_list:
    with open(a_file ,'rb') as f:
        ftp.storbinary('STOR %s' % f , f)
    print("\n@@@@\n\n=> ", f,"\n@@@")

# ftp.nlst()

ftp.quit()

####

