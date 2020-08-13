#Use command line to send email

#Instruction: Run python3 mailsender.py -h to get all info which is provided here

#Use to send to single email
    python3 mailsender.py -e mymail mypass recievermail message
      1: mymain -> enter your email here
      2: mypass -> import your password from pass.txt(any text file)
      3: recivermain -> enter Recivermail
      4: message -> use text file to import your message
#Use to send to multiple email
    python3 mailsender.py -E mymail mypass all_email_file message
      1: mymain -> enter your email here
      2: mypass -> import your password from pass.txt(any text file)
      3: all_reciver_mail -> save all your email in file then give file name commond
      #(USE NEW LINE FOR EACH ID)
      4: message -> use text file to import your message
      
#Use to send to single email with Document
    python3 mailsender.py -f mymail mypass recievermail message file
      1: mymain -> enter your email here
      2: mypass -> import your password from pass.txt(any text file)
      3: recivermain -> enter Recivermail
      4: message -> use text file to import your message
      5: Name of your file(pdf)
 
#Use to send to multiple email with Document
    python3 mailsender.py -F mymail mypass all_email_file message file
      1: mymain -> enter your email here
      2: mypass -> import your password from pass.txt(any text file)
      3: all_reciver_mail -> save all your email in file then give file name commond
      4: message -> use text file to import your message
      5: Name of your file(pdf)
